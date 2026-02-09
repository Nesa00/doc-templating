@echo off
cd ../
call .\venv\Scripts\activate.bat
python generate_pdf.py
call .\venv\Scripts\deactivate.bat
