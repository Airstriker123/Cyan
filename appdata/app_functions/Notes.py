from colors_app import *
import webbrowser
import subprocess
import sys
# Open Notepad

print(f'''
{green}Select options below:
{lc}=========================================================================||
{purple}Current options for flashcards:                                     
{cyan}[{white}1{cyan}]{yellow} Website {green} (notion) 
{cyan}[{white}2{cyan}]{yellow} inbuilt  {yellow}(notepad/windows only)
{cyan}[{white}3{cyan}]{red} Exit app                                      
{lc}=========================================================================||

''')

x = input(f'{yellow}Enter option {blue}(1,2,3):{red} ')
def website():
    print(f'{yellow}Opening web browser:')
    webbrowser.open("https://www.notion.com/")
    print(f'{green}Success!')

def inbuilt():
    print(f'{yellow}Starting notepad.exe!')
    subprocess.Popen(["notepad.exe"])


if x in ['1', 'one', 'first']:
    website()
elif x in ['2', 'two', 'second']:
    inbuilt()
elif x in ['3', 'three', 'ThREE', 'exit']:
    sys.exit()
else:
  print(f'{red}INVALID OPTION FOR FLASHCARDS!')