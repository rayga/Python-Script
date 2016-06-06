__author__ = 'n4rut0'

import socket
import sys
print''
print"##########"

MAX_PORT = 1000
MIN_PORT = 0

hostname = raw_input("[*]Enter hostname : ")
IP = raw_input("[*]Enter IP Address : ")

print "[*]IP address of ",hostname," is : ", socket.gethostbyname(hostname)
print "[*]IP Address list of ", hostname, "is : ", socket.gethostbyname_ex(hostname)

print "[*]Fully Qualified Domain Name (FQDN) of ",hostname, "is : ", socket.getfqdn(hostname)
print "[*]Reverse IP Address of ",IP, "is : ", socket.gethostbyaddr(IP)
print "[*]The active service of " ,IP, "is : ", socket.getservbyname('http')

print "[*]List of OPEN port..."
for portlist in range(MIN_PORT, MAX_PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((IP,portlist))
    if result == 0:
        print portlist, ": OPEN"
    s.close()

sys.exit()
