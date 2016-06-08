#### struct.py ####
__author__ = 'n4rut0'
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

#### unstruct.py ####

import struct
import socket

hostname = raw_input('Enter hostname target : ")
port = int(raw_input('Enter port number : ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
msg = s.recv(1024)
print msg
print struct.unpack('hhl',msg)
s.close()

##### Real Sniffing #####
__author__ = 'n4rut0'

import socket
import struct
import binascii

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x800))

while True:
    pkt = recvfrom(2048)
    ethead = pkt[0][0:14]
    eth = struct.unpack("!6s6s2s",pkt)
    
    print "Destination Mac address ", binascii.hexlify(eth[0])
    print "Source Mac Address ",binascii.hexlify(eth[1])
    binascii.hexlify(eth[2])
    
    ipheader = pkt [0][14:34]
    ip_hdr = struct.unpack("!12s4s2s",ipheader)
    
    print "Source IP ", socket.inet_ntoa(ip_hdr[1])
    print "Destination IP ", socket.inet_ntoa(ip_hdr[2])
    
    tcpheader = pkt[0][34:54]
    tcp_hdr = struct.unpack("!HH9ss6s",tcpheader)
    
    print "Source port ",tcp_hdr[0]
    print "Destination port ",tcp_hdr[1]
    print "Flag ", binascii.hexlify(tcp_hdr[3])



