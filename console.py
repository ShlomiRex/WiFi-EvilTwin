import os

os.chdir(r"tools/")

scripts = list()


def init_scripts():
	global scripts
	tools_scripts = [f for f in os.listdir('.') if os.path.isfile(f)]
	for s in tools_scripts:
		scripts.append(s)

	tools_other_scripts = [f for f in os.listdir(r"other/") if os.path.isfile(os.path.join("other/", f))]

	for s in tools_other_scripts:
		scripts.append(s)
	

# x <= y <= z (included)
def user_input_from_to(fr, to):
	print 'Choose: ',fr,'-',to
	choice = input()
	
	if fr <= choice <= to:
		return choice
	print "You must enter correct input. Please try again"
	return user_input(fr, to)

def user_input_Yn(text):
	print text
	choice = raw_input()
	if choice == 'Y' or choice == 'y' or choice == '':
		return True
	else:
		return False

def print_scripts():
	for script in scripts:
		print str(scripts.index(script)) + ') ',script
	ind = user_input_from_to(0, len(scripts)-1)
	print 'Choosing ',scripts[ind]

def first_screen():
	print 'WiFi-EvilTwin\n'
	yn = user_input_Yn('Automatic start?(Y/n)')
	if yn:
		os.system("bash ../start.sh")
	else:
		print_scripts()













if __name__ == "__main__"	:
	init_scripts()
	first_screen()


