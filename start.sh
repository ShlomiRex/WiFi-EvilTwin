#bash setup.sh

#cd tools

echo "Starting Monitor Mode"
bash tools/start-monitor.sh
echo "Setting interface ip"
bash tools/set-interface-ip.sh

echo "Stopping hostapd"
bash tools/stop-hostapd.sh

echo "Starting dnsmasq"
bash tools/start-dnsmasq.sh
echo "Starting hostapd"
bash tools/start-hostapd.sh
