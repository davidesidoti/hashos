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
import json
import signal

class HashOS:
    settings = None
    cwd = None
    loopQuit = False

    def __init__(self) -> None:
        printHeader()

        self.cwd = "/".join(__file__.split("/")[:-1])
        
        hlog("Loading settings file...", LogLevelEnum.INFO.value)
        with open(self.cwd + "/config/settings.json", "r") as settingsFile:
            self.settings = json.load(settingsFile)
            settingsFile.close()

        hlog("HashOS Version {}".format(self.settings["general"]["version"]), LogLevelEnum.INFO.value)
        signal.signal(signal.SIGINT, lambda signal, frame: self.quitLoop())
        self.loop()


    def quitLoop(self) -> None:
        """
        The function `quitLoop` sets the `loopQuit` attribute to `True`.
        """
        self.loopQuit = True


    def loop(self):
        while not self.loopQuit:
            pass
        hlog("Bye! :D", LogLevelEnum.INFO.value)

if __name__ == "__main__":
    HashOS()