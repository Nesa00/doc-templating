@echo off
cd ../examples/html_1
call ..\..\.venv\Scripts\activate.bat
python generate_pdf.py
call ..\..\.venv\Scripts\deactivate.bat
