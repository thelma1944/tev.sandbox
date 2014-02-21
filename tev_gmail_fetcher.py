#http://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/
#http://stackoverflow.com/questions/261655/converting-a-list-of-tuples-into-a-dict-in-python
#Making a proxy: ssh -L1993:imap.gmail.com:993 login@shell-account.com
import imaplib
import getpass
import datetime
import email
import email.header
import pprint
import quopri
import re
import HTMLParser

gm_header_re = re.compile("^(\d+) \(X-GM-THRID (\d+) X-GM-MSGID (\d+) X-GM-LABELS \(([^\)]*)\) UID (\d+) RFC822 {(\d+)}$")


def parse_email(full_message):
    raw_email = full_message[0][1]
    gm_headers = full_message[0][0]
    flags = full_message[1]
    email_message = email.message_from_string(raw_email)
    # note that if you want to get text content (body) and the email contains
    # multiple payloads (plaintext/ html), you must parse each message separately.
    # use something like the following: (taken from a stackoverflow post)
    def parse_headers():
        global gm_header_re
        hdict = {}
        for hdr, val in email_message.items():
            for decoded_val in email.header.decode_header(val):
                hdict.setdefault(hdr, []).append(unicode(decoded_val[0], decoded_val[1] if decoded_val[1] is not None else "ascii"))
        groups = gm_header_re.match(gm_headers).groups()
        hdict['X-GM-THRID'] = groups[1]
        hdict['X-GM-MSGID'] = groups[2]
        hdict['X-GM-LABELS'] = groups[3]
        hdict['IMAP-UID'] = groups[4]
        return hdict

    def get_first_text_block():
        def toutf(part):
            charset = part.get_content_charset() if part.get_content_charset() is not None else 'ascii'
            s = part.get_payload(decode=True)
            if part.get_content_type() == "text/html":
                h = HTMLParser.HTMLParser()
                return h.unescape(unicode(s, charset))
            else:
                return unicode(quopri.decodestring(s), charset)
        maintype = email_message.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message.get_payload():
                if part.get_content_maintype() == 'text':
                    return toutf(part)
                elif maintype == 'text':
                    return toutf(email_message)
        else:
            return toutf(email_message)
    #print email_message['To']
    #print email.utils.parseaddr(email_message['From']) # for parsing "Yuji Tomita" <yuji@grovemade.com>
    return {
        'headers': parse_headers(),
        'body': get_first_text_block(),
        'raw': full_message
    }

def fetch_email(mail, uid):
    result, data = mail.uid('fetch', uid, '(RFC822 X-GM-THRID X-GM-MSGID X-GM-LABELS X-GM-MSGID)')
    return data

def make_query():
    return '(SENTSINCE {startdate}) (SENTBEFORE {enddate})'.format(
        startdate=(datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y"),
        enddate=(datetime.date.today()).strftime("%d-%b-%Y")
        )

def auth():
 
    mail = imaplib.IMAP4_SSL("imap.gmail.com")  #get mail from gmai.com.
    username= "baastet.project"
    password= "meowpurr"
    mail.login(username, password)
    # Out: list of "folders" aka labels in gmail.
    mail.select("[Gmail]/All Mail") # connect to "All Mail" folder.
resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
items = items[0].split() # getting the mails id

for emailid in items:
    resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
    email_body = data[0][1] # getting the mail content
    mail = email.message_from_string(email_body) # parsing the mail content to get a mail object
   #Check if any attachments at all
    if mail.get_content_maintype() != 'multipart':
        continue

    print "["+mail["From"]+"] :" + mail["Subject"]

    # we use walk to create a generator so we can iterate on the parts and forget about the recursive headach
    for part in mail.walk():
        # multipart are just containers, so we skip them
        if part.get_content_maintype() == 'multipart':
            continue

        # is this part an attachment ?
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        counter = 1

        # if there is no filename, we create one with a counter to avoid duplicates
        if not filename:
            filename = 'part-%03d%s' % (counter, 'bin')
            counter += 1

        att_path = os.path.join(detach_dir, filename)

        #Check if its already there
        if not os.path.isfile(att_path) :
            # finally write the stuff
            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()

