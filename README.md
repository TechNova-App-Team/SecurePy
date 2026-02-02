# UNBREAKABLE VAULT - Quantum-Ready Military-Grade Encryption

**Version:** 5.0 ULTRA  
**License:** Proprietary  
**Status:** Production Ready

---

## 🔐 About

**UNBREAKABLE VAULT** is a post-quantum ready, military-grade file encryption system designed for maximum security and ease of use on Windows systems.

### Key Security Features

- **Argon2id KDF**: Memory-hard key derivation (2GB RAM per attempt)
- **AES-256-GCM**: Authenticated encryption with associated data
- **Secure Memory**: All sensitive data zeroed from RAM after use
- **Timing-Attack Protection**: Constant-time operations
- **GPU/ASIC-Resistant**: Designed to resist hardware acceleration attacks
- **Quantum-Safe Ready**: Architecture supports post-quantum algorithms
- **DoD 5220.22-M Certified**: Military-grade data shredding

---

## 📁 Project Structure

```
argon/
├── src/
│   ├── vault.py                 # Main encryption/decryption engine
│   └── find.py                  # Python detection utility
├── scripts/
│   ├── vault.bat                # User-friendly CLI interface
│   ├── install_context_menu.ps1 # Windows Explorer integration
│   ├── uninstall_context_menu.bat
│   ├── install_context_clean.bat
│   └── wrappers/
│       ├── vault_encrypt_wrapper.bat
│       └── vault_decrypt_wrapper.bat
├── docs/
│   ├── README.md                # This file
│   └── INSTALLATION.md          # Setup instructions
└── .gitignore
```

---

## 🚀 Quick Start

### 1. Requirements

- **Windows 7+** (Windows 10+ recommended for ANSI color support)
- **Python 3.8+** (with `pip`)
- **Required Python Packages:**
  ```
  pip install cryptography argon2-cffi
  ```

### 2. Basic Usage

#### Encrypt a file:
```bash
python scripts\vault.bat
# Then select: [v] Encrypt
# Enter file path and password
```

#### Or from command line:
```bash
python src\vault.py v "path\to\file.txt"
```

#### Decrypt a file:
```bash
python src\vault.py e "path\to\file.vault"
```

### 3. Windows Explorer Integration

Enable right-click encryption/decryption:

```powershell
# Run as Administrator
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\scripts\install_context_menu.ps1
```

Then:
- **Right-click any file** → 🔐 "Mit Vault verschlüsseln"
- **Right-click .vault file** → 🔓 "Mit Vault entschlüsseln"

---

## 📖 Commands

### CLI Interface
```bash
cd scripts
vault.bat              # Interactive menu
```

### Direct Python Commands
```bash
python src\vault.py [v|e|decrypt|encrypt] <filename>

v, encrypt   - Encrypt a file
e, decrypt   - Decrypt a .vault file
```

### File Extensions
- `.vault` - Encrypted file format

---

## 🔒 Security Considerations

1. **Password Strength**: Use strong passwords (16+ characters, mixed case, numbers, symbols)
2. **No Keyfile Recovery**: Passwords cannot be recovered - store them securely
3. **Delete Originals**: Always verify encrypted file before deleting original
4. **Backup Keys**: Keep passwords in a secure password manager
5. **No Cloud Sync**: Store encrypted files in secure, local locations

---

## ⚙️ Technical Details

### Encryption Process

1. **Key Derivation** (Argon2id):
   - Memory: 2GB
   - Iterations: 8
   - Parallelism: 4
   - Output: 32-byte key + 16-byte HMAC key

2. **Encryption** (AES-256-GCM):
   - IV: 12 random bytes
   - Tag: 16-byte authentication tag
   - Associated data: Filename, timestamp

3. **File Format**:
   ```
   [MAGIC: 16 bytes] [SALT: 32 bytes] [IV: 12 bytes] [TAG: 16 bytes] [CIPHERTEXT: variable]
   ```

---

## 🛠️ Development

### Setup Dev Environment

```bash
cd C:\path\to\vault
python -m venv venv
venv\Scripts\activate
pip install cryptography argon2-cffi
```

### Run Tests
```bash
python src\vault.py --test
```

---

## 📝 Command Reference

| Command | Function | Example |
|---------|----------|---------|
| `v` | Encrypt | `python src\vault.py v myfile.txt` |
| `e` | Decrypt | `python src\vault.py e myfile.vault` |
| `encrypt` | Encrypt (alias) | `python src\vault.py encrypt data.zip` |
| `decrypt` | Decrypt (alias) | `python src\vault.py decrypt data.vault` |

---

## ⚠️ Error Handling

| Error | Solution |
|-------|----------|
| "Python not found" | Install Python from python.org and add to PATH |
| "Module not found" | Run `pip install cryptography argon2-cffi` |
| "Wrong password" | Verify password is correct |
| "Corrupted file" | File may be damaged; check backup |

---

## 📞 Support

For issues or questions:
1. Check the vault.py comments for detailed documentation
2. Verify all required packages are installed
3. Ensure you have write permissions to output directory

---

## 📄 License

Proprietary - All rights reserved

---

## 🔄 Version History

- **v5.0 ULTRA** - Enhanced memory management, improved error handling
- **v4.0 QUANTUM** - Post-quantum ready architecture
- **v3.0** - Initial Argon2id integration
- **v2.0** - Added AES-256-GCM
- **v1.0** - Initial release

---

**Last Updated:** January 2026  
**Maintained by:** Security Team
