# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors
import struct

from pymysql.constants.COMMAND import COM_BINLOG_DUMP
from pymysql.util import int2byte

from .packet import BinLogPacketWrapper
from .constants.BINLOG import TABLE_MAP_EVENT, ROTATE_EVENT
from .event import NotImplementedEvent

class BinLogStreamReader(object):
    """Connect to replication stream and read event
    """

    def __init__(self, connection_settings={}, resume_stream=False,
                 blocking=False, only_events=None, server_id=255,
                 log_file=None, log_pos=None, filter_non_implemented_events=True):
        """
        Attributes:
            resume_stream: Start for event from position or the latest event of
                           binlog or from older available event
            blocking: Read on stream is blocking
            only_events: Array of allowed events
            log_file: Set replication start log file
            log_pos: Set replication start log pos
        """
        self.__connection_settings = connection_settings
        self.__connection_settings["charset"] = "utf8"

        self.__connected_stream = False
        self.__connected_ctl = False
        self.__resume_stream = resume_stream
        self.__blocking = blocking
        self.__only_events = only_events
        self.__filter_non_implemented_events = filter_non_implemented_events
        self.__server_id = server_id
        self.__use_checksum = False

        #Store table meta information
        self.table_map = {}
        self.log_pos = log_pos
        self.log_file = log_file

    def close(self):
        if self.__connected_stream:
            self._stream_connection.close()
            self.__connected_stream = False
        if self.__connected_ctl:
            self._ctl_connection.close()
            self.__connected_ctl = False

    def __connect_to_ctl(self):
        self._ctl_connection_settings = dict(self.__connection_settings)
        self._ctl_connection_settings["db"] = "information_schema"
        self._ctl_connection_settings["cursorclass"] = \
            pymysql.cursors.DictCursor
        self._ctl_connection = pymysql.connect(**self._ctl_connection_settings)
        self._ctl_connection._get_table_information = self.__get_table_information
        self.__connected_ctl = True

    def __checksum_enabled(self):
        '''Return True if binlog-checksum = CRC32. Only for MySQL > 5.6 '''
        cur = self._stream_connection.cursor()
        cur.execute("SHOW GLOBAL VARIABLES LIKE 'BINLOG_CHECKSUM'")
        result = cur.fetchone()
        cur.close()

        if result is None:
            return False
        var, value = result[:2]
        if value == 'NONE':
            return False
        return True

    def __connect_to_stream(self):
        # log_pos (4) -- position in the binlog-file to start the stream with
        # flags (2) BINLOG_DUMP_NON_BLOCK (0 or 1)
        # server_id (4) -- server id of this slave
        # log_file (string.EOF) -- filename of the binlog on the master
        self._stream_connection = pymysql.connect(**self.__connection_settings)

        self.__use_checksum = self.__checksum_enabled()

        #If cheksum is enabled we need to inform the server about the that we support it
        if self.__use_checksum:
            cur = self._stream_connection.cursor()
            cur.execute("set @master_binlog_checksum= @@global.binlog_checksum")
            cur.close()

        # only when log_file and log_pos both provided, the position info is
        # valid, if not, get the current position from master
        if self.log_file is None or self.log_pos is None:
            cur = self._stream_connection.cursor()
            cur.execute("SHOW MASTER STATUS")
            self.log_file, self.log_pos = cur.fetchone()[:2]
            cur.close()

        prelude = struct.pack('<i', len(self.log_file) + 11) \
            + int2byte(COM_BINLOG_DUMP)

        if self.__resume_stream:
            prelude += struct.pack('<I', self.log_pos)
        else:
            prelude += struct.pack('<I', 4)

        if self.__blocking:
            prelude += struct.pack('<h', 0)
        else:
            prelude += struct.pack('<h', 1)

        prelude += struct.pack('<I', self.__server_id)
        prelude += self.log_file.encode()

        if pymysql.VERSION < (0, 6, None):
            self._stream_connection.wfile.write(prelude)
            self._stream_connection.wfile.flush()
        else:
            self._stream_connection._write_bytes(prelude)
        self.__connected_stream = True

    def fetchone(self):
        while True:
            if not self.__connected_stream:
                self.__connect_to_stream()

            if not self.__connected_ctl:
                self.__connect_to_ctl()

            try:
                if pymysql.VERSION < (0, 6, None):
                    pkt = self._stream_connection.read_packet()
                else:
                    pkt = self._stream_connection._read_packet()
            except pymysql.OperationalError as error:
                code, message = error.args
                # 2013: Connection Lost
                if code == 2013:
                    self.__connected_stream = False
                    continue

            if pkt.is_eof_packet():
                return None

            if not pkt.is_ok_packet():
                continue

            binlog_event = BinLogPacketWrapper(pkt, self.table_map,
                                               self._ctl_connection,
                                               self.__use_checksum)
            if binlog_event.event_type == TABLE_MAP_EVENT:
                self.table_map[binlog_event.event.table_id] = \
                    binlog_event.event.get_table()

            if binlog_event.event_type == ROTATE_EVENT:
                self.log_pos = binlog_event.event.position
                self.log_file = binlog_event.event.next_binlog
            elif binlog_event.log_pos:
                self.log_pos = binlog_event.log_pos

            if self.__filter_event(binlog_event.event):
                continue

            return binlog_event.event

    def __filter_event(self, event):
        if self.__filter_non_implemented_events and isinstance(event, NotImplementedEvent):
            return True

        if self.__only_events is not None:
            for allowed_event in self.__only_events:
                if isinstance(event, allowed_event):
                    return False
            return True
        return False

    def __get_table_information(self, schema, table):
        for i in range(1, 3):
            try:
                if not self.__connected_ctl:
                    self.__connect_to_ctl()

                cur = self._ctl_connection.cursor()
                cur.execute("""
                    SELECT
                        COLUMN_NAME, COLLATION_NAME, CHARACTER_SET_NAME,
                        COLUMN_COMMENT, COLUMN_TYPE
                    FROM
                        columns
                    WHERE
                        table_schema = %s AND table_name = %s
                    """, (schema, table))

                return cur.fetchall()
            except pymysql.OperationalError as error:
                code, message = error.args
                # 2013: Connection Lost
                if code == 2013:
                    self.__connected_ctl = False
                    continue
                else:
                    raise error

    def __iter__(self):
        return iter(self.fetchone, None)
