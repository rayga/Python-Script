__author__ = 'n4rut0'

import urllib2
import sys
url = raw_input("Enter URL : ")
headers = {}
header['User-Agent'] = "Googlebot"

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

print response.read()
response.close()
