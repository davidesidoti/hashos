#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from lib.hargs import LogLevelEnum, BColors


def printHeader():
    print(r""".__                  .__                  
|  |__ _____    _____|  |__   ____  ______
|  |  \\__  \  /  ___/  |  \ /  _ \/  ___/
|   Y  \/ __ \_\___ \|   Y  (  <_> )___ \ 
|___|  (____  /____  >___|  /\____/____  >
     \/     \/     \/     \/           \/ """)
    print("\n*****************************************************************************")
    print("\n* Copyright of hashdeveloper, 2022				             *")
    print("\n* https://tryhackme.com/p/hashdeveloper			                     *")
    print(f"\n* {BColors.FAIL}WARNING: Please remember, illegal activity is forbidden using hashos tool.{BColors.ENDC} *")
    print(f"\n* {BColors.FAIL}All actions carried out using this tool are solely your responsibility.{BColors.ENDC}    *")
    print("\n*****************************************************************************")


def hlog(msg=None, logLevel=LogLevelEnum.DEBUG.value):
    print("{} - {}: {}".format(datetime.now().isoformat(), logLevel, msg))
    sys.stdout.flush()
