Perbedaan script dibawah ini dengan script server.py & client.py adalah adanya penambahan code "bytearray".

####server2.py####

__author__ = 'n4rut0'

import socket

hostname = raw_input("Enter hostname : ")
port = int(raw_input(("Enter port number : ")))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((hostname, port))
s.listen(2)
conn, addr = s.accept()
print "Connected by ", addr
conn.send("Thanks")
print s.recv(1024)
s.close()

####client2.py####

__author__ = 'n4rut0'

import socket

hostname = raw_input("Enter hostname : ")
port = int(raw_input("Enter port number : "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
s.send("Hallo Server")
buf = bytearray("-" * 30)
print "Number by Bytes ", s.recv_into(buf)
print buf




