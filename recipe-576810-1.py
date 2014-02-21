#!/usr/bin/env python

import paramiko
ssh = paramiko.SSHClient()

ssh.connect('216.97.82.48', username='root', password='meow12')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
stdin, stdout, stderr = ssh.exec_command('ls -l /var/downloads')

print stdout.readlines()
ssh.close()