@echo off
setlocal

REM Run Fractured Light prototype on Windows.
REM Usage: double-click this file or run from cmd/powershell.

set "ROOT_DIR=%~dp0"
cd /d "%ROOT_DIR%"
set "PYTHONPATH=src"

if not exist "src\fractured_light\main.py" (
    echo [ERROR] Could not find src\fractured_light\main.py
    echo Make sure this script is in the repository root.
    exit /b 1
)

where py >nul 2>&1
if %errorlevel%==0 (
    py -3 -m fractured_light.main
) else (
    python -m fractured_light.main
)

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to launch the game.
    echo Try installing Python 3 and run: python -m fractured_light.main
    pause
    exit /b 1
)

echo.
echo Done.
pause
