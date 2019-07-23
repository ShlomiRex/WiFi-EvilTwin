echo "Killing all dnsmasq processes..."
killall dnsmasq
echo "Starting dnsmasq..."
dnsmasq -C conf/dnsmasq.conf
