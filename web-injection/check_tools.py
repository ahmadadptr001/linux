# default library python

import os, re, sys, time
from subprocess import getoutput

# customize library anon011Enjinering

from color import *


# clear terminal

os.system('cls') if os.name == 'nt' else os.system('clear')









# checking mode:  mode must in root mode

if os.geteuid() != 0:
	print(f"\n\n\t\t\t{onRed} Change your linux in mode root, use command: $ sudo su {default}{white}\n")
	sys.exit()










# checking dalfox

prompt_export_dalfox = "export $PATH:$HOME/go/bin"
prompt_check_dalfox = "dalfox"

alert_dalfox_error = "Command 'dalfox' not found"
alert_dalfox_success = "Dalfox is a powerful open-source XSS scanner and utility focused on automation."

result_dalfox_prompt = getoutput(f"{prompt_export_dalfox}; {prompt_check_dalfox}")

if re.findall ( alert_dalfox_error, result_dalfox_prompt ):

	print (f"{white}[{red}!{white}] Your {onyellow}must{default}{white}installing {red}dalfox{white} before use {yellow}this tool")

	yes_or_no = input (f"{white}[{yellow}*{white}] You want to {yellow}install{white} dalfox? [{yellow}y{white}/n] ")

	if yes_or_no in ["Y", "y"]:

		os.system('clear')
		os.system("apt-get install go");
		os.system("go install github.com/hahwul/dalfox/v2@latest")

		print (f"\n{white}[{green}✔{white}] Success {green}installing{white} dalfox\n")

		time.sleep(1)

	else:
		os.system('clear')
		print(f"white[{cyan}i{white}] {green}see you next time{white}\n\t\t\t--anon011Enjinering")
		sys.exit()













# checking requirements

list_library = "inquirer,certifi,chardet,idna,requests,urllib3".split(",")

for lib in list_library:


	result_check_library = getoutput(f"pip show {lib}")
	result_error = "WARNING: Package"


	if not re.findall ( result_error, result_check_library ):
		print (f"{white}[{green}✔{white}] Found {green}{lib}{white}")

	else:

		print (f"{white}[{red}!{white}] Not found {red}{lib}{white}")
		print (f"\n{yellow}installing library/module {lib}{white}\n")

		time.sleep(1)

		os.system('clear')
		os.system(f"pip install {lib}")
		os.system('clear')



time.sleep(0.5)

os.system('clear')
print (f"{white}[{cyan}i{white}] running {cyan}tools{white}..")
time.sleep(1)













