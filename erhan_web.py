__author__ = 'n4rut0'

import re
import urllib2
import sys

url = raw_input("Enter URL target : ")
u = http://
url1 = u + url
uri = urllib2.urlopen(url1)

a = raw_input("Enter search tag : ")

content = uri.read()
flag = 1
i = 0
list = []
file_text = open("error_web",a)
while flag==0:
      if uri.getcode() == 404:
          file_text.write("-"*20)
          file_text.write(uri)
          file_text.write("-"*20)
          file_text.write(content)
          
          for match in re.finditer(a,content):
              a = match.start()
              b = match.end()
              list.append(a)
              list.append(b)
              if len(list)>0:
                  print "Coding is not good"
                  x = list[0]
                  y = list[1]
                  print content[a:b]
              else:
                  print "Error handling seems good"
      elif uri.getcode() == 200:
          "Web is OK"
          
              
              
          
      
      

