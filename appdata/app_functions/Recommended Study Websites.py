from colors_app import *
import webbrowser

STUDY_WEBSITES = {
    "Khan Academy": "https://www.khanacademy.org",
    "Physics Classroom": "https://www.physicsclassroom.com",
    "Grammarly": "https://www.grammarly.com",
    "Wolfram Alpha": "https://www.wolframalpha.com",
    "Don't study :)": "-_-"
}


print(f"\n{blue}Recommended Study Websites:")

def display():
 for name, url in STUDY_WEBSITES.items():
    print(f""
          f"\n{red}[{cyan}!{red}]{lc} {name}{white}:{green} {url} {purple}|")




def open():
  choice = input(f"\n{yellow}Enter website name to open (or press Enter to skip):{red} ")
  if choice in STUDY_WEBSITES:
    webbrowser.open(STUDY_WEBSITES[choice])


display()
open()