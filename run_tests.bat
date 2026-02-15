@echo off
setlocal

REM Run Fractured Light unit tests on Windows.

set "ROOT_DIR=%~dp0"
cd /d "%ROOT_DIR%"
set "PYTHONPATH=src"

where py >nul 2>&1
if %errorlevel%==0 (
    py -3 -m unittest discover -s tests -v
) else (
    python -m unittest discover -s tests -v
)

if errorlevel 1 (
    echo.
    echo [ERROR] Tests failed.
    pause
    exit /b 1
)

echo.
echo All tests passed.
pause
