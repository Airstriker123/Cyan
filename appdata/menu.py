#yt vid to mp3/mp4
#ai chatbot v2
#snake game??
#calender/assignments
# my plans not all made 


from .colors import * # import files rather than fucntions just import the whole file!
from .functions import *


# option names
option_01 = "Google-Classroom" #1
option_02 = "ChatGPT (Web-Version)" #@
option_03 = "GitHub" ##@
option_04 = "YouTube"
option_05 = "Calendar"
option_06 = "youtube to mp3 or mp4"
option_07 = "Alarm"
option_08 = "Timer"
option_09 = "Dictionary & Thesaurus" #api 
option_10 = "Flashcards" #api
option_11 = "Ai chatbot (inbuilt)" #api
option_12 = "Notes" #api
option_13 = "Essay Structure Guide" 
option_14 = "Random Fact of the Day" #api
option_15 = "Math Solver" 
option_16 = "Terminal app wallpaper changer"
option_17 = "Physics Formula Sheet"
option_18 = "Spelling & Grammar Check" #api 
option_19 = "Recommended Study Websites"

option_next = "Credits"
option_site = "clear"
option_info = "Help"

# option display
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


option_next_txt = option_next + f" {cyan}[{white}C{cyan}]{white}"

option_site_txt = f"{cyan}[{white}R{cyan}]{white} " + option_site
option_info_txt =  f"{cyan}[{white}H{cyan}]{white} " + option_info





#menu display
menu1 = f""" ┌─{option_site_txt}                                                                                             {option_next_txt}─┐
 ├─{option_info_txt      }  ┌─────────────────┐                        ┌───────┐                           ┌───────────┐            │
 └─┬─────────┤ General tools   ├─────────┬──────────────┤ Study ├──────────────┬────────────┤ Utilities ├────────────┴─
   │         └─────────────────┘         │              └───────┘              │            └───────────┘
   ├─ {option_01_txt                    }├─ {option_07_txt                    }├─ {option_14_txt}
   ├─ {option_02_txt                    }├─ {option_08_txt                    }├─ {option_15_txt}
   ├─ {option_03_txt                    }├─ {option_09_txt                    }├─ {option_16_txt}
   ├─ {option_04_txt                    }├─ {option_10_txt                    }├─ {option_17_txt}
   ├─ {option_05_txt                    }├─ {option_11_txt                    }├─ {option_18_txt}
   └─ {option_06_txt                    }├─ {option_12_txt                    }└─ {option_19_txt}
                                         └─ {option_13_txt                    }

"""
#gradient again (functions.py refused to import)
# 
#--------------------------------------------------------------------------------#
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

def menu():
    Slow((MainColor(menu1)))

