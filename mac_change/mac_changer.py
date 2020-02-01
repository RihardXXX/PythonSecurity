#!/usr/bin/env python

# program for changed mac-adress


import subprocess       # Modul for call
import optparse         # Modul for parse string
import re               # Modul refular expression

"""~sudo ifconfig~ show list interface computer"""

def get_arguments():
    parser = optparse.OptionParser()                                            # Create object parser
    """i and m it`s key for commandline start scripts, dest it`s value enter last key user"""
    parser.add_option("-i", "--interface", dest="interface", help="-i = key for enter interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="-m = key for enter new mac adress")
    (value, key) = parser.parse_args()                                           # return two value
    if not value.interface:
        parser.error("[-] Please specify an interface, more info -help")
    elif not value.new_mac:
        parser.error("[-] Please specify an mac address, more info -help")
    return value


def change_mac_adress(interface, new_mac):
    print("[+] Changed Mac adress for " + interface + " to " + new_mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])                    # stop mac-adress
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])    # install new mac-adress
    subprocess.call(["sudo", "ifconfig", interface, "up"])                      # new mac-adress activate

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["sudo", "ifconfig", interface])              # result work command
    mac_adress_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) # search mac address return list
    if mac_adress_search_result:
        return mac_adress_search_result.group(0)  # 0 number result
    else:
        print("[-] Could not read Mac address")

value = get_arguments()                                                         # result function add variable

curent_mac = get_current_mac(value.interface)
print("Current mac = " + str(curent_mac))

change_mac_adress(value.interface, value.new_mac)                               # run function
curent_mac = get_current_mac(value.interface)
if curent_mac == value.new_mac:                                                 # comparing current and past mac
    print("[+] Mac address was successfully changed to " + curent_mac)
else:
    print("[-] Mac address did not get changed")





