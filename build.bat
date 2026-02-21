@echo off
echo =========================================
echo Building Roku Bridge Windows Executable
echo =========================================

REM 1. Create and activate an isolated Virtual Environment
echo Setting up Python Virtual Environment...
if not exist "venv" python -m venv venv
call venv\Scripts\activate

REM 2. Install required dependencies cleanly
echo Installing dependencies...
pip install -r requirements.txt

REM 3. Clean up old builds to prevent conflicts
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

REM 4. Compile the executable
echo Compiling the executable...
pyinstaller ^
  --noconfirm ^
  --onefile ^
  --windowed ^
  --name "RokuBridge" ^
  --icon "icon.ico" ^
  --add-data "templates;templates" ^
  --add-data "static;static" ^
  app.py

echo.
echo =========================================
echo Build Complete! Check the \dist\ folder.
echo =========================================
pause