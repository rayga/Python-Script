__author__ = 'n4rut0'

import socket
import sys

ip = raw_input("[*]Enter ipaddress/hostname : ")
min_port = 1
max_port = 1000

for portlist in range(min_port,max_port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = s.connect_ex((ip,portlist))
    if (result == 0):
       print portlist, "[",socket.getservbyport(portlis),"] : OPEN"
    s.close()
    
sys.exit()

####Update terbaru####

##########
import socket
import sys
from datetime import datetime

ip = raw_input("[*]Enter hostname target : ")
min = 1
max = 1150
print"Scanning proses...."
t1 = datetime.now()

try:
    for port in xrange(min,max):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((ip,port))
        if (result == 0):
            print port, "[ ",socket.getservbyport(port),"] : OPEN"
        s.close()
except KeyboardInterrupt:
    print "User interrupt keyboard"
    sock.close()
    t2 = datetime.now()
    total = t2 - t1
    print "Scanning completed in ",total

t2 = datetime.now()
total = t2 - t1
print "Scanning completed in ",total
sys.exit()

