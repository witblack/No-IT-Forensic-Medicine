#!/usr/bin/python
# coding: latin-1
#---------------------------
# Writed By WitBlack HAcker
#---------------------------
#💬 Telegram:
#Https://t.me/WitBlack_ch
#
#💻 Web:
#Https://BugZone.ir
#
#📹 YouTube:
#https://www.youtube.com/channel/UCIgk2ldVeelyaHW3s4UkIIg (WitBlack)
#
#🎥 Aparat:
#Https://aparat.com/WitBlack
#
#⌨️ Github:
#Https://github.com/WitBlack
#
#📧 E-Mail:
#admin@bugzone.ir
try:
	from shutil import copyfile
	from shutil import rmtree
	from string import lower
	from termcolor import colored
	from time import sleep
	import os
except:
	print('Some Deepends not installed. Visit: Https://GitHub.com/WitBlack/No-IT-Forensic-Medicine')
	exit(1)
char_fill = [79] #79 is 'a' character - you can set oly from 33 to 126
file_names = 'a' * 255 #bigest size file for delete all inode lenth ( 255 character )
tmp_dir = '/dev/shm/'
addresses = []
big_file_address = '' #if don't have, set as ''
pow_of_big_file_size = 10485760 #by byte ( x2 value )
user_request_exit = colored("\n\nExited with user request.",'red')
if os.path.exists('/dev/'):
        OS = 'Linux'
elif os.path.exists('C:/'):
        OS = 'Windows'
else:
        print("your operation system don't suport!")
        exit(1)
def Clear():
	if OS == 'Linux':
		os.system('clear')
	else:
		os.system('cls')
def Banner():
	Clear()
	print(colored(' __     __     __      __        __         ','magenta') + colored('|','red') + colored(' No IT Forensic Medicine','cyan'))
	print(colored('/\ \   /\ \   /\ \    /\_\      /\ \        ','magenta') + colored('|','red') + colored(' _-_-_-_-_-_-_-_-_-_-_-_','green'))
	print(colored('\ \ \  \ \ \  \ \ \   \/_/     _\_\_\____   ','magenta') + colored('|','red'))
	print(colored(' \ \ \  \ \ \  \ \ \     __   /\_________\  ','magenta') + colored('|','red') + 'Web Site:')
	print(colored('  \ \ \  \ \ \  \ \ \   /\ \  \/___/\ \__/  ','magenta') + colored('|','red') + '	- Https://BugZone.ir')
	print(colored('   \ \ \__\_\ \__\_\ \  \ \ \      \ \ \    ','magenta') + colored('|','red') + 'Email:')
	print(colored('    \ \_____________\_\  \ \_\      \ \_\   ','magenta') + colored('|','red') + '	- admin@bugzone.ir')
	print(colored('     \/_______________/   \/_/       \/_/   ','magenta') + colored('|_____________________________','red') + "\n")
	print(colored(' ________     __     _________     ____________      __','magenta'))
	print(colored('/\  ____ \   /\ \   /\  _____ \   /\  ________/\    /\ \    __','magenta'))
	print(colored('\ \ \__/\ \  \ \ \  \ \_\___/\ \  \ \ \______/\ \   \ \ \  / /\\','magenta'))
	print(colored(' \ \ \_\_\ \  \ \ \  \/_/___\_\ \  \ \ \     \/_/__  \ \ \/ / /','magenta'))
	print(colored('  \ \  ____ \  \ \ \   /\  _____ \  \ \ \       /\ \  \ \ \/_/____ ','magenta'))
	print(colored('   \ \ \__/\ \  \ \ \  \ \ \___/\ \  \ \ \      \ \ \  \ \  ___ \ \\','magenta'))
	print(colored('    \ \ \_\_\ \  \ \ \  \ \ \__\_\ \  \ \ \______\/  \  \ \ \  \ \ \\','magenta'))
	print(colored('     \ \_______\  \ \_\  \ \________\  \ \___________/   \ \_\  \ \_\\','magenta'))
	print(colored('      \/_______/   \/_/   \/________/   \/__________/     \/_/   \/_/','magenta'))
	print("\nProgramed By WitBlack HAcker. - Git ~> Https://GitHub.com/WitBlack")
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print(colored('Warning:','red') + colored(" Don't break script while cleaning Inodes or Disk/RAM.",'yellow'))
	print(colored("VERSION ",'blue') + colored("1.0.0",'white'))
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
def fix(number):
	end = len(file_names) - len(str(number))
	string = file_names[0:end] + str(number)
	return string
Banner()
user_choose = raw_input("If you don't have big file we create it. Do you have a big file? [y/n] ")
if str.lower(user_choose) == 'y' or str.lower(user_choose) == 'yes':
	while True:
		try:
			Banner()
			big_file_address = raw_input("Enter address of your big file. If enter empty we ceate it.\nAddress: ")
			if big_file_address == '':
				break
			elif not os.path.isfile():
				Banner()
				print(colored("This file address don't exists or not is a file.\nTry again.",'yellow'))
				sleep(3)
			else:
				break
		except:
			print(user_request_exit)
Banner()
index = 1
while True:
	try:
		user_choose = raw_input("Enter your mounted device Address for clean.\nIf you don't have another address, enter empty.\nAddress" + str(index) + ': ')
	except:
		print(user_request_exit)
	Banner()
	if user_choose == '':
		if index > 1:
			break;
		else:
			print(colored("Invalid Choose. You don't entered any address so can't continue. Try again!",'yellow'))
	else:
		if os.path.isdir(user_choose):
			if user_choose[-1] != '/':
				user_choose=user_choose+'/'
			addresses.append(user_choose)
			index=index+1
		else:
			print(colored("Entered address don't exists or not is a directory! Try again.",'yellow'))
Banner()
try:
	user_choose = raw_input('Do You want use default configs? [y/n] ')
except:
	print(user_request_exit)
if str.lower(user_choose) == 'n' or str.lower(user_choose) == 'no':
	while True:
		try:
			Banner()
			user_choose = [int(raw_input("Enter number of character writen in files.\n( It only can between 33 to 126, Press enter empty for use default(79). )\n Number: "))]
			if user_choose[0] < 33 or user_choose[0] > 126:
				Banner()
				print(colored('Selected number is out of range. Try aganin.','yellow'))
				sleep(3)
			elif user_choose[0] == '':
				break
			else:
				char_fill=[user_choose[0]]
				break
		except:
			Banner()
			print(colored('Invalid Number! Try again.','yelllow'))
			sleep(2)
	while True:
		Banner()
		user_choose = raw_input("Enter your temp directory address.\nEnter empty to use default ( /dev/shm/ ( RAM Storage ))\nAddress: ")
		if user_choose == '':
			break
		if user_choose[-1] != '/':
			user_choose=user_choose+'/'
		if not os.path.isdir(user_choose):
			Banner()
			print(colored("Location not exists or not a directory!\nTry again.",'yellow'))
			sleep(3)
		else:
			if os.path.exists(user_choose + 'bigfile') or os.path.exists(user_choose + 'smalfile'):
				print(colored("Selected directory have file(s) named 'bigfile' or 'smalfile'.\nRename and try again.",'yellow'))
				sleep(5)
			else:
				tmp_dir=user_choose
				break
	while True:
		try:
			Banner()
			user_choose = int(raw_input("Enter pow of big file size.\nEnter empty to use default value.\n( this value only can between 1 to 104857600 (100 MB))\nValue: "))
			if user_choose == '':
				break
			elif user_choose < 1 or user_choose > 104857600:
				Banner()
				print(colored('Value is out of range! Try again.','yellow'))
				sleep(3)
			else:
				pow_of_big_file_size=user_choose
				break
		except:
			Banner()
			print(colored('Invalid value! Try again.','yellow'))
			sleep(2)
	while True:
		Banner()
		user_choose = raw_input("Enter name of files:\nEnter empty to use default name ( 255 'a' characters )\nWe suggest names with 255 characters.\nFiles Name: ")
		if len(user_choose) > 255:
			print(colored("Your file name so long. Try again.\nMax file name lenth: 255",'yellow'))
		elif len(user_choose) == 0:
			break
		else:
			if len(user_choose) < 255:
				user_choose2 = raw_input("Your file name so short. All Hard disk Inodes will not cleaned.\nContinue with entered file name? [y/n] ")
				if str.lower(user_choose2) == 'y' or str.lower(user_choose2) == 'yes':
					file_names=user_choose
					break
			else:
				file_names=user_choose
				break
if not os.path.isdir(tmp_dir):
	print(colored('[*] Temp directory not found! Creating "tmp_dir" directory inside of script...','yellow'))
	os.mkdir('tmp_dir')
	tmp_dir='tmp_dir'
	print('[*] Creating temp directory finished.')
file = open(tmp_dir + 'smalfile', 'wb')
for char in char_fill:
	file.write(str(char))
file.close()
print('[*] Start for delete Inodes...')
for address in addresses:
	os.mkdir(address + file_names)
	inode = 1
	try:
		while True:
			copyfile(tmp_dir + 'smalfile', address + file_names + '/' + fix(inode))
			inode=inode+1
	except:
		rmtree(address + file_names)
		print('[*] Inodes cleaned.')
if len(big_file_address) == 0:
	try:
		print('[*] Start creating big file...')
		file = open(tmp_dir + 'bigfile', 'wb')
		index = 1
		while index <= pow_of_big_file_size:
			for char in char_fill:
        			file.write(str(char))
			index=index+1
		file.close()
		print('[*] Big file created.')
	except:
		file.close()
		print(user_request_exit)
print('[*] Start for delete Disk/RAM...')
for address in addresses:
	try:
		os.mkdir(address + file_names)
		index = 1
		if len(big_file_address) > 0:
			while True:
				copyfile(big_file_address, address + file_names + '/' + fix(index))
				index=index+1
		else:
			while True:
				copyfile(tmp_dir + 'bigfile', address + file_names + '/' + fix(index))
				index=index+1
	except:
		rmtree(address + file_names)
		print('[*] Delete Disk/RAM "' + address + '" finished.')
print('[*] Delete big file and smal file...')
os.remove(tmp_dir + 'smalfile')
if len(big_file_address) == 0:
	os.remove(tmp_dir + 'bigfile')
print('[*] big file and smal file deleted.')
if os.path.isdir('tmp_dir'):
	print('[*] Temp directory inside script found. Deleting...')
	rmtree('tmp_dir')
	print('[*] Deleteing temp directory finished.')
input = raw_input('Disk cleened! Do you want reboot? [y/n]')
if lower(input) == 'y' or lower(input) == 'yes':
	if OS == 'Linux':
		os.system('reboot')
	else:
		os.system('shutdown /r /t 1')
else:
	print('Ok! Good By...')
