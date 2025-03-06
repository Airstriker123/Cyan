import requests
from spellchecker import SpellChecker # 99% of work right here on line 2
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


note = MainColor2(r"""                          
                                                                                                    
                                                                                                    
      █████████████████████████████████████████████████████████████████                             
   ████████████████████████████████████████████████████████████████████████                         
  ██████████████████████████████████████████████████████████████████████████                        
  ██████████████████████████████████████████████████████████████████████████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                                                              ██████                        
  ██████                        █████                                 ██████                        
  ██████                        █████                                 ██████                        
  ██████                        █████                                 ██████                        
  ██████                        █████                                 ██████                        
  ██████        ██████████████  ██████████████        ███████████     ██████                        
  ██████      ████████████████  ████████████████    █████████████     ██████                        
  ██████     ███████   ███████  ███████    ██████  ██████     ██      ██████                        
  ██████     █████       █████  ██████      █████  █████              ██████                        
  ██████     █████       █████  █████       █████ █████               ██████                  ███   
  ██████     █████       █████  █████       █████ ██████              ██████              █████████ 
  ██████     ██████    ███████  ███████    ██████  ██████     ██      ██████           ████████████ 
  ██████      ████████████████  ████████████████    █████████████     ██████         █████████████  
  ██████        ██████████████  ██████████████        ██████████      ██████       █████████████    
  ██████           ████                 ███              ████         ████       █████████████      
  ██████                                                              ██       █████████████        
  ██████                                                                     █████████████          
  ██████                                                                   ██████████████           
  ██████                                                                 ██████████████             
  ██████                                                                █████████████               
  ██████                                                              ██████████████                
  ██████                                                            ██████████████                  
  ██████                                                          ███████████████                   
  ██████                                    ███                  ███████████████                    
  ███████████████████████████████████     ███████████          ███████████████                      
  ███████████████████████████████████    ████████████████    ████████████████                       
   ██████████████████████████████████     ██████████████████████████████████                        
      ███████████████████████████████       ███████████████████████████████                         
                                              ████████████████████████████                          
                                                █████████████████████████                           
                                                 ███████████████████████                            
                                                   ███████████████████                              
                                                    ██████████████████                              
                                                     ████████████████                               
                                                      ██████████████                                
                                                        ███████████                                 
                                                         █████████                                  
                                                          ███████                                   
                                                           ██████                                   
                                                            ████                                    
                                                                                                                                                                                             
""")

def check_spelling_grammar():
    Slow(note)
    text = input(f"\n{yellow}Enter text to check: ")
    spell = SpellChecker()
    words = text.split()
    misspelled = spell.unknown(words)

    if misspelled:
        print(f"\n🔍{lc} Spelling Suggestions:")
        for word in misspelled:
            correction = spell.correction(word)
            print(f"{green}- {word} → {correction if correction else 'No suggestion'}")
    else:
        print(f"✅{green} No spelling errors found!")
      #bad api should use ai api instead -_-
      #to lazy to implement ai again -_-
    api_url = "https://api.languagetool.org/v2/check"
    params = {"text": text, "language": "en-US"}
    response = requests.post(api_url, data=params)

    if response.status_code == 200:
        result = response.json()
        if result["matches"]:
            print(f"\n📝{yellow} Grammar Suggestions:")
            for match in result["matches"]:
                print(f"- {match['message']}")
        else:
            print(f"✅{green} No grammar errors found!")
    else:
        print(f"⚠️{red} Error checking grammar!")



check_spelling_grammar()
