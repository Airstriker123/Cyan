import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment
from colors_app import *
import requests
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


yt = MainColor2(r"""                                                                                                      
                            ██████████████████████████████████████████████████                            
                          ██████████████████████████████████████████████████████                          
                         ████████████████████████████████████████████████████████                         
                        ██████████████████████████████████████████████████████████                        
                        ███████████████████████████████████████████████████████████                       
                       ████████████████████████████████████████████████████████████                       
                       ████████████████████████  ██████████████████████████████████                       
                       ████████████████████████     ███████████████████████████████                       
                       ████████████████████████         ███████████████████████████                       
                       ████████████████████████            ████████████████████████                       
                       ████████████████████████                ████████████████████                       
                       ████████████████████████             ███████████████████████                       
                       ████████████████████████          ██████████████████████████                       
                       ████████████████████████      ██████████████████████████████                       
                       ████████████████████████   █████████████████████████████████                       
                       ████████████████████████████████████████████████████████████                       
                       ████████████████████████████████████████████████████████████                       
                        ███████████████████████████████████████████████████████████                       
                        ██████████████████████████████████████████████████████████                        
                         █████████████████████████████████████████████████████████                        
                          ██████████████████████████████████████████████████████                          
                            ██████████████████████████████████████████████████                            

""")

download_folder = "downloaded content"
os.makedirs(download_folder, exist_ok=True)

Slow(yt)
file_type = input(f'{yellow}What type of video do you wish to download (mp3/mp4): {white}')
url = input(f'{cyan}Enter URL of the video you want to download: {white}')

def mp4():
    try:
        yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
        print(f"Downloading: {yt.title}")
        ys = yt.streams.get_highest_resolution()
        ys.download(download_folder)
    except Exception as e:
        print(f"{red}Error: {e}")

def mp3():
    try:
        yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
        print(f"Downloading Audio: {yt.title}")
        stream = yt.streams.filter(only_audio=True).first()

        if not stream:
            print(f"{red}No audio stream available.")
            return

        temp_file = stream.download(download_folder)
        mp3_file = os.path.join(download_folder, os.path.splitext(os.path.basename(temp_file))[0] + ".mp3")

        try:
            audio = AudioSegment.from_file(temp_file, format="m4a")
            audio.export(mp3_file, format="mp3")
            os.remove(temp_file)
            print(f"{green}MP3 downloaded! Check the {red}'downloaded content' folder.")
        except Exception as e:
            print(f"{red}Error during conversion: {e}")
    except Exception as e:
        print(f"{red}Error: {e}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"{red}Error: Unable to access the URL. Please check the URL and try again.")
else:
    if file_type.lower() in ['mp4', '2', 'mpfour', '4']:
        mp4()
        print(f'\n{green}Video downloaded! Check the {lc}"downloaded content"{red} folder.')
    elif file_type.lower() in ['mp3', '1', 'mpthree', '3']:
        mp3()
        print(f'\n{green}MP3 downloaded! Check the {lc}"downloaded content"{red} folder.')
    else:
        print(f'An error occurred, most likely a network issue. Try using a different network.')


