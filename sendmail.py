#!/usr/bin/python


import os
import imp
import sys
import getpass
import smtplib
import argparse
import email.mime.text

parser = argparse.ArgumentParser(description='Send email \
                                 from command line or from within other programs')
parser.add_argument('to', type=str, default=[], nargs='?',
                    help='List of email addresses')
parser.add_argument('subject', type=str, default='', 
                    help='Subject of the email. Will be an empty string if omitted.')
parser.add_argument('text', type=str, default='-',
                    help='Text of the message. Taken from stdin if not specified')
parser.add_argument('--from', type=str, default='',
                    help='Override the email address specified in configuration')

args = None


if __name__ == '__main__':
    args = parser.parse_args()

# TODO: Configuration file.
servconf = {}  # Server configuration
authinfo = {} 
sender = {} 

servconf['smtpserver'] = 'smtp.gmail.com'
servconf['timeout'] = 10
servconf['useSSL'] = True

sender['fullname'] = ''
sender['emailaddress'] = ''
sender['signature'] = ''

authinfo['login'] = 's.pasoev@gmail.com'
authinfo['password'] = '******'

filewithtext =  open('email', 'r')
messagetext = ''
if args.text == '-':
    messagetext = sys.stdin.read()
else:
    messagetext = args.text
    
msg = email.mime.text.MIMEText(messagetext)
filewithtext.close()

msg['From'] = sender['emailaddress']
msg['To'] = args.to
msg['Subject'] = args.subject

# Login to smtp server

server = smtplib.SMTP_SSL(servconf['smtpserver'], smtplib.SMTP_SSL_PORT)
server.login(authinfo['login'], getpass.getpass())

server.send_message(msg)
