@echo off
color 2
echo Installing Python modules:
pip install -r appdata\requirements.txt
color 1
echo starting app (cyan.py)
python cyan.py
pause
