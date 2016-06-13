#ACK Scan ini dilakukan untuk mengetahui apakah port dari suatu hostname tersebut protected oleh system filtering seperti Snort, iptables, dll.

__author__ = 'n4rut0'

from scapy.all import *

hostname = raw_input("Enter local hostname : ")
target = raw_input("Enter target hostname : ")

ip1 = IP(src=hostname, dst=target)
ack1 = TCP(sport=1024, dport=80,flags="A",seq=12345)

packet = ip1/ack1
sr = sr1(packet)
s.show()
