#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# @Author: jouny
# @Date:   2017-10-03 10:01:30
# @Last Modified by:   jouny
# @Last Modified time: 2017-10-06 19:55:50
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTP_SSL
import sys
import time
import Config

def send_email(receivers,mail_content,mail_title,mail_attach):
	try:
		smtp = SMTP_SSL(Config.host_server)
		smtp.login(Config.sender_mail, Config.pwd)
		msg = MIMEMultipart()
		msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
		msg["Subject"] = Header(mail_title, 'utf-8')
		if mail_attach:
			att = MIMEText(open(mail_attach, 'rb').read(), 'base64', 'utf-8')
			att["Content-Type"] = 'application/octet-stream'
			att["Content-Disposition"] = 'attachment; filename="%s"'%mail_attach
			msg.attach(att)
		smtp.sendmail(Config.sender_mail, receivers, msg.as_string())
		smtp.quit()
		print 'send email to '+ str(receivers) +' success'
	except Exception as e:
		print "Error: send email faild\n"+str(e)
if __name__=='__main__':
	send_email(Config.receivers,Config.mail_content,Config.mail_title,Config.mail_attach)