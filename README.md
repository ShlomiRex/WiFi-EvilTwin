# WiFi-EvilTwin 
Create wifi AP that enables users to browse the internet
Highly customizable (simple bash scripts)

You can also run deauth attack (to disconnect all clients, so then they automatically connect to you)
https://github.com/ShlomiRex/WiFi-Deauthernticator

====================================================

hostapd - Host AP
Configuration: /etc/hostapd/hostapd.conf
Used to open AP wirelessly.

dnsmasq - DHCP server
Configuration: /etc/dnsmasq.conf
Used to assign IP for clients on AP.

====================================================

## Requierments 

You need Debian based OS. This tool was tested on Kali 2018, but should work with every linux distrubution

## Usage 

To automatically run:
$ bash start.sh

To manually run:

* Run setup.sh (Only run it once. Installs dependencies)
* Run start-monitor.sh
* Run set-interface-ip.sh
* Run start-dnsmasq.sh
* Run start-hostapd.sh

There you go


## Logs 
Logs located at:
/var/log/WiFi-EvilTwin

dnsmasq.log - is the DHCP server logs (logs queries and dns requests)


## Troubleshooting

### dnsmasq and systemd-resolv
Please check that the systemd-resolv uses port 53. If it does, then kill it by:
$ killall systemd-resolv


## Links 
https://nims11.wordpress.com/2012/04/27/hostapd-the-linux-way-to-create-virtual-wifi-access-point/             # This one really works well for me
https://askubuntu.com/questions/21679/how-to-stop-wireless-ap-hosting-using-network-manager-on-ubuntu
https://www.raspberrypi.org/forums/viewtopic.php?t=128150
https://wiki.gentoo.org/wiki/Hostapd#802.11b.2Fg.2Fn_triple_AP
https://forums.hak5.org/topic/37033-no-access-to-my-fake-ap/
https://rootsh3ll.com/evil-twin-attack/
