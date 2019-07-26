# WiFi-EvilTwin 
Create wifi AP that enables users to browse the internet

Highly customizable (simple bash scripts)

You can also run deauth attack (to disconnect all clients, so then they automatically connect to you)
https://github.com/ShlomiRex/WiFi-Deauthernticator

====================================================

## Dependencies

* hostapd - Host AP

Default configuration: /etc/hostapd/hostapd.conf

Used to open AP wirelessly.


* dnsmasq - DHCP server + DNS server

Default configuration: /etc/dnsmasq.conf

Used to assign IP for clients on AP.

====================================================

## Requierments 

You need Debian based OS. This tool was tested on Kali 2018, but should work with every linux distrubution

## Usage 

To automatically run:
$ python console.py


## Logs 
Logs located at:
/var/log/WiFi-EvilTwin

You can also log with dnsspoof.

Usage:
$ dnsspoof -i <name of interface of AP>


## Troubleshooting

### Obtaining IP address...
When you try to connect to the AP, and you see this message or something simillar, the problem is with dnsmasq, spesifically with DHCP. Please check you'r configuration.

### dnsmasq and systemd-resolv
Please check that the systemd-resolv does not uses port 53. If it does, then kill it by:

$ killall systemd-resolv

### hostapd spitting out errors / AP not started
Please make sure to run the command:
$ airmon-ng check kill

This will eliminate any server that interfers with hostapd.


## Links 
https://nims11.wordpress.com/2012/04/27/hostapd-the-linux-way-to-create-virtual-wifi-access-point/             # This one really works well for me

https://askubuntu.com/questions/21679/how-to-stop-wireless-ap-hosting-using-network-manager-on-ubuntu

https://www.raspberrypi.org/forums/viewtopic.php?t=128150

https://wiki.gentoo.org/wiki/Hostapd#802.11b.2Fg.2Fn_triple_AP

https://forums.hak5.org/topic/37033-no-access-to-my-fake-ap/

https://rootsh3ll.com/evil-twin-attack/
