# WiFi-EvilTwin 
Create wifi AP that enables users to browse the internet


I'm currently working on my university projects. After that I will focus on this repo. 

## Upcoming
*  Automation
*  Ubuntu 18.04 LTS support
*  Remove hard-coded values to single conf file
*  Tutorial how to use
*  Research how to get Wifi to your evil machine without must-have ethernet cable
*  Allow full packet interception (all traffic) with Wireshark for hostapd
*  DNS2Proxy plugin



Highly customizable (simple bash scripts)

You can also run deauth attack (to disconnect all clients, so then they automatically connect to you)
https://github.com/ShlomiRex/WiFi-Deauthernticator

## Hardware requierments
2 wifi adapters with Monitor mode(for deauth) and Master mode(for AP station).

## Report
https://docs.google.com/document/d/1pRLTep1HHcjlyrZKoXwlNAHaTazGWdiJjDP2X9-b4Ag/edit#

## Dependencies

* hostapd - Host AP

Default configuration: /etc/hostapd/hostapd.conf

Used to open AP wirelessly.


* dnsmasq - DHCP server + DNS server

Default configuration: /etc/dnsmasq.conf

Used to assign IP for clients on AP.

## Requierments 

You need the Aptitude package manager (comes with debian) (You can install manually the dependencies). It is highly recommended to use Kali since it comes with dnsmasq instead of systemd-resolv (on ubuntu distros).

## Usage 
$ python console.py


## Logs 
Logs located at:
/var/log/WiFi-EvilTwin

You can also log with dnsspoof.

Usage:
$ dnsspoof -i <name of interface of AP>


## Troubleshooting

## DNS not working / No redirection on Mobile
Disable Mobile Data.

### Obtaining IP address...
When you try to connect to the AP, and you see this message or something simillar, the problem is with dnsmasq, spesifically with DHCP. Please check you'r configuration.

### dnsmasq and systemd-resolv
Please check that the systemd-resolv does not uses port 53. If it does, then kill it by:

$ killall systemd-resolv

### hostapd spitting out errors / AP not started
Please make sure to run the command:
$ airmon-ng check kill

This will eliminate any server that interfers with hostapd.

### Running AP with Deauth script
To create AP and use deauth script you need 2 wireless adapters capable of monitor mode / packet injection. Adapter 1 will be used as AP and the second will be used as deauth. You can manually run deauth script via the console, or by running $ python tools/deauth.py.

Make sure to set the channel of interface of adapter 2 to the channel of the AP you want to fake. You can find the channel by running the scan.sh script, or with the console.

### Enable internet to users on the AP
You need another adapter or ethernet cable. This adapter doesn't need to have monitor mode.

Manually change the enable-nat.sh, replace "eth0" with the adapter you have.

### Not redirecting users to my website / dnsmasq configuration not working
The script should killall dnsmasq before the start of dnsmasq. You can type killall dnsmasq before running the console.


## Links 
* https://nims11.wordpress.com/2012/04/27/hostapd-the-linux-way-to-create-virtual-wifi-access-point/             # This one really works well for me
* https://askubuntu.com/questions/21679/how-to-stop-wireless-ap-hosting-using-network-manager-on-ubuntu
* https://www.raspberrypi.org/forums/viewtopic.php?t=128150
* https://wiki.gentoo.org/wiki/Hostapd#802.11b.2Fg.2Fn_triple_AP
* https://forums.hak5.org/topic/37033-no-access-to-my-fake-ap/
* https://rootsh3ll.com/evil-twin-attack/
