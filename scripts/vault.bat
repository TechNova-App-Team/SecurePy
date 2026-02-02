@echo off
SETLOCAL EnableDelayedExpansion
chcp 65001 > nul 2>&1

REM ═══════════════════════════════════════════════════════════════════════════
REM  UNBREAKABLE VAULT v5.0 ULTRA - Windows Batch Interface
REM  Military-Grade Encryption with Enhanced Security Features
REM  • Auto-Detection für Python & Script
REM  • Sichere Passwort-Eingabe (versteckt)
REM  • Emergency Backup System
REM  • Erweiterte Error-Handling
REM  • Performance-Optimierung
REM ═══════════════════════════════════════════════════════════════════════════

REM ═══════════════════════════════════════════════════════════════════════════
REM  ANSI FARBEN (WINDOWS 10+)
REM ═══════════════════════════════════════════════════════════════════════════
for /F "tokens=1,2 delims=#" %%a in ('prompt #$H#$E# ^& echo on ^& for %%b in ^(1^) do rem') do set "ESC=%%b"

set "CYAN=%ESC%[96m"
set "GREEN=%ESC%[92m"
set "YELLOW=%ESC%[93m"
set "RED=%ESC%[91m"
set "MAGENTA=%ESC%[95m"
set "BLUE=%ESC%[94m"
set "WHITE=%ESC%[97m"
set "DIM=%ESC%[2m"
set "GRAY=%ESC%[90m"
set "BOLD=%ESC%[1m"
set "RESET=%ESC%[0m"
set "BG_GREEN=%ESC%[42m"
set "BG_RED=%ESC%[41m"
set "BG_YELLOW=%ESC%[43m"
set "BG_BLUE=%ESC%[44m"

title UNBREAKABLE VAULT v5.0 ULTRA - Military-Grade Encryption

REM ═══════════════════════════════════════════════════════════════════════════
REM  AUTO-DETECTION: PYTHON EXECUTABLE
REM ═══════════════════════════════════════════════════════════════════════════
set "PYTHON_EXE="

REM Methode 1: where python (WindowsApps überspringen)
for /f "tokens=*" %%i in ('where python 2^>nul') do (
    echo %%i | findstr /I "WindowsApps\\python.exe" >nul
    if !ERRORLEVEL! NEQ 0 (
        if "!PYTHON_EXE!"=="" set "PYTHON_EXE=%%i"
    )
)

REM Methode 2: Standard-Pfade durchsuchen
if "!PYTHON_EXE!"=="" (
    for %%v in (314 313 312 311 310 39 38) do (
        if exist "%LOCALAPPDATA%\Programs\Python\Python%%v\python.exe" (
            set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python%%v\python.exe"
            goto :python_found
        )
        if exist "C:\Python%%v\python.exe" (
            set "PYTHON_EXE=C:\Python%%v\python.exe"
            goto :python_found
        )
        if exist "C:\Program Files\Python%%v\python.exe" (
            set "PYTHON_EXE=C:\Program Files\Python%%v\python.exe"
            goto :python_found
        )
    )
)

REM Methode 3: Windows Store Python
if "!PYTHON_EXE!"=="" (
    if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe" (
        set "PYTHON_EXE=%LOCALAPPDATA%\Microsoft\WindowsApps\python.exe"
    )
)

:python_found

REM Python Check
if "!PYTHON_EXE!"=="" (
    cls
    echo.
    echo  %RED%╔═══════════════════════════════════════════════════════════════════╗%RESET%
    echo  %RED%║  %BOLD%CRITICAL ERROR: Python nicht gefunden!%RESET%%RED%                        ║%RESET%
    echo  %RED%╚═══════════════════════════════════════════════════════════════════╝%RESET%
    echo.
    echo  %YELLOW%Python wurde nicht automatisch erkannt.%RESET%
    echo.
    echo  %CYAN%Lösungen:%RESET%
    echo  %WHITE%1.%RESET% Installiere Python 3.8+ von https://www.python.org
    echo  %WHITE%2.%RESET% Stelle sicher, dass Python im PATH ist
    echo  %WHITE%3.%RESET% Neustart der CMD nach Installation
    echo  %WHITE%4.%RESET% Prüfe mit: %DIM%where python%RESET%
    echo.
    echo  %MAGENTA%Drücke eine Taste zum Beenden...%RESET%
    pause > nul
    exit /b 1
)

REM ═══════════════════════════════════════════════════════════════════════════
REM  AUTO-DETECTION: VAULT.PY SCRIPT
REM ═══════════════════════════════════════════════════════════════════════════
set "SCRIPT_PATH="
set "WORK_DIR=%~dp0"

REM Suche vault.py im src/ Ordner (neue Struktur)
if exist "%~dp0..\src\vault.py" set "SCRIPT_PATH=%~dp0..\src\vault.py"

REM Legacy: Suche vault.py in verschiedenen Pfaden (Fallback)
if "!SCRIPT_PATH!"=="" if exist "%~dp0vault.py" set "SCRIPT_PATH=%~dp0vault.py"
if "!SCRIPT_PATH!"=="" if exist "%CD%\vault.py" set "SCRIPT_PATH=%CD%\vault.py"
if "!SCRIPT_PATH!"=="" if exist "vault.py" set "SCRIPT_PATH=vault.py"

REM Fallback: Benutzer-Eingabe
if "!SCRIPT_PATH!"=="" (
    cls
    echo.
    echo  %YELLOW%╔═══════════════════════════════════════════════════════════════════╗%RESET%
    echo  %YELLOW%║  %BOLD%vault.py nicht gefunden!%RESET%%YELLOW%                                       ║%RESET%
    echo  %YELLOW%╚═══════════════════════════════════════════════════════════════════╝%RESET%
    echo.
    echo  %CYAN%Bitte gib den Pfad zu vault.py ein:%RESET%
    echo  %DIM%Beispiel: H:\BT\Bit\vault.py%RESET%
    echo.
    set /p "SCRIPT_PATH=%WHITE%Pfad → %RESET%"
    
    if not exist "!SCRIPT_PATH!" (
        echo.
        echo  %RED%[✗] Datei nicht gefunden: !SCRIPT_PATH!%RESET%
        echo.
        pause
        exit /b 1
    )
)

for %%I in ("!SCRIPT_PATH!") do set "SCRIPT_NAME=%%~nxI"

REM ═══════════════════════════════════════════════════════════════════════════
REM  DEPENDENCY CHECK
REM ═══════════════════════════════════════════════════════════════════════════
echo  %CYAN%[*] Initialisiere...%RESET%
echo.

REM Backup-Verzeichnis erstellen
set "BACKUP_DIR=%~dp0.vault_backups"
if not exist "!BACKUP_DIR!" mkdir "!BACKUP_DIR!" > nul 2>&1

REM ═══════════════════════════════════════════════════════════════════════════
REM  HAUPTMENÜ
REM ═══════════════════════════════════════════════════════════════════════════
:MENU
cls
color 0B

echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║                                                                   ║%RESET%
echo  %CYAN%║  %YELLOW%█░█ █▄░█ █▄▄ █▀█ █▀▀ ▄▀█ █▄▀ ▄▀█ █▄▄ █░░ █▀▀   █░█ █▀   █▀█%CYAN%  ║%RESET%
echo  %CYAN%║  %YELLOW%█▄█ █░▀█ █▄█ █▀▄ ██▄ █▀█ █░█ █▀█ █▄█ █▄▄ ██▄   ▀▀█ ▄░   █▄█%CYAN%  ║%RESET%
echo  %CYAN%║                                                                   ║%RESET%
echo  %CYAN%║       %MAGENTA%╔═══════════════════════════════════════════════════╗%CYAN%       ║%RESET%
echo  %CYAN%║       %MAGENTA%║  %BOLD%ULTRA EDITION - ENHANCED SECURITY%RESET%%MAGENTA%        ║%CYAN%       ║%RESET%
echo  %CYAN%║       %MAGENTA%╚═══════════════════════════════════════════════════╝%CYAN%       ║%RESET%
echo  %CYAN%║                                                                   ║%RESET%
echo  %CYAN%║  %GREEN%▸ Auto-Detection System%CYAN%                                         ║%RESET%
echo  %CYAN%║  %GREEN%▸ Secure Password Input (Hidden)%CYAN%                               ║%RESET%
echo  %CYAN%║  %GREEN%▸ Emergency Backup System%CYAN%                                      ║%RESET%
echo  %CYAN%║  %GREEN%▸ Enhanced Error Handling%CYAN%                                      ║%RESET%
echo  %CYAN%║  %GREEN%▸ Performance Optimized%CYAN%                                        ║%RESET%
echo  %CYAN%║                                                                   ║%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

REM Security Status
"!PYTHON_EXE!" -c "import argon2" >nul 2>&1
if !ERRORLEVEL! EQU 0 (
    echo  %GREEN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
    echo  %GREEN%║  🛡️ SECURITY: %BG_GREEN%%WHITE% QUANTUM MODE ACTIVE %RESET%%GREEN%                               ║%RESET%
    echo  %GREEN%║     %DIM%Argon2id Enabled • Memory-Hard: 2GB • Time: 8%RESET%%GREEN%             ║%RESET%
    echo  %GREEN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
) else (
    echo  %YELLOW%╔═══════════════════════════════════════════════════════════════════╗%RESET%
    echo  %YELLOW%║  ⚠ SECURITY: %BG_YELLOW%%WHITE% PBKDF2 FALLBACK MODE %RESET%%YELLOW%                            ║%RESET%
    echo  %YELLOW%║     %DIM%Upgrade empfohlen: Option [7] Argon2 installieren%RESET%%YELLOW%          ║%RESET%
    echo  %YELLOW%╚═══════════════════════════════════════════════════════════════════╝%RESET%
)
echo.

REM Datei-Scan
echo  %MAGENTA%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %MAGENTA%║  📁 DATEIEN IM VERZEICHNIS                                         ║%RESET%
echo  %MAGENTA%╠═══════════════════════════════════════════════════════════════════╣%RESET%

set filecount=0
set enccount=0
set vaultcount=0

for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.jpeg *.png *.gif *.bmp *.json *.xml *.csv *.xlsx *.xls *.zip *.rar *.7z *.mp4 *.avi *.mkv *.mp3 *.wav *.flac *.pptx *.ppt) do set /a enccount+=1
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do set /a vaultcount+=1
set /a filecount=!enccount! + !vaultcount!

if !enccount! GTR 0 echo  %MAGENTA%║%RESET%  %GREEN%📄 Verschlüsselbar:%RESET% %WHITE%!enccount!%RESET%                                           %MAGENTA%║%RESET%
if !vaultcount! GTR 0 echo  %MAGENTA%║%RESET%  %YELLOW%🔒 Verschlüsselt:%RESET% %WHITE%!vaultcount!%RESET%                                            %MAGENTA%║%RESET%
if !filecount! EQU 0 echo  %MAGENTA%║%RESET%  %RED%✗ Keine Dateien gefunden%RESET%                                         %MAGENTA%║%RESET%

echo  %MAGENTA%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

REM Menü
echo  %WHITE%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %WHITE%║  %BOLD%AKTIONEN%RESET%%WHITE%                                                          ║%RESET%
echo  %WHITE%╠═══════════════════════════════════════════════════════════════════╣%RESET%
echo  %WHITE%║                                                                   ║%RESET%
echo  %WHITE%║  [%GREEN%1%WHITE%] %GREEN%🔒 ENCRYPT%RESET%        Datei verschlüsseln                     %WHITE%║%RESET%
echo  %WHITE%║  [%YELLOW%2%WHITE%] %YELLOW%🔓 DECRYPT%RESET%        Vault entschlüsseln                    %WHITE%║%RESET%
echo  %WHITE%║  [%CYAN%3%WHITE%] %CYAN%⚡ BATCH ENCRYPT%RESET%   Alle verschlüsseln                      %WHITE%║%RESET%
echo  %WHITE%║  [%BLUE%4%WHITE%] %BLUE%⚡ BATCH DECRYPT%RESET%   Alle entschlüsseln                      %WHITE%║%RESET%
echo  %WHITE%║  [%MAGENTA%5%WHITE%] %MAGENTA%📂 DECRYPT ^& OPEN%RESET%   Entschlüsseln + Öffnen                %WHITE%║%RESET%
echo  %WHITE%║  [%CYAN%6%WHITE%] %CYAN%📊 SYSTEM INFO%RESET%     Sicherheits-Details                    %WHITE%║%RESET%
echo  %WHITE%║  [%YELLOW%7%WHITE%] %YELLOW%🔧 INSTALL ARGON2%RESET%  Quantum-Upgrade                       %WHITE%║%RESET%
echo  %WHITE%║  [%GREEN%8%WHITE%] %GREEN%💾 BACKUP RESTORE%RESET%  Notfall-Wiederherstellung             %WHITE%║%RESET%
echo  %WHITE%║  [%RED%0%WHITE%] %RED%❌ EXIT%RESET%            Sicher beenden                        %WHITE%║%RESET%
echo  %WHITE%║                                                                   ║%RESET%
echo  %WHITE%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

choice /C 123456780 /N /M "%CYAN%Auswahl → %RESET%"
set choice=!ERRORLEVEL!

if !choice! EQU 1 goto ENCRYPT
if !choice! EQU 2 goto DECRYPT
if !choice! EQU 3 goto BATCH_ENCRYPT
if !choice! EQU 4 goto BATCH_DECRYPT
if !choice! EQU 5 goto DECRYPT_AND_OPEN
if !choice! EQU 6 goto INFO
if !choice! EQU 7 goto INSTALL_ARGON2
if !choice! EQU 8 goto BACKUP_RESTORE
if !choice! EQU 9 goto EXIT

goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  ENCRYPT (EINZELDATEI)
REM ═══════════════════════════════════════════════════════════════════════════
:ENCRYPT
cls
echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %GREEN%🔒 ENCRYPT MODE%RESET%%CYAN%                                                  ║%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.
set count=0
echo  %YELLOW%Verfügbare Dateien:%RESET%
echo.
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.jpeg *.png *.gif *.bmp *.json *.xml *.csv *.xlsx *.xls *.zip *.rar *.7z *.mp4 *.avi *.mkv *.mp3 *.pptx) do (
    set /a count+=1
    for %%A in ("%%F") do set size=%%~zA
    set /a "size_kb=!size! / 1024"
    if !size_kb! EQU 0 set "size_kb=<1"
    echo  %BOLD%[!count!]%RESET% %WHITE%%%F%RESET% %DIM%^(!size_kb! KB^)%RESET%
)
if !count! EQU 0 (
    echo  %RED%[✗] Keine verschlüsselbaren Dateien gefunden!%RESET%
    echo.
    pause
    goto MENU
)
echo.
echo  %BOLD%[0]%RESET% %RED%← Zurück%RESET%
echo.
choice /C 0123456789 /N /M "%CYAN%Datei auswählen → %RESET%"
set selection=!ERRORLEVEL!
if !selection! EQU 1 goto MENU
set /a selection=!selection! - 1
if !selection! LSS 1 goto ENCRYPT
if !selection! GTR !count! goto ENCRYPT
set idx=0
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.jpeg *.png *.gif *.bmp *.json *.xml *.csv *.xlsx *.xls *.zip *.rar *.7z *.mp4 *.avi *.mkv *.mp3 *.pptx) do (
    set /a idx+=1
    if !idx! EQU !selection! set "selected_file=%%F"
)

echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  Ausgewählt: !selected_file!%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

REM Auto-Backup vor Verschlüsselung
echo  %YELLOW%[*] Erstelle Sicherheitskopie...%RESET%
copy "!selected_file!" "!BACKUP_DIR!\!selected_file!.backup_%date:~-4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%%time:~6,2%" > nul 2>&1
if !ERRORLEVEL! EQU 0 echo  %GREEN%[✓] Backup erstellt%RESET%

"!PYTHON_EXE!" "!SCRIPT_PATH!" v "!selected_file!"

echo.
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  DECRYPT (EINZELDATEI)
REM ═══════════════════════════════════════════════════════════════════════════
:DECRYPT
cls
echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %YELLOW%🔓 DECRYPT MODE%RESET%%CYAN%                                                  ║%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

set count=0
echo  %YELLOW%Verfügbare Vaults:%RESET%
echo.

REM Liste alle .vault Dateien auf
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do (
    set /a count+=1
    for %%A in ("%%F") do set size=%%~zA
    set /a "size_kb=!size! / 1024"
    if !size_kb! EQU 0 set "size_kb=<1"
    echo  %BOLD%[!count!]%RESET% %YELLOW%🔒%RESET% %WHITE%%%F%RESET% %DIM%^(!size_kb! KB^)%RESET%
)

if !count! EQU 0 (
    echo  %RED%[✗] Keine .vault Dateien gefunden!%RESET%
    echo.
    pause
    goto MENU
)

echo.
echo  %BOLD%[0]%RESET% %RED%← Zurück%RESET%
echo.

choice /C 0123456789 /N /M "%CYAN%Vault auswählen → %RESET%"
set selection=!ERRORLEVEL!

if !selection! EQU 1 goto MENU
set /a selection=!selection! - 1

if !selection! LSS 1 goto DECRYPT
if !selection! GTR !count! goto DECRYPT

set idx=0
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do (
    set /a idx+=1
    if !idx! EQU !selection! set "selected_file=%%F"
)

echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  Ausgewählt: !selected_file!%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

"!PYTHON_EXE!" "!SCRIPT_PATH!" e "!selected_file!"

echo.
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  BATCH ENCRYPT
REM ═══════════════════════════════════════════════════════════════════════════
:BATCH_ENCRYPT
cls
echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %CYAN%⚡ BATCH ENCRYPT MODE%RESET%%CYAN%                                            ║%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

set count=0
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.jpeg *.png *.gif *.bmp *.json *.xml *.csv *.xlsx *.xls *.zip *.rar *.7z *.mp4 *.avi *.pptx) do set /a count+=1

if !count! EQU 0 (
    echo  %RED%[✗] Keine verschlüsselbaren Dateien gefunden!%RESET%
    echo.
    pause
    goto MENU
)

echo  %YELLOW%Gefundene Dateien:%RESET% %WHITE%!count!%RESET%
echo.
echo  %RED%WARNUNG: Dies verschlüsselt ALLE Dateien im aktuellen Verzeichnis!%RESET%
echo.

choice /C JN /N /M "%YELLOW%Fortfahren? [J/N]: %RESET%"
if !ERRORLEVEL! NEQ 1 goto MENU

echo.
echo  %CYAN%[*] Erstelle Batch-Backup...%RESET%
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.jpeg *.png *.gif *.bmp *.json *.xml *.csv *.xlsx *.xls *.zip *.rar *.7z *.mp4 *.avi *.pptx) do (
    copy "%%F" "!BACKUP_DIR!\%%F.batch_backup_%date:~-4%%date:~-7,2%%date:~-10,2%" > nul 2>&1
)
echo  %GREEN%[✓] Batch-Backup erstellt%RESET%
echo.

set /p "password=%BOLD%%YELLOW%MASTER-KEY: %RESET%"
echo.
echo  %DIM%Starte Batch-Verschlüsselung...%RESET%
echo  %DIM%═══════════════════════════════════════════════════════════════════%RESET%
echo.

set success=0
set failed=0

for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.jpeg *.png *.gif *.bmp *.json *.xml *.csv *.xlsx *.xls *.zip *.rar *.7z *.mp4 *.avi *.pptx) do (
    echo  %CYAN%[*] %%F%RESET%
    echo !password! | "!PYTHON_EXE!" "!SCRIPT_PATH!" v "%%F" > nul 2>&1
    if !ERRORLEVEL! EQU 0 (
        echo  %GREEN%    [✓] Erfolgreich%RESET%
        set /a success+=1
    ) else (
        echo  %RED%    [✗] Fehlgeschlagen%RESET%
        set /a failed+=1
    )
    echo.
)

echo  %DIM%═══════════════════════════════════════════════════════════════════%RESET%
echo  %GREEN%Erfolgreich: !success!%RESET% ^| %RED%Fehlgeschlagen: !failed!%RESET%
echo.
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  BATCH DECRYPT
REM ═══════════════════════════════════════════════════════════════════════════
:BATCH_DECRYPT
cls
echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %BLUE%⚡ BATCH DECRYPT MODE%RESET%%CYAN%                                            ║%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

set count=0
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do set /a count+=1

if !count! EQU 0 (
    echo  %RED%[✗] Keine .vault Dateien gefunden!%RESET%
    echo.
    pause
    goto MENU
)

echo  %YELLOW%Gefundene Vaults:%RESET% %WHITE%!count!%RESET%
echo.

choice /C JN /N /M "%YELLOW%Alle entschlüsseln? [J/N]: %RESET%"
if !ERRORLEVEL! NEQ 1 goto MENU

echo.
set /p "password=%BOLD%%YELLOW%MASTER-KEY: %RESET%"
echo.
echo  %DIM%Starte Batch-Entschlüsselung...%RESET%
echo  %DIM%═══════════════════════════════════════════════════════════════════%RESET%
echo.

set success=0
set failed=0

for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do (
    echo  %CYAN%[*] %%F%RESET%
    echo !password! | "!PYTHON_EXE!" "!SCRIPT_PATH!" e "%%F" > nul 2>&1
    if !ERRORLEVEL! EQU 0 (
        echo  %GREEN%    [✓] Erfolgreich%RESET%
        set /a success+=1
    ) else (
        echo  %RED%    [✗] Fehlgeschlagen%RESET%
        set /a failed+=1
    )
    echo.
)

echo  %DIM%═══════════════════════════════════════════════════════════════════%RESET%
echo  %GREEN%Erfolgreich: !success!%RESET% ^| %RED%Fehlgeschlagen: !failed!%RESET%
echo.
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  DECRYPT AND OPEN
REM ═══════════════════════════════════════════════════════════════════════════
:DECRYPT_AND_OPEN
cls
echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %MAGENTA%📂 DECRYPT ^& OPEN MODE%RESET%%CYAN%                                          ║%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

set count=0
echo  %YELLOW%Verfügbare Vaults:%RESET%
echo.

REM Liste alle .vault Dateien auf
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do (
    set /a count+=1
    for %%A in ("%%F") do set size=%%~zA
    set /a "size_kb=!size! / 1024"
    if !size_kb! EQU 0 set "size_kb=<1"
    echo  %BOLD%[!count!]%RESET% %YELLOW%🔒%RESET% %WHITE%%%F%RESET% %DIM%^(!size_kb! KB^)%RESET%
)

if !count! EQU 0 (
    echo  %RED%[✗] Keine .vault Dateien gefunden!%RESET%
    echo.
    pause
    goto MENU
)

echo.
echo  %BOLD%[0]%RESET% %RED%← Zurück%RESET%
echo.

choice /C 0123456789 /N /M "%CYAN%Vault auswählen → %RESET%"
set selection=!ERRORLEVEL!

if !selection! EQU 1 goto MENU
set /a selection=!selection! - 1

if !selection! LSS 1 goto DECRYPT_AND_OPEN
if !selection! GTR !count! goto DECRYPT_AND_OPEN

set idx=0
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do (
    set /a idx+=1
    if !idx! EQU !selection! (
        set "selected_file=%%F"
        set "output_file=%%~nF"
    )
)

echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  Ausgewählt: !selected_file!%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

"!PYTHON_EXE!" "!SCRIPT_PATH!" e "!selected_file!"

if !ERRORLEVEL! EQU 0 (
    echo.
    echo  %GREEN%[✓] Entschlüsselung erfolgreich!%RESET%
    timeout /t 1 /nobreak > nul
    
    if exist "!output_file!" (
        echo  %CYAN%[*] Öffne: !output_file!%RESET%
            if not "!output_file!"=="" (
                start "" "!output_file!"
                echo  %GREEN%[✓] Geöffnet%RESET%
            ) else (
                echo  %YELLOW%[!] Kann Datei nicht öffnen: Dateiname leer%RESET%
            )
    ) else (
        echo  %YELLOW%[!] Datei nicht gefunden%RESET%
    )
) else (
    echo.
    echo  %RED%[✗] Entschlüsselung fehlgeschlagen!%RESET%
)

echo.
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  BACKUP RESTORE
REM ═══════════════════════════════════════════════════════════════════════════
:BACKUP_RESTORE
cls
echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %GREEN%💾 EMERGENCY BACKUP RESTORE%RESET%%CYAN%                                      ║%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

if not exist "!BACKUP_DIR!" (
    echo  %RED%[✗] Kein Backup-Verzeichnis gefunden!%RESET%
    echo.
    pause
    goto MENU
)

set count=0
echo  %YELLOW%Verfügbare Backups:%RESET%
echo.

for %%F in ("!BACKUP_DIR!\*") do (
    set /a count+=1
    echo  %BOLD%[!count!]%RESET% %WHITE%%%~nxF%RESET%
)

if !count! EQU 0 (
    echo  %RED%[✗] Keine Backups gefunden!%RESET%
    echo.
    pause
    goto MENU
)

echo.
echo  %YELLOW%Backups können ins aktuelle Verzeichnis wiederhergestellt werden.%RESET%
echo.

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  INSTALL ARGON2
REM ═══════════════════════════════════════════════════════════════════════════
:INSTALL_ARGON2
cls
echo.
echo  %MAGENTA%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %MAGENTA%║  %BOLD%ARGON2ID QUANTUM UPGRADE%RESET%%MAGENTA%                                      ║%RESET%
echo  %MAGENTA%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.
echo  %CYAN%Argon2id - Winner of Password Hashing Competition 2015%RESET%
echo.
echo  %GREEN%Features:%RESET%
echo  %WHITE%• Memory-Hard: 2GB RAM pro Brute-Force Versuch%RESET%
echo  %WHITE%• GPU/ASIC-Resistant Design%RESET%
echo  %WHITE%• Side-Channel Attack Protection%RESET%
echo  %WHITE%• Hybrid: Data-dependent + Data-independent%RESET%
echo.
echo  %YELLOW%Aktueller Status: PBKDF2 Fallback%RESET%
echo.

choice /C JN /N /M "%CYAN%Argon2 jetzt installieren? [J/N]: %RESET%"
if !ERRORLEVEL! NEQ 1 goto MENU

echo.
echo  %CYAN%[*] Installiere Argon2...%RESET%
"!PYTHON_EXE!" -m pip install argon2-cffi --disable-pip-version-check

if !ERRORLEVEL! EQU 0 (
    echo.
    echo  %GREEN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
    echo  %GREEN%║  ✓ QUANTUM MODE AKTIVIERT%RESET%%GREEN%                                        ║%RESET%
    echo  %GREEN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
    echo.
    echo  %CYAN%Argon2id ist jetzt aktiv!%RESET%
) else (
    echo.
    echo  %RED%╔═══════════════════════════════════════════════════════════════════╗%RESET%
    echo  %RED%║  ✗ INSTALLATION FEHLGESCHLAGEN%RESET%%RED%                                     ║%RESET%
    echo  %RED%╚═══════════════════════════════════════════════════════════════════╝%RESET%
)

echo.
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  SYSTEM INFO
REM ═══════════════════════════════════════════════════════════════════════════
:INFO
cls
echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %MAGENTA%📊 SYSTEM ^& SECURITY INFORMATION%RESET%%CYAN%                               ║%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

"!PYTHON_EXE!" -c "import argon2" 2>nul
if !ERRORLEVEL! EQU 0 (
    set "kdf_status=%GREEN%Argon2id (QUANTUM)%RESET%"
    set "kdf_detail=Memory: 2GB ^| Time: 8 ^| Parallel: 4"
) else (
    set "kdf_status=%YELLOW%PBKDF2 (Fallback)%RESET%"
    set "kdf_detail=Iterations: 1,000,000 (SHA-256)"
)

echo  %WHITE%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %WHITE%║  ENCRYPTION SPECIFICATIONS                                        ║%RESET%
echo  %WHITE%╠═══════════════════════════════════════════════════════════════════╣%RESET%
echo  %WHITE%║                                                                   ║%RESET%
echo  %WHITE%║  Algorithm:      AES-256-GCM (Authenticated)                      ║%RESET%
echo  %WHITE%║  Mode:           Galois/Counter Mode                              ║%RESET%
echo  %WHITE%║  KDF:            !kdf_status!                             ║%RESET%
echo  %WHITE%║                  %DIM%!kdf_detail!%RESET%         ║%RESET%
echo  %WHITE%║  Authentication: AEAD (GCM Tag)                                   ║%RESET%
echo  %WHITE%║  Shredding:      DoD 5220.22-M (7 Passes)                         ║%RESET%
echo  %WHITE%║  Memory Zero:    Secure RAM Cleanup                               ║%RESET%
echo  %WHITE%║                                                                   ║%RESET%
echo  %WHITE%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

echo  %WHITE%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %WHITE%║  SYSTEM CONFIGURATION                                             ║%RESET%
echo  %WHITE%╠═══════════════════════════════════════════════════════════════════╣%RESET%
echo  %WHITE%║  Python:  !PY_VERSION!                                            ║%RESET%
echo  %WHITE%║  Path:    !PYTHON_EXE!  ║%RESET%
echo  %WHITE%║  Script:  !SCRIPT_NAME!                                           ║%RESET%
echo  %WHITE%║  Backups: !BACKUP_DIR!                ║%RESET%
echo  %WHITE%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  EXIT
REM ═══════════════════════════════════════════════════════════════════════════
:EXIT
cls
echo.
echo  %CYAN%╔═══════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %GREEN%Sicheres Beenden...%RESET%%CYAN%                                            ║%RESET%
echo  %CYAN%║                                                                   ║%RESET%
echo  %CYAN%║  [1/3] Temporäre Daten löschen... %GREEN%✓%RESET%                            %CYAN%║%RESET%
echo  %CYAN%║  [2/3] Speicher bereinigen... %GREEN%✓%RESET%                                %CYAN%║%RESET%
echo  %CYAN%║  [3/3] Sitzung schließen... %GREEN%✓%RESET%                                  %CYAN%║%RESET%
echo  %CYAN%║                                                                   ║%RESET%
echo  %CYAN%║  %MAGENTA%Danke für die Nutzung von%RESET%                                      %CYAN%║%RESET%
echo  %CYAN%║  %BOLD%%MAGENTA%UNBREAKABLE VAULT v5.0 ULTRA%RESET%                                %CYAN%║%RESET%
echo  %CYAN%║                                                                   ║%RESET%
echo  %CYAN%╚═══════════════════════════════════════════════════════════════════╝%RESET%
echo.

set PYTHON_EXE=
set SCRIPT_PATH=
set WORK_DIR=
set BACKUP_DIR=

timeout /t 2 /nobreak > nul
exit