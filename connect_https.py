#! /usr/bin/python
# coding: utf-8

print "Hello"

import urllib
import httplib

from urllib import urlopen
import threading

from threading import Thread

def connect(url):
	try:
		#import pdb; pdb.set_trace()
		url = urlopen(url)
		print url
		if url.code == 200:
			import pdb; pdb.set_trace()
			print url.url
	except Exception as e:
		print "Can't connect exception"

def treatment(url):
	threads = []
	for i in range(1000):
		t = Thread(target=connect, args=(url,))
		threads.append(t)
		t.start()

connect("https://www.google.fr")

#treatment("http://scm.softwareinlife.com/jenkins/")