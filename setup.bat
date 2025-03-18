@echo off
color 2
echo Make sure you have the latest version of Python!
echo This script will install the required Python modules for your application.
echo.

echo The following modules will be installed:
echo.
color 3
echo colorama - Provides color support for console text.
echo pytubefix - A patched version of pytube for downloading YouTube videos.
echo pydub - Handles audio processing, including conversion and manipulation.
echo ffmpeg - A multimedia framework used for handling audio, video, and other media files.
echo imageio[ffmpeg] - Enables reading and writing of images and videos, integrating ffmpeg.
echo fade - Adds text fading effects in the console.
echo Flask - A lightweight web framework for creating web applications.
echo requests - A popular library for handling HTTP requests.
echo rich - Provides rich text formatting for the console.
echo PyExecJS - Allows running JavaScript code from Python.
echo datetime - Handles date and time operations.
echo simplejson - An extension of the built-in JSON module with extra features.
echo jsons - A JSON serialization/deserialization library.
echo pypi-json - Retrieves package metadata from PyPI.
echo textblob - A text processing library for natural language processing (NLP).
echo pyspellchecker - A simple spell-checking library.
echo sympy - A symbolic mathematics library for algebraic computations.
echo.
color 2
echo Note: This app depends on all of these modules to run
choice /c YN /m "Do you want to install these modules?"
if errorlevel 2 exit /b

color 2
echo Installing Python modules...
pip install --upgrade pip
pip install -r appdata/requirements.txt

if %errorlevel% neq 0 (
    echo Error installing modules. Check errors above.
    pause
    exit /b
)

color 1
echo Starting app (cyan.py)
python appdata/fd.py
python cyan.py
pause
