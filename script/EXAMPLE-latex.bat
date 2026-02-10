@echo off
call ..\.venv\Scripts\activate.bat
cd ..\examples\latex
python generate_pdf.py
call ..\..\.venv\Scripts\deactivate.bat
cd ..\..\script
