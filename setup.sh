sudo apt update && sudo apt install apache2 hostapd dnsmasq -y
sudo a2enmod php5 #enable php to run in apache2
echo "Starting apache2 web server at localhost:80"
service apache2 start
sudo systemctl status apache2

# Allow port 67 for DHCP
sudo iptables -A INPUT -p tcp --dport 67 -j ACCEPT
sudo iptables -L


# DNSMASQ
sudo dnsmasq --test
service dnsmasq status
sudo dnsmasq --no-daemon --log-queries -C conf/dnsmasq.conf 

# HOSTAPD
sudo hostapd conf/hostapd2.conf

