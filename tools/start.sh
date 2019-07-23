echo ">>> Starting Monitor Mode"
bash start-monitor.sh

echo ">>> Setting interface ip"
bash set-interface-ip.sh

echo ">>> Starting dnsmasq"
bash start-dnsmasq.sh

echo ">>> Enabling NAT"
bash enable-nat.sh

echo ">>> Starting hostapd"
bash start-hostapd.sh
