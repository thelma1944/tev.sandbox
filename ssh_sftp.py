#!/usr/bin/python

import paramiko


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('216.97.82.48', username='root', password='meow12')

stdin, stdout, stderr = ssh.exec_command(' ls -la /var/downloads')
directory_is = stdout.readlines()

for element in  directory_is:
      print element 

import subprocess

subprocess.check_call(['scp', '216.97.82.48', 'openpyxl-1.5.8.tar.gz'])

ssh.close()



 
 
 