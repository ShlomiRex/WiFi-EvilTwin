import configparser
from utils import select_interface
from networking import WifiScan
import os


HOSTAPD_CONF = "conf/hostapd.conf"

hostapd_config = configparser.ConfigParser()


def hostapd_read_iface() -> str:
	print("Reading hostapd conf file: " + HOSTAPD_CONF)
	with open(HOSTAPD_CONF) as file:
		hostapd_config.read_string("[root]\n" + file.read())
		return hostapd_config["root"]["interface"]


def hostapd_change_iface(new_iface: str):
	with open(HOSTAPD_CONF, "r") as file:
		lines = file.readlines()
		for line in lines:
			if "interface=".lower() in line.lower():
				line = "interface="+new_iface
	with open(HOSTAPD_CONF, "w") as file:
		file.writelines(lines)

def create_hostapd_conf(iface: str, ssid: str, channel: int):
	os.makedirs("conf", exist_ok=True)

	with open(HOSTAPD_CONF, "w") as file:
		file.writelines(f"interface={iface}\ndriver=nl80211\nssid={ssid}\nchannel={channel}")

def print_hostapd_conf():
	with open(HOSTAPD_CONF) as file:
		print(file.read())

def init_hostapd_conf(wifiscan: WifiScan):
	if not os.path.exists(HOSTAPD_CONF):
		print("hostapd configuration file doesn't exist; Creating one now...")

		print("Please select interface for creating Wifi access point on\n")
		iface = select_interface()
		create_hostapd_conf(iface, wifiscan.essid, wifiscan.channel)
		print("Using hostapd conf file: " + HOSTAPD_CONF + "\n")
		print_hostapd_conf()
	else:
		print("hostapd conf file exists: " + HOSTAPD_CONF + "\n")
		print_hostapd_conf()