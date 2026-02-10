@echo off
call ..\.venv\Scripts\activate.bat
cd ..\examples\markdown
python generate_pdf.py
call ..\..\.venv\Scripts\deactivate.bat
cd ..\..\script
