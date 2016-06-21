__author__ = 'n4rut0'

import os
import platform
from datetime import datetime

net = raw_input("Enter the network address : ")
net1 = net.split('.')
a = '.'
net2 = net1[0]+a+net1[1]+a+net[2]+a
st1 = int(raw_input("Enter starting host : ")
en1 = int(raw_input("Enter the last host : ")
en1 = en1 + 1

oper = platform.system()

if (oper == "Windows"):
  ping1 = "ping -n 1 "
elif (oper == "Linux"):
  ping1 = "ping -c 1 "
else:
  ping1 = "ping -c 1 "

t1 = datetime.now()
print "Scanning in progress...."
for ip in xrange(st1, en1):
  addr = net2 + ip
  comm = ping1 + addr
  response = os.popen(comm)
  for line in response.readlines():
    if(line.count("TTL")):
      break
    if(line.count("TTL")):
      print addr, "--> LIVE"
      
t2 = datetime.now()
total = t2 - t1
print "Scanning complete in ", total

####Revisi####

import os
import platform
from datetime import datetime

ip = raw_input("[*]Enter network address : ")
start = raw_input("[*]Enter start address : ")
end = raw_input("[*]Enter end address : ")
end = end + 1
os = platform.system()
split = ip.split(".")
a = "."
net = split[0] + a + split[1] + a + split[2]
ping = "ping -n 1 "

t1 = datetime.now()
print "Scanning host...."
for p in xrange(start,end):
  link = net + p
  req = ping + link
  res = os.popen(req)
  for opt in res.readlines():
    if opt.count("TTL"):
      print link, " : LIVE"
  
t2 = datetime.now()
total = t2 - t1
print "Scanning completed in % " %(total)

