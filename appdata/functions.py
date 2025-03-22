# Import necessary modules for coloring, subprocess management, file handling, etc.
from .colors import *
import colorama
import ctypes
import subprocess
import os
import time
import sys
import datetime
import requests

# Define colors for terminal output using colorama
color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE
yellow = color.YELLOW


# Get the current logged-in username on the PC
try:
    username_pc = os.getlogin()
except:
    username_pc = "username"  # Default value in case of failure

# Check the operating system (Windows, Linux, or unknown)
try:
    if sys.platform.startswith("win"):
        os_name = "Windows"
    elif sys.platform.startswith("linux"):
        os_name = "Linux"
    else:
        os_name = "Unknown"
except:
    os_name = "???"  # Default value if the OS can't be determined

# Set the tool's file path
tool_path = os.path.dirname(os.path.abspath(__file__)).split("Program\\")[0].strip()

# Get the current date and time formatted as YYYY-MM-DD HH:MM:SS
def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Get the current time formatted as HH:MM:SS
def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

# Define a few pre-formatted strings to be used as prefixes for logging or output
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

# Function to clear the terminal screen based on the OS (Windows or Linux)
def Clear():
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")

# Function to reset the program by running a specific script (keeping for compatibility purposes)
def Reset():
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "cyan.py")]
        subprocess.run(file)
    elif os_name == "Linux":
        file = ['python3', os.path.join(tool_path, "cyan.py")]
        subprocess.run(file)

# Function to start another program (useful for launching other Python scripts)
def StartProgram(program):
    if os_name == "Windows":
        file = ['python', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)
    elif os_name == "Linux":
        file = ['python3', os.path.join(tool_path, "Program", program)]
        subprocess.run(file)

# Function to print text slowly with a delay between each line (creates animation effect)
def Slow(text):
    delai = 0.03  # Delay time (30ms between lines)
    lignes = text.split('\n')  # Split input text into lines
    for ligne in lignes:
        print(ligne)  # Print each line
        time.sleep(delai)  # Pause between prints for the animation effect

# Function that prompts the user to press Enter to continue (prevents terminal reset without user input)
def Continue():
    input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press enter to continue -> " + reset)

# Error handling functions: These are called when errors occur during execution
def Error(e):
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error: {white}{e}", reset)
    Continue()  # Ask the user to press Enter to continue
    Reset()  # Reset the program

def ErrorChoiceStart():
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(1)

def ErrorChoice():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(3)  # Wait before resetting
    Reset()

def ErrorResponse():
    print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Response !", reset)
    time.sleep(3)  # Wait before resetting
    Reset()

# Function that applies a gradient of cyan colors to menu text (animated gradient effect)
def MainColor(menu1):
    start_color = (0, 200, 150)  # Start color for the gradient (RGB)
    end_color = (0, 255, 255)  # End color for the gradient (RGB)
    num_steps = 15  # Number of gradient steps

    colors = []
    # Create gradient colors by interpolating between the start and end colors
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))

    # Add a reversed copy of the colors for a fading effect
    colors += list(reversed(colors[:-1]))

    # Set of characters to apply the color gradient effect to
    gradient_chars = '┌─┬│└┐┘┴├┤▓▒░█▄▌▀'
    num_colors = len(colors)  # Number of colors in the gradient

    # Function to format text with RGB color codes
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    lines = menu1.split('\n')  # Split the input menu into lines
    result = []  # Store the final colored output

    # Loop through each line and each character to apply the gradient
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors  # Cycle through the colors
            color = colors[color_index]

            # Apply color to the character if it's part of the gradient characters
            if char in gradient_chars:
                result.append(text_color(*color) + char + "\033[0m")
            else:
                result.append(char)  # Keep other characters unchanged

        if i < len(lines) - 1:
            result.append('\n')  # Add a newline between lines

    return ''.join(result)  # Return the final colored string




