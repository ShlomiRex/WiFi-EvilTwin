import os
import collections

os.chdir(r"tools/")

scripts = collections.OrderedDict()


def init_scripts():
	global scripts

	tools_scripts = [f for f in os.listdir('.') if os.path.isfile(f)]
	for s in tools_scripts:
		abs_path = os.path.abspath(s)
		scripts[s] = abs_path

	tools_other_scripts = [f for f in os.listdir(r"other/") if os.path.isfile(os.path.join("other/", f))]
	for s in tools_other_scripts:
		abs_path = os.path.abspath(os.path.join("other/", f))
		scripts[s] = abs_path

	

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
	i = 0
	for k,v in scripts.items():
		print str(i)+') ',k,'                ',v
		i += 1
	ind = user_input_from_to(0, len(scripts)-1)
	choice = scripts.items()[ind]
	
	script_filename = choice[0]
	script_abs_path = choice[1]

	print 'Choosing \'' + str(script_filename) + '\'...'
	file_extension = os.path.splitext(script_abs_path)
	if file_extension[1] == '.sh':
		os.system("bash " + str(script_abs_path))
	elif file_extension[1] == '.py':
		os.system("python " + str(script_abs_path))
	else:
		print 'ERROR'

def first_screen():
	print 'WiFi-EvilTwin\n'
	yn = user_input_Yn('Automatic start?(Y/n)')
	if yn:
		os.system("bash start.sh")
	else:
		print_scripts()





if __name__ == "__main__"	:
	init_scripts()
	first_screen()


