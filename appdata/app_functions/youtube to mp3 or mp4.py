#youtube to mp3/mp4

'''

src:
https://www.youtube.com/watch?v=VgxnyKnB3qc
https://www.youtube.com/watch?v=ucXTQ0V8qMA&t=164s

'''
#autmatic?
#pip install pytube pydub ffmpeg
# pip install pytubefix
#pip install imageio[ffmpeg]
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment
from colors_app import *
import os


download_folder = "downloaded content"
os.makedirs(download_folder, exist_ok=True)

file_type = input(f'{yellow}What type of video do you wish to download (mp3/mp4): {white}')
url = input(f'{cyan}Enter URL of the video you want to download: {white}')


def mp4():
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Downloading: {yt.title}")
    ys = yt.streams.get_highest_resolution()
    ys.download(download_folder)


def mp3():
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"Downloading Audio: {yt.title}")
    stream = yt.streams.filter(only_audio=True).first()

    if not stream:
        print(f"{red}No audio stream available.")
        return

    # this will usually be in M4A format
    temp_file = stream.download(download_folder)
    mp3_file = os.path.join(download_folder, os.path.splitext(os.path.basename(temp_file))[0] + ".mp3")

    # Convert M4A to MP3 using pydub ;0
    try:
        audio = AudioSegment.from_file(temp_file, format="m4a")  # this prob does not work ;/
        audio.export(mp3_file, format="mp3")
        os.remove(temp_file)  # delete useless file ewwwwwwwwwwww -_-
        print(f"{green}MP3 downloaded! Check the {red}'downloaded content' folder.")
    except Exception as e:
        print(f"{red}Error during conversion: {e}")


if file_type in ['mp4', 'MP4', '2', 'Mp4', 'mP4', 'MPFOUR', '4', 'mpfour']:
    mp4()
    print(f'\n{green}Video downloaded! Check the {lc}"downloaded content"{red} folder.')
elif file_type in ['mp3', 'MP3', '1', 'Mp3', 'mP3', 'MPTHREE', '3', 'mpthree']:
    mp3()
    print(f'\n{green}MP3 downloaded! Check the {lc}"downloaded content"{red} folder.')


