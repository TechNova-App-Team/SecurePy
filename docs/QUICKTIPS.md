# Quick Tips & Tricks

## Common Workflows

### 1. Encrypt Sensitive File and Delete Original

```batch
# From vault directory
python src\vault.py v "C:\my_document.pdf"

# If encryption successful, delete original
del "C:\my_document.pdf"
```

### 2. Batch Encrypt All Documents in Folder

```batch
cd "C:\Documents"
for %%F in (*.doc *.docx *.pdf *.txt) do (
    echo Encrypting %%F...
    python "C:\vault\src\vault.py" v "%%F"
)
```

### 3. Backup and Encrypt

```batch
# Create backup
copy "C:\Database\data.db" "D:\Backup\data_2024-01.db"

# Encrypt backup
python "C:\vault\src\vault.py" v "D:\Backup\data_2024-01.db"
```

### 4. Decrypt Temporarily, Then Re-encrypt

```batch
# Decrypt to temp location
python "C:\vault\src\vault.py" e "important.vault"

# Work with important.* (original file)

# Re-encrypt
python "C:\vault\src\vault.py" v "important.*"

# Delete unencrypted version
del "important.*"
```

---

## Best Practices

### 1. Password Management
- ✅ Store passwords in KeePass, 1Password, or Bitwarden
- ✅ Use strong passwords (16+ characters)
- ✅ Include uppercase, lowercase, numbers, symbols
- ❌ Don't store passwords in plain text files
- ❌ Don't use simple passwords like "password123"

### 2. File Organization
```
D:\Secure\
├── Documents/
│   ├── contract.docx.vault
│   └── invoice.pdf.vault
├── Photos/
│   ├── family.zip.vault
│   └── backup.tar.vault
└── Backups/
    ├── database_2024-01.db.vault
    └── files_2024-01.vault
```

### 3. Before Encryption
- [ ] Verify file is complete and intact
- [ ] Check you have the correct password written down
- [ ] Ensure backup exists elsewhere
- [ ] Test encryption on small file first

### 4. After Encryption
- [ ] Verify .vault file exists and has reasonable size
- [ ] Test decrypt with correct password
- [ ] Only then delete original file
- [ ] Store backup in separate location

---

## Windows Explorer Context Menu

### Quick Access

Right-click any file:
- **🔐 Mit Vault verschlüsseln** = Encrypt this file

Right-click .vault file:
- **🔓 Mit Vault entschlüsseln** = Decrypt this file

### Keyboard Shortcut
After installation, in Explorer:
1. Select file
2. Press `Shift+F10` to open context menu
3. Navigate to Vault option
4. Press `E` for encrypt or `D` for decrypt

---

## Performance Tips

### Faster Encryption
- Use SSD instead of HDD
- Close other applications
- Don't use while system is busy
- Larger files take longer but are more efficient per MB

### System Requirements
- **Minimum**: Dual-core CPU, 4GB RAM
- **Recommended**: Quad-core CPU, 8GB RAM
- **Optimal**: 6+ cores, 16GB RAM, NVMe SSD

### Benchmark Times
```
File Size   Time        Throughput
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
100 MB      10-15 sec   ~7-10 MB/s
500 MB      45-60 sec   ~8-10 MB/s
1 GB        90-120 sec  ~8-10 MB/s
5 GB        7-10 min    ~8-10 MB/s
```

---

## Disaster Recovery

### "I Forgot My Password"
❌ **Unfortunately, there is no recovery.**
- Passwords cannot be reset
- No backdoor exists
- File is permanently inaccessible

**Prevention:**
- Store password in password manager
- Keep encrypted password file elsewhere
- Use consistent passwords you can remember

### "File Got Corrupted"
1. Don't try to edit the .vault file
2. Don't overwrite with new data
3. Restore from backup (if available)
4. Contact backup administrator

### "Lost the .vault File"
- Restore from system backup
- Check Recycle Bin
- Use file recovery tool (if recent)
- Restore from external backup

---

## Advanced Usage

### Encrypting Large Archives

For very large files, compress first:

```batch
# Create compressed archive
7z a -t7z -m0=lzma2 -mx=9 data_2024.7z D:\Documents\

# Encrypt the archive
python src\vault.py v data_2024.7z

# Delete uncompressed version
rmdir /s /q D:\Documents\
```

### Cloud Storage Encryption

Before uploading to cloud:

```batch
# Encrypt all files
for %%F in (*.*) do python src\vault.py v "%%F"

# Upload .vault files to cloud
# Original files deleted
```

### Database Backups

```batch
# Backup database
mysqldump -u user -p database > backup.sql

# Encrypt backup
python src\vault.py v backup.sql

# Upload to cloud
```

---

## Integration Examples

### Scheduled Daily Backup

**File: backup_and_encrypt.bat**
```batch
@echo off
setlocal

set VAULT_DIR=C:\vault
set BACKUP_DIR=E:\Backups
set BACKUP_DATE=%date:~-4%-%date:~-10,2%-%date:~-7,2%
set PASSWORD=backup_password_here

cd /d %BACKUP_DIR%

REM Create backup
backup_software.exe /output="backup_%BACKUP_DATE%.bak"

REM Encrypt backup
python "%VAULT_DIR%\src\vault.py" v "backup_%BACKUP_DATE%.bak"

REM Delete unencrypted version
del "backup_%BACKUP_DATE%.bak"

REM Optional: Upload to cloud
REM rclone copy . remote:backups/
```

**Windows Task Scheduler:**
- Create basic task
- Trigger: Daily at 2:00 AM
- Action: Run backup_and_encrypt.bat

---

## Verification Checklist

### After Installing
- [ ] Python works (`python --version`)
- [ ] Packages installed (`pip list | findstr cryptography`)
- [ ] vault.py accessible (`python src\vault.py --help`)
- [ ] Context menu shows (right-click file)

### After Encrypting
- [ ] .vault file created
- [ ] File size reasonable (original + 100 bytes)
- [ ] Original file still exists (if not deleted)
- [ ] Can successfully decrypt

### Before Deleting Original
- [ ] Decrypt test successful
- [ ] File integrity verified
- [ ] Backup exists elsewhere
- [ ] Password written down safely

---

**Last Updated**: January 2026  
**Version**: 5.0
