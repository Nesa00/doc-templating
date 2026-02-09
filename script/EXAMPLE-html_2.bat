@echo off
cd ../examples/html_2
call ..\..\.venv\Scripts\activate.bat
python generate_html.py
call ..\..\.venv\Scripts\deactivate.bat
