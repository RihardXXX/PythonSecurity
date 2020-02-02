#!/usr/bin/env/ python

import scapy.all as scapy
from scapy.all import *

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)                           # Create object ARP request
    print(arp_request.summary())



scan("10.0.2.1/24")