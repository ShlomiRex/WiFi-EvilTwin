import os
import collections
import subprocess
from prettytable import PrettyTable
from networking import WifiScan, start_managed_mode, scan_wifi
from typing import List
import time

os.chdir("scripts/")

scripts = collections.OrderedDict()
flag = 0

USER_ID = os.geteuid()
if USER_ID != 0:
	print("You must run this script as root")
	exit()


# x <= y <= z (included)
def user_input_from_to(fr, to):
	print('Choose: ', fr, '-', to)
	choice = input()

	if fr <= choice <= to:
		return choice
	print("You must enter correct input. Please try again")
	return user_input(fr, to)


def user_input_Yn(text):
	print(text)
	choice = input()
	if choice == 'Y' or choice == 'y' or choice == '':
		return True
	else:
		return False


def print_scripts():
	try:
		i = 0
		for k, v in scripts.items():
			print(str(i)+') ', k)
			i += 1
		ind = user_input_from_to(0, len(scripts)-1)
		choice = scripts.items()[ind]

		script_filename = choice[0]
		script_abs_path = choice[1]

		print('Choosing \'' + str(script_filename) + '\'...')
		file_extension = os.path.splitext(script_abs_path)
		os.system("clear")
		if file_extension[1] == '.sh':
			os.system("bash " + str(script_abs_path))
		elif file_extension[1] == '.py':
			os.system("python " + str(script_abs_path))
		else:
			print('ERROR')
		print('Finished running', script_filename, '\n')
		print_scripts()

	except KeyboardInterrupt:
		print("\nThanks for using Wi-Fi EvilTwin script by Sagi Saada and Shlomi Domennko\n")

def print_wifi_scan_result(res: List[WifiScan]):
	x = PrettyTable()

	x.field_names = ["Row", "ESSID", "Address", "Channel", "Power", "Frequency"]
	
	# Sort by power
	res.sort()

	i = 1
	for wifiscan in res:
		x.add_row([i, wifiscan.essid, wifiscan.address, wifiscan.channel,  wifiscan.power, wifiscan.freq])
		i += 1
	print(x)


def choose_wifiscan(interface) -> WifiScan:
	def scan() -> List[WifiScan]:
		print('Scanning...')

		res = scan_wifi(interface)
		while res == []:
			print("Scanning again, scan result was empty...")
			time.sleep(1)
			res = scan_wifi(interface)

		print_wifi_scan_result(res)
		return res
	
	user_input = None
	while user_input is None or user_input in ["0", ""]:
		res = scan()

		print('Choose row (or 0 to re-scan):')
		user_input = input()
		if user_input in ["0", ""]:
			continue
		try:
			row = int(user_input)
			return res[row]
		except ValueError:
			print("Could not parse row. Please try again.")
		


def first_screen(interface: str):
	print(f'Setting {interface} to managed mode...')

	start_managed_mode(interface)

	essid = choose_wifiscan(interface)

	#print('Choose AP channel(leave blank for default):')
	#channel = input()

	#open('conf/hostapd.conf', 'w').close()
	# with open("conf/hostapd.conf", "a") as myfile:
	# 	myfile.write("interface=wlan0\n")
	# 	myfile.write("driver=nl80211\n")

	# with open("conf/hostapd.conf", "a") as myfile:
	# 	if essid != '':
	# 		myfile.write("ssid="+essid+"\n")
	# 	else:
	# 		myfile.write("ssid=Test\n")
	# 	if channel != '':
	# 		myfile.write("channel="+channel+"\n")
	# 	else:
	# 		myfile.write("channel=1\n")

	yn = user_input_Yn('Automatic start?(Y/n)')
	if yn:
		os.system("bash start.sh")
	else:
		print_scripts()


def available_interfaces():
	result = subprocess.run(['ip', 'link', 'show'], stdout=subprocess.PIPE)
	# Decode bytes to utf, then split lines (\n), then take only even indexes from the list
	out = result.stdout.decode().splitlines()[0::2]
	interfaces = []
	for line in out:
		split = line.split(" ")
		ifindex = int(split[0].replace(":", ""))
		ifname = split[1].replace(":", "")
		interfaces.append((ifindex, ifname))

	return interfaces


def select_interface():
	interfaces = available_interfaces()

	x = PrettyTable()
	x.field_names = ["iface index", "iface name"]
	x.add_rows(interfaces)

	print("Available interfaces:")
	print(x)
	print("Select interface (index or name): ")
	i = input()

	selected = None
	try:
		index = int(i)
		for (ifindex, ifname) in interfaces:
			if ifindex == index:
				return ifname
	except ValueError:
		for (ifindex, ifname) in interfaces:
			if ifname == i:
				return ifname
		print("WRANING: You selected unrecognized interface")
		return i


if __name__ == "__main__"	:
	interface = select_interface()
	print("Interface selected: " + interface)
	first_screen(interface)
