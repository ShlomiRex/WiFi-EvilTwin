sudo apt-get update && sudo apt-get install hostapd dnsmasq apache2 -y
mkdir /var/log/WiFi-EvilTwin/
touch /var/log/WiFi-EvilTwin/dnsmasq.log
echo "Starting apache2 web server at localhost:80"
service apache2 start
