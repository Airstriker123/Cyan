import requests
import webbrowser
from colors_app import *

def random_fact():
    print(f'{yellow}Fetching fact please wait...')
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            fact = response.json()["text"]
            print(f"\n{lc}Random Fact:{white} {fact}")
        else:
            print(f"\n{red}Couldn't fetch a fact, try again later.")
    except:
        print(f"\n{red}Network error. Check your internet connection.")


random_fact()
