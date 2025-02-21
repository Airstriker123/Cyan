@echo off
color 2
echo Installing Python modules... 
color 2
echo you can open cyan.py or start.bat if you opened this file before!)
color 2
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
