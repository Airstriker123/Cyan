from colors_app import *
import json
import requests
import time
import sys

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

AI = MainColor2gpt = MainColor2(r"""                                                                                         
                                                                                             
                                   :@@@@@@@@@@@@@@=                                          
                                 @@@@@@@@@@@@@@@@@@@@.                                       
                               @@@@@@:          .@@@@@@@@@@@@%+                              
                             @@@@@*               -@@@@@@@@@@@@@@@@                          
                            #@@@@              @@@@@@@@@*:  =%@@@@@@@@                       
                           *@@@%           :@@@@@@@*             :@@@@@*                     
                      *@@@@@@@@         @@@@@@@@-                   @@@@@                    
                    @@@@@@@@@@%      #@@@@@@%:                       #@@@@                   
                  @@@@@@  .@@@%     #@@@@#           @@@@@@+          %@@@#                  
                :@@@@#    .@@@%     #@@@          #@@@@@@@@@@@+        @@@@                  
               -@@@@-     .@@@%     #@@@      +@@@@@@#    @@@@@@@@     @@@@                  
               @@@@       .@@@%     #@@@   -@@@@@@#          +@@@@@@@- @@@@                  
              :@@@*       .@@@%     #@@@@@@@@@@@@@@@@           :@@@@@@@@@%                  
              =@@@        .@@@%     #@@@@@@-     -@@@@@@:          .#@@@@@#                  
              =@@@:       .@@@%     #@@@            :@@@@@@@           @@@@@                 
              .@@@%       .@@@%     #@@@             @@@@@@@@@#         #@@@@                
               %@@@*       @@@@@@#  #@@@             @@@+  %@@@@@@       #@@@%               
                @@@@*        .%@@@@@@@@@             @@@+     %@@@        @@@@.              
                 @@@@@           @@@@@@@            :@@@+     #@@@        -@@@=              
                  #@@@@@#           -@@@@@@:     -@@@@@@+     #@@@        .@@@=              
                  @@@@@@@@@@.           @@@@@@@@@@@@@@@@+     #@@@        #@@@-              
                  @@@@ =@@@@@@@=          #@@@@@@=   @@@+     #@@@       .@@@@               
                  @@@@     @@@@@@@@    %@@@@@@=      @@@+     #@@@      -@@@@:               
                  @@@@        +@@@@@@@@@@@#.         @@@+     #@@@     #@@@@                 
                  *@@@#          *@@@@@@           %@@@@+     #@@@   @@@@@@                  
                   @@@@#                       :%@@@@@@#      %@@@@@@@@@@                    
                    @@@@@                   -@@@@@@@@         @@@@@@@@#                      
                     #@@@@@.             *@@@@@@@-           %@@@#.                          
                       @@@@@@@@%=  :*@@@@@@@@@              @@@@*                            
                         .@@@@@@@@@@@@@@@@+               +@@@@%                             
                              *@@@@@@@@@@@@@           .@@@@@@                               
                                       :@@@@@@@@@@@@@@@@@@@@                                 
                                          =@@@@@@@@@@@@@@:                                                                                                                                                                                                                  
""")


api_keys = {
    "163e456ed8e04d0fae7175b2cc658bde",
    "18a044c6953047519763a05c80c9379f",
    "a5271f71f5354b03939e0b648a74eb98",
    "451d904cff5b4e25886acbef9d58d42d",
    "aaef4a4975cf4f67a4932899fb228435",
}
api_url = "https://api.aimlapi.com/v1/chat/completions"

def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def send_message(user_message):
    if not user_message:
        print("Error: No message entered.")
        return

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": user_message}
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
                sys.stdout.write(f"{lc}Cyan🤖: {white}")
                type_text(f"{white} {ai_message}", 0.005)

                break  # Exit loop if the request is successful
            else:
                print("Error: Unable to retrieve response. Trying next API key.")
                print(f"{red}Switching to the next API key, please wait...")

        except requests.exceptions.RequestException as error:
            print(f"{red}Error: Unable to connect with API key {api_key}. {error}")
            print(f"{red}Attempting to use the next available API key...")


# rest

def Cyam_AI():
    Slow(AI)
    print(
        f'{green}Remember to type {red}exit {green} once you have completed your prompts!')
    sys.stdout.write(f"{lc}Cyan🤖: {white}")
    type_text(f"{white} Hello, how can I help you today? 😁", 0.005)
    while True:
        user_input = input(f"{yellow}\b👨‍💻You: ")
        if user_input.lower() == "exit":
            print(f'{red}Exiting program.')
            break
        send_message(user_input)

Cyam_AI()



