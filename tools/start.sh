echo ">>> Enableing Monitor Mode"
bash start-monitor.sh

echo ">>> Setting interface ip"
bash set-interface-ip.sh

echo ">>> Enableing NAT"
bash enable-nat.sh

echo ">>> Killing dnsmasq"
bash other/stop-dnsmasq.sh

echo ">>> Starting dnsmasq"
bash start-dnsmasq.sh

echo ">>> Killing hostapd"
bash other/stop-hostapd.sh

echo ">>> Starting hostapd"
bash start-hostapd.sh
