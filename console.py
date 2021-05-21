import os
from utils import select_interface
from prettytable import PrettyTable
from networking import WifiScan, start_hostapd, scan_wifi
from typing import List
from conf import hostapd_read_iface, init_hostapd_conf
import time

def check_root():
	USER_ID = os.geteuid()
	if USER_ID != 0:
		print("You must run this script as root.")
		exit()

def user_input_Yn(text):
	choice = input(text)
	if choice == 'Y' or choice == 'y' or choice == '':
		return True
	else:
		return False

def user_input_yN(text):
	choice = input(text)
	if choice == 'N' or choice == 'n' or choice == '':
		return False
	else:
		return True

def print_wifi_scan_result(res: List[WifiScan]):
	x = PrettyTable()

	x.field_names = ["Row", "ESSID", "Address",
					 "Channel", "Power", "Frequency"]

	# Sort by power
	res.sort()

	i = 1
	for wifiscan in res:
		x.add_row([i, wifiscan.essid, wifiscan.address,
				  wifiscan.channel,  wifiscan.power, wifiscan.freq])
		i += 1
	print(x)

def choose_wifiscan(interface, scan_tries=3) -> WifiScan:
	def scan() -> List[WifiScan]:
		print('Scanning...')

		tries = 0
		res = scan_wifi(interface)
		while res == []:
			print("Scanning again, scan result was empty...")
			res = scan_wifi(interface)
			tries += 1
			if tries == scan_tries:
				return None

		print_wifi_scan_result(res)
		return res

	user_input = None
	while user_input is None or user_input in ["0", ""]:
		res = scan()
		if res is None:
			return None

		user_input = input('Choose row (or 0 to re-scan): ')
		if user_input in ["0", ""]:
			continue
		try:
			row = int(user_input) - 1 # Minus 1 because row in UI starts at 1
			return res[row]
		except ValueError:
			print("Could not parse row. Please try again.")
			user_input = None
		except IndexError:
			print("Please enter valid row number.")
			user_input = None


def start_ap():
	iface = hostapd_read_iface()
	print("Starting Access Point on interface: " + iface)
	p = start_hostapd(iface, "conf/hostapd.conf")

if __name__ == "__main__"	:
	check_root()

	# Choose iface to scan wifi
	print("Please select interface used to scan Wifi beacons\n")
	iface = select_interface()
	print("Interface: " + iface)

	# Choose beacon to mock / create Evil Twin on
	wifiscan = None
	sure = False
	while wifiscan is None:
		print("Please choose beacon to create Evil Twin\n")
		wifiscan = choose_wifiscan(iface)
		if wifiscan is None and not sure:
			yn = user_input_yN("Are you sure you selected the right interface? [y/N] ")
			if not yn:
				print("Please select interface used to scan Wifi beacons\n")
				iface = select_interface()
				print("Interface: " + iface)
			else:
				sure = True

	# Use conf file for AP
	init_hostapd_conf(wifiscan)
	start_ap()
	print("AP is running...")


	time.sleep(60)
