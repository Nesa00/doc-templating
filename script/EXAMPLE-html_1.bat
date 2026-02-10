@echo off
call ..\.venv\Scripts\activate.bat
cd ..\examples\html_1
python generate_pdf.py
call ..\..\.venv\Scripts\deactivate.bat
cd ..\..\script
