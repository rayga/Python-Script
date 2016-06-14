__author__ = 'n4rut0'

import socket
wireless = socket.socket(socket.AF_INET, socket.SOCK_RAW, 3)
wireless.bind(("mon0",0x0003)
ap_list = []

while True:
  fm1 = wireless.recvfrom(6000)
  fm = fm1[0]
  if fm[26] == "\x80" 
    if fm[36:42] not in ap_list:
      ap_list.append(fm[36:42])
      a = ord(fm[63])
      print "SSID -->",fm[64:64+a], " BSSID --> ", fm[36:42].encode('hex'), " Channel --> ", ord(fm[64 + a + 12])
      
