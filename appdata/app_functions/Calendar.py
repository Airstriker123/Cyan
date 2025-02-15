import os
from colors_app import *

file_path = os.path.abspath("appdata/app_functions/Calendar/app.py")
print(f'{red}If python requests permmisions please click yes in order for the app to work. {purple}(retry this option if an error occurs)')
input(f'{yellow}press enter to launch app: ')
print(f'{green}Starting web app please wait')
os.system(f'start cmd /k python "{file_path}"')
print(f'{cyan}local server started!')

