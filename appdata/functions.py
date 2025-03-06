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
# contains most of functions and other features needed for my app 

color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE
yellow = color.YELLOW

# no i am not stealing you information (i am) THAT WAS A JOKE
# gets pc name
try: username_pc = os.getlogin()
except: username_pc = "username"

# does this even work? i don't know tbh
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

#delete printed messages in terminal 
def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")
# i don't need this but I am keeping it 
def Reset():
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "cyan.py")]
        subprocess.run(file)

    elif os_name == "Linux":
        file = ['python3', os.path.join(tool_path, "cyan.py")]
        subprocess.run(file)
# i don't need this but I am keeping it 
def StartProgram(program):
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)
        
    elif os_name == "Linux":
        file = ['python3', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)
# I love animated text!
def Slow(text):
    delai = 0.03 # 30ms delay lower valuie = faster print
    lignes = text.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)
# to avoid terminal resets in 0ms the user needs to press enter to reset
def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press enter to continue -> " + reset)
#errors
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
# makes menu have a cyan gradient to match app 
def MainColor(menu1):
    start_color = (0, 200, 150)
    end_color = (0, 255, 255)
    num_steps = 15

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))

    colors += list(reversed(colors[:-1]))

    gradient_chars = '┌─┬│└┐┘┴├┤▓▒░█▄▌▀'
    num_colors = len(colors)

    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    lines = menu1.split('\n')
    result = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors
            color = colors[color_index]

            if char in gradient_chars:
                result.append(text_color(*color) + char + "\033[0m")
            else:
                result.append(char)

        if i < len(lines) - 1:
            result.append('\n')

    return ''.join(result)



