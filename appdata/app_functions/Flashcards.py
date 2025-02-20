import webbrowser
from colors_app import *
import sys
import requests
import json


#get keys at https://aimlapi.com
api_keys = {
    "163e456ed8e04d0fae7175b2cc658bde",
    "18a044c6953047519763a05c80c9379f",
    "a5271f71f5354b03939e0b648a74eb98",
    "451d904cff5b4e25886acbef9d58d42d",
    "aaef4a4975cf4f67a4932899fb228435",
}
api_url = "https://api.aimlapi.com/v1/chat/completions"
define = "Create flashcards for the following topic:"
info = "also add info on the topic for preparing for test"

print(f"""
{lc}=========================================================================
{purple}Current options for flashcards:
{cyan}[{white}1{cyan}]{yellow} Website {green}(recommended!)
{cyan}[{white}2{cyan}]{yellow} inbuilt A.i flashcards {red}(NOT recommended!)
{cyan}[{white}3{cyan}]{yellow} Exit app
{lc}=========================================================================
""")
x = input(f'{yellow}Enter option {blue}(1,2):{red} ')


def website():
    print(f'{yellow}Opening web browser:')
    webbrowser.open("https://shepherd.study")
    print(f'{green}Success!')

def send_message(user_message):
    if not user_message:
        print("Error: No message entered.")
        return

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": f"{define}  {user_message} {info}"}
        ]
    }

    for api_key in api_keys:
        try:
            response = requests.post(api_url, headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }, data=json.dumps(payload))

            #error handle
            data = response.json()

            if data and "choices" in data:
                ai_message = data["choices"][0]["message"]["content"]
                print(f"{cyan}Flashcards A.I🤖:",  f"{white}{ai_message}")
                break  # Exit loop if the request is successful
            else:
                print(f"{red}Error: Unable to retrieve response. Trying next API key. (you used all tokens)")
                print(f"{red}Switching to the next API key, please wait... (you used all tokens)")

        except requests.exceptions.RequestException as error:
            print(f"Error: Unable to connect with API key {api_key}. {error}")
            print( f"{red}Attempting to use the next available API key...")


# rest

def AI():
    print(
        f'{green}Remember to type{red} exit{green} once you have completed your prompts')
    while True:
        user_input = input(f"{yellow}\b👨‍💻Enter topic you want flashcards: ")
        if user_input.lower() == "exit":
            print(f'{red}Exiting program.')
            break
        send_message(user_input)


if x in ['1', 'one', 'first']:
    website()
elif x in ['2', 'two', 'second']:
    AI()
elif x in ['3', 'three', 'ThREE', 'exit']:
    sys.exit()
else:
  print(f'{red}INVALID OPTION FOR FLASHCARDS!')