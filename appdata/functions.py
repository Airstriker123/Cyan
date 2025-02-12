from .colors import *
import colorama
import ctypes
import subprocess
import os
import time
import sys
import datetime
import sys
import requests

color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE
yellow = color.YELLOW

try: username_pc = os.getlogin()
except: username_pc = "username"

try:
    if sys.platform.startswith("win"):
        os_name = "Windows"
    elif sys.platform.startswith("linux"):
        os_name = "Linux"
    else:
        os_name = "Unknown"
except:
    os_name = "None"

tool_path = os.path.dirname(os.path.abspath(__file__)).split("Program\\")[0].strip()

def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

BEFORE = f'{red}[{white}'
AFTER = f'{red}]'

BEFORE_GREEN = f'{green}[{white}'
AFTER_GREEN = f'{green}]'

INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'
NOTE = f'{BEFORE}NOTE{AFTER} |'

GEN_VALID = f'{BEFORE_GREEN}+{AFTER_GREEN} |'
GEN_INVALID = f'{BEFORE}x{AFTER} |'

INFO_ADD = f'{white}[{red}+{white}]{red}'

def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")

def Reset():
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "cyan.py")]
        subprocess.run(file)

    elif os_name == "Linux":
        file = ['python3', os.path.join(tool_path, "cyan.py")]
        subprocess.run(file)

def StartProgram(program):
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)
        
    elif os_name == "Linux":
        file = ['python3', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)

def Slow(text):
    delai = 0.03
    lignes = text.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)

def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press enter to continue -> " + reset)

def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}", reset)
    Continue()
    Reset()

def ErrorChoiceStart():
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(1)

def ErrorChoice():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(3)
    Reset()

def ErrorResponse():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Response !", reset)
    time.sleep(3)
    Reset()

