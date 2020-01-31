#!/usr/bin/env python

# program for changed mac-adress


import subprocess       # Modul for call
import optparse         # Modul for parse string

"""~sudo ifconfig~ show list interface computer"""

def get_arguments():
    parser = optparse.OptionParser()                                            # Create object parser
    """i and m it`s key for comandline start scripts, dest it`s value enter last key user"""
    parser.add_option("-i", "--interface", dest="interface", help="-i = key for enter interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="-m = key for enter new mac adress")
    (value, key) = parser.parse_args()                                           # return two value
    if not value.interface:
        parser.error("[-] Please specify an interface, more info -help")
    elif not value.new_mac:
        parser.error("[-] Please specify an mac adress, more info -help")
    return value


def change_mac_adress(interface, new_mac):
    print("[+] Changed Mac adress for " + interface + " to " + new_mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])                    # stop mac-adress
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])    # install new mac-adress
    subprocess.call(["sudo", "ifconfig", interface, "up"])                      # new mac-adress activate
    subprocess.call(["sudo", "ifconfig", interface])                            # help mac adress

value = get_arguments()                                                         # result function add variable
change_mac_adress(value.interface, value.new_mac)                               # run function







