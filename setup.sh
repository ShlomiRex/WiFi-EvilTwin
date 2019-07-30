sudo apt-get update && sudo apt-get install hostapd dnsmasq apache2 php7.x libapache2-mod-php7.x libapache2-mod-php -y
sudo a2enmod php5 #enable php to run in apache2
mkdir /var/log/WiFi-EvilTwin/
touch /var/log/WiFi-EvilTwin/dnsmasq.log
echo "Starting apache2 web server at localhost:80"
service apache2 start
sudo systemctl status apache2
