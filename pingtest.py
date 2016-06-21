#Script pingtest.py ini sebenarnya gabungan dari script sebelumnya yang sudah dibuat untuk melakukan ACK scan, FIN scan, dan SYN scan.
#Untuk mempermudahnya dan membuatnya lebih efisien, maka disatukanlah script tersebut

__author__ = 'n4rut0'

from scapy.all import *
import sys,getopt

flag =""
port = ""
ip = ""

myopts,args = getopt.getopt(sys.argv[:1],"i:p:f")

for o,a in myopts:
  if o == "-i":
    ip = a
  elif o == "-p":
    port = a
  elif o == "-f":
    flag = a
  else:
    print "Usage: % -i IPADDRESS -p PORT -f FLAGS(S/F/A)"
  
ip1 = IP(dst=ip)
tcp1 = TCP(sport =12345, dport=port, flags = flag, seq=1234)
packet = ip1/tcp1
p = sr1(packet)
p.show()
#p.summary()

