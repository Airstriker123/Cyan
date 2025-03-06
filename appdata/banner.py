import fade # module for faded text 
from .functions import *

# function prints banner 
def banner():

    banner = """    
                             ▄████▓██   ██▓▄▄▄      ███▄    █    ▄▄▄█████▓▒█████  ▒█████  ██▓    
                            ▒██▀ ▀█▒██  ██▒████▄    ██ ▀█   █    ▓  ██▒ ▓▒██▒  ██▒██▒  ██▓██▒    
                            ▒▓█    ▄▒██ ██▒██  ▀█▄ ▓██  ▀█ ██▒   ▒ ▓██░ ▒▒██░  ██▒██░  ██▒██░    
                            ▒▓▓▄ ▄██░ ▐██▓░██▄▄▄▄██▓██▒  ▐▌██▒   ░ ▓██▓ ░▒██   ██▒██   ██▒██░    
                            ▒ ▓███▀ ░ ██▒▓░▓█   ▓██▒██░   ▓██░     ▒██▒ ░░ ████▓▒░ ████▓▒░██████▒
                            ░ ░▒ ▒  ░██▒▒▒ ▒▒   ▓▒█░ ▒░   ▒ ▒      ▒ ░░  ░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░▓  ░
                              ░  ▒ ▓██ ░▒░  ▒   ▒▒ ░ ░░   ░ ▒░       ░     ░ ▒ ▒░  ░ ▒ ▒░░ ░ ▒  ░
                            ░      ▒ ▒ ░░   ░   ▒     ░   ░ ░      ░     ░ ░ ░ ▒ ░ ░ ░ ▒   ░ ░   
                            ░ ░    ░ ░          ░  ░        ░                ░ ░     ░ ░     ░  ░
                            ░      ░ ░                                                                                                                             
    """
    # Apply fade effect to the banner
    faded_text = fade.greenblue(banner)

    # Print the faded text
    (Slow(f"{faded_text}\n"))

