__author__ = 'n4rut0'

from socket import *
import sys, time
from datetime import datetime

host = ""
min_port = int(raw_input("[*] Min Port : "))
max_port = int(raw_input("[*] Max Port : "))

def scan_host(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host,port))

        if code == 0:
            s.close()
    except Exception,e:
        pass

    return code

try:
    host = raw_input("[*] Enter Target Hostname : ")
except KeyboardInterrupt:
    print("\n\n[*] User Requested An Interrupt. ")
    print("\n\n[*] Application Shutting Down.")
    sys.exit(1)

hostip = gethostbyname(host)
print("\n[*] Host: %s IP: %s" % (host, hostip))
print("[*] Scanning Started at %s..\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port,max_port):
    try:
        response = scan_host(host, port)
        if response == 0:
            print("[*] Port %d: Open" %(port))
    except Exception, e:
        pass

stop_time = datetime.now()
total_time_duration = start_time + stop_time
print("\n[*] Scanning Finished at %s ..."%(time.strftime("%H:%M:%S")))
print("[*] Scaninng Duration : %s ..." %(total_time_duration))
print("[*] Have a nice day !!! ... Rayga Lightscene")



