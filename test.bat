@echo off
REM Activate the virtual environment and run all pytest tests
call .venv\Scripts\activate.bat
pytest
call .venv\Scripts\deactivate.bat
