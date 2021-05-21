########### Enable NAT ############
sudo sysctl -w net.ipv4.ip_forward=1 #ENable ip forwarding

# NAT table in iptables, add to POSTROUTING 
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE #eth0 is interface (NOT the interface you are using as AP station) for internet access. eth0 for me means ethernet cable connected to my home router.
sudo iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan1 -o wlan0 -j ACCEPT


##############################
##############################
sudo iptables -A FORWARD -i wlan1 -o wlan0 -j ACCEPT
modprobe ip_conntrack
sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
sudo iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT



sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE #eth0 is interface (NOT the interface you are using as AP station) for internet access. eth0 for me means ethernet cable connected to my home router.
sudo iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan1 -o wlan0 -j ACCEPT