__author__ = "n4rut0"

import socket

hostname = raw_input("Enter hostname : ")
port = int(raw_input("Enter port number : ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
  s.bind((hostname, port))
  s.settimeout(60)
  data, addr = s.recvfrom(1024)
  print "Received from : ", addr
  print "Obtained : ", data
  s.close()
  
except socket.timeout:
  print "Client not connected"
  s.close()
