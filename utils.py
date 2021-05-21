

import subprocess

from prettytable.prettytable import PrettyTable


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

	def print_ifaces():
		x = PrettyTable()
		x.field_names = ["iface index", "iface name"]
		x.add_rows(interfaces)
		print("Available interfaces:")
		print(x)

	i = None
	while i is None:
		print_ifaces()
		i = input("Select interface (index or name): ")

		try:
			index = int(i)
			for (ifindex, ifname) in interfaces:
				if ifindex == index:
					return ifname
			print("You selected index out of range. Please try again.")
			i = None
		except ValueError:
			for (ifindex, ifname) in interfaces:
				if ifname == i:
					return ifname
			print("Please select valid interface.")
			i = None
