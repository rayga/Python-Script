Perbedaan script python ini dengan script server sebelumny adalah pada code "s.settimeout()"

__author__ = 'n4rut0'

import socket

hostname = raw_input("Enter hostname : ")
port = int(raw_input("Enter port number : "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, port))
s.settimeout(5) #Jika tertulis 5, berarti durasinya adalah 5 Detik
data, addr = s.recvfrom(1024)
print "Received from ", addr
print "Obtained ", data, " Bytes"
s.close()

