__author__ = 'n4rut0'

from scapy.all import *

hostname = raw_input("[*]Enter local hostname : ")
target = raw_input("[*]Enter target hostname : ")

ip1=IP(src=hostname,dst=target)
tcp1 = TCP(sport=1024, dport=80, flags="S",seq=12345)
packet = ip1/tcp1
p = sr1(packet, inter=1)
p.show()

tcp2 = TCP(sport=1024, dport=80, flags="R", seq=12347)
packet1 = ip1/tcp2
p1 = sr1(packet1, inter=1)
p1.show()



