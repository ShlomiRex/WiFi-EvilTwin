########### Enable NAT ############
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE #eth0 is interface (NOT the interface you are using as AP station) for internet access. eth0 for me means ethernet cable connected to my home router.
iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

sysctl -w net.ipv4.ip_forward=1 #ENable ip forwarding
