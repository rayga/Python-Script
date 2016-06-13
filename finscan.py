#Beberapa firewall dan IDS biasanya mengkonfigurasi untuk mendisable SYN Scans dari hostname lainnya.
#Untuk mengakali hal tersebut, maka digunakanlah FIN scan, yang hanya mengirimkan flag FIN saja ke hostname target.
#Ketika flag FIN dikirim, dan tidak ada response dari hostname target, itu berarti port nya terbuka.
#Jika local hostname kita menerima response flag RST (Reset) / ACK (Acknowledge) maka port nya tertutup

__author__ = 'n4rut0'

from scapy.all import *

hostname = raw_input("Enter local hostname : ")
target = raw_input("Enter target hostname : ")

ip1 = IP(src=hostname, dst=target)
syn1 = TCP(sport=1024, dport=80, flags="F", seq=12345)
packet=ip1/syn1
s = sr1(packet, inter=1)
s.show()
