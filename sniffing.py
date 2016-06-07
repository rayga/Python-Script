import struct
import socket

hostname = raw_input("Enter hostname target : ")
port = int(raw_input("Enter port number : ")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((hostname,port))
s.listen(1)
conn, addr = s.accept()

print "Connected by ", addr
msz = struct.pack('hhl',1,2)
conn.send(msz)
conn.close()


