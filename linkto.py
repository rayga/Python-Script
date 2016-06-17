# Script for grabbing link in a website
__author__ = 'n4rut0'

import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter hostname target : ")
u = "http://"
uri = u + url
read_page = uri.read()
parser = BeautifulSoup(read_page, "html.parser")
print parser.title
print parser.title.text
for link in parser.find_all('a'):
    print(link.get('href'))
