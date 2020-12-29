import os
print("Interfaces:")
os.system('sudo iwconfig')
old_inter = input("Type in old interface name:")
new_inter = input("Type in new interface name:")
os.system("sudo ifconfig "+old_inter+" down")
os.system("sudo ip link set "+old_inter+" name "+new_inter)
os.system("sudo ifconfig "+new_inter+" up")
print("Successfuly changed interface \'"+old_inter+"\' to \'"+new_inter)
