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
