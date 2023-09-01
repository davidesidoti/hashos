#!/usr/bin/python
# -*- coding: utf-8 -*-

# The code is importing the necessary modules and classes for the script to run properly.
import sys
from datetime import datetime
from lib.hargs import LogLevelEnum, BColors


def printHeader() -> None:
    """
    The `printHeader()` function prints a header with a logo, copyright information, and a warning
    message.
    """
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


def hlog(msg=None, logLevel=LogLevelEnum.DEBUG.value) -> None:
    """
    The function `hlog` is a logging function that prints a message with a timestamp and log level.
    
    :param msg: The `msg` parameter is used to specify the message that you want to log. It is an
    optional parameter, which means you can choose to provide a message or leave it empty
    :param logLevel: The `logLevel` parameter is an optional parameter that specifies the level of the
    log message. It is set to `LogLevelEnum.DEBUG.value` by default
    """
    print("{} - {}: {}".format(datetime.now().isoformat(), logLevel, msg))
    sys.stdout.flush()
