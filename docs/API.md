# API Reference - UNBREAKABLE VAULT

## Python Module: vault.py

### Quick Reference

```python
from vault import VaultManager

vault = VaultManager()
vault.encrypt("sensitive.txt", "my_secure_password")
vault.decrypt("sensitive.vault", "my_secure_password")
```

---

## Command Line Interface

### Syntax
```
python src/vault.py [COMMAND] [FILE] [OPTIONS]
```

### Commands

#### Encrypt
```
python src/vault.py v "file.txt"
python src/vault.py encrypt "file.txt"
```
- Prompts for password
- Creates `file.txt.vault`
- Original file remains unchanged

#### Decrypt
```
python src/vault.py e "file.vault"
python src/vault.py decrypt "file.vault"
```
- Prompts for password
- Recovers original file
- .vault file remains unchanged

#### Help
```
python src/vault.py --help
python src/vault.py -h
```

### Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --version` | Show version |
| `--test` | Run self-tests |
| `--verify FILE` | Verify encrypted file integrity |

---

## Security Parameters

### Argon2id Configuration
- **Memory**: 2 GB per operation
- **Iterations**: 8 (high-cost)
- **Parallelism**: 4 threads
- **Hash Type**: Argon2id (hybrid mode)
- **Salt Size**: 32 bytes (256 bits)

### AES-256-GCM Configuration
- **Key Size**: 256 bits (32 bytes)
- **IV Size**: 96 bits (12 bytes)
- **Tag Size**: 128 bits (16 bytes)
- **Mode**: GCM (Galois/Counter Mode)

### Key Derivation
```
SALT (32 bytes) → Argon2id → KEY (32 bytes) + HMAC_KEY (16 bytes)
```

---

## File Format

### Encrypted File Structure
```
[HEADER: 16 bytes "VAULT_V5_ULTRA"]
[SALT: 32 bytes]
[IV: 12 bytes]
[TAG: 16 bytes]
[CIPHERTEXT: variable length]
```

**Total Overhead**: ~76 bytes per file

### File Size Impact
```
Original: 1 MB
Encrypted: 1 MB + 76 bytes
```

---

## Error Codes

| Code | Meaning | Solution |
|------|---------|----------|
| 0 | Success | N/A |
| 1 | Python not found | Install Python |
| 2 | Module not found | `pip install cryptography argon2-cffi` |
| 3 | File not found | Check file path |
| 4 | Invalid password | Try again with correct password |
| 5 | Corrupted file | File may be damaged |
| 6 | Permission denied | Check file permissions |
| 7 | Insufficient space | Free up disk space |

---

## Performance

### Encryption Speed
- Small files (<10MB): ~1-2 seconds
- Medium files (10-100MB): ~5-20 seconds
- Large files (>100MB): ~30-60 seconds

*Depends on hardware and Argon2id memory allocation*

### Memory Usage
- Peak RAM: ~2.5 GB during key derivation
- After completion: ~50-100 MB for file buffering

---

## Batch Mode Examples

### Encrypt Multiple Files

```batch
@echo off
setlocal enabledelayedexpansion

set PYTHON=python
set VAULT=src\vault.py
set PASSWORD=my_secure_password

for %%F in (*.txt *.pdf *.doc) do (
    echo Encrypting: %%F
    echo !PASSWORD! | !PYTHON! !VAULT! v "%%F"
)
```

### Decrypt All .vault Files

```batch
@echo off
setlocal enabledelayedexpansion

set PYTHON=python
set VAULT=src\vault.py
set PASSWORD=my_secure_password

for %%F in (*.vault) do (
    echo Decrypting: %%F
    echo !PASSWORD! | !PYTHON! !VAULT! e "%%F"
)
```

### Scheduled Backup Encryption

```batch
REM Script: encrypt_backup.bat
REM Run via Windows Task Scheduler

set BACKUP_DIR=D:\Backups
set PYTHON=python
set VAULT=%~dp0src\vault.py
set PASSWORD=backups_2024

cd /d %BACKUP_DIR%

for %%F in (*.bak *.zip) do (
    echo Securing backup: %%F
    echo %PASSWORD% | %PYTHON% %VAULT% v "%%F"
    if !ERRORLEVEL! EQU 0 (
        del "%%F"
        echo Backup encrypted and original deleted: %%F
    )
)
```

---

## Integration with Other Tools

### PowerShell Integration

```powershell
$vault = "python C:\vault\src\vault.py"
$file = "C:\sensitive_data.txt"
$password = "SecurePass123!"

# Encrypt
$password | & $vault v $file

# Decrypt
$password | & $vault e "$file.vault"
```

### Python Integration

```python
import subprocess
import sys

def encrypt_file(filepath, password):
    cmd = [sys.executable, "src/vault.py", "v", filepath]
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        text=True
    )
    process.communicate(input=password)
    return process.returncode == 0

def decrypt_file(filepath, password):
    cmd = [sys.executable, "src/vault.py", "e", filepath]
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        text=True
    )
    process.communicate(input=password)
    return process.returncode == 0
```

---

## Troubleshooting

### "Wrong Password" Error
- Ensure CAPS LOCK is off
- Password is case-sensitive
- Check for leading/trailing spaces

### "Corrupted File" Error
- File may have been partially overwritten
- Restore from backup
- Try with different password (may fail but won't corrupt further)

### Performance Issues
- Close other applications
- Check available RAM (need ~2.5 GB free)
- Large files on slow storage (use SSD if possible)

---

**Version**: 5.0 ULTRA  
**Last Updated**: January 2026
