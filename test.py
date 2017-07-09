#! /usr/bin/python
# coding : utf8

import requests
import urllib2

URL = 'http://web/nvidia/favicon.ico'

class Test:
	'''
	This is a class to test functions
	'''
	def __init__(self):
		''' Constructeur
		'''
		pass

	def get_image_request(self, url):
		req = requests.get(URL)
		print req.headers
		print req.status_code

	def get_image_urllib(self, url):
		req = urllib2.urlopen(URL)
		res = req.read()
		#print res


test = Test()
test.get_image_request(URL)
test.get_image_urllib(URL)