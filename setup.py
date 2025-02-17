import os
import sys


requirements = os.path.abspath("appdata/requirements.txt")

if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for the Cyan Tool:\n")
        print("This will take longer so it is recommended to use setup.bat instead of setup.py\n")
        input("Press enter to continue: ")
        os.system(f"python -m pip install -r {requirements}")
        os.system("python cyan.py")

elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the python modules required for the Cyan Tool:\n")
        os.system("python3 -m pip3 install -r requirements.txt")
        os.system("python3 cyan.py")

