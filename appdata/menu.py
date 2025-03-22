# YouTube video to MP3/MP4 converter  
# AI Chatbot v2  
# Snake game (possibly planned)  
# Calendar/Assignments manager  
# My plans are not fully made yet  

# Importing necessary modules  
from .colors import *  # Importing the entire 'colors' module (rather than specific functions)  
from .functions import *  # Importing the entire 'functions' module  

# Defining option names for menu items  
option_01 = "Google-Classroom"  # 1  
option_02 = "ChatGPT (Web-Version)"  # @  
option_03 = "GitHub"  ##@  
option_04 = "YouTube"  
option_05 = "Calendar"  
option_06 = "YouTube to MP3 or MP4"  
option_07 = "Alarm"  
option_08 = "Google Calendar"  
option_09 = "Dictionary & Thesaurus"  # Uses an API  
option_10 = "Flashcards"  # Uses an API  
option_11 = "AI Chatbot (Inbuilt)"  # Uses an API  
option_12 = "Notes"  # Uses an API  
option_13 = "Essay Structure Guide"  
option_14 = "Random Fact of the Day"  # Uses an API  
option_15 = "Math Solver"  
option_16 = "Terminal app wallpaper changer"  
option_17 = "Physics Formula Sheet"  
option_18 = "Spelling & Grammar Check"  # Uses an API  
option_19 = "Recommended Study Websites"  

# Additional menu options  
option_next = "Credits"  
option_site = "clear"  
option_info = "Help"  

# Formatting the options for display in the menu  
# Using ANSI color codes (cyan and white) to style the text  
option_01_txt = f"{cyan}[{white}01{cyan}]{white} " + option_01.ljust(30)[:30].replace("-", " ")  
option_02_txt = f"{cyan}[{white}02{cyan}]{white} " + option_02.ljust(30)[:30].replace("-", " ")  
option_03_txt = f"{cyan}[{white}03{cyan}]{white} " + option_03.ljust(30)[:30].replace("-", " ")  
option_04_txt = f"{cyan}[{white}04{cyan}]{white} " + option_04.ljust(30)[:30].replace("-", " ")  
option_05_txt = f"{cyan}[{white}05{cyan}]{white} " + option_05.ljust(30)[:30].replace("-", " ")  
option_06_txt = f"{cyan}[{white}06{cyan}]{white} " + option_06.ljust(30)[:30].replace("-", " ")  
option_07_txt = f"{cyan}[{white}07{cyan}]{white} " + option_07.ljust(30)[:30].replace("-", " ")  
option_08_txt = f"{cyan}[{white}08{cyan}]{white} " + option_08.ljust(30)[:30].replace("-", " ")  
option_09_txt = f"{cyan}[{white}09{cyan}]{white} " + option_09.ljust(30)[:30].replace("-", " ")  
option_10_txt = f"{cyan}[{white}10{cyan}]{white} " + option_10.ljust(30)[:30].replace("-", " ")  

option_11_txt = f"{cyan}[{white}11{cyan}]{white} " + option_11.ljust(30)[:30].replace("-", " ")  
option_12_txt = f"{cyan}[{white}12{cyan}]{white} " + option_12.ljust(30)[:30].replace("-", " ")  
option_13_txt = f"{cyan}[{white}13{cyan}]{white} " + option_13.ljust(30)[:30].replace("-", " ")  
option_14_txt = f"{cyan}[{white}14{cyan}]{white} " + option_14.ljust(30)[:30].replace("-", " ")  
option_15_txt = f"{cyan}[{white}15{cyan}]{white} " + option_15.ljust(30)[:30].replace("-", " ")  
option_16_txt = f"{cyan}[{white}16{cyan}]{white} " + option_16.ljust(30)[:30].replace("-", " ")  
option_17_txt = f"{cyan}[{white}17{cyan}]{white} " + option_17.ljust(30)[:30].replace("-", " ")  
option_18_txt = f"{cyan}[{white}18{cyan}]{white} " + option_18.ljust(30)[:30].replace("-", " ")  
option_19_txt = f"{cyan}[{white}19{cyan}]{white} " + option_19.ljust(30)[:30].replace("-", " ")  

# Formatting special options  
option_next_txt = option_next + f" {cyan}[{white}C{cyan}]{white}"  
option_site_txt = f"{cyan}[{white}R{cyan}]{white} " + option_site  
option_info_txt = f"{cyan}[{white}H{cyan}]{white} " + option_info  

# Creating the menu layout with properly aligned text  
menu1 = f""" ┌─{option_site_txt}                                                                                             {option_next_txt}─┐  
 ├─{option_info_txt}  ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            │  
 └─┬─────────┤ General tools   ├─────────┬──────────────┤ Study ├──────────────┬────────────┤ Utilities ├────────────┴─  
   │         └─────────────────┘         │              └───────┘              │            └───────────┘  
   ├─ {option_01_txt}├─ {option_07_txt}├─ {option_14_txt}  
   ├─ {option_02_txt}├─ {option_08_txt}├─ {option_15_txt}  
   ├─ {option_03_txt}├─ {option_09_txt}├─ {option_16_txt}  
   ├─ {option_04_txt}├─ {option_10_txt}├─ {option_17_txt}  
   ├─ {option_05_txt}├─ {option_11_txt}├─ {option_18_txt}  
   └─ {option_06_txt}├─ {option_12_txt}└─ {option_19_txt}  
                                         └─ {option_13_txt}  

"""

# Function to add a color gradient effect to the menu text  
def MainColor(menu1):  
    start_color = (0, 200, 150)  # Starting color (RGB)  
    end_color = (0, 255, 255)  # Ending color (RGB)  
    num_steps = 15  # Number of gradient steps  

    # Generating a list of colors transitioning from start to end  
    colors = []  
    for i in range(num_steps):  
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)  
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)  
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)  
        colors.append((r, g, b))  

    colors += list(reversed(colors[:-1]))  # Mirroring the gradient for a smooth effect  

    gradient_chars = '┌─┬│└┐┘┴├┤▓▒░█▄▌▀'  # Characters to apply gradient  
    num_colors = len(colors)  

    def text_color(r, g, b):  
        return f"\033[38;2;{r};{g};{b}m"  # ANSI escape sequence for RGB colors  

    lines = menu1.split('\n')  
    result = []  

    for i, line in enumerate(lines):  
        for j, char in enumerate(line):  
            color_index = (i + j) % num_colors  
            color = colors[color_index]  

            if char in gradient_chars:  
                result.append(text_color(*color) + char + "\033[0m")  # Apply gradient  
            else:  
                result.append(char)  

        if i < len(lines) - 1:  
            result.append('\n')  

    return ''.join(result)  

# Function to display the menu with a slow effect  
def menu():  
    Slow((MainColor(menu1)))  
