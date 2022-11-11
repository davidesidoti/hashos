#!/usr/bin/python3

#	.__                  .__                  
#	|  |__ _____    _____|  |__   ____  ______
#	|  |  \\__  \  /  ___/  |  \ /  _ \/  ___/
#	|   Y  \/ __ \_\___ \|   Y  (  <_> )___ \ 
#	|___|  (____  /____  >___|  /\____/____  >
#	     \/     \/     \/     \/           \/ 
#	****************************************************************
#	* Copyright of hashdeveloper, 2022                             *
#	* https://tryhackme.com/p/hashdeveloper                        *
#	****************************************************************

# This is the main file of the "hashos", a tool made by hashdeveloper to make
# penetration testing easier :)

# WARNING: Please remember, illegal activity is forbidden using hashos tool. All actions carried out using this tool are solely your responsibility.

# Import the functions file
import functions

# Import os module
import os

# Import socket module
import socket

# Import columnar modul
from columnar import columnar

# Help command to display the available commands
def help(cmd=""):
	if cmd == "":
		print(f"hashOS Version 0.0.2\nhttps://github.com/davidesidoti/hashos\n")
		help_table = [
			["help", "help [OPTIONAL: command]", "Display this help message or help for a specific command."],
			["clear", "clear", "Clear the current terminal."]
		]
		table = columnar(help_table, headers=["COMMAND", "USAGE", "DESCRIPTION"])
		print(table)
	elif cmd == "help":
		help_table = [
			["help", "help [OPTIONAL: command]", "Display this help message or help for a specific command."],
		]
		table = columnar(help_table, headers=["COMMAND", "USAGE", "DESCRIPTION"])
		print(table)
	elif cmd == "clear":
		help_table = [
			["clear", "clear", "Clear the current terminal."]
		]
		table = columnar(help_table, headers=["COMMAND", "USAGE", "DESCRIPTION"])
		print(table)
	
	__main__()

# Clear command to clean the terminal
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	__main__()

# Main function of the program
def __main__():
	# Get current working directory
	current_path = os.getcwd()

	# Get current IP address
	hostname=socket.gethostname()   
	IPAddr=socket.gethostbyname(hostname)

	cmd = input(f"{functions.bcolors.OKGREEN}root@{IPAddr}{functions.bcolors.ENDC}: {functions.bcolors.OKBLUE}{current_path}{functions.bcolors.ENDC}# ")
	args = []
	# Command check for arguments
	if len(cmd.lower().split(" ")) > 1:
		args = cmd.lower().split(" ")[1:]
		cmd = cmd.lower().split(" ")[0]

	# Command check and return the correct function
	# HELP COMMAND
	if cmd.lower() == "help":
		if len(args) > 1:
			help("help")

		if len(args) > 0:
			arg = args[0]
		else:
			arg = ""
		help(arg)
	# CLEAR COMMAND
	elif cmd.lower() == "clear":
		if len(args) > 0:
			help("clear")
		clear()
	# COMMAND NOT FOUND
	else:
		print(f"{functions.bcolors.FAIL}Error{functions.bcolors.ENDC}: Command '{cmd}' not found. Run 'help' for a list of commands.")
		__main__()

# Basic user interface header
os.system('cls' if os.name == 'nt' else 'clear')
functions.print_header()

# Start the program
__main__()