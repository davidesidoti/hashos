#!/usr/bin/python
# -*- coding: utf-8 -*-

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

from lib.hargs import LogLevelEnum
from lib.hlog import printHeader, hlog

class HashOS:
	def __init__(self) -> None:
		printHeader()

if __name__ == "__main__":
	HashOS()