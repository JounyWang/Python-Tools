#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By linjie
# Python 2.7
# import urllib
import urllib2
import urllib
import os
import time
from bs4 import BeautifulSoup
def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time()))
def get_soup(url):
	try:
		return BeautifulSoup(urllib2.urlopen(url,timeout=30).read(),"lxml")
	except Exception as e:
		pass
		print get_time()+' get_soup error \n'+repr(e)
def get_img(url):
	soup = get_soup(url)
	try:
		image_tags = soup.find_all('meta',property="og:image")
		for tag in image_tags:
			img_url = tag['content']
		name_tags = soup.find_all('meta',property="og:description")
		for tag in name_tags:
			content = tag['content']
			name = content[content.index('(')+2:content.index(')')]
		f = urllib2.urlopen(img_url,timeout=30)
		data = f.read()
		with open(name+'.jpg', "wb") as code:
			code.write(data)
	except Exception as e:
		pass
		print get_time()+' get_img error \n'+repr(e)
if __name__ == '__main__':
	print get_time()
	url='https://www.instagram.com/p/BZgaNv1n753/'
	get_img(url)
	print get_time()