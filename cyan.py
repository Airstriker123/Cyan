from appdata.menu import * # import menu.py file
from appdata.functions import * # imports other python files to reduce lines
from appdata.banner import *
from appdata.guide import *   # I got so much errors from trying to import files into parent file (cyan.py)
from appdata.welcome import *  # fixed by adding a dot ;)
from appdata.Credits import * 

welcome_flag_path = os.path.join("appdata", "Welcome_complete.txt")
sys.stdout.reconfigure(encoding='utf-8')

# if welcome_complete does not exist in path welcome user to app
if not os.path.exists(welcome_flag_path): 
    first_time_run()
    with open(welcome_flag_path, "w") as file:
        file.write("Completed=True")
# main function/app executed into terminal 
# output
def main():
    while True:
        Clear()
        banner()
        menu()
        app()
        input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press enter to clear menu -> {reset} " + reset)

# used if user types help
def continuemain():
    while True:
        input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
        menu()
        app()

#error message
def ErrorChoiceStart():
    print(f"\n{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Choice !", reset)
    time.sleep(1)

# inputs functions
# get input from user 
def app():
    options = {
        '01': option_01, '02': option_02, '03': option_03, '04': option_04,
        '05': option_05, '06': option_06, '07': option_07, '08': option_08,
        '09': option_09, '10': option_10, '11': option_11, '12': option_12,
        '13': option_13, '14': option_14, '15': option_15, '16': option_16,
        '17': option_17, '18': option_18, '19': option_19,
    }

    menu_number = '1'
    username_pc = os.getlogin()
    choice = input(
        f""" {lc}┌──({purple}{username_pc}{lc}@cyan{lc})─{lc}[{red}~/{os_name}/Menu-{menu_number}{lc}]
 {lc}└─{lc}> {reset}""")
# checks input e.g if input is c execute credits function
    try:
        if choice in ['C', 'credits', 'author', 'c', 'CREDITS', 'Credits', 'CreDIts']:
            credits()
        if choice in ['Help', 'H', 'h', 'HELP', 'HeLp', '?', 'help']:
            help()
            continuemain()
        if choice in ['alt+f4', 'exit', 'leave', 'end', 'EXITAPP', 'exitapp']:
            sys.exit()
        if choice in ['R', 'r', 'reset', 'refresh', 'clear']:
            input(f"{BEFORE + current_time_hour() + AFTER} {INFO} Press enter to continue -> {reset} " + reset)
            main()

        script_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "appdata", "app_functions"))

        if choice in options and options[choice]:
            script_path = os.path.join(script_folder, f"{options[choice]}.py")

            if os.path.exists(script_path):
                os.system(f"python \"{script_path}\"")
            else:
                print(f"{red}Error: {blue}{script_path} {red}not found! -_-")

        elif '0' + choice in options and options['0' + choice]:
            script_path = os.path.join(script_folder, f"{options['0' + choice]}.py")

            if os.path.exists(script_path):
                os.system(f"python \"{script_path}\"")
            else:
                print(f"Error: {script_path} not found!")

        else:
            ErrorChoiceStart()
#Prints error message e.g a filepath is not found in code or could not find a specific module.
    except Exception as e:
        print(f"Error: {e}")

#run main function
main()
#continuemain()
# This took a month to make I am not lying -_-
