#!/usr/bin/env/ python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)                           # Create object ARP request
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")           # Create package send
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request              # sum two pakcage
    arp_request_broadcast.show()




scan("10.0.2.1")