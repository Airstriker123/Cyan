import json
import os
from colors_app import *
import time


def Slow(text, delay=0.03):
    for line in text.split("\n"):
        print(line, flush=True)
        time.sleep(delay)


def MainColor2(text):
    start_color = (0, 200, 150)
    end_color = (0, 255, 255)

    num_steps = 16
    colors = [
        (
            start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1),
            start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1),
            start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1),
        )
        for i in range(num_steps)
    ]

    colors += list(reversed(colors[:-1]))

    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    result = []
    lines = text.split("\n")

    for i, line in enumerate(lines):
        color_index = i % len(colors)
        r, g, b = colors[color_index]
        colored_line = text_color(r, g, b) + line + "\033[0m"
        result.append(colored_line)

    return "\n".join(result)

term = MainColor2(r"""                                                                                                       
                                      ██████████████                              
                                     ████████████████                             
                                    ████          ████                            
                       ███          ████          ████          ███               
                     ████████       ████          ████       ████████             
                   █████ █████    ██████          ██████    █████ █████           
                 ██████    ████████████             ███████████     █████         
                █████        ██████                    ██████         █████       
               ████                                                    █████      
              █████                                                     ████      
               █████                     █████████                    █████       
                 █████              ██████████████████              █████         
                   ████           ███████        ████████           ███           
                     █          █████                ██████         ███           
                                ███                    █████        ████          
                     ████████████                        ████        █████████    
                    ██████████████                        ████        ████████████
           ███      ███████████████     ███                ███                ████
         ████████   ███████████████   ████████             ████                ███
       █████████████████████████████████████████            ███                ███
      ███████████████████████████████████████████           ███                ███
    ██████████████████████████████████████████████         ████                ███
    ██████████████████████████████████████████████         ████                ███
     █████████████████████████████████████████████        ████         ███████████
       █████████████████████████████████████████         █████        ███████████ 
       ████████████████        █████████████████        ████         ████         
  ███████████████████             ███████████████████  ████         ████          
███████████████████                ████████████████████ ██          ███           
███████████████████                 ███████████████████             █████         
██████████████████                  ███████████████████              █████        
██████████████████                  ███████████████████                ████       
███████████████████                 ███████████████████                 ████      
███████████████████                ████████████████████   ██          █████       
 ████████████████████             ███████████████████    █████       █████        
       ████████████████        █████████████████           █████   █████          
       █████████████████████████████████████████             █████████            
     ████████████████████████████████████████████              █████              
    ██████████████████████████████████████████████                                
    ██████████████████████████████████████████████                                
     ████████████████████████████████████████████                                 
       █████████████████████████████████████████                                  
         ████████  ████████████████   ████████                                    
            ██      ███████████████      ██                                       
                    ██████████████                                                
                      ███████████                                                 
""")

# same code a fd.py but for manual input
def change_windows_terminal_background(image_path):
    settings_path = os.path.expanduser(
        r"~\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json")

    if not os.path.exists(settings_path):
        print(f"❌{red} Error: Windows Terminal settings file not found.")
        return


    with open(settings_path, "r", encoding="utf-8") as file:
        settings = json.load(file)


    default_profile_guid = settings.get("defaultProfile")


    profiles_list = settings.get("profiles", {}).get("list", [])
    if not profiles_list:
        print(f"❌{red} Error: No profiles found in settings.json.")
        return

    changed = False
    default_profile_found = False


    for profile in profiles_list:
        if "backgroundImage" not in profile:
            print(f"🛠{green} Adding background settings to profile: {profile.get('name', 'Unnamed Profile')}")

        profile["backgroundImage"] = image_path
        profile["backgroundImageStretchMode"] = "uniformToFill"
        profile["backgroundImageOpacity"] = 0.8
        changed = True


        if profile.get("guid") == default_profile_guid:
            print("🎯 Updating default profile background.")
            profile["backgroundImage"] = image_path
            default_profile_found = True


    if default_profile_found:
        settings["profiles"]["defaults"]["backgroundImage"] = image_path

    if changed:

        with open(settings_path, "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)
        print(
            f"""✅{green} 
              
  ______   __    __   ______    ______   ________   ______    ______   __ 
 /      \ |  \  |  \ /      \  /      \ |        \ /      \  /      \ |  \
|  $$$$$$\| $$  | $$|  $$$$$$\|  $$$$$$\| $$$$$$$$|  $$$$$$\|  $$$$$$\| $$
| $$___\$$| $$  | $$| $$   \$$| $$   \$$| $$__    | $$___\$$| $$___\$$| $$
 \$$    \ | $$  | $$| $$      | $$      | $$  \    \$$    \  \$$    \ | $$
 _\$$$$$$\| $$  | $$| $$   __ | $$   __ | $$$$$    _\$$$$$$\ _\$$$$$$\ \$$
|  \__| $$| $$__/ $$| $$__/  \| $$__/  \| $$_____ |  \__| $$|  \__| $$ __ 
 \$$    $$ \$$    $$ \$$    $$ \$$    $$| $$     \ \$$    $$ \$$    $$|  \
  \$$$$$$   \$$$$$$   \$$$$$$   \$$$$$$  \$$$$$$$$  \$$$$$$   \$$$$$$  \$$
    
            """)
    else:
        print(f"{purple}⚠️ No changes were made.")
        print(f"""{red}
        
__/\\\\\\\\\\\\\\\_____/\\\\\\\\\_____/\\\\\\\\\\\__/\\\______________/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\________/\\\____        
 _\/\\\///////////____/\\\\\\\\\\\\\__\/////\\\///__\/\\\_____________\/\\\///////////__\/\\\////////\\\____/\\\\\\\__       
  _\/\\\______________/\\\/////////\\\_____\/\\\_____\/\\\_____________\/\\\_____________\/\\\______\//\\\__/\\\\\\\\\_      
   _\/\\\\\\\\\\\_____\/\\\_______\/\\\_____\/\\\_____\/\\\_____________\/\\\\\\\\\\\_____\/\\\_______\/\\\_\//\\\\\\\__     
    _\/\\\///////______\/\\\\\\\\\\\\\\\_____\/\\\_____\/\\\_____________\/\\\///////______\/\\\_______\/\\\__\//\\\\\___    
     _\/\\\_____________\/\\\/////////\\\_____\/\\\_____\/\\\_____________\/\\\_____________\/\\\_______\/\\\___\//\\\____   
      _\/\\\_____________\/\\\_______\/\\\_____\/\\\_____\/\\\_____________\/\\\_____________\/\\\_______/\\\_____\///_____  
       _\/\\\_____________\/\\\_______\/\\\__/\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\/_______/\\\____ 
        _\///______________\///________\///__\///////////__\///////////////__\///////////////__\////////////________\///_____

        
        """)
Slow(term)
image_path = input(f'{purple}Enter full image path (PNG, JPG, GIF) {red}(Do not include "" in path):{yellow} ').strip()
change_windows_terminal_background(image_path)
# this was pain to make ;/
