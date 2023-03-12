#! /usr/bin/python
# coding : utf8

import requests
import urllib3

URL = 'http://web/nvidia/favicon.ico'

class Test:
	'''
	This is a class to test functions
	'''
	def __init__(self):
		''' Constructor
		'''
		pass

	def get_image_request(self, URL):
		req = requests.get(URL)
		print(req.headers)
		print(req.status_code)

	def get_image_urllib(self, URL):
		req = urllib3.urlopen(URL)
		res = req.read()
		return res

	def multiply_2(self, x):
		return x*2


# test = Test()
# test.get_image_request(URL)
# test.get_image_urllib(URL)
