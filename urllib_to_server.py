#! /usr/bin/python
# coding: utf8

import httplib2
import urllib


print "Try to connect to site ..."

h = httplib2.Http()
headers, content = h.request("https://www.google.fr", "GET")
print content