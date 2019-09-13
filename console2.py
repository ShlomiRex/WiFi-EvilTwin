#run as python3

#dep: net-tools, hostapd, ip, nmcli (if you using ubuntu's NetworkManager)

import os
import platform


# Default configuration
iface = "wlx000f00fa480f"
iface_ip = "10.0.0.1"


def start_monitor():
    os.system("sudo ifconfig %s down" % (iface))
    os.system("sudo iwconfig %s mode monitor" % (iface))
    os.system("sudo ifconfig %s up" % (iface))

def stop_monitor():
    os.system("sudo ifconfig %s down" % (iface))
    os.system("sudo iwconfig %s mode managed" % (iface))
    os.system("sudo ifconfig %s up" % (iface))

def set_iface_ip():
    os.system("sudo ip addr add %s dev %s" % (iface_ip, iface))

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

    distro_name = platform.linux_distribution()[0]
    print("Are you using NetworkManager? (Ubuntu) [Y/n]")
    user_input = input()
    if user_input in ["Y", "y", ""]:
        #If using NetworkManager (Ubuntu), set in unmanaged. (hostapd will manage the device instead)
        os.system("sudo nmcli d set %s managed no" % (iface))
    else:
        print("Not yet implimented.")


    print("Starting hostapd (conf/hostapd.conf)")
    os.system("sudo hostapd conf/hostapd.conf")


print("Wireless interface name(default is '%s'):" % (iface))
user_input = input()
if user_input != "":
    iface = user_input

start_monitor()
#set_iface_ip()
start_hostapd()