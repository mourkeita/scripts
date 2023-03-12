#!/usr/bin/python
# coding: utf8

print "Test to connect to url with requests in HTTPS"

import requests
from requests.auth import HTTPBasicAuth
url = 'https://api.github.com/user'

r = requests.get(url, auth=HTTPBasicAuth('mourkeita', 'za4EeshaGithub'))
print r.status_code
print r.text