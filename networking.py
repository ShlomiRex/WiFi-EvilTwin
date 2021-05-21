import os
import subprocess
from dataclasses import dataclass
import re
from typing import List
from enum import Enum


@dataclass
class WifiScan:
	channel: int
	address: str
	freq: str
	power: str
	essid: str
	mode: str

	def __lt__(self, other):
		return self.power < other.power

class iface_mode(Enum):
	MONITOR = "monitor"
	MANAGED = "managed"

def change_iface_mode(iface: str, mode: iface_mode):
	os.system(f"ifconfig {iface} down")
	os.system(f"iwconfig {iface} mode {mode.value}")
	os.system(f"ifconfig {iface} up")	

def start_managed_mode(iface: str):
	print("Setting managed mode for iface: " + iface)
	change_iface_mode(iface, iface_mode.MANAGED)

def start_monitor_mode(iface: str):
	print("Setting monitor mode for iface: " + iface)
	change_iface_mode(iface, iface_mode.MONITOR)

def set_iface_ip(iface: str, ip: str):
	os.system(f"sudo ip addr add {ip}/24 dev {iface}")

def set_channel(iface: str, channel: int):
	os.system(f"sudo iwconfig {iface} channel {str(channel)}")

def start_apache():
	os.system("sudo service apache2 restart")
	os.system("sudo service apache2 start")

def start_hostapd(iface: str, conf_path: str) -> subprocess.Popen:
	# Note: iface is the interface in the conf_path.
	# Note: hostapd already sets iface to Master mode. No need to do that manually.
	return subprocess.Popen(f"sudo hostapd {conf_path}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

def scan_wifi(interface: str) -> List[WifiScan]:
	"""
	Scan wifi and return result.
	"""
	ret = []

	# Scan wifi
	result = subprocess.run(
		['iwlist', interface, 'scan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out = result.stdout.decode()
	
	# Read output with custom regex and save to "filtered_matches"
	pattern = r'(Cell \d+.*\n(?:\s{20}.*\n)+)'
	compiled_pattern = re.compile(pattern, re.MULTILINE)

	m = re.findall(compiled_pattern, out)

	# filtered_matches = []
	# for match in m:
	#     lines = match.split('\n')
	#     # Remove IE: Unkown: lines
	#     lines = [line for line in lines if "IE: Unknown:" not in line]
	#     filtered_matches.append(lines)

	# for cell in filtered_matches:
	#     address = re.search("Address: (.*)", cell[0]).group(1)
	#     channel = int(re.search("Channel:(\d+)", cell[1]).group(1))
	#     freq = re.search("Frequency:(.+GHz)", cell[2]).group(1)
	#     power = re.search("Signal level=(.*dBm)", cell[3]).group(1)
	#     essid = re.search("ESSID:\"(.*)\"", cell[5]).group(1)
	#     mode = re.search("Mode:(.*)\n", cell[9]).group(1)

	#     wifiscan = WifiScan(channel, address, freq, power, essid, mode)
	#     ret.append(wifiscan)

	for match in m:
		address = re.search("Address: (.*)", match).group(1)
		channel = int(re.search("Channel:(\d+)", match).group(1))
		freq = re.search("Frequency:(.+GHz)", match).group(1)
		power = re.search("Signal level=(.*dBm)", match).group(1)
		essid = re.search("ESSID:\"(.*)\"", match).group(1)
		mode = re.search("Mode:(.*)\n", match).group(1)
		wifiscan = WifiScan(channel, address, freq, power, essid, mode)
		ret.append(wifiscan)

	return ret

