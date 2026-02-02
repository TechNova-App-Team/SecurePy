@echo off
setlocal enabledelayedexpansion

REM Admin-Check
net session >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo FEHLER: Bitte mit Administrator-Rechten ausführen!
    echo.
    pause
    exit /b
)

echo.
echo Deinstalliere Vault Context Menu...
echo.

REM Entferne ALLE Registry-Eintraege (alte und neue Varianten)
echo Entferne Registry-Eintraege...

REM Neue Variante (VaultEncrypt/VaultDecrypt)
reg delete "HKCU\Software\Classes\*\shell\VaultEncrypt" /f >nul 2>&1
reg delete "HKCU\Software\Classes\.vault\shell\VaultDecrypt" /f >nul 2>&1

REM Alte Variante (EncryptWithVault/DecryptWithVault)
reg delete "HKCU\Software\Classes\*\shell\EncryptWithVault" /f >nul 2>&1
reg delete "HKCU\Software\Classes\.vault\shell\DecryptWithVault" /f >nul 2>&1

REM .vault File Association komplett entfernen
reg delete "HKCU\Software\Classes\.vault" /f >nul 2>&1
reg delete "HKCU\Software\Classes\VaultFile" /f >nul 2>&1

REM Default Icons entfernen (falls vorhanden)
reg delete "HKCU\Software\Classes\.vault\DefaultIcon" /f >nul 2>&1

REM UserChoice entfernen
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.vault" /f >nul 2>&1

echo [OK] Alle Registry-Eintraege geloescht

REM Explorer aktualisieren
echo.
echo Aktualisiere Windows Explorer...
taskkill /F /IM explorer.exe >nul 2>&1
timeout /t 1 /nobreak >nul
start explorer.exe

echo [OK] Explorer neugestartet

echo.
echo Deinstallation erfolgreich abgeschlossen!
echo Die Rechtsklick-Menues sollten nun entfernt sein.
echo.
pause
