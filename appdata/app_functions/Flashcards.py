import webbrowser
from colors_app import *
import sys
import requests
import json
import time
"""
if you need comments check essay structure guide this is same code
"""

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

fc =  MainColor2(r"""

                   ███                                                                    
                ████  ████                                                                
              ███        ██                                                               
              ██          ██                                                              
              █           ██                                                              
              █        ██ ██                                                              
              █        ██ ██                                                              
              █        ██                                                                 
     ████████  ████████  ██████████████████████████████████████████                       
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████                      
    ██████████ ████████  ███████████████████████████████████████████  █████████           
             █  █     █  █                                            █████████           
    ██████████  ██████   ███████████████████████████████████████████  █████████           
    ████████████       █████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████                                                        ████                      
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████                                                        ████       ████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████                                                        ████       ████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
    ████████████████████████████████████████████████████████████████  █████████           
                                                                          █████           
               ████████████████████████████████████████████████████████████████           
               ████████████████████████████████████████████████████████████████           
               ████████████████████████████████████████████████████████████████           
               ████████████████████████████████████████████████████████████████           
               ████████████████████████████████████████████████████████████████           
                                                                                          

""")

#get keys at https://aimlapi.com
api_keys = {
    "3f493a0d62df472bbe2efda6d4b2bbf9",
    "451d904cff5b4e25886acbef9d58d42d",
    "fdef3c79fa85472f8ae5a88882ef0bdc",
    "e7b4aaffb85f466e92c374d92cba75af",
    "78621e4ee5154de18617765dc7ae2001",
    "e7711e86290a454c99431fd3f2e1a4d1",
}
api_url = "https://api.aimlapi.com/v1/chat/completions"
define = "Create flashcards for the following topic:"
info = "also add info on the topic for preparing for test"

Slow(fc)
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
