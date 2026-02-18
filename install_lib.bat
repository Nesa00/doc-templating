@echo off
REM Activate the virtual environment and install dependencies from requirements.txt
call .venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
call .venv\Scripts\deactivate.bat