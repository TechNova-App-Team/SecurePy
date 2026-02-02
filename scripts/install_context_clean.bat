@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 2>&1

REM Admin-Check
net session >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo FEHLER: Bitte mit Administrator-Rechten ausführen!
    echo Rechtsklick auf diese Datei > 'Als Administrator ausführen'
    echo.
    pause
    exit /b
)

REM Finde vault.py und Wrapper
set "SCRIPT_DIR=%~dp0"
set "VAULT_PY=%SCRIPT_DIR%..\src\vault.py"
set "ENCRYPT_WRAPPER=%SCRIPT_DIR%wrappers\vault_encrypt_wrapper.bat"
set "DECRYPT_WRAPPER=%SCRIPT_DIR%wrappers\vault_decrypt_wrapper.bat"

if not exist "%VAULT_PY%" (
    echo.
    echo [x] Fehler: vault.py nicht gefunden!
    echo    Pfad: %VAULT_PY%
    echo.
    pause
    exit /b
)

if not exist "%ENCRYPT_WRAPPER%" (
    echo.
    echo [x] Fehler: vault_encrypt_wrapper.bat nicht gefunden!
    echo    Pfad: %ENCRYPT_WRAPPER%
    echo.
    pause
    exit /b
)

if not exist "%DECRYPT_WRAPPER%" (
    echo.
    echo [x] Fehler: vault_decrypt_wrapper.bat nicht gefunden!
    echo    Pfad: %DECRYPT_WRAPPER%
    echo.
    pause
    exit /b
)

echo.
echo Installation wird durchgefuehrt...
echo.

REM 1. Alle Dateien - Verschluesseln
echo [1/4] Registriere: Alle Dateien - Mit Vault verschluesseln

reg add "HKCU\Software\Classes\*\shell\VaultEncrypt" /ve /d "Mit Vault verschluesseln" /f >nul 2>&1
reg add "HKCU\Software\Classes\*\shell\VaultEncrypt\command" /ve /d "\"%ENCRYPT_WRAPPER%\" \"%%1\"" /f >nul 2>&1

echo      [OK] Alle Dateitypen registriert

REM 2. .vault Dateien - Datei-Assoziation erstellen
echo [2/4] Registriere: .vault als Dateityp

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.vault\UserChoice" /ve /d "VaultFile" /f >nul 2>&1
reg add "HKCU\Software\Classes\.vault" /ve /d "VaultFile" /f >nul 2>&1

echo      [OK] .vault Dateityp erstellt

REM 3. .vault Default-Handler - Entschlüsseln
echo [3/4] Registriere: .vault Standard-Handler (Entschlusseln)

reg add "HKCU\Software\Classes\VaultFile" /ve /d "Vault Encrypted File" /f >nul 2>&1
reg add "HKCU\Software\Classes\VaultFile\shell" /ve /d "open" /f >nul 2>&1
reg add "HKCU\Software\Classes\VaultFile\shell\open\command" /ve /d "\"%DECRYPT_WRAPPER%\" \"%%1\"" /f >nul 2>&1

REM Auch als Context-Menu-Option
reg add "HKCU\Software\Classes\.vault\shell\VaultDecrypt" /ve /d "Mit Vault entschlusseln" /f >nul 2>&1
reg add "HKCU\Software\Classes\.vault\shell\VaultDecrypt\command" /ve /d "\"%DECRYPT_WRAPPER%\" \"%%1\"" /f >nul 2>&1

echo      [OK] .vault Entschluesselung registriert

REM 4. Explorer aktualisieren
echo [4/4] Aktualisiere Windows Explorer...

taskkill /F /IM explorer.exe >nul 2>&1
timeout /t 1 /nobreak >nul
start explorer.exe

echo      [OK] Explorer aktualisiert

echo.
echo Installation erfolgreich abgeschlossen!
echo.
echo Verwendung:
echo  - Rechtsklick auf Datei > "Mit Vault verschluesseln"
echo  - Rechtsklick auf .vault Datei > "Mit Vault entschlusseln"
echo  - ODER: Doppelklick auf .vault Datei (startet Entschluesselung direkt)
echo.
pause
