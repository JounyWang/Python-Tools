#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 保存读者杂志全部文章为TXT
# By linjie
# Python 2.7
import urllib2
import os
from bs4 import BeautifulSoup

def urlBS(url):
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,"lxml")
	return soup
def main(baseurl): 
	soup = urlBS(baseurl)
	month_link=soup.select('.time a')
	for item in month_link:
		url = baseurl+item['href']
		time=item['href'][:7]
		if time[:1] =='1':
			time=item['href'][2:9]
		month_soup = urlBS(url)
		link = month_soup.select('.booklist a')
		path = os.getcwd()+u'/读者/'+time[:4]+'/'+time[-2:]+'/'
		if not os.path.isdir(path):
			os.makedirs(path)
		for item in link:
			newurl = baseurl +'/'+time+'/'+ item['href']
			result = urlBS(newurl)
			title = result.find("h1").string
			writer = result.find(id="pub_date").string.strip()
			filename = path + title + '.txt'
			print filename.encode("gbk")
			new=open(filename,"w")
			new.write("<<" + title.encode("gbk") + ">>\n\n")
			new.write(writer.encode("gbk")+"\n\n")
			text = result.select('.blkContainerSblkCon p')
			for p in text:
				context = p.text
				new.write(context.encode("gbk"))
			print title+' done.'
			new.close()
		print time+' done! -----sleep(10)'
		time.sleep(10)
if __name__ == '__main__':
	baseurl = 'http://www.52duzhe.com/'
	main(baseurl)