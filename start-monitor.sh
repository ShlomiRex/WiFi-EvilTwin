inter=wlan0

ifconfig $inter down
iwconfig $inter mode monitor
ifconfig $inter up
