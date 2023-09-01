#!/usr/bin/python
# -*- coding: utf-8 -*-

# The line `from enum import Enum` is importing the `Enum` class from the `enum` module. The `Enum`
# class is used to create enumeration classes, which are a set of named values. In this code, it is
# used to define the `LogLevelEnum` enumeration class.
from enum import Enum


# The above class defines an enumeration for different log levels.
class LogLevelEnum(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


# The class BColors defines a set of color codes for formatting text in the terminal.
class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
