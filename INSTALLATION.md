# Installation Guide - UNBREAKABLE VAULT

## Windows Setup

### Step 1: Install Python

1. Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. **Important**: Check "Add Python to PATH" during installation
3. Verify installation:
   ```cmd
   python --version
   ```

### Step 2: Install Required Packages

```cmd
pip install cryptography argon2-cffi
```

### Step 3: Verify Installation

```cmd
cd path\to\vault
python src\vault.py --help
```

---

## Windows Explorer Context Menu Integration

### Enable Context Menu (Recommended)

1. **Open PowerShell as Administrator**
   - Right-click PowerShell → "Run as Administrator"

2. **Run the installation script:**
   ```powershell
   cd path\to\vault
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\scripts\install_context_menu.ps1
   ```

3. **Verify** - Right-click any file, you should see:
   - 🔐 "Mit Vault verschlüsseln" (encrypt)
   - For .vault files: 🔓 "Mit Vault entschlüsseln" (decrypt)

### Disable Context Menu

```cmd
cmd /c ".\scripts\uninstall_context_menu.bat"
```

---

## Troubleshooting

### Python Not Found

**Problem:** "Python nicht gefunden!" error

**Solution:**
1. Reinstall Python and ensure "Add to PATH" is checked
2. Restart Command Prompt/PowerShell after installation
3. Verify with: `where python`

### Module Not Found (cryptography/argon2)

**Problem:** "No module named 'cryptography'"

**Solution:**
```cmd
pip install --upgrade pip
pip install cryptography argon2-cffi
```

### PowerShell Execution Policy Error

**Problem:** "cannot be loaded because running scripts is disabled"

**Solution:**
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\scripts\install_context_menu.ps1
```

### Context Menu Not Appearing

**Solution:**
1. Restart Windows Explorer: Press `Ctrl+Shift+Esc`, kill `explorer.exe`, restart it
2. Clear registry cache:
   ```cmd
   reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /f
   ```
3. Re-run installation script

---

## Project Structure

```
argon/
├── src/                           # Core application
│   ├── vault.py                  # Main engine
│   └── find.py                   # Python finder
├── scripts/                       # Windows tools
│   ├── vault.bat                 # CLI wrapper
│   ├── install_context_menu.ps1  # Setup
│   ├── uninstall_context_menu.bat
│   ├── install_context_clean.bat
│   └── wrappers/                 # Context menu executors
│       ├── vault_encrypt_wrapper.bat
│       └── vault_decrypt_wrapper.bat
└── docs/                          # Documentation
    ├── README.md
    └── INSTALLATION.md            # This file
```

---

## File Locations

The tool searches for `vault.py` in this order:

1. `scripts\..\src\vault.py` (Primary - new structure)
2. `scripts\vault.py` (Legacy fallback)
3. Current working directory
4. System PATH

---

## Security Checklist

- [ ] Python installed with PATH configured
- [ ] Cryptography packages installed
- [ ] Context menu integration successful
- [ ] Test encryption on a test file
- [ ] Verify encrypted file can be decrypted
- [ ] Password saved in secure password manager
- [ ] Original file deleted after successful backup

---

## Advanced Configuration

### Custom Python Interpreter

Edit `scripts\vault.bat` and set:
```batch
set "PYTHON_EXE=C:\path\to\python.exe"
```

### Custom Vault.py Location

Edit `scripts\install_context_menu.ps1` and modify:
```powershell
$pythonScript = "C:\path\to\vault.py"
```

---

## Updating

1. Backup your encrypted files
2. Replace `src\vault.py` with new version
3. Re-run `install_context_menu.ps1` if structure changed

---

## Uninstall

```cmd
# Remove context menu
.\scripts\uninstall_context_menu.bat

# Delete project directory
rmdir /s /q "path\to\vault"
```

---

**Date:** January 2026  
**Version:** 5.0
