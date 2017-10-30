#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# By linjie
# Python 2.7
import urllib2
import os
from bs4 import BeautifulSoup
import urllib 
import time
import zipfile  
import os  
import Config as cf
from Email import send_email
def get_time():
	return time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime(time.time()))
def pojie_zip(zip_path,password):  
    zip = zipfile.ZipFile(zip_path, "r",zipfile.zlib.DEFLATED)  
    try:
        zip.extractall(members=zip.namelist() , pwd=password)  
        print get_time()+' ----success!,The password is %s' % password  
        zip.close()
        os.remove(zip_path)  
        return True  
    except:  
        pass
    print get_time()+'pojie_zip error'
def get_zip(zip_path,date):
	url = 'https://iiio.io/download/'+str(date)+'/Windows系列跟苹果系列.zip'
	content=urllib.urlopen(url)
	if content.getcode()==200:
		urllib.urlretrieve(url, zip_path)
		print get_time()+' get zip done'
		return 1
	else:
		print get_time()+' Not Update.'
		return 0

def get_pwd(url):
	tags = BeautifulSoup(urllib2.urlopen(url).read(),"lxml").find_all('span',style="color: #3366ff;")
	for tag in tags:
		pwd = tag.string.split('密码：'.decode('utf-8'))[1]
		print get_time()+'get password: '+pwd
		return pwd

if __name__=='__main__':
	print get_time()+'go on ...'
	if cf.sended_date != cf.date:
		if get_zip(cf.zip_path,str(cf.date)):
			pwd = get_pwd(cf.hosts_url)
			pojie_zip(cf.zip_path,cf.pwd)
			send_email(cf.receivers,cf.mail_content,cf.mail_title,cf.mail_attach)
			cf.sended_date = cf.date
	else:
		print get_time()+'sended today'