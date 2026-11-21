@echo off
TITLE The Future of Renewable Energy - Launch Script
COLOR 0B

echo =========================================================================
echo    THE FUTURE OF RENEWABLE ENERGY -- POWERING A SUSTAINABLE TOMORROW
echo    Authors: Dr. Sebastian Clarke ^& Dr. Oliver Bennett
echo =========================================================================
echo.

cd /d "%~dp0"
echo [SETUP] Current Directory: %CD%

:: Check Python installation
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python was not found in your system PATH!
    echo Please install Python 3.10+ from python.org and add it to your PATH.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VER=%%i
echo [SETUP] Detected %PYTHON_VER%

:: Install dependencies if missing
echo [SETUP] Checking required dependencies...
python -m pip install -r requirements.txt --quiet --disable-pip-version-check
if %ERRORLEVEL% NEQ 0 (
    echo [WARN] Pip install returned a non-zero code; proceeding with system libraries...
) else (
    echo [SETUP] Dependencies verified.
)

:: Run MATLAB runner to ensure all results and plots are precomputed
if not exist "results\solar_irradiance_power.png" (
    echo [SETUP] Generating scientific plots and numerical results...
    python matlab_runner.py
)

:: Open web browser after 2 seconds in parallel
start "" cmd /c "timeout /t 2 /nobreak >nul & start http://127.0.0.1:5000/"

:: Launch Flask server
echo.
echo =========================================================================
echo   Starting local Flask server on http://127.0.0.1:5000/
echo   Press CTRL+C in this terminal window to stop the server.
echo =========================================================================
echo.
python app.py

pause
