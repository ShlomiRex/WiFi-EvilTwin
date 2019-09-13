#run as python3

#dep: net-tools, hostapd, dnsmasq, ip, nmcli (if you using ubuntu's NetworkManager), iptables

import os
import platform
import time

#TODO: don't use killall dnsmasq because kali linux uses it as default dns client/server.

# Default configuration
iface = "wlx000f00fa480f" #hostapd iface (AP will be listening here)
iface_ip = "10.0.0.1"
dnsmasq_port = 5353 #We don't want to interfere with default local dns on your machine, so we create another but on diffirent port


def start_monitor():
    os.system("sudo ifconfig %s down" % (iface))
    os.system("sudo iwconfig %s mode monitor" % (iface))
    os.system("sudo ifconfig %s up" % (iface))

def set_iface_ip():
    os.system("sudo ip addr add %s dev %s" % (iface_ip, iface))

def start_dnsmasq():
    os.system("sudo killall dnsmasq | cat /dev/null")
    print("Starting dnsmasq")
    os.system("sudo dnsmasq -C conf/dnsmasq.conf -p %s" % (dnsmasq_port) )

def disable_hostapd_manage_iface():
    distro_name = platform.linux_distribution()[0]
    print("Are you using NetworkManager? (Ubuntu) [Y/n]")
    user_input = input()
    if user_input in ["Y", "y", ""]:
        #If using NetworkManager (Ubuntu), set in unmanaged. (hostapd will manage the device instead)
        os.system("sudo nmcli d set %s managed no" % (iface))
    else:
        print("Not yet implimented.") #TODO: Fix

def start_hostapd():
    #When user enters interface name, change conf file
    with open("conf/hostapd.conf", "r") as f:
        content = f.readlines()

    if content[0] != "interface=%s" % (iface) + "\n":
        #Write interface name to conf file
        with open("conf/hostapd.conf", "w") as f:
            content[0] = "interface="+iface+"\n"
            f.truncate()
            for line in content:
                f.write(line)

    os.system("sudo killall hostapd")
    print("Starting hostapd (conf/hostapd.conf)")
    os.system("sudo hostapd conf/hostapd.conf")


print("Wireless interface name(default is '%s'):" % (iface))
user_input = input()
if user_input != "":
    iface = user_input

start_monitor()
#set_iface_ip()
start_dnsmasq()
disable_hostapd_manage_iface()
start_hostapd()