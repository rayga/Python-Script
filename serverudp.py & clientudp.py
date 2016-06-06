#### serverudp.py #####

__author__ = "n4rut0"

import socket

hostname = raw_input("Enter hostname : ")
port = int(raw_input("Enter port number : ")

s = socket.socket(AF_INET, SOCK_DGRAM)
s.bind((hostname,port))
data, addr = recvfrom(1024)
print "Received from : ", addr
print "Obtained : ", data , "bytes"

s.close()

#### clientudp.py ####

__author__ = "n4rut0"

import socket

hostname = raw_input("Enter hostname : ")
port = int(raw_input("Enter port number : ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("Hello all", (hostname, port))
s.close()
