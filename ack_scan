from scapy.all import *

ip1 = IP(src="10.133.1.153",dst="10.133.1.181")
sy1 = TCP(sport=1024, dport=137, flags="A", seq=12345)
packet = ip1/sy1
p = sr1(packet)
p.show()
