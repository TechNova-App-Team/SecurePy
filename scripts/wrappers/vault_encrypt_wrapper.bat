@echo off
setlocal enabledelayedexpansion

REM Wrapper für Verschlüsselung
REM Wird vom Context Menu aufgerufen mit %1 = Dateiname

set "SCRIPT_DIR=%~dp0"
set "VAULT_PY=%SCRIPT_DIR%..\..\src\vault.py"
set "DATEI=%~1"

REM Finde Python
set "PYTHON_EXE="
for /f "tokens=*" %%i in ('where python 2^>nul') do (
    if "!PYTHON_EXE!"=="" set "PYTHON_EXE=%%i"
)

if "!PYTHON_EXE!"=="" (
    echo.
    echo FEHLER: Python nicht gefunden!
    echo Bitte installiere Python und füge es zu PATH hinzu.
    echo.
    pause
    exit /b 1
)

REM Starte Verschlüsselung
"!PYTHON_EXE!" "!VAULT_PY!" v "!DATEI!"

pause
