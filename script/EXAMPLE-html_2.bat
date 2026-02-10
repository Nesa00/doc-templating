@echo off
call ..\.venv\Scripts\activate.bat
cd ..\examples\html_2
python generate_pdf.py
call ..\..\.venv\Scripts\deactivate.bat
cd ..\..\script
