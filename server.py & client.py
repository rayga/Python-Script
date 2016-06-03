#####Server Side#####
__author__ = 'n4rut0'

import socket

hostname = raw_input("Enter hostname : ")
port = int(raw_input("Enter port number : "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(hostname, port)
s.listen(2)
conn, addr = s.accept()
print addr, ("Now Connected !")
conn.send("Thank you for connecting !")
print conn.recv(1024)
conn.close()


#####Client Side#####
__author__ = 'n4rut0'

import socket

hostname = raw_input("Enter hostname : ")
port = int(raw_input("Enter port number : "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
print s.recv(1024)
s.send("Hallo server")
s.close()
