#script to check HTTP Header

__author__ = 'n4rut0'

import urllib2

url = raw_input("Enter hostname target : ")
u = "http://"
link = u + url
uri = urllib2.urlopen(link)

if uri.getcode() == 200:
    print uri.headers
