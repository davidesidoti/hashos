#!/usr/bin/python3
# File containing all the general functions used.

# Class to store every color used in the terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to print the header of the program


def print_header():
    print(r""".__                  .__                  
|  |__ _____    _____|  |__   ____  ______
|  |  \\__  \  /  ___/  |  \ /  _ \/  ___/
|   Y  \/ __ \_\___ \|   Y  (  <_> )___ \ 
|___|  (____  /____  >___|  /\____/____  >
     \/     \/     \/     \/           \/ """)
    print("\n*****************************************************************************")
    print("\n* Copyright of hashdeveloper, 2022				             *")
    print("\n* https://tryhackme.com/p/hashdeveloper			                     *")
    print(f"\n* {bcolors.FAIL}WARNING: Please remember, illegal activity is forbidden using hashos tool.{bcolors.ENDC} *")
    print(f"\n* {bcolors.FAIL}All actions carried out using this tool are solely your responsibility.{bcolors.ENDC}    *")
    print("\n*****************************************************************************")
