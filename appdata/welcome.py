import os
import sys
import fade
import colorama
import time
from colorama import Fore, Style
import sys

name = os.getlogin()
try:
    if sys.platform.startswith("win"):
        os_name = "Windows"
    elif sys.platform.startswith("linux"):
        os_name = "Linux"
    else:
        os_name = "Unknown"
except:
    os_name = "None"

color = colorama.Fore
red = Fore.RED
white = Fore.WHITE
green = Fore.GREEN
reset = Fore.RESET
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
lc = Fore.LIGHTCYAN_EX
grey = Fore.LIGHTBLACK_EX
BEFORE_CYAN= f'{cyan + white}'
purple = Fore.MAGENTA
aqua = Fore.LIGHTCYAN_EX



def Slow(text):
    delai = 0.03
    lignes = text.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)


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

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")

def welcome():
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text(f"Hello {purple}{name},{white} welcome to {lc}Cyan! 😁🎉 \n", 0.04)

    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text("Cyan is a multi-tool designed to help students with their HSC journey! 📚👑 \n", 0.05)


# welcome func
def first_time_run():

    banner = """    
  ▄ ▄   ▄███▄   █     ▄█▄    ████▄ █▀▄▀█ ▄███▄          ▄▄▄▄▀ ████▄     ▄█▄  ▀▄    ▄ ██      ▄         ▄ 
 █   █  █▀   ▀  █     █▀ ▀▄  █   █ █ █ █ █▀   ▀      ▀▀▀ █    █   █     █▀ ▀▄  █  █  █ █      █       █  
█ ▄   █ ██▄▄    █     █   ▀  █   █ █ ▄ █ ██▄▄            █    █   █     █   ▀   ▀█   █▄▄█ ██   █     █   
█  █  █ █▄   ▄▀ ███▄  █▄  ▄▀ ▀████ █   █ █▄   ▄▀        █     ▀████     █▄  ▄▀  █    █  █ █ █  █     █   
 █ █ █  ▀███▀       ▀ ▀███▀           █  ▀███▀         ▀                ▀███▀ ▄▀        █ █  █ █         
  ▀ ▀                                ▀                                                 █  █   ██     ▀   
                                                                                      ▀                                                                        
"""

    Clear()
    faded_text = fade.water(banner)
    (Slow(f"{faded_text}\n"))
    type_text(f"{red}[{yellow}❗{red}]{yellow} ⚠️ WARNING:{red} THIS APP CONTAINS {purple}API KEYS!{red} DO NOT{white}{red} SHARE OR SHOW THESE KEYS TO OTHERS!\n", 0.0009999999999)
    print(f'{purple}========================================================================================================================\n')
    welcome()
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text(f"Cyan is a very simple and easy app to use! \n", 0.025)
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text("Let's say you don't know what a word means, you can simply use the dictionary option to find it! \n",
              0.025)
    sys.stdout.write(f"{lc}Cyan🤖: {white}[")
    type_text(
        f"{red}09{white}] {yellow}Dictionary & Thesaurus, where {green}09 {yellow}or{green} 9 {white}is the number you have to type to start the app. 😊 \n",
        0.025)
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text(f"Begin by typing the number {yellow}9{white} and pressing {red}Enter! \n", 0.025)
    #help() (useless)
    input(f'{red}Press {lc}enter {red}if you understand how to use app:')

