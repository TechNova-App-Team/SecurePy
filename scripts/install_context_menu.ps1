# ═══════════════════════════════════════════════════════════════════════════
# VAULT - Windows Context Menu Integration
# Installiert Rechtsklick-Menü für Verschlüsseln/Entschlüsseln
# ═══════════════════════════════════════════════════════════════════════════

# Admin-Check
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "❌ Fehler: Bitte mit Administrator-Rechten ausführen!" -ForegroundColor Red
    Write-Host "   Rechtsklick auf diese Datei → 'Mit PowerShell als Administrator ausführen'" -ForegroundColor Yellow
    pause
    exit
}

# Pfade
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$rootPath = Split-Path -Parent $scriptPath
$pythonScript = Join-Path $rootPath "src\vault.py"
$batchScript = Join-Path $scriptPath "vault.bat"

Write-Host "╔══════════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  VAULT Context Menu Installation                                    ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Prüfe ob vault.py existiert
if (-NOT (Test-Path $pythonScript)) {
    Write-Host "❌ Fehler: vault.py nicht gefunden!" -ForegroundColor Red
    Write-Host "   Pfad: $pythonScript" -ForegroundColor Yellow
    pause
    exit
}

Write-Host "✓ vault.py gefunden" -ForegroundColor Green
Write-Host "  Pfad: $pythonScript" -ForegroundColor DIM

# Escaping für Registry
$pythonScriptEscaped = $pythonScript -replace '\\', '\\'
$batchScriptEscaped = $batchScript -replace '\\', '\\'

# ═══════════════════════════════════════════════════════════════════════════
# 1. ENCRYPT: Alle Dateitypen - "Mit Vault verschlüsseln"
# ═══════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "[1/4] Registriere: Alle Dateien → 'Mit Vault verschlüsseln'" -ForegroundColor Cyan

$regPathEncrypt = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
$regPath = "HKCU:\Software\Classes\*\shell\EncryptWithVault"
$regPathCmd = "HKCU:\Software\Classes\*\shell\EncryptWithVault\command"

try {
    # Shell-Eintrag
    New-Item -Path $regPath -Force | Out-Null
    Set-ItemProperty -Path $regPath -Name "(Default)" -Value "🔐 Mit Vault verschlüsseln" -Force
    Set-ItemProperty -Path $regPath -Name "Icon" -Value "📦" -Force
    
    # Command
    New-Item -Path $regPathCmd -Force | Out-Null
    $cmd = "python `"$pythonScriptEscaped`" v `"%1`""
    Set-ItemProperty -Path $regPathCmd -Name "(Default)" -Value $cmd -Force
    
    Write-Host "  ✓ Registriert für alle Dateitypen" -ForegroundColor Green
} catch {
    Write-Host "  ❌ Fehler: $_" -ForegroundColor Red
}

# ═══════════════════════════════════════════════════════════════════════════
# 2. DECRYPT: .vault Dateien - "Mit Vault entschlüsseln"
# ═══════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "[2/4] Registriere: .vault Dateien → 'Mit Vault entschlüsseln'" -ForegroundColor Cyan

$regPathVault = "HKCU:\Software\Classes\.vault"
$regPathVaultShell = "HKCU:\Software\Classes\.vault\shell\DecryptWithVault"
$regPathVaultCmd = "HKCU:\Software\Classes\.vault\shell\DecryptWithVault\command"

try {
    # .vault Extension registrieren
    New-Item -Path $regPathVault -Force | Out-Null
    Set-ItemProperty -Path $regPathVault -Name "(Default)" -Value "Vault Encrypted File" -Force
    
    # Shell-Eintrag
    New-Item -Path $regPathVaultShell -Force | Out-Null
    Set-ItemProperty -Path $regPathVaultShell -Name "(Default)" -Value "🔓 Mit Vault entschlüsseln" -Force
    Set-ItemProperty -Path $regPathVaultShell -Name "Icon" -Value "🔑" -Force
    
    # Command
    New-Item -Path $regPathVaultCmd -Force | Out-Null
    $cmdDecrypt = "python `"$pythonScriptEscaped`" e `"%1`""
    Set-ItemProperty -Path $regPathVaultCmd -Name "(Default)" -Value $cmdDecrypt -Force
    
    Write-Host "  ✓ Registriert für .vault Dateien" -ForegroundColor Green
} catch {
    Write-Host "  ❌ Fehler: $_" -ForegroundColor Red
}

# ═══════════════════════════════════════════════════════════════════════════
# 3. Explorer aktualisieren
# ═══════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "[3/4] Aktualisiere Windows Explorer..." -ForegroundColor Cyan

try {
    # Registry-Cache leeren
    cmd /c "reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /f" 2>$null
    
    # Explorer neu starten
    Stop-Process -Name explorer -Force -ErrorAction SilentlyContinue
    Start-Sleep -Milliseconds 500
    Start-Process explorer.exe
    
    Write-Host "  ✓ Explorer aktualisiert" -ForegroundColor Green
} catch {
    Write-Host "  ⚠ Explorer-Update fehlgeschlagen (nicht kritisch)" -ForegroundColor Yellow
}

# ═══════════════════════════════════════════════════════════════════════════
# 4. Fertig
# ═══════════════════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║  ✓ Installation erfolgreich abgeschlossen!                          ║" -ForegroundColor Green
Write-Host "╚══════════════════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
Write-Host "Verwendung:" -ForegroundColor Cyan
Write-Host "  • Rechtsklick auf eine Datei → 🔐 'Mit Vault verschlüsseln'" -ForegroundColor White
Write-Host "  • Rechtsklick auf .vault Datei → 🔓 'Mit Vault entschlüsseln'" -ForegroundColor White
Write-Host ""
Write-Host "Python wird automatisch von der Kommandozeile aufgerufen." -ForegroundColor DIM
Write-Host ""
pause
