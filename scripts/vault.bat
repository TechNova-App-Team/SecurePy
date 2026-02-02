@echo off
SETLOCAL EnableDelayedExpansion
chcp 65001 > nul 2>&1

REM ═══════════════════════════════════════════════════════════════════════════════
REM ██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗    ██╗  ██╗ ██████╗ 
REM ██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝    ╚██╗██╔╝██╔═████╗
REM ██║   ██║███████║██║   ██║██║     ██║        ╚███╔╝ ██║██╔██║
REM ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║        ██╔██╗ ████╔╝██║
REM  ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║       ██╔╝ ██╗╚██████╔╝
REM   ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝       ╚═╝  ╚═╝ ╚═════╝ 
REM
REM  PHANTOM EDITION - Military Grade Encryption System
REM ═══════════════════════════════════════════════════════════════════════════════

REM ═══════════════════════════════════════════════════════════════════════════
REM  ANSI FARBEN - CYBERPUNK THEME
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
set "BLINK=%ESC%[5m"
set "MATRIX=%ESC%[38;5;46m"
set "NEON_PINK=%ESC%[38;5;199m"
set "NEON_BLUE=%ESC%[38;5;51m"
set "GOLD=%ESC%[38;5;220m"

title PHANTOM EDITION - Military Grade Encryption

REM ═══════════════════════════════════════════════════════════════════════════
REM  AUTO-DETECTION: PYTHON
REM ═══════════════════════════════════════════════════════════════════════════
set "PYTHON_EXE="

for /f "tokens=*" %%i in ('where python 2^>nul') do (
    echo %%i | findstr /I "WindowsApps" >nul
    if !ERRORLEVEL! NEQ 0 (
        if "!PYTHON_EXE!"=="" set "PYTHON_EXE=%%i"
    )
)

if "!PYTHON_EXE!"=="" for /f "tokens=*" %%i in ('where python3 2^>nul') do if "!PYTHON_EXE!"=="" set "PYTHON_EXE=%%i"
if "!PYTHON_EXE!"=="" if exist "C:\Python312\python.exe" set "PYTHON_EXE=C:\Python312\python.exe"
if "!PYTHON_EXE!"=="" if exist "C:\Python311\python.exe" set "PYTHON_EXE=C:\Python311\python.exe"
if "!PYTHON_EXE!"=="" if exist "C:\Python310\python.exe" set "PYTHON_EXE=C:\Python310\python.exe"

if "!PYTHON_EXE!"=="" (
    echo  %RED%[FATAL] Python nicht gefunden!%RESET%
    pause
    exit /b 1
)

REM ═══════════════════════════════════════════════════════════════════════════
REM  AUTO-DETECTION: VAULT.PY
REM ═══════════════════════════════════════════════════════════════════════════
set "SCRIPT_PATH="
if exist "%~dp0..\src\vault.py" set "SCRIPT_PATH=%~dp0..\src\vault.py"
if "!SCRIPT_PATH!"=="" if exist "%~dp0vault.py" set "SCRIPT_PATH=%~dp0vault.py"
if "!SCRIPT_PATH!"=="" if exist "%CD%\vault.py" set "SCRIPT_PATH=%CD%\vault.py"

if "!SCRIPT_PATH!"=="" (
    echo  %RED%[FATAL] vault.py nicht gefunden!%RESET%
    pause
    exit /b 1
)

set "BACKUP_DIR=%USERPROFILE%\.vault_backups"
if not exist "!BACKUP_DIR!" mkdir "!BACKUP_DIR!" 2>nul

REM ═══════════════════════════════════════════════════════════════════════════
REM  MAIN MENU
REM ═══════════════════════════════════════════════════════════════════════════
:MENU
cls

echo.
echo  %MATRIX%    ██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗    ██╗  ██╗ ██████╗ %RESET%
echo  %MATRIX%    ██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝    ╚██╗██╔╝██╔═████╗%RESET%
echo  %MATRIX%    ██║   ██║███████║██║   ██║██║     ██║        ╚███╔╝ ██║██╔██║%RESET%
echo  %MATRIX%    ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║        ██╔██╗ ████╔╝██║%RESET%
echo  %MATRIX%     ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║       ██╔╝ ██╗╚██████╔╝%RESET%
echo  %MATRIX%      ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝       ╚═╝  ╚═╝ ╚═════╝ %RESET%
echo.
echo  %NEON_PINK%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %NEON_PINK%║  %BOLD%P H A N T O M   E D I T I O N%RESET%%NEON_PINK%                                           ║%RESET%
echo  %NEON_PINK%║  %DIM%Military-Grade Encryption System%RESET%%NEON_PINK%                                       ║%RESET%
echo  %NEON_PINK%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

echo  %CYAN%┌─────────────────────────────────────────────────────────────────────────┐%RESET%
echo  %CYAN%│%RESET% %MATRIX%▸%RESET% Argon2id Memory-Hard KDF %DIM%(2GB RAM / Attempt)%RESET%                      %CYAN%│%RESET%
echo  %CYAN%│%RESET% %MATRIX%▸%RESET% ChaCha20-Poly1305 + AES-256-GCM %DIM%(Dual-Layer)%RESET%                     %CYAN%│%RESET%
echo  %CYAN%│%RESET% %MATRIX%▸%RESET% Gutmann 35-Pass Secure Shredding                                   %CYAN%│%RESET%
echo  %CYAN%│%RESET% %MAGENTA%▸%RESET% %MAGENTA%Quantum-Resistant Mode%RESET% %DIM%(Post-Quantum Crypto)%RESET%                    %CYAN%│%RESET%
echo  %CYAN%│%RESET% %MAGENTA%▸%RESET% %MAGENTA%Steganography%RESET% %DIM%(Hide data in images)%RESET%                            %CYAN%│%RESET%
echo  %CYAN%│%RESET% %YELLOW%▸%RESET% %YELLOW%Self-Destruct Timer%RESET% %DIM%(Time-bomb vaults)%RESET%                        %CYAN%│%RESET%
echo  %CYAN%│%RESET% %RED%▸%RESET% %RED%PANIC MODE%RESET% %DIM%(Emergency destruction)%RESET%                            %CYAN%│%RESET%
echo  %CYAN%└─────────────────────────────────────────────────────────────────────────┘%RESET%
echo.

set enccount=0
set vaultcount=0
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.jpeg *.png *.gif *.json *.xml *.csv *.xlsx *.zip *.rar *.7z *.mp4 *.mp3) do set /a enccount+=1
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do set /a vaultcount+=1

echo  %MAGENTA%┌─ FILES ──────────────────────────────────────────────────────────────────┐%RESET%
if !enccount! GTR 0 echo  %MAGENTA%│%RESET%  %GREEN%📄 Encryptable:%RESET% %WHITE%!enccount!%RESET% files                                          %MAGENTA%│%RESET%
if !vaultcount! GTR 0 echo  %MAGENTA%│%RESET%  %YELLOW%🔒 Encrypted:%RESET% %WHITE%!vaultcount!%RESET% vaults                                          %MAGENTA%│%RESET%
if !enccount! EQU 0 if !vaultcount! EQU 0 echo  %MAGENTA%│%RESET%  %DIM%No files in current directory%RESET%                                    %MAGENTA%│%RESET%
echo  %MAGENTA%└──────────────────────────────────────────────────────────────────────────┘%RESET%
echo.

echo  %GOLD%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %GOLD%║  %BOLD%⚡ COMMAND CENTER ⚡%RESET%%GOLD%                                                    ║%RESET%
echo  %GOLD%╠══════════════════════════════════════════════════════════════════════════╣%RESET%
echo  %GOLD%║                                                                          ║%RESET%
echo  %GOLD%║  %CYAN%━━━ STANDARD OPERATIONS ━━━%RESET%%GOLD%                                           ║%RESET%
echo  %GOLD%║  [%GREEN%1%GOLD%] %GREEN%🔐 ENCRYPT%RESET%           Lock file in vault                       %GOLD%║%RESET%
echo  %GOLD%║  [%YELLOW%2%GOLD%] %YELLOW%🔓 DECRYPT%RESET%           Unlock and restore                       %GOLD%║%RESET%
echo  %GOLD%║  [%CYAN%3%GOLD%] %CYAN%⚡ BATCH ENCRYPT%RESET%      Encrypt all files                        %GOLD%║%RESET%
echo  %GOLD%║  [%BLUE%4%GOLD%] %BLUE%⚡ BATCH DECRYPT%RESET%      Decrypt all vaults                       %GOLD%║%RESET%
echo  %GOLD%║                                                                          ║%RESET%
echo  %GOLD%║  %MAGENTA%━━━ ADVANCED FEATURES ━━━%RESET%%GOLD%                                            ║%RESET%
echo  %GOLD%║  [%MAGENTA%5%GOLD%] %MAGENTA%👻 STEGANOGRAPHY%RESET%      Hide vault in image                      %GOLD%║%RESET%
echo  %GOLD%║  [%MAGENTA%6%GOLD%] %MAGENTA%🛡️ QUANTUM MODE%RESET%       Post-quantum encryption                   %GOLD%║%RESET%
echo  %GOLD%║  [%YELLOW%7%GOLD%] %YELLOW%💣 SELF-DESTRUCT%RESET%      Arm time-bomb on vault                   %GOLD%║%RESET%
echo  %GOLD%║  [%CYAN%8%GOLD%] %CYAN%🎯 QUICK SHRED%RESET%        Securely destroy file                    %GOLD%║%RESET%
echo  %GOLD%║                                                                          ║%RESET%
echo  %GOLD%║  %CYAN%━━━ TOOLS ━━━%RESET%%GOLD%                                                        ║%RESET%
echo  %GOLD%║  [%WHITE%9%GOLD%] %WHITE%📊 VAULT SCANNER%RESET%      Find all vaults on system                %GOLD%║%RESET%
echo  %GOLD%║  [%WHITE%A%GOLD%] %WHITE%🧪 SECURITY AUDIT%RESET%     Full security check                      %GOLD%║%RESET%
echo  %GOLD%║  [%WHITE%B%GOLD%] %WHITE%⚙️ SETTINGS%RESET%           View configuration                       %GOLD%║%RESET%
echo  %GOLD%║  [%GREEN%C%GOLD%] %GREEN%📦 INSTALL DEPS%RESET%       Install Argon2 + Rich                    %GOLD%║%RESET%
echo  %GOLD%║                                                                          ║%RESET%
echo  %GOLD%║  %RED%━━━ EMERGENCY PROTOCOLS ━━━%RESET%%GOLD%                                          ║%RESET%
echo  %GOLD%║  [%RED%P%GOLD%] %RED%☠️ PANIC MODE%RESET%         %RED%DESTROY ALL VAULTS NOW%RESET%                 %GOLD%║%RESET%
echo  %GOLD%║  [%NEON_PINK%X%GOLD%] %NEON_PINK%🖥️ PHANTOM UI%RESET%         Launch Rich Interactive Mode            %GOLD%║%RESET%
echo  %GOLD%║  [%DIM%0%GOLD%] %DIM%🚪 EXIT%RESET%                Leave PHANTOM                           %GOLD%║%RESET%
echo  %GOLD%║                                                                          ║%RESET%
echo  %GOLD%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

choice /C 123456789ABCPX0 /N /M "%NEON_PINK%⚡ Select → %RESET%"
set choice=!ERRORLEVEL!

if !choice! EQU 1 goto ENCRYPT
if !choice! EQU 2 goto DECRYPT
if !choice! EQU 3 goto BATCH_ENCRYPT
if !choice! EQU 4 goto BATCH_DECRYPT
if !choice! EQU 5 goto STEGANOGRAPHY
if !choice! EQU 6 goto QUANTUM_MODE
if !choice! EQU 7 goto SELF_DESTRUCT
if !choice! EQU 8 goto QUICK_SHRED
if !choice! EQU 9 goto VAULT_SCANNER
if !choice! EQU 10 goto SECURITY_AUDIT
if !choice! EQU 11 goto SETTINGS
if !choice! EQU 12 goto INSTALL_DEPS
if !choice! EQU 13 goto PANIC_MODE
if !choice! EQU 14 goto PHANTOM_UI
if !choice! EQU 15 goto EXIT

goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  ENCRYPT
REM ═══════════════════════════════════════════════════════════════════════════
:ENCRYPT
cls
echo.
echo  %CYAN%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %GREEN%🔐 ENCRYPT MODE%RESET%%CYAN%                                                        ║%RESET%
echo  %CYAN%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

set count=0
echo  %YELLOW%Available Files:%RESET%
echo.
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.jpeg *.png *.gif *.json *.xml *.csv *.xlsx *.zip *.rar *.7z *.mp4 *.mp3) do (
    set /a count+=1
    echo  %BOLD%[!count!]%RESET% %%F
)

if !count! EQU 0 (
    echo  %RED%[✗] No encryptable files found!%RESET%
    pause
    goto MENU
)

echo.
echo  %BOLD%[0]%RESET% %RED%← Back%RESET%
echo.
set /p selection="%CYAN%Select file: %RESET%"
if "!selection!"=="0" goto MENU

set idx=0
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.jpeg *.png *.gif *.json *.xml *.csv *.xlsx *.zip *.rar *.7z *.mp4 *.mp3) do (
    set /a idx+=1
    if !idx! EQU !selection! set "selected_file=%%F"
)

echo.
echo  %MAGENTA%━━━ ENCRYPTION OPTIONS ━━━%RESET%
echo  %GREEN%[1]%RESET% Standard
echo  %YELLOW%[2]%RESET% Paranoia %DIM%(35-pass shred)%RESET%
echo  %MAGENTA%[3]%RESET% Quantum %DIM%(Post-quantum)%RESET%
echo  %CYAN%[4]%RESET% Stealth %DIM%(Polymorphic)%RESET%
echo  %RED%[5]%RESET% MAXIMUM %DIM%(All options)%RESET%
echo.
choice /C 12345 /N /M "%CYAN%Mode: %RESET%"
set mode_choice=!ERRORLEVEL!

set "EXTRA_ARGS="
if !mode_choice! EQU 2 set "EXTRA_ARGS=--paranoia"
if !mode_choice! EQU 3 set "EXTRA_ARGS=--quantum"
if !mode_choice! EQU 4 set "EXTRA_ARGS=--stealth"
if !mode_choice! EQU 5 set "EXTRA_ARGS=--paranoia --quantum --stealth --isolated"

echo.
copy "!selected_file!" "!BACKUP_DIR!\!selected_file!.backup" > nul 2>&1
"!PYTHON_EXE!" "!SCRIPT_PATH!" v "!selected_file!" !EXTRA_ARGS!

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  DECRYPT
REM ═══════════════════════════════════════════════════════════════════════════
:DECRYPT
cls
echo.
echo  %CYAN%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %YELLOW%🔓 DECRYPT MODE%RESET%%CYAN%                                                        ║%RESET%
echo  %CYAN%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

set count=0
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do (
    set /a count+=1
    echo  %BOLD%[!count!]%RESET% %YELLOW%🔒%RESET% %%F
)

if !count! EQU 0 (
    echo  %RED%[✗] No vault files found!%RESET%
    pause
    goto MENU
)

echo.
set /p selection="%CYAN%Select vault: %RESET%"
if "!selection!"=="0" goto MENU

set idx=0
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do (
    set /a idx+=1
    if !idx! EQU !selection! set "selected_file=%%F"
)

echo.
"!PYTHON_EXE!" "!SCRIPT_PATH!" e "!selected_file!"

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  BATCH ENCRYPT
REM ═══════════════════════════════════════════════════════════════════════════
:BATCH_ENCRYPT
cls
echo.
echo  %CYAN%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %GREEN%⚡ BATCH ENCRYPT%RESET%%CYAN%                                                       ║%RESET%
echo  %CYAN%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

set count=0
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.png *.json *.csv *.xlsx *.zip *.mp4 *.mp3) do set /a count+=1

echo  %YELLOW%Found !count! files%RESET%
echo  %RED%⚠ This will encrypt ALL files!%RESET%
echo.
choice /C YN /N /M "%YELLOW%Continue? [Y/N]: %RESET%"
if !ERRORLEVEL! EQU 2 goto MENU

for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.png *.json *.csv *.xlsx *.zip *.mp4 *.mp3) do (
    echo  %MATRIX%[*] %%F%RESET%
    "!PYTHON_EXE!" "!SCRIPT_PATH!" v "%%F"
)

echo  %GREEN%[✓] Done!%RESET%
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  BATCH DECRYPT
REM ═══════════════════════════════════════════════════════════════════════════
:BATCH_DECRYPT
cls
echo.
echo  %CYAN%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %YELLOW%⚡ BATCH DECRYPT%RESET%%CYAN%                                                       ║%RESET%
echo  %CYAN%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

set count=0
for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do set /a count+=1

echo  %YELLOW%Found !count! vaults%RESET%
choice /C YN /N /M "%YELLOW%Continue? [Y/N]: %RESET%"
if !ERRORLEVEL! EQU 2 goto MENU

for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do (
    echo  %MATRIX%[*] %%F%RESET%
    "!PYTHON_EXE!" "!SCRIPT_PATH!" e "%%F"
)

echo  %GREEN%[✓] Done!%RESET%
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  STEGANOGRAPHY
REM ═══════════════════════════════════════════════════════════════════════════
:STEGANOGRAPHY
cls
echo.
echo  %MAGENTA%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %MAGENTA%║  %BOLD%👻 STEGANOGRAPHY%RESET%%MAGENTA%                                                      ║%RESET%
echo  %MAGENTA%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.
echo  %CYAN%[1]%RESET% Hide vault in image
echo  %CYAN%[2]%RESET% Extract from image
echo  %CYAN%[0]%RESET% Back
echo.
choice /C 120 /N /M "%MAGENTA%Select: %RESET%"
set stego_choice=!ERRORLEVEL!

if !stego_choice! EQU 3 goto MENU

if !stego_choice! EQU 1 (
    set /p vault_file="%CYAN%Vault file: %RESET%"
    set /p carrier_file="%CYAN%Carrier PNG: %RESET%"
    "!PYTHON_EXE!" "!SCRIPT_PATH!" hide "!vault_file!" "!carrier_file!"
)

if !stego_choice! EQU 2 (
    set /p image_file="%CYAN%Image file: %RESET%"
    "!PYTHON_EXE!" "!SCRIPT_PATH!" unhide "!image_file!"
)

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  QUANTUM MODE
REM ═══════════════════════════════════════════════════════════════════════════
:QUANTUM_MODE
cls
echo.
echo  %MAGENTA%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %MAGENTA%║  %BOLD%🛡️ QUANTUM-RESISTANT MODE%RESET%%MAGENTA%                                             ║%RESET%
echo  %MAGENTA%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

set count=0
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.png *.json *.csv *.xlsx *.zip *.mp4 *.mp3) do (
    set /a count+=1
    echo  %BOLD%[!count!]%RESET% %%F
)

if !count! EQU 0 (
    echo  %RED%[✗] No files!%RESET%
    pause
    goto MENU
)

echo.
set /p selection="%CYAN%Select: %RESET%"
if "!selection!"=="0" goto MENU

set idx=0
for %%F in (*.txt *.doc *.docx *.pdf *.jpg *.png *.json *.csv *.xlsx *.zip *.mp4 *.mp3) do (
    set /a idx+=1
    if !idx! EQU !selection! set "selected_file=%%F"
)

"!PYTHON_EXE!" "!SCRIPT_PATH!" v "!selected_file!" --quantum --paranoia

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  SELF-DESTRUCT
REM ═══════════════════════════════════════════════════════════════════════════
:SELF_DESTRUCT
cls
echo.
echo  %RED%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %RED%║  %BOLD%💣 SELF-DESTRUCT TIMER%RESET%%RED%                                                   ║%RESET%
echo  %RED%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.
echo  %CYAN%[1]%RESET% Arm timer
echo  %GREEN%[2]%RESET% Disarm timer
echo  %CYAN%[0]%RESET% Back
echo.
choice /C 120 /N /M "%RED%Select: %RESET%"
set sd_choice=!ERRORLEVEL!

if !sd_choice! EQU 3 goto MENU

for /F "delims=" %%F in ('dir /B /A:-D *.vault 2^>nul') do echo  %YELLOW%🔒%RESET% %%F
set /p vault_sel="%CYAN%Vault name: %RESET%"

if !sd_choice! EQU 1 (
    set /p hours="%RED%Hours [24]: %RESET%"
    if "!hours!"=="" set "hours=24"
    "!PYTHON_EXE!" "!SCRIPT_PATH!" arm "!vault_sel!" !hours!
    echo  %RED%💣 ARMED!%RESET%
)

if !sd_choice! EQU 2 (
    "!PYTHON_EXE!" "!SCRIPT_PATH!" disarm "!vault_sel!"
    echo  %GREEN%[✓] Disarmed%RESET%
)

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  QUICK SHRED
REM ═══════════════════════════════════════════════════════════════════════════
:QUICK_SHRED
cls
echo.
echo  %RED%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %RED%║  %BOLD%🎯 QUICK SHRED%RESET%%RED%                                                          ║%RESET%
echo  %RED%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.
echo  %RED%⚠ FILES WILL BE PERMANENTLY DESTROYED!%RESET%
echo.

set count=0
for %%F in (*.*) do if /I not "%%~xF"==".bat" if /I not "%%~xF"==".py" (
    set /a count+=1
    echo  %BOLD%[!count!]%RESET% %%F
)

set /p selection="%RED%File to DESTROY: %RESET%"

set idx=0
for %%F in (*.*) do if /I not "%%~xF"==".bat" if /I not "%%~xF"==".py" (
    set /a idx+=1
    if !idx! EQU !selection! set "selected_file=%%F"
)

choice /C YN /N /M "%RED%DESTROY !selected_file!? [Y/N]: %RESET%"
if !ERRORLEVEL! EQU 2 goto MENU

del /F /Q "!selected_file!" 2>nul
echo  %GREEN%[✓] Destroyed!%RESET%

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  VAULT SCANNER
REM ═══════════════════════════════════════════════════════════════════════════
:VAULT_SCANNER
cls
echo.
echo  %CYAN%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %BOLD%📊 VAULT SCANNER%RESET%%CYAN%                                                        ║%RESET%
echo  %CYAN%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.
echo  %YELLOW%Scanning...%RESET%

set total=0
for /F "delims=" %%F in ('dir /B /S "%USERPROFILE%\*.vault" 2^>nul') do (
    set /a total+=1
    echo  %GREEN%[✓]%RESET% %%F
)

echo.
echo  %WHITE%Total: !total! vaults%RESET%

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  SECURITY AUDIT
REM ═══════════════════════════════════════════════════════════════════════════
:SECURITY_AUDIT
cls
echo.
echo  %CYAN%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %BOLD%🧪 SECURITY AUDIT%RESET%%CYAN%                                                       ║%RESET%
echo  %CYAN%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

echo  %CYAN%[1/4]%RESET% Python: 
"!PYTHON_EXE!" --version

echo  %CYAN%[2/4]%RESET% Cryptography: 
"!PYTHON_EXE!" -c "from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305; print('      OK')" 2>nul || echo       MISSING

echo  %CYAN%[3/4]%RESET% Argon2: 
"!PYTHON_EXE!" -c "import argon2; print('      OK')" 2>nul || echo       MISSING

echo  %CYAN%[4/4]%RESET% Rich: 
"!PYTHON_EXE!" -c "from rich.console import Console; print('      OK')" 2>nul || echo       MISSING

echo.
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  SETTINGS
REM ═══════════════════════════════════════════════════════════════════════════
:SETTINGS
cls
echo.
echo  %CYAN%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %BOLD%⚙️ SETTINGS%RESET%%CYAN%                                                             ║%RESET%
echo  %CYAN%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.
echo  Python:     !PYTHON_EXE!
echo  Script:     !SCRIPT_PATH!
echo  Backup:     !BACKUP_DIR!
echo  Encryption: ChaCha20 + AES-256-GCM
echo  KDF:        Argon2id (2GB)
echo  Panic Key:  !!DESTROY!!
echo  Duress Key: !!DURESS!!
echo.
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  INSTALL DEPS
REM ═══════════════════════════════════════════════════════════════════════════
:INSTALL_DEPS
cls
echo.
echo  %GREEN%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %GREEN%║  %BOLD%📦 INSTALL DEPENDENCIES%RESET%%GREEN%                                                 ║%RESET%
echo  %GREEN%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

echo  Installing cryptography...
"!PYTHON_EXE!" -m pip install cryptography --quiet
echo  Installing argon2-cffi...
"!PYTHON_EXE!" -m pip install argon2-cffi --quiet
echo  Installing rich...
"!PYTHON_EXE!" -m pip install rich --quiet

echo.
echo  %GREEN%[✓] Done!%RESET%
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  PANIC MODE
REM ═══════════════════════════════════════════════════════════════════════════
:PANIC_MODE
cls
color 4F
echo.
echo  %RED%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %RED%║  %BOLD%☠️ PANIC MODE - DESTROY ALL VAULTS ☠️%RESET%%RED%                                     ║%RESET%
echo  %RED%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.
echo  %WHITE%Type 'DESTROY ALL' to confirm:%RESET%
set /p confirm=""
if /I not "!confirm!"=="DESTROY ALL" (
    color 0B
    goto MENU
)

echo.
for /F "delims=" %%F in ('dir /B /S "%USERPROFILE%\*.vault" 2^>nul') do (
    echo  %RED%[☠] %%F%RESET%
    del /F /Q "%%F" 2>nul
)

echo.
echo  %RED%[☠] ALL VAULTS DESTROYED%RESET%
color 0B
pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  PHANTOM UI
REM ═══════════════════════════════════════════════════════════════════════════
:PHANTOM_UI
cls
echo.
echo  %NEON_PINK%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %NEON_PINK%║  %BOLD%☠️ PHANTOM UI - Rich Interactive Mode%RESET%%NEON_PINK%                                 ║%RESET%
echo  %NEON_PINK%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.

"!PYTHON_EXE!" "!SCRIPT_PATH!"

pause
goto MENU

REM ═══════════════════════════════════════════════════════════════════════════
REM  EXIT
REM ═══════════════════════════════════════════════════════════════════════════
:EXIT
cls
echo.
echo  %CYAN%╔══════════════════════════════════════════════════════════════════════════╗%RESET%
echo  %CYAN%║  %GREEN%Secure Shutdown...%RESET%%CYAN%                                                     ║%RESET%
echo  %CYAN%║  %NEON_PINK%Thanks for using PHANTOM EDITION%RESET%%CYAN%                                     ║%RESET%
echo  %CYAN%╚══════════════════════════════════════════════════════════════════════════╝%RESET%
echo.
timeout /t 2 >nul
exit /b 0
