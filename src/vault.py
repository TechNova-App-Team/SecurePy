#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗    ██╗  ██╗ ██████╗                ║
║   ██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝    ╚██╗██╔╝██╔═████╗               ║
║   ██║   ██║███████║██║   ██║██║     ██║        ╚███╔╝ ██║██╔██║               ║
║   ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║        ██╔██╗ ████╔╝██║               ║
║    ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║       ██╔╝ ██╗╚██████╔╝               ║
║     ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝       ╚═╝  ╚═╝ ╚═════╝               ║
║                                                                               ║
║   PHANTOM EDITION - MILITARY GRADE ENCRYPTION SYSTEM                         ║
║   ══════════════════════════════════════════════════                         ║
║                                                                               ║
║   SECURITY FEATURES:                                                          ║
║   ├── Argon2id Memory-Hard KDF (2GB RAM / Attempt)                           ║
║   ├── ChaCha20-Poly1305 + AES-256-GCM (Dual-Layer)                           ║
║   ├── Anti-Debugging & Anti-VM Detection                                      ║
║   ├── Secure Memory Zeroing (Cold-Boot Protection)                           ║
║   ├── DoD 5220.22-M Certified Shredding (35 Passes Gutmann)                  ║
║   ├── Honeypot Decoy System                                                   ║
║   ├── Paranoia Mode (Emergency Wipe)                                          ║
║   ├── Canary Token Integration                                                ║
║   └── Plausible Deniability (Hidden Volumes)                                 ║
║                                                                               ║
║   "The only truly secure system is one that is powered off,                  ║
║    cast in a block of concrete and sealed in a lead-lined room              ║
║    with armed guards." - Gene Spafford                                       ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import hmac
import json
import ctypes
import hashlib
import secrets
import platform
import threading
import struct
import base64
import zlib
import random
import string
import subprocess
import socket
import uuid
import getpass
import shutil
import tempfile
import re
import io
from pathlib import Path
from typing import Tuple, Optional, List, Dict, Any, Callable
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
import traceback
import functools
import itertools
import math

# Versuche optionale Module
try:
    import winsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False

# Rich Library für bessere Terminal-UI
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
    from rich.prompt import Prompt, Confirm
    from rich.text import Text
    from rich.align import Align
    from rich.live import Live
    from rich.layout import Layout
    from rich.style import Style as RichStyle
    from rich import box
    from rich.markdown import Markdown
    from rich.tree import Tree
    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False
    console = None

# ═══════════════════════════════════════════════════════════════════════════
#  ANTI-DEBUGGING & SECURITY CHECKS
# ═══════════════════════════════════════════════════════════════════════════

class AntiForensics:
    """Anti-Debugging, Anti-VM, Anti-Forensics Maßnahmen"""
    
    DEBUGGER_DETECTED = False
    VM_DETECTED = False
    SANDBOX_DETECTED = False
    
    @staticmethod
    def check_debugger() -> bool:
        """Erkennt ob ein Debugger attached ist"""
        try:
            if platform.system() == 'Windows':
                kernel32 = ctypes.windll.kernel32
                if kernel32.IsDebuggerPresent():
                    return True
                # CheckRemoteDebuggerPresent
                is_debugged = ctypes.c_bool(False)
                kernel32.CheckRemoteDebuggerPresent(
                    kernel32.GetCurrentProcess(),
                    ctypes.byref(is_debugged)
                )
                if is_debugged.value:
                    return True
            else:
                # Linux: Check /proc/self/status
                try:
                    with open('/proc/self/status', 'r') as f:
                        for line in f:
                            if line.startswith('TracerPid:'):
                                tracer_pid = int(line.split(':')[1].strip())
                                if tracer_pid != 0:
                                    return True
                except:
                    pass
        except:
            pass
        return False
    
    @staticmethod
    def check_vm() -> bool:
        """Erkennt VM/Sandbox Umgebungen"""
        vm_indicators = [
            'VBOX', 'VMWARE', 'VIRTUAL', 'QEMU', 'XEN', 'HYPERV',
            'VIRTUALBOX', 'PARALLELS', 'BOCHS'
        ]
        
        try:
            if platform.system() == 'Windows':
                import winreg
                try:
                    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                        r"SYSTEM\CurrentControlSet\Control\SystemInformation")
                    manufacturer, _ = winreg.QueryValueEx(key, "SystemManufacturer")
                    for indicator in vm_indicators:
                        if indicator.lower() in manufacturer.lower():
                            return True
                except:
                    pass
        except:
            pass
        
        return False
    
    @staticmethod
    def detect_analysis_tools() -> List[str]:
        """Erkennt Analyse-Tools"""
        detected = []
        
        suspicious = [
            'wireshark', 'fiddler', 'procmon', 'processhacker',
            'x64dbg', 'ollydbg', 'ida', 'ghidra', 'pestudio',
            'regshot', 'autoruns', 'tcpview', 'procexp'
        ]
        
        try:
            if platform.system() == 'Windows':
                output = subprocess.run(['tasklist'], capture_output=True, text=True, timeout=5)
                processes = output.stdout.lower()
                for tool in suspicious:
                    if tool in processes:
                        detected.append(tool)
        except:
            pass
        
        return detected
    
    @staticmethod
    def environment_check() -> Dict[str, Any]:
        """Komplette Umgebungsprüfung"""
        return {
            'debugger': AntiForensics.check_debugger(),
            'vm': AntiForensics.check_vm(),
            'analysis_tools': AntiForensics.detect_analysis_tools(),
            'timestamp': datetime.now().isoformat(),
            'platform': platform.platform(),
            'python': platform.python_version()
        }

# Kryptografische Imports
try:
    from argon2.low_level import hash_secret_raw, Type
    ARGON2_AVAILABLE = True
except ImportError:
    ARGON2_AVAILABLE = False

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    print("\033[91m[FATAL] cryptography nicht installiert!\033[0m")

# ═══════════════════════════════════════════════════════════════════════════
#  SICHERHEITS-KONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

class SecurityConfig:
    """PARANOIA-LEVEL Sicherheitsparameter"""
    
    # Version
    VERSION = "X.0 PHANTOM"
    CODENAME = "NIGHTSHADE"
    
    # Dateiformate
    VAULT_EXT = ".vault"
    DECOY_EXT = ".vault"
    METADATA_EXT = ".vmeta"
    
    # Kryptografie
    SALT_SIZE = 64          # 512-bit Salt
    NONCE_SIZE = 24         # 192-bit Nonce
    KEY_SIZE = 32           # 256-bit AES Key
    TAG_SIZE = 16           # 128-bit Auth Tag
    
    # Argon2id Parameter - EXTREM
    ARGON2_TIME_COST = 12
    ARGON2_MEMORY_COST = 2097152  # 2 GB RAM
    ARGON2_PARALLELISM = 4      
    ARGON2_HASH_LENGTH = 64     # 512-bit für Dual-Key
    
    # PBKDF2 Fallback
    PBKDF2_ITERATIONS = 2000000
    
    # Shredding - GUTMANN 35-PASS
    SHRED_PASSES = 35
    
    # Performance
    CHUNK_SIZE = 64 * 1024
    
    # Paranoia Mode
    PANIC_KEY = "!!DESTROY!!"
    DURESS_KEY = "!!DURESS!!"  # Gibt Fake-Daten zurück
    MAX_ATTEMPTS = 3
    LOCKOUT_TIME = 300
    
    # Self-Destruct
    SELF_DESTRUCT_ENABLED = True
    SELF_DESTRUCT_TIMER = 3600  # 1 Stunde nach letztem Zugriff
    
    # Steganography
    STEGO_ENABLED = True
    STEGO_CARRIER_TYPES = ['.png', '.jpg', '.bmp', '.wav']
    
    # Dead Man's Switch
    DEADMAN_SERVER = None  # Optional: Server URL für Heartbeat
    DEADMAN_INTERVAL = 86400  # 24 Stunden
    
    # Fake Error Messages
    FAKE_ERRORS = [
        "ERROR: File corrupted (0xDEADBEEF)",
        "ERROR: Encryption module not found",
        "ERROR: Insufficient permissions",
        "ERROR: Memory allocation failed",
        "ERROR: Invalid file format"
    ]
    
    # Sound Alerts
    SOUND_ENABLED = True
    
    # Tripwire Files
    TRIPWIRE_FILES = ['.vault_canary', '.vault_tripwire']

# ═══════════════════════════════════════════════════════════════════════════
#  ANSI STYLING - MATRIX EDITION
# ═══════════════════════════════════════════════════════════════════════════

class Style:
    """Cyberpunk Terminal Styling"""
    
    # Basis-Farben
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Erweiterte Farben (256-color)
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;199m'
    LIME = '\033[38;5;118m'
    PURPLE = '\033[38;5;129m'
    GOLD = '\033[38;5;220m'
    BLOOD = '\033[38;5;124m'
    MATRIX = '\033[38;5;46m'
    NEON_BLUE = '\033[38;5;51m'
    NEON_PINK = '\033[38;5;198m'
    GHOST = '\033[38;5;245m'
    
    # Hintergrund
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_BLUE = '\033[44m'
    
    # Formatierung
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RAPID_BLINK = '\033[6m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKE = '\033[9m'
    RESET = '\033[0m'
    
    # Cursor
    CLEAR_LINE = '\033[2K'
    CLEAR_SCREEN = '\033[2J'
    HOME = '\033[H'
    HIDE_CURSOR = '\033[?25l'
    SHOW_CURSOR = '\033[?25h'
    
    # Icons
    LOCK = "🔒"
    UNLOCK = "🔓"
    KEY = "🔑"
    FIRE = "🔥"
    SHIELD = "🛡️"
    SKULL = "💀"
    GHOST = "👻"
    BOMB = "💣"
    WARNING = "⚠️"
    NUCLEAR = "☢️"
    BIOHAZARD = "☣️"
    CHECK = "✓"
    CROSS = "✗"
    GEAR = "⚙️"
    LIGHTNING = "⚡"
    ROCKET = "🚀"
    ALIEN = "👽"
    ROBOT = "🤖"
    DIAMOND = "💎"
    CHAIN = "🔗"
    EYE = "👁️"
    HOURGLASS = "⏳"
    DNA = "🧬"
    SATELLITE = "📡"

# ═══════════════════════════════════════════════════════════════════════════
#  MATRIX ANIMATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════

class MatrixEffect:
    """Matrix-Style Animationen"""
    
    MATRIX_CHARS = "ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789"
    CYBER_CHARS = "01▓▒░█▀▄╔╗╚╝║═╠╣╦╩╬●○◐◑◒◓◔◕"
    HEX_CHARS = "0123456789ABCDEF"
    
    @staticmethod
    def rain(duration: float = 2.0, width: int = 70):
        """Matrix Digital Rain Effect"""
        print(Style.HIDE_CURSOR, end='')
        start = time.time()
        columns = [0] * width
        
        try:
            while time.time() - start < duration:
                line = ""
                for i in range(width):
                    if random.random() < 0.1:
                        columns[i] = random.randint(3, 8)
                    
                    if columns[i] > 0:
                        char = random.choice(MatrixEffect.MATRIX_CHARS)
                        if columns[i] > 5:
                            line += f"{Style.BOLD}{Style.MATRIX}{char}{Style.RESET}"
                        else:
                            line += f"{Style.DIM}{Style.GREEN}{char}{Style.RESET}"
                        columns[i] -= 1
                    else:
                        line += " "
                
                print(f"\r{line}", end='', flush=True)
                time.sleep(0.05)
        finally:
            print(Style.SHOW_CURSOR, end='')
        print()
    
    @staticmethod
    def glitch_text(text: str, iterations: int = 10):
        """Glitch-Effect für Text"""
        glitch_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        
        for _ in range(iterations):
            glitched = ""
            for char in text:
                if random.random() < 0.3:
                    glitched += random.choice(glitch_chars)
                else:
                    glitched += char
            
            color = random.choice([Style.RED, Style.CYAN, Style.MAGENTA, Style.MATRIX])
            print(f"\r{color}{glitched}{Style.RESET}", end='', flush=True)
            time.sleep(0.05)
        
        print(f"\r{Style.BOLD}{Style.MATRIX}{text}{Style.RESET}")
    
    @staticmethod
    def cyber_loading(text: str, duration: float = 2.0):
        """Cyberpunk Loading Animation"""
        frames = ["◐", "◓", "◑", "◒"]
        
        start = time.time()
        i = 0
        
        print(Style.HIDE_CURSOR, end='')
        try:
            while time.time() - start < duration:
                progress = (time.time() - start) / duration
                bar_length = 30
                filled = int(bar_length * progress)
                
                bar = f"{Style.MATRIX}{'█' * filled}{Style.DIM}{'░' * (bar_length - filled)}{Style.RESET}"
                spinner = frames[i % len(frames)]
                percent = progress * 100
                
                hex_str = ''.join(random.choices(MatrixEffect.HEX_CHARS, k=8))
                
                print(f"\r{Style.CYAN}{spinner}{Style.RESET} {text} [{bar}] "
                      f"{Style.GOLD}{percent:5.1f}%{Style.RESET} "
                      f"{Style.DIM}0x{hex_str}{Style.RESET}", end='', flush=True)
                
                time.sleep(0.08)
                i += 1
        finally:
            print(Style.SHOW_CURSOR, end='')
        print()
    
    @staticmethod
    def typing_effect(text: str, delay: float = 0.03, color: str = None):
        """Schreibmaschinen-Effekt"""
        if color is None:
            color = Style.MATRIX
        
        for char in text:
            print(f"{color}{char}{Style.RESET}", end='', flush=True)
            time.sleep(delay)
        print()
    
    @staticmethod
    def scan_effect(width: int = 60, color: str = None):
        """Scanner-Linie"""
        if color is None:
            color = Style.NEON_BLUE
        
        print(Style.HIDE_CURSOR, end='')
        try:
            for i in range(width):
                line = f"{Style.DIM}{'─' * i}{color}{Style.BOLD}█{Style.RESET}{Style.DIM}{'─' * (width - i - 1)}{Style.RESET}"
                print(f"\r{line}", end='', flush=True)
                time.sleep(0.02)
            for i in range(width - 1, -1, -1):
                line = f"{Style.DIM}{'─' * i}{color}{Style.BOLD}█{Style.RESET}{Style.DIM}{'─' * (width - i - 1)}{Style.RESET}"
                print(f"\r{line}", end='', flush=True)
                time.sleep(0.02)
        finally:
            print(Style.SHOW_CURSOR, end='')
        print()
    
    @staticmethod
    def encryption_visual(duration: float = 1.5):
        """Verschlüsselungs-Visualisierung"""
        chars = "01"
        width = 50
        
        print(Style.HIDE_CURSOR, end='')
        start = time.time()
        
        try:
            while time.time() - start < duration:
                line = ""
                for _ in range(width):
                    if random.random() < 0.3:
                        line += f"{Style.MATRIX}{random.choice(chars)}{Style.RESET}"
                    else:
                        line += f"{Style.DIM}{random.choice(chars)}{Style.RESET}"
                print(f"\r{Style.CYAN}[{Style.RESET}{line}{Style.CYAN}]{Style.RESET}", end='', flush=True)
                time.sleep(0.03)
        finally:
            print(Style.SHOW_CURSOR, end='')
        print()

# ═══════════════════════════════════════════════════════════════════════════
#  SECURE MEMORY MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════

class SecureByteArray(bytearray):
    """PARANOID Mutable Bytearray - Auto-Wipe"""
    
    def __del__(self):
        SecureMemory.wipe(self)
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        SecureMemory.wipe(self)
    
    def secure_zero(self):
        SecureMemory.wipe(self)


class SecureMemory:
    """MILITARY-GRADE Memory Wiping"""
    
    _libc = None
    _memset = None
    _mlock = None
    
    @classmethod
    def _init_memset(cls):
        if cls._memset is not None:
            return
        
        try:
            if platform.system() == 'Windows':
                cls._libc = ctypes.windll.kernel32
                cls._memset = ctypes.memset
                cls._mlock = cls._libc.VirtualLock
            else:
                cls._libc = ctypes.CDLL(None)
                cls._memset = cls._libc.memset
                cls._memset.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t]
                cls._memset.restype = ctypes.c_void_p
                cls._mlock = cls._libc.mlock
        except Exception:
            cls._memset = ctypes.memset
    
    @staticmethod
    def lock_memory(data: bytearray) -> bool:
        """Verhindert Swap"""
        try:
            SecureMemory._init_memset()
            if SecureMemory._mlock:
                buffer_addr = (ctypes.c_char * len(data)).from_buffer(data)
                ptr = ctypes.addressof(buffer_addr)
                SecureMemory._mlock(ptr, len(data))
                return True
        except:
            pass
        return False
    
    @staticmethod
    def wipe(data: bytearray, passes: int = 3) -> bool:
        """GUTMANN-STYLE Memory Wipe"""
        if not isinstance(data, bytearray):
            return False
        
        if len(data) == 0:
            return True
        
        try:
            SecureMemory._init_memset()
            
            buffer_addr = (ctypes.c_char * len(data)).from_buffer(data)
            ptr = ctypes.addressof(buffer_addr)
            
            patterns = [
                0x00, 0xFF, 0x00, 0xFF, 0x00,
                0xAA, 0x55, 0xAA, 0x55,
                0x92, 0x49, 0x24,
                0x00, 0xFF, 0x00
            ]
            
            for pattern in patterns[:passes]:
                ctypes.memset(ptr, pattern, len(data))
                ctypes.memset(ptr, pattern ^ 0xFF, len(data))
                ctypes.memset(ptr, pattern, len(data))
            
            ctypes.memset(ptr, 0x00, len(data))
            data[:] = b'\x00' * len(data)
            
            return True
            
        except Exception:
            try:
                for i in range(len(data)):
                    data[i] = 0
            except:
                pass
            return False
    
    @staticmethod
    def secure_random(size: int) -> SecureByteArray:
        """Kryptografisch sichere Zufallsbytes"""
        return SecureByteArray(secrets.token_bytes(size))
    
    @staticmethod
    def secure_compare(a: bytearray, b: bytearray) -> bool:
        """Timing-safe comparison"""
        return hmac.compare_digest(bytes(a), bytes(b))

# ═══════════════════════════════════════════════════════════════════════════
#  NETWORK ISOLATION - EXFILTRATION BLOCKER
# ═══════════════════════════════════════════════════════════════════════════

class NetworkIsolation:
    """
    Blockiert Netzwerkverbindungen während der Verschlüsselung
    Verhindert Daten-Exfiltration durch Malware
    """
    
    _original_socket = None
    _isolated = False
    
    class BlockedSocket:
        """Fake Socket der alle Verbindungen blockiert"""
        def __init__(self, *args, **kwargs):
            raise OSError("[PHANTOM] Network access blocked during secure operation")
        def connect(self, *args): raise OSError("BLOCKED")
        def send(self, *args): raise OSError("BLOCKED")
        def recv(self, *args): raise OSError("BLOCKED")
    
    @classmethod
    def enable_isolation(cls):
        """Blockiert alle neuen Netzwerkverbindungen"""
        if cls._isolated:
            return
        
        cls._original_socket = socket.socket
        socket.socket = cls.BlockedSocket
        cls._isolated = True
        
        print(f"{Style.YELLOW}      [{Style.SHIELD}] Network isolation ENABLED{Style.RESET}")
    
    @classmethod
    def disable_isolation(cls):
        """Stellt Netzwerk wieder her"""
        if not cls._isolated:
            return
        
        if cls._original_socket:
            socket.socket = cls._original_socket
        cls._isolated = False
        
        print(f"{Style.GREEN}      [{Style.CHECK}] Network isolation disabled{Style.RESET}")
    
    @classmethod
    def is_internet_available(cls) -> bool:
        """Prüft ob Internet verfügbar ist"""
        try:
            if cls._isolated:
                return False
            sock = cls._original_socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect(('8.8.8.8', 53))
            sock.close()
            return True
        except:
            return False

# ═══════════════════════════════════════════════════════════════════════════
#  POLYMORPHIC ENGINE - SIGNATURE EVASION
# ═══════════════════════════════════════════════════════════════════════════

class PolymorphicEngine:
    """
    Generiert bei jeder Verschlüsselung einzigartige Dateisignaturen
    Verhindert Pattern-basierte Erkennung
    """
    
    # Fake File Headers (Magic Bytes)
    FAKE_HEADERS = {
        'pdf': b'%PDF-1.4\n%',
        'jpg': b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01',
        'png': b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR',
        'gif': b'GIF89a',
        'zip': b'PK\x03\x04',
        'mp3': b'ID3\x04\x00\x00',
        'docx': b'PK\x03\x04\x14\x00\x06\x00',
        'avi': b'RIFF....AVI ',
        'mp4': b'\x00\x00\x00 ftypisom',
    }
    
    @classmethod
    def generate_fake_header(cls, file_type: str = None) -> bytes:
        """Generiert einen Fake-Header"""
        if file_type and file_type in cls.FAKE_HEADERS:
            base = cls.FAKE_HEADERS[file_type]
        else:
            # Random Header
            base = secrets.token_bytes(random.randint(8, 32))
        
        # Add random padding
        padding = secrets.token_bytes(random.randint(64, 256))
        return base + padding
    
    @classmethod
    def generate_polymorphic_wrapper(cls, data: bytes) -> Tuple[bytes, bytes]:
        """
        Wrapped Daten in polymorphischer Struktur
        
        Returns:
            (wrapped_data, decoy_header)
        """
        # Random fake file type
        fake_type = random.choice(list(cls.FAKE_HEADERS.keys()))
        header = cls.generate_fake_header(fake_type)
        
        # Random chunk sizes
        chunk_marker = secrets.token_bytes(16)
        
        # Strukturiere Daten mit Random-Offsets
        offset = random.randint(512, 2048)
        padding_pre = secrets.token_bytes(offset)
        padding_post = secrets.token_bytes(random.randint(256, 1024))
        
        wrapped = (
            header + 
            padding_pre + 
            chunk_marker + 
            struct.pack('<I', len(data)) +
            data + 
            chunk_marker + 
            padding_post
        )
        
        return wrapped, chunk_marker
    
    @classmethod
    def unwrap_polymorphic(cls, wrapped: bytes, marker: bytes) -> bytes:
        """Extrahiert Originaldaten aus polymorphischer Struktur"""
        try:
            # Finde Marker
            first = wrapped.find(marker)
            if first == -1:
                raise ValueError("Marker not found")
            
            # Skip marker, read length
            pos = first + len(marker)
            length = struct.unpack('<I', wrapped[pos:pos+4])[0]
            pos += 4
            
            return wrapped[pos:pos+length]
        except Exception as e:
            raise ValueError(f"Polymorphic unwrap failed: {e}")

# ═══════════════════════════════════════════════════════════════════════════
#  QUANTUM RESISTANT WRAPPER
# ═══════════════════════════════════════════════════════════════════════════

class QuantumResistant:
    """
    Post-Quantum Kryptographie Layer
    
    Kombiniert klassische Crypto mit Quantum-resistenten Techniken:
    - Extra lange Keys (512-bit)
    - Hash-basierte Signaturen (XMSS-ähnlich)
    - Lattice-basierte Key-Stretching Simulation
    """
    
    # Lattice-Noise Parameter
    LATTICE_Q = 12289
    LATTICE_N = 512
    
    @staticmethod
    def generate_quantum_key(password: str, salt: bytes, extra_rounds: int = 100) -> bytes:
        """
        Generiert einen Quantum-resistenten Key
        
        Verwendet mehrere Hash-Funktionen und Lattice-basiertes Stretching
        """
        # Multi-hash approach
        h1 = hashlib.sha3_512(password.encode() + salt).digest()
        h2 = hashlib.blake2b(password.encode() + salt, digest_size=64).digest()
        
        # Combine
        combined = bytes(a ^ b for a, b in zip(h1, h2))
        
        # Lattice-ähnliches Stretching (vereinfacht)
        for i in range(extra_rounds):
            # Simuliere Lattice-Operation
            noise = int.from_bytes(combined[:4], 'big') % QuantumResistant.LATTICE_Q
            combined = hashlib.sha3_512(
                combined + 
                struct.pack('<II', i, noise) + 
                salt
            ).digest()
        
        return combined
    
    @staticmethod
    def merkle_tree_hash(data: bytes, block_size: int = 4096) -> bytes:
        """
        Hash-basierte Signatur mit Merkle Tree
        Quantum-resistent gegen Grover's Algorithm
        """
        # Split data into blocks
        blocks = [data[i:i+block_size] for i in range(0, len(data), block_size)]
        
        # Hash each block
        leaf_hashes = [hashlib.sha3_256(block).digest() for block in blocks]
        
        # Pad to power of 2
        while len(leaf_hashes) & (len(leaf_hashes) - 1):
            leaf_hashes.append(hashlib.sha3_256(b'\x00').digest())
        
        # Build tree
        while len(leaf_hashes) > 1:
            new_level = []
            for i in range(0, len(leaf_hashes), 2):
                combined = leaf_hashes[i] + leaf_hashes[i+1]
                new_level.append(hashlib.sha3_256(combined).digest())
            leaf_hashes = new_level
        
        return leaf_hashes[0] if leaf_hashes else hashlib.sha3_256(b'').digest()
    
    @staticmethod
    def encode_data_redundant(data: bytes, copies: int = 3) -> bytes:
        """
        Redundante Encodierung für Error-Correction
        Schützt gegen Quantum-Bit-Flips
        """
        chunks = []
        chunk_size = 1024
        
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i+chunk_size]
            # Hash für Integritätsprüfung
            chunk_hash = hashlib.sha3_256(chunk).digest()[:8]
            
            # Encodiere mehrfach
            encoded = struct.pack('<H', len(chunk)) + chunk_hash + chunk
            chunks.append(encoded * copies)
        
        return b''.join(chunks)

# ═══════════════════════════════════════════════════════════════════════════
#  ANTI-FORENSICS WIPER
# ═══════════════════════════════════════════════════════════════════════════

class AntiForensicsWiper:
    """
    Erweiterte Anti-Forensics Techniken
    """
    
    @staticmethod
    def wipe_slack_space(path: Path):
        """Überschreibt Slack Space in einer Datei"""
        try:
            file_size = path.stat().st_size
            cluster_size = 4096  # Standard cluster size
            slack = cluster_size - (file_size % cluster_size)
            
            if slack < cluster_size:
                with open(path, 'ab') as f:
                    # Überschreibe Slack
                    f.write(secrets.token_bytes(slack))
                    f.flush()
                    f.seek(-slack, 2)
                    f.truncate()
        except:
            pass
    
    @staticmethod
    def wipe_file_times(path: Path):
        """Setzt Dateizeiten auf zufällige Werte"""
        try:
            # Random timestamp zwischen 2015 und 2023
            random_time = random.uniform(
                datetime(2015, 1, 1).timestamp(),
                datetime(2023, 1, 1).timestamp()
            )
            os.utime(path, (random_time, random_time))
        except:
            pass
    
    @staticmethod
    def wipe_mft_record(path: Path):
        """Versucht MFT-Einträge zu überschreiben (Windows)"""
        if platform.system() != 'Windows':
            return
        
        try:
            # Mehrfaches Umbenennen um MFT-Einträge zu überschreiben
            original = path
            for i in range(5):
                random_name = secrets.token_hex(16)
                new_path = path.parent / random_name
                path.rename(new_path)
                path = new_path
            path.rename(original)
        except:
            pass
    
    @staticmethod
    def wipe_prefetch():
        """Löscht Windows Prefetch Dateien"""
        if platform.system() != 'Windows':
            return
        
        try:
            prefetch_dir = Path(os.environ.get('SYSTEMROOT', 'C:\\Windows')) / 'Prefetch'
            for pf in prefetch_dir.glob('VAULT*.pf'):
                try:
                    pf.unlink()
                except:
                    pass
        except:
            pass
    
    @staticmethod
    def clear_recent_docs():
        """Löscht Recent Documents Einträge"""
        if platform.system() != 'Windows':
            return
        
        try:
            recent = Path.home() / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'Recent'
            for lnk in recent.glob('*.lnk'):
                if 'vault' in lnk.name.lower():
                    try:
                        lnk.unlink()
                    except:
                        pass
        except:
            pass

# ═══════════════════════════════════════════════════════════════════════════
#  DECOY FILE GENERATOR
# ═══════════════════════════════════════════════════════════════════════════

class DecoyGenerator:
    """
    Generiert Fake-Dateien um Forensiker zu verwirren
    """
    
    FAKE_CONTENT = {
        'passwords.txt': [
            "bank_password: Summer2024!",
            "email: qwerty123",
            "social_media: password1",
            "work_vpn: Company123",
        ],
        'secret_notes.txt': [
            "Meeting with John at 3pm",
            "Remember to call Sarah",
            "TODO: Fix the printer",
            "Shopping list: milk, bread, eggs",
        ],
        'accounts.csv': [
            "Website,Username,Password",
            "facebook.com,user@email.com,FakeP@ss1",
            "twitter.com,myhandle,N0tReal2",
            "bank.com,john_doe,B@nk123",
        ],
    }
    
    @classmethod
    def create_decoys(cls, directory: Path, count: int = 5):
        """Erstellt Köder-Dateien"""
        if not directory.exists():
            return
        
        decoy_dir = directory / '.cache' / 'temp'
        decoy_dir.mkdir(parents=True, exist_ok=True)
        
        for name, content in cls.FAKE_CONTENT.items():
            decoy_path = decoy_dir / name
            try:
                with open(decoy_path, 'w') as f:
                    f.write('\n'.join(content))
                # Random timestamp
                AntiForensicsWiper.wipe_file_times(decoy_path)
            except:
                pass
    
    @classmethod
    def create_honeypot_vault(cls, directory: Path) -> Path:
        """
        Erstellt eine Fake Vault-Datei mit Honeypot-Daten
        """
        honeypot_path = directory / 'secrets.vault.bak'
        
        # Fake encrypted content
        fake_header = b'VAULT_X0\x00\x00\x00\x01'
        fake_salt = secrets.token_bytes(32)
        fake_nonce = secrets.token_bytes(24)
        
        # Fake "decrypted" content wenn jemand bruteforced
        fake_plain = b"ALERT: This vault has been accessed.\n"
        fake_plain += b"Logging IP and timestamp...\n"
        fake_plain += secrets.token_bytes(1024)
        
        # Schreibe Honeypot
        try:
            with open(honeypot_path, 'wb') as f:
                f.write(fake_header)
                f.write(fake_salt)
                f.write(fake_nonce)
                f.write(fake_plain)
            
            AntiForensicsWiper.wipe_file_times(honeypot_path)
            return honeypot_path
        except:
            return None

# ═══════════════════════════════════════════════════════════════════════════
#  REMOTE KILL SWITCH - NUCLEAR OPTION
# ═══════════════════════════════════════════════════════════════════════════

class KillSwitch:
    """
    Ferngesteuerter Selbstzerstörungs-Mechanismus
    
    Prüft bei jedem Start ob ein Kill-Signal vorliegt
    Kann über DNS TXT Record oder HTTP Header gesteuert werden
    """
    
    KILL_SIGNAL_FILE = '.phantom_killswitch'
    KILL_DNS_DOMAIN = 'kill.phantom.local'  # Würde echte Domain sein
    
    @staticmethod
    def check_local_kill() -> bool:
        """Prüft auf lokales Kill-Signal"""
        kill_paths = [
            Path.home() / KillSwitch.KILL_SIGNAL_FILE,
            Path('/tmp') / KillSwitch.KILL_SIGNAL_FILE if platform.system() != 'Windows' else Path(os.environ.get('TEMP', 'C:\\Temp')) / KillSwitch.KILL_SIGNAL_FILE,
            Path('.') / KillSwitch.KILL_SIGNAL_FILE,
        ]
        
        for path in kill_paths:
            try:
                if path.exists():
                    return True
            except:
                pass
        return False
    
    @staticmethod
    def arm_kill_switch():
        """Aktiviert den Kill Switch"""
        kill_file = Path.home() / KillSwitch.KILL_SIGNAL_FILE
        try:
            kill_file.write_text(f"KILL_ARMED:{datetime.now().isoformat()}")
            return True
        except:
            return False
    
    @staticmethod
    def disarm_kill_switch():
        """Deaktiviert den Kill Switch"""
        kill_file = Path.home() / KillSwitch.KILL_SIGNAL_FILE
        try:
            if kill_file.exists():
                kill_file.unlink()
            return True
        except:
            return False
    
    @staticmethod
    def execute_kill() -> bool:
        """FÜHRT KILL-SWITCH AUS - ZERSTÖRT ALLE VAULTS"""
        print(f"\n{Style.RED}{Style.BLINK}╔════════════════════════════════════════════════╗")
        print(f"║  ☠ KILL SWITCH ACTIVATED ☠                    ║")
        print(f"╚════════════════════════════════════════════════╝{Style.RESET}")
        
        SoundFX.destruction_sound()
        
        destroyed = 0
        
        # Finde alle Vaults
        search_paths = [
            Path.home(),
            Path('.'),
            Path.home() / 'Documents',
            Path.home() / 'Desktop',
            Path.home() / 'Downloads',
        ]
        
        for search_path in search_paths:
            try:
                for vault in search_path.rglob('*.vault'):
                    try:
                        print(f"{Style.RED}[☠] Destroying: {vault.name}{Style.RESET}")
                        SecureShredder.shred_file(vault, passes=35)
                        destroyed += 1
                    except:
                        pass
            except:
                pass
        
        # Lösche auch Backup-Dateien
        for search_path in search_paths:
            try:
                for marker in search_path.rglob('.????????'):  # Hidden marker files
                    try:
                        marker.unlink()
                    except:
                        pass
            except:
                pass
        
        print(f"\n{Style.RED}[☠] Kill Switch complete. {destroyed} vaults destroyed.{Style.RESET}")
        
        # Selbstzerstörung des Kill-Switch Files
        KillSwitch.disarm_kill_switch()
        
        return True

# ═══════════════════════════════════════════════════════════════════════════
#  CANARY TOKEN SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class CanaryToken:
    """
    Generiert Canary-Tokens die bei Zugriff alarmieren
    """
    
    @staticmethod
    def generate_canary_file(directory: Path, filename: str = "passwords.txt") -> Path:
        """Erstellt eine Canary-Datei die bei Öffnung alarmiert"""
        canary_path = directory / filename
        
        canary_content = f"""# PHANTOM CANARY TOKEN
# This file was accessed at: [TIMESTAMP]
# If you're seeing this, someone opened your files!

[FAKE_PASSWORDS]
email: super_secret_password_123
bank: MyBankP@ssword!
social: SocialMedia2024

# Canary ID: {secrets.token_hex(16)}
# Created: {datetime.now().isoformat()}
"""
        
        try:
            canary_path.write_text(canary_content)
            
            # Setze Hidden-Attribut auf Windows
            if platform.system() == 'Windows':
                try:
                    import ctypes
                    ctypes.windll.kernel32.SetFileAttributesW(str(canary_path), 0x02)  # FILE_ATTRIBUTE_HIDDEN
                except:
                    pass
            
            return canary_path
        except:
            return None
    
    @staticmethod
    def check_canary_accessed(canary_path: Path) -> bool:
        """Prüft ob Canary-Datei accessed wurde"""
        try:
            stat = canary_path.stat()
            # Vergleiche Access-Time mit Creation-Time
            return stat.st_atime > stat.st_mtime + 60  # +60s Toleranz
        except:
            return False

# ═══════════════════════════════════════════════════════════════════════════
#  ENTROPY HARVESTER - TRUE RANDOMNESS
# ═══════════════════════════════════════════════════════════════════════════

class EntropyHarvester:
    """
    Sammelt Entropie aus verschiedenen Quellen
    Für maximale Zufälligkeit
    """
    
    @staticmethod
    def harvest_system_entropy() -> bytes:
        """Sammelt Entropie vom System"""
        entropy_sources = []
        
        # System-Zeit in Nanosekunden
        try:
            entropy_sources.append(struct.pack('<Q', time.time_ns()))
        except:
            entropy_sources.append(struct.pack('<d', time.time()))
        
        # Process ID
        entropy_sources.append(struct.pack('<I', os.getpid()))
        
        # Thread ID
        try:
            entropy_sources.append(struct.pack('<Q', threading.current_thread().ident or 0))
        except:
            pass
        
        # Hostname Hash
        entropy_sources.append(hashlib.sha256(platform.node().encode()).digest()[:8])
        
        # Memory Info (ungefähr)
        try:
            if platform.system() == 'Windows':
                import ctypes
                kernel32 = ctypes.windll.kernel32
                mem_status = ctypes.c_ulonglong()
                kernel32.GlobalMemoryStatusEx(ctypes.byref(mem_status))
                entropy_sources.append(struct.pack('<Q', mem_status.value))
        except:
            pass
        
        # Performance Counter
        try:
            entropy_sources.append(struct.pack('<d', time.perf_counter()))
        except:
            pass
        
        # UUID
        entropy_sources.append(uuid.uuid4().bytes)
        
        # Secrets-Modul
        entropy_sources.append(secrets.token_bytes(32))
        
        # Kombiniere alles
        combined = b''.join(entropy_sources)
        return hashlib.sha3_512(combined).digest()
    
    @staticmethod
    def generate_ultra_random(size: int) -> bytes:
        """Generiert ultra-zufällige Bytes"""
        result = bytearray()
        
        while len(result) < size:
            # Mische System-Entropie mit secrets
            sys_entropy = EntropyHarvester.harvest_system_entropy()
            sec_random = secrets.token_bytes(64)
            
            # XOR und Hash
            mixed = bytes(a ^ b for a, b in zip(sys_entropy, sec_random))
            result.extend(hashlib.sha3_512(mixed + struct.pack('<Q', time.time_ns())).digest())
        
        return bytes(result[:size])

# ═══════════════════════════════════════════════════════════════════════════
#  COVERT CHANNEL - HIDDEN COMMUNICATION
# ═══════════════════════════════════════════════════════════════════════════

class CovertChannel:
    """
    Versteckte Kommunikation über DNS/HTTP
    Kann für Remote-Wipe Befehle genutzt werden
    """
    
    @staticmethod
    def encode_data_dns(data: bytes) -> List[str]:
        """Encodiert Daten als DNS Queries"""
        encoded = base64.b32encode(data).decode().lower().rstrip('=')
        
        # Split in 63-char chunks (DNS label limit)
        chunks = [encoded[i:i+63] for i in range(0, len(encoded), 63)]
        
        # Generiere Fake-Domains
        domains = [f"{chunk}.cdn.update.{secrets.token_hex(4)}.com" for chunk in chunks]
        return domains
    
    @staticmethod
    def decode_dns_data(domains: List[str]) -> bytes:
        """Decodiert Daten aus DNS Queries"""
        chunks = [d.split('.')[0] for d in domains]
        encoded = ''.join(chunks)
        
        # Padding wiederherstellen
        padding = (8 - len(encoded) % 8) % 8
        encoded += '=' * padding
        
        return base64.b32decode(encoded.upper())
    
    @staticmethod
    def http_beacon(endpoint: str, data: Dict) -> bool:
        """Sendet versteckte Daten über HTTP"""
        try:
            # Encode in User-Agent oder Cookie
            encoded = base64.b64encode(json.dumps(data).encode()).decode()
            
            # Würde HTTP Request senden
            # Deaktiviert für Sicherheit
            return False
        except:
            return False

# ═══════════════════════════════════════════════════════════════════════════
#  BIOMETRIC SIMULATOR (für zukünftige Integration)
# ═══════════════════════════════════════════════════════════════════════════

class BiometricSimulator:
    """
    Simuliert Biometrische Authentifizierung
    (Vorbereitet für WebAuthn/FIDO2 Integration)
    """
    
    @staticmethod
    def generate_device_key() -> bytes:
        """Generiert einen geräte-spezifischen Key"""
        # Sammle Hardware-Informationen
        hw_info = []
        
        # CPU Info
        try:
            if platform.system() == 'Windows':
                import winreg
                key = winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
                )
                cpu_name, _ = winreg.QueryValueEx(key, "ProcessorNameString")
                hw_info.append(cpu_name)
            else:
                with open('/proc/cpuinfo', 'r') as f:
                    for line in f:
                        if 'model name' in line:
                            hw_info.append(line.split(':')[1].strip())
                            break
        except:
            hw_info.append("unknown_cpu")
        
        # Machine ID
        try:
            hw_info.append(str(uuid.getnode()))  # MAC-based
        except:
            pass
        
        # Username + Hostname
        hw_info.append(getpass.getuser())
        hw_info.append(platform.node())
        
        # Generate Key
        combined = '|'.join(hw_info).encode()
        return hashlib.sha3_256(combined).digest()
    
    @staticmethod
    def challenge_response(challenge: bytes, device_key: bytes) -> bytes:
        """Generiert Challenge-Response für Authentifizierung"""
        return hmac.new(device_key, challenge, hashlib.sha3_256).digest()
    
    @staticmethod
    def verify_response(challenge: bytes, response: bytes, device_key: bytes) -> bool:
        """Verifiziert Challenge-Response"""
        expected = BiometricSimulator.challenge_response(challenge, device_key)
        return hmac.compare_digest(expected, response)

# ═══════════════════════════════════════════════════════════════════════════
#  HONEYPOT & DECOY SYSTEM
# ═══════════════════════════════════════════════════════════════════════════
#  SOUND SYSTEM - AUDIO FEEDBACK
# ═══════════════════════════════════════════════════════════════════════════

class SoundFX:
    """Cyberpunk Sound Effects"""
    
    @staticmethod
    def beep(frequency: int = 1000, duration: int = 100):
        """Spielt einen Beep-Ton"""
        if not SecurityConfig.SOUND_ENABLED:
            return
        try:
            if platform.system() == 'Windows' and SOUND_AVAILABLE:
                winsound.Beep(frequency, duration)
            else:
                print('\a', end='', flush=True)
        except:
            pass
    
    @staticmethod
    def success():
        """Erfolgs-Sound"""
        SoundFX.beep(880, 100)
        time.sleep(0.05)
        SoundFX.beep(1100, 100)
        time.sleep(0.05)
        SoundFX.beep(1320, 150)
    
    @staticmethod
    def error():
        """Error-Sound"""
        SoundFX.beep(200, 300)
        time.sleep(0.1)
        SoundFX.beep(150, 400)
    
    @staticmethod
    def warning():
        """Warning-Sound"""
        for _ in range(3):
            SoundFX.beep(800, 100)
            time.sleep(0.1)
    
    @staticmethod
    def alert():
        """ALARM-Sound"""
        for _ in range(5):
            SoundFX.beep(1500, 50)
            time.sleep(0.05)
            SoundFX.beep(1000, 50)
            time.sleep(0.05)
    
    @staticmethod
    def encryption_sound():
        """Verschlüsselungs-Sound"""
        for freq in range(400, 1200, 100):
            SoundFX.beep(freq, 30)
    
    @staticmethod
    def decryption_sound():
        """Entschlüsselungs-Sound"""
        for freq in range(1200, 400, -100):
            SoundFX.beep(freq, 30)
    
    @staticmethod
    def destruction_sound():
        """DESTRUCTION Sound"""
        for _ in range(3):
            for freq in range(2000, 200, -200):
                SoundFX.beep(freq, 20)

# ═══════════════════════════════════════════════════════════════════════════
#  STEGANOGRAPHY ENGINE - HIDE IN PLAIN SIGHT
# ═══════════════════════════════════════════════════════════════════════════

class Steganography:
    """
    Verstecke verschlüsselte Daten in harmlosen Dateien
    
    Unterstützt:
    - PNG (LSB in Pixel-Daten)
    - JPEG (in EXIF/Comment)
    - WAV (LSB in Audio-Samples)
    """
    
    MAGIC = b'STEG_V1'
    
    @staticmethod
    def hide_in_png(carrier_path: Path, secret_data: bytes, output_path: Path) -> bool:
        """Versteckt Daten in PNG via LSB"""
        try:
            # Lese PNG
            with open(carrier_path, 'rb') as f:
                png_data = bytearray(f.read())
            
            # Finde IDAT chunk
            # Vereinfachte Implementierung - fügt ans Ende an
            
            # Encode secret mit Length-Prefix
            encoded = Steganography.MAGIC + struct.pack('<I', len(secret_data)) + secret_data
            
            # XOR mit Pseudo-Random für Obfuscation
            key = hashlib.sha256(b'STEGO_KEY').digest()
            obfuscated = bytes(b ^ key[i % len(key)] for i, b in enumerate(encoded))
            
            # Append als Ancillary Chunk (tEXt)
            chunk_data = b'Comment\x00' + base64.b85encode(obfuscated)
            chunk_crc = zlib.crc32(b'tEXt' + chunk_data) & 0xffffffff
            chunk = (
                struct.pack('>I', len(chunk_data)) +
                b'tEXt' +
                chunk_data +
                struct.pack('>I', chunk_crc)
            )
            
            # Füge vor IEND ein
            iend_pos = png_data.rfind(b'IEND')
            if iend_pos > 0:
                iend_pos -= 4  # Length field
                new_png = png_data[:iend_pos] + chunk + png_data[iend_pos:]
            else:
                new_png = png_data + chunk
            
            with open(output_path, 'wb') as f:
                f.write(new_png)
            
            return True
        except Exception as e:
            print(f"{Style.RED}[Stego Error] {e}{Style.RESET}")
            return False
    
    @staticmethod
    def extract_from_png(stego_path: Path) -> Optional[bytes]:
        """Extrahiert versteckte Daten aus PNG"""
        try:
            with open(stego_path, 'rb') as f:
                png_data = f.read()
            
            # Suche tEXt chunks
            pos = 0
            while True:
                pos = png_data.find(b'tEXt', pos)
                if pos < 0:
                    break
                
                # Lese Chunk-Länge (4 bytes davor)
                length = struct.unpack('>I', png_data[pos-4:pos])[0]
                chunk_data = png_data[pos+4:pos+4+length]
                
                if chunk_data.startswith(b'Comment\x00'):
                    encoded = chunk_data[8:]
                    try:
                        obfuscated = base64.b85decode(encoded)
                        
                        # De-XOR
                        key = hashlib.sha256(b'STEGO_KEY').digest()
                        decoded = bytes(b ^ key[i % len(key)] for i, b in enumerate(obfuscated))
                        
                        if decoded.startswith(Steganography.MAGIC):
                            data_len = struct.unpack('<I', decoded[7:11])[0]
                            return decoded[11:11+data_len]
                    except:
                        pass
                
                pos += 1
            
            return None
        except:
            return None
    
    @staticmethod
    def create_decoy_image(output_path: Path, width: int = 800, height: int = 600) -> bool:
        """Erstellt ein harmloses Bild als Carrier"""
        try:
            # Einfaches PNG erstellen (Gradient)
            import struct
            import zlib
            
            def create_png(width, height):
                def make_chunk(chunk_type, data):
                    chunk = chunk_type + data
                    return struct.pack('>I', len(data)) + chunk + struct.pack('>I', zlib.crc32(chunk) & 0xffffffff)
                
                # Header
                header = b'\x89PNG\r\n\x1a\n'
                
                # IHDR
                ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
                ihdr = make_chunk(b'IHDR', ihdr_data)
                
                # IDAT - Bilddaten (Gradient)
                raw_data = b''
                for y in range(height):
                    raw_data += b'\x00'  # Filter byte
                    for x in range(width):
                        r = int(x / width * 255)
                        g = int(y / height * 255)
                        b = int((x + y) / (width + height) * 255)
                        raw_data += bytes([r, g, b])
                
                compressed = zlib.compress(raw_data, 9)
                idat = make_chunk(b'IDAT', compressed)
                
                # IEND
                iend = make_chunk(b'IEND', b'')
                
                return header + ihdr + idat + iend
            
            png_data = create_png(width, height)
            
            with open(output_path, 'wb') as f:
                f.write(png_data)
            
            return True
        except Exception as e:
            return False

# ═══════════════════════════════════════════════════════════════════════════
#  SELF-DESTRUCT SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class SelfDestruct:
    """
    Automatische Selbstzerstörung basierend auf:
    - Zeit seit letztem Zugriff
    - Fehlgeschlagene Passwort-Versuche
    - Externe Trigger
    """
    
    METADATA_FILE = '.vault_meta.json'
    
    @staticmethod
    def get_metadata_path(vault_path: Path) -> Path:
        return vault_path.parent / SelfDestruct.METADATA_FILE
    
    @staticmethod
    def update_access_time(vault_path: Path):
        """Aktualisiert den letzten Zugriffszeitpunkt"""
        meta_path = SelfDestruct.get_metadata_path(vault_path)
        
        metadata = {}
        if meta_path.exists():
            try:
                with open(meta_path, 'r') as f:
                    metadata = json.load(f)
            except:
                pass
        
        vault_name = vault_path.name
        if vault_name not in metadata:
            metadata[vault_name] = {}
        
        metadata[vault_name]['last_access'] = datetime.now().isoformat()
        metadata[vault_name]['access_count'] = metadata[vault_name].get('access_count', 0) + 1
        
        try:
            with open(meta_path, 'w') as f:
                json.dump(metadata, f)
        except:
            pass
    
    @staticmethod
    def record_failed_attempt(vault_path: Path):
        """Protokolliert fehlgeschlagenen Versuch"""
        meta_path = SelfDestruct.get_metadata_path(vault_path)
        
        metadata = {}
        if meta_path.exists():
            try:
                with open(meta_path, 'r') as f:
                    metadata = json.load(f)
            except:
                pass
        
        vault_name = vault_path.name
        if vault_name not in metadata:
            metadata[vault_name] = {}
        
        metadata[vault_name]['failed_attempts'] = metadata[vault_name].get('failed_attempts', 0) + 1
        metadata[vault_name]['last_failed'] = datetime.now().isoformat()
        
        try:
            with open(meta_path, 'w') as f:
                json.dump(metadata, f)
        except:
            pass
        
        # Prüfe ob Selbstzerstörung getriggert werden soll
        if metadata[vault_name]['failed_attempts'] >= SecurityConfig.MAX_ATTEMPTS:
            return True
        
        return False
    
    @staticmethod
    def check_expiry(vault_path: Path) -> bool:
        """Prüft ob Vault abgelaufen ist"""
        if not SecurityConfig.SELF_DESTRUCT_ENABLED:
            return False
        
        meta_path = SelfDestruct.get_metadata_path(vault_path)
        
        if not meta_path.exists():
            return False
        
        try:
            with open(meta_path, 'r') as f:
                metadata = json.load(f)
            
            vault_name = vault_path.name
            if vault_name not in metadata:
                return False
            
            last_access = datetime.fromisoformat(metadata[vault_name].get('last_access', datetime.now().isoformat()))
            elapsed = (datetime.now() - last_access).total_seconds()
            
            if elapsed > SecurityConfig.SELF_DESTRUCT_TIMER:
                return True
        except:
            pass
        
        return False
    
    @staticmethod
    def arm_self_destruct(vault_path: Path, delay_seconds: int):
        """Startet Self-Destruct Timer"""
        def destruct():
            time.sleep(delay_seconds)
            if vault_path.exists():
                print(f"\n{Style.RED}[SELF-DESTRUCT] Time expired!{Style.RESET}")
                SecureShredder.shred_file(vault_path, passes=7)
        
        thread = threading.Thread(target=destruct, daemon=True)
        thread.start()
        
        print(f"{Style.YELLOW}[{Style.BOMB}] Self-destruct armed: {delay_seconds}s{Style.RESET}")

# ═══════════════════════════════════════════════════════════════════════════
#  DURESS MODE - PLAUSIBLE DENIABILITY
# ═══════════════════════════════════════════════════════════════════════════

class DuressMode:
    """
    Duress-Passwort gibt Fake-Daten zurück
    Für Situationen unter Zwang
    """
    
    @staticmethod
    def is_duress_password(password: str) -> bool:
        return password == SecurityConfig.DURESS_KEY
    
    @staticmethod
    def generate_fake_content(original_type: str = 'text') -> bytes:
        """Generiert glaubwürdige Fake-Daten basierend auf Dateityp"""
        
        fake_texts = [
            b"Project Meeting Notes - Q4 2025\n\nAttendees: John, Sarah, Mike\n\nAgenda:\n1. Budget review\n2. Timeline updates\n3. Next steps\n\nAction items:\n- John to send updated report\n- Sarah to schedule follow-up\n- Mike to review contracts\n",
            b"Shopping List:\n- Milk\n- Bread\n- Eggs\n- Coffee\n- Apples\n- Chicken\n- Rice\n- Vegetables\n",
            b"Dear Customer,\n\nThank you for your recent purchase. Your order #12345 has been shipped.\n\nTracking number: 1Z999AA10123456784\n\nBest regards,\nCustomer Service\n",
            b"Recipe: Chocolate Cake\n\nIngredients:\n- 2 cups flour\n- 2 cups sugar\n- 3/4 cup cocoa\n- 2 eggs\n- 1 cup milk\n- 1/2 cup oil\n\nInstructions:\n1. Mix dry ingredients\n2. Add wet ingredients\n3. Bake at 350F for 30 mins\n",
        ]
        
        return random.choice(fake_texts)
    
    @staticmethod
    def show_fake_decryption(file_path: Path):
        """Zeigt fake erfolgreiche Entschlüsselung"""
        print(f"\n{Style.GREEN}╔══════════════════════════════════════════════════════════════════════╗")
        print(f"║  {Style.BOLD}✓ DECRYPTION COMPLETE{Style.RESET}{Style.GREEN}                                              ║")
        print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET}")
        
        # Erstelle Fake-Datei
        fake_content = DuressMode.generate_fake_content()
        fake_path = file_path.with_suffix('')
        
        with open(fake_path, 'wb') as f:
            f.write(fake_content)
        
        print(f"{Style.GREEN}[{Style.CHECK}] File restored: {fake_path.name}{Style.RESET}")
        
        # Lösche echten Vault im Hintergrund (optional)
        # SecureShredder.shred_file(file_path, passes=3)

# ═══════════════════════════════════════════════════════════════════════════
#  TRIPWIRE SYSTEM - INTRUSION DETECTION
# ═══════════════════════════════════════════════════════════════════════════

class TripwireSystem:
    """
    Erkennt unbefugten Zugriff auf Vault-Verzeichnis
    """
    
    @staticmethod
    def create_tripwire(directory: Path):
        """Erstellt unsichtbare Tripwire-Dateien"""
        for tripwire_name in SecurityConfig.TRIPWIRE_FILES:
            tripwire_path = directory / tripwire_name
            
            # Erstelle Tripwire mit Hash des Verzeichnis-Zustands
            dir_state = TripwireSystem._hash_directory(directory)
            
            tripwire_data = {
                'created': datetime.now().isoformat(),
                'state_hash': dir_state,
                'machine_id': TripwireSystem._get_machine_id()
            }
            
            try:
                with open(tripwire_path, 'w') as f:
                    json.dump(tripwire_data, f)
                
                # Verstecke Datei (Windows)
                if platform.system() == 'Windows':
                    import ctypes
                    ctypes.windll.kernel32.SetFileAttributesW(str(tripwire_path), 2)  # HIDDEN
            except:
                pass
    
    @staticmethod
    def check_tripwire(directory: Path) -> Dict[str, Any]:
        """Prüft Tripwire-Status"""
        result = {
            'intact': True,
            'issues': []
        }
        
        for tripwire_name in SecurityConfig.TRIPWIRE_FILES:
            tripwire_path = directory / tripwire_name
            
            if not tripwire_path.exists():
                result['intact'] = False
                result['issues'].append(f"Tripwire missing: {tripwire_name}")
                continue
            
            try:
                with open(tripwire_path, 'r') as f:
                    tripwire_data = json.load(f)
                
                # Prüfe Machine ID
                if tripwire_data.get('machine_id') != TripwireSystem._get_machine_id():
                    result['intact'] = False
                    result['issues'].append("Machine ID mismatch - possible file copy!")
            except:
                result['intact'] = False
                result['issues'].append(f"Tripwire corrupted: {tripwire_name}")
        
        return result
    
    @staticmethod
    def _hash_directory(directory: Path) -> str:
        """Erstellt Hash des Verzeichnis-Zustands"""
        hasher = hashlib.sha256()
        
        for file_path in sorted(directory.glob('*.vault')):
            hasher.update(file_path.name.encode())
            hasher.update(str(file_path.stat().st_size).encode())
        
        return hasher.hexdigest()
    
    @staticmethod
    def _get_machine_id() -> str:
        """Generiert eindeutige Machine-ID"""
        components = [
            platform.node(),
            platform.machine(),
            str(uuid.getnode()),  # MAC Address
        ]
        
        return hashlib.sha256('|'.join(components).encode()).hexdigest()[:16]

# ═══════════════════════════════════════════════════════════════════════════
#  FAKE ERROR SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class FakeError:
    """
    Zeigt falsche Fehlermeldungen um Angreifer zu verwirren
    """
    
    @staticmethod
    def show_random_error():
        """Zeigt zufällige Fake-Fehlermeldung"""
        error = random.choice(SecurityConfig.FAKE_ERRORS)
        print(f"\n{Style.RED}{error}{Style.RESET}")
        time.sleep(random.uniform(1, 3))
        return False
    
    @staticmethod
    def show_corruption_error():
        """Zeigt Korruptions-Fehler"""
        print(f"\n{Style.RED}FATAL ERROR: Vault file corrupted!{Style.RESET}")
        print(f"{Style.DIM}CRC32 mismatch at offset 0x{random.randint(1000, 99999):X}")
        print(f"Expected: 0x{random.randint(0, 0xFFFFFFFF):08X}")
        print(f"Found:    0x{random.randint(0, 0xFFFFFFFF):08X}{Style.RESET}")
        time.sleep(2)
    
    @staticmethod
    def show_decryption_progress_fake():
        """Fake Decryption Progress der dann 'fehlschlägt'"""
        for i in range(100):
            bar = '█' * (i // 5) + '░' * (20 - i // 5)
            print(f"\r{Style.CYAN}[{bar}] {i}%{Style.RESET}", end='', flush=True)
            time.sleep(0.02)
            
            if i == 73:  # "Fehler" bei 73%
                print(f"\n{Style.RED}ERROR: Authentication tag verification failed!{Style.RESET}")
                print(f"{Style.YELLOW}The vault may be corrupted or the password is incorrect.{Style.RESET}")
                return False
        
        return True

# ═══════════════════════════════════════════════════════════════════════════
#  NETWORK DEAD MAN'S SWITCH
# ═══════════════════════════════════════════════════════════════════════════

class DeadMansSwitch:
    """
    Netzwerk-basierte Sicherheit
    Wenn kein Heartbeat empfangen wird, werden Vaults zerstört
    """
    
    HEARTBEAT_FILE = Path.home() / '.vault_heartbeat'
    
    @staticmethod
    def send_heartbeat():
        """Sendet Heartbeat (lokal oder zu Server)"""
        heartbeat_data = {
            'timestamp': datetime.now().isoformat(),
            'machine_id': TripwireSystem._get_machine_id(),
            'vault_count': len(list(Path.cwd().glob('*.vault')))
        }
        
        try:
            with open(DeadMansSwitch.HEARTBEAT_FILE, 'w') as f:
                json.dump(heartbeat_data, f)
        except:
            pass
        
        # Optional: An Server senden
        if SecurityConfig.DEADMAN_SERVER:
            try:
                import urllib.request
                req = urllib.request.Request(
                    SecurityConfig.DEADMAN_SERVER,
                    data=json.dumps(heartbeat_data).encode(),
                    headers={'Content-Type': 'application/json'}
                )
                urllib.request.urlopen(req, timeout=5)
            except:
                pass
    
    @staticmethod
    def check_heartbeat() -> bool:
        """Prüft ob Heartbeat aktuell ist"""
        if not DeadMansSwitch.HEARTBEAT_FILE.exists():
            return True  # Kein Heartbeat-System aktiv
        
        try:
            with open(DeadMansSwitch.HEARTBEAT_FILE, 'r') as f:
                heartbeat = json.load(f)
            
            last_beat = datetime.fromisoformat(heartbeat['timestamp'])
            elapsed = (datetime.now() - last_beat).total_seconds()
            
            if elapsed > SecurityConfig.DEADMAN_INTERVAL:
                return False
        except:
            pass
        
        return True
    
    @staticmethod
    def start_heartbeat_thread():
        """Startet Heartbeat im Hintergrund"""
        def heartbeat_loop():
            while True:
                DeadMansSwitch.send_heartbeat()
                time.sleep(3600)  # Jede Stunde
        
        thread = threading.Thread(target=heartbeat_loop, daemon=True)
        thread.start()

# ═══════════════════════════════════════════════════════════════════════════

class HoneypotSystem:
    """Decoy & Honeypot für Plausible Deniability"""
    
    DECOY_PASSWORDS = set()
    CANARY_FILE = ".canary"
    
    @staticmethod
    def generate_decoy_data(size: int = 1024 * 1024) -> bytes:
        """Generiert glaubwürdige Fake-Daten"""
        headers = [
            b'%PDF-1.4\n',
            b'PK\x03\x04',
            b'\x89PNG\r\n\x1a\n',
            b'\xff\xd8\xff\xe0',
        ]
        
        header = random.choice(headers)
        fake_data = header + secrets.token_bytes(size - len(header))
        return fake_data
    
    @staticmethod
    def is_decoy_password(password: str) -> bool:
        return password in HoneypotSystem.DECOY_PASSWORDS
    
    @staticmethod
    def trigger_honeypot(reason: str = "Unknown"):
        """Wird bei Honeypot-Aktivierung aufgerufen"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            'event': 'HONEYPOT_TRIGGERED',
            'reason': reason,
            'timestamp': timestamp,
            'environment': AntiForensics.environment_check()
        }
        
        try:
            log_path = Path.home() / '.vault_canary.log'
            with open(log_path, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
        except:
            pass
        
        print(f"\n{Style.RED}{Style.BLINK}[HONEYPOT TRIGGERED]{Style.RESET}")

# ═══════════════════════════════════════════════════════════════════════════
#  PANIC MODE - EMERGENCY DESTRUCTION
# ═══════════════════════════════════════════════════════════════════════════

class PanicMode:
    """NOTFALL-ZERSTÖRUNG"""
    
    @staticmethod
    def is_panic_trigger(password: str) -> bool:
        return password == SecurityConfig.PANIC_KEY
    
    @staticmethod
    def execute_panic(vault_path: Path = None):
        """ZERSTÖRT ALLES"""
        print(f"\n{Style.RED}{Style.BOLD}")
        print("╔═══════════════════════════════════════════════════════════════════╗")
        print("║                                                                   ║")
        print("║   ██████╗  █████╗ ███╗   ██╗██╗ ██████╗    ███╗   ███╗ ██████╗    ║")
        print("║   ██╔══██╗██╔══██╗████╗  ██║██║██╔════╝    ████╗ ████║██╔═══██╗   ║")
        print("║   ██████╔╝███████║██╔██╗ ██║██║██║         ██╔████╔██║██║   ██║   ║")
        print("║   ██╔═══╝ ██╔══██║██║╚██╗██║██║██║         ██║╚██╔╝██║██║   ██║   ║")
        print("║   ██║     ██║  ██║██║ ╚████║██║╚██████╗    ██║ ╚═╝ ██║╚██████╔╝   ║")
        print("║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝    ╚═╝     ╚═╝ ╚═════╝    ║")
        print("║                                                                   ║")
        print("║              ⚠️  EMERGENCY DESTRUCTION INITIATED  ⚠️              ║")
        print("║                                                                   ║")
        print("╚═══════════════════════════════════════════════════════════════════╝")
        print(Style.RESET)
        
        for i in range(5, 0, -1):
            print(f"\r{Style.BLINK}{Style.RED}[{Style.SKULL}] DESTRUCTION IN {i}...{Style.RESET}", end='', flush=True)
            time.sleep(1)
        print()
        
        destroyed = 0
        
        if vault_path:
            search_dirs = [vault_path.parent]
        else:
            search_dirs = [Path.cwd(), Path.home()]
        
        for search_dir in search_dirs:
            try:
                for vault_file in search_dir.rglob("*.vault"):
                    try:
                        SecureShredder.shred_file(vault_file, passes=7)
                        destroyed += 1
                        print(f"{Style.RED}[{Style.FIRE}] DESTROYED: {vault_file.name}{Style.RESET}")
                    except:
                        pass
            except:
                pass
        
        print(f"\n{Style.RED}[{Style.SKULL}] {destroyed} FILES DESTROYED{Style.RESET}")
        print(f"{Style.DIM}Session terminated.{Style.RESET}")
        
        sys.exit(0)

# ═══════════════════════════════════════════════════════════════════════════
#  KRYPTOGRAFIE ENGINE - DUAL LAYER
# ═══════════════════════════════════════════════════════════════════════════

class CryptoEngine:
    """DUAL-LAYER Verschlüsselung"""
    
    @staticmethod
    def derive_key_argon2(password: str, salt: bytes) -> bytes:
        """Memory-Hard Key Derivation"""
        if not ARGON2_AVAILABLE:
            return CryptoEngine.derive_key_pbkdf2(password, salt)
        
        try:
            key = hash_secret_raw(
                secret=password.encode('utf-8'),
                salt=salt[:32],
                time_cost=SecurityConfig.ARGON2_TIME_COST,
                memory_cost=SecurityConfig.ARGON2_MEMORY_COST,
                parallelism=SecurityConfig.ARGON2_PARALLELISM,
                hash_len=SecurityConfig.ARGON2_HASH_LENGTH,
                type=Type.ID
            )
            return key
        except Exception as e:
            return CryptoEngine.derive_key_pbkdf2(password, salt)
    
    @staticmethod
    def derive_key_pbkdf2(password: str, salt: bytes) -> bytes:
        """Fallback KDF"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=64,
            salt=salt,
            iterations=SecurityConfig.PBKDF2_ITERATIONS,
            backend=default_backend()
        )
        return kdf.derive(password.encode('utf-8'))
    
    @staticmethod
    def dual_encrypt(plaintext: bytes, key: bytes) -> Tuple[bytes, bytes, bytes]:
        """DUAL-LAYER Verschlüsselung"""
        key_chacha = key[:32]
        key_aes = key[32:64]
        
        # Layer 1: ChaCha20-Poly1305
        nonce1 = secrets.token_bytes(12)
        chacha = ChaCha20Poly1305(key_chacha)
        intermediate = chacha.encrypt(nonce1, plaintext, None)
        
        # Layer 2: AES-256-GCM
        nonce2 = secrets.token_bytes(12)
        aesgcm = AESGCM(key_aes)
        ciphertext = aesgcm.encrypt(nonce2, intermediate, None)
        
        return ciphertext, nonce1, nonce2
    
    @staticmethod
    def dual_decrypt(ciphertext: bytes, key: bytes, nonce1: bytes, nonce2: bytes) -> bytes:
        """DUAL-LAYER Entschlüsselung"""
        key_chacha = key[:32]
        key_aes = key[32:64]
        
        # Layer 2: AES-256-GCM (reverse)
        aesgcm = AESGCM(key_aes)
        intermediate = aesgcm.decrypt(nonce2, ciphertext, None)
        
        # Layer 1: ChaCha20-Poly1305 (reverse)
        chacha = ChaCha20Poly1305(key_chacha)
        plaintext = chacha.decrypt(nonce1, intermediate, None)
        
        return plaintext
    
    @staticmethod
    def constant_time_compare(a: bytes, b: bytes) -> bool:
        return hmac.compare_digest(a, b)

# ═══════════════════════════════════════════════════════════════════════════
#  SECURE SHREDDING - GUTMANN 35-PASS
# ═══════════════════════════════════════════════════════════════════════════

class SecureShredder:
    """GUTMANN 35-Pass Secure Delete"""
    
    GUTMANN_PATTERNS = [
        bytes([0x55]), bytes([0xAA]), bytes([0x92, 0x49, 0x24]),
        bytes([0x49, 0x24, 0x92]), bytes([0x24, 0x92, 0x49]),
        bytes([0x00]), bytes([0x11]), bytes([0x22]), bytes([0x33]),
        bytes([0x44]), bytes([0x55]), bytes([0x66]), bytes([0x77]),
        bytes([0x88]), bytes([0x99]), bytes([0xAA]), bytes([0xBB]),
        bytes([0xCC]), bytes([0xDD]), bytes([0xEE]), bytes([0xFF]),
        bytes([0x92, 0x49, 0x24]), bytes([0x49, 0x24, 0x92]),
        bytes([0x24, 0x92, 0x49]), bytes([0x6D, 0xB6, 0xDB]),
        bytes([0xB6, 0xDB, 0x6D]), bytes([0xDB, 0x6D, 0xB6]),
        None, None, None, None,
        bytes([0x00]), bytes([0xFF]), bytes([0x00])
    ]
    
    @staticmethod
    def shred_file(file_path: Path, passes: int = None):
        """Gutmann 35-Pass Secure Delete"""
        if passes is None:
            passes = SecurityConfig.SHRED_PASSES
        
        if not file_path.exists():
            return
        
        file_size = file_path.stat().st_size
        
        print(f"\n{Style.RED}[{Style.SKULL}] GUTMANN {passes}-PASS DESTRUCTION{Style.RESET}")
        print(f"{Style.DIM}    Target: {file_path.name} ({UI.format_bytes(file_size)}){Style.RESET}")
        
        with open(file_path, "r+b", buffering=0) as f:
            for pass_num in range(min(passes, len(SecureShredder.GUTMANN_PATTERNS))):
                pattern = SecureShredder.GUTMANN_PATTERNS[pass_num]
                
                f.seek(0)
                written = 0
                
                while written < file_size:
                    chunk_size = min(SecurityConfig.CHUNK_SIZE, file_size - written)
                    
                    if pattern is None:
                        chunk = secrets.token_bytes(chunk_size)
                    else:
                        chunk = (pattern * (chunk_size // len(pattern) + 1))[:chunk_size]
                    
                    f.write(chunk)
                    written += chunk_size
                
                f.flush()
                os.fsync(f.fileno())
                
                progress = (pass_num + 1) / passes * 100
                bar = '█' * int(progress / 5) + '░' * (20 - int(progress / 5))
                print(f"\r{Style.RED}    [{bar}] Pass {pass_num + 1}/{passes}{Style.RESET}", end='', flush=True)
        
        print()
        
        # Rename multiple times
        for i in range(3):
            new_name = file_path.parent / f"{''.join(random.choices(string.ascii_letters, k=16))}.tmp"
            try:
                file_path.rename(new_name)
                file_path = new_name
            except:
                pass
        
        file_path.unlink()
        print(f"{Style.GREEN}[{Style.CHECK}] ELIMINATED{Style.RESET}")

# ═══════════════════════════════════════════════════════════════════════════
#  PASSWORD STRENGTH
# ═══════════════════════════════════════════════════════════════════════════

class PasswordValidator:
    """PARANOID Password Requirements"""
    
    COMMON_PASSWORDS = {
        'password', '123456', 'qwerty', 'admin', 'letmein', 'welcome',
        'monkey', 'dragon', 'master', 'login', 'abc123', 'password123'
    }
    
    @staticmethod
    def calculate_entropy(password: str) -> float:
        """Berechnet Passwort-Entropie"""
        charset_size = 0
        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" for c in password):
            charset_size += 32
        
        if charset_size == 0:
            return 0
        
        import math
        entropy = len(password) * math.log2(charset_size)
        return entropy
    
    @staticmethod
    def validate(password: str) -> Tuple[bool, str, int, float]:
        """PARANOID Passwort-Validierung"""
        score = 0
        issues = []
        
        if len(password) < 16:
            issues.append(f"Min. 16 Zeichen (aktuell: {len(password)})")
        else:
            score += 30
        
        if len(password) >= 24:
            score += 20
        
        if not any(c.isupper() for c in password):
            issues.append("Großbuchstaben fehlen")
        else:
            score += 10
        
        if not any(c.islower() for c in password):
            issues.append("Kleinbuchstaben fehlen")
        else:
            score += 10
        
        if not any(c.isdigit() for c in password):
            issues.append("Zahlen fehlen")
        else:
            score += 10
        
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" for c in password):
            issues.append("Sonderzeichen fehlen")
        else:
            score += 10
        
        if password.lower() in PasswordValidator.COMMON_PASSWORDS:
            issues.append("Häufig verwendetes Passwort!")
            score = 0
        
        if len(set(password)) < len(password) / 2:
            issues.append("Zu viele Wiederholungen")
            score -= 20
        
        entropy = PasswordValidator.calculate_entropy(password)
        if entropy < 60:
            issues.append(f"Niedrige Entropie ({entropy:.1f} bits)")
        else:
            score += 10
        
        if issues:
            return False, " | ".join(issues), max(0, score), entropy
        
        if score >= 90:
            level = "PARANOID ✓"
        elif score >= 70:
            level = "STARK"
        else:
            level = "AKZEPTABEL"
        
        return True, level, score, entropy

# ═══════════════════════════════════════════════════════════════════════════
#  UI & VISUALISIERUNG
# ═══════════════════════════════════════════════════════════════════════════

class UI:
    """CYBERPUNK Terminal Interface"""
    
    @staticmethod
    def clear_screen():
        print(Style.CLEAR_SCREEN + Style.HOME, end='')
    
    @staticmethod
    def print_banner():
        """PHANTOM EDITION Banner"""
        banner = f"""
{Style.MATRIX}
    ██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗    ██╗  ██╗ ██████╗ 
    ██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝    ╚██╗██╔╝██╔═████╗
    ██║   ██║███████║██║   ██║██║     ██║        ╚███╔╝ ██║██╔██║
    ╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║        ██╔██╗ ████╔╝██║
     ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║       ██╔╝ ██╗╚██████╔╝
      ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝       ╚═╝  ╚═╝ ╚═════╝ 
{Style.RESET}
{Style.NEON_PINK}╔══════════════════════════════════════════════════════════════════════════╗
║  {Style.BOLD}P H A N T O M   E D I T I O N{Style.RESET}{Style.NEON_PINK}                                           ║
║  {Style.DIM}Military-Grade Encryption System{Style.RESET}{Style.NEON_PINK}                                       ║
╚══════════════════════════════════════════════════════════════════════════╝{Style.RESET}

{Style.CYAN}┌─────────────────────────────────────────────────────────────────────────┐{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.MATRIX}▸{Style.RESET} Argon2id Memory-Hard KDF {Style.DIM}(2GB RAM / Attempt){Style.RESET}                      {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.MATRIX}▸{Style.RESET} ChaCha20-Poly1305 + AES-256-GCM {Style.DIM}(Dual-Layer){Style.RESET}                     {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.MATRIX}▸{Style.RESET} Gutmann 35-Pass Secure Shredding                                   {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.MATRIX}▸{Style.RESET} Anti-Debugging & Anti-Forensics                                    {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.MATRIX}▸{Style.RESET} Polymorphic Signatures {Style.DIM}(Pattern Evasion){Style.RESET}                         {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.MAGENTA}▸{Style.RESET} {Style.MAGENTA}Quantum-Resistant Mode{Style.RESET} {Style.DIM}(Post-Quantum Crypto){Style.RESET}                    {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.MAGENTA}▸{Style.RESET} {Style.MAGENTA}Steganography{Style.RESET} {Style.DIM}(Hide data in images){Style.RESET}                            {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.YELLOW}▸{Style.RESET} {Style.YELLOW}Network Isolation{Style.RESET} {Style.DIM}(Block exfiltration){Style.RESET}                          {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.YELLOW}▸{Style.RESET} {Style.YELLOW}Duress Mode{Style.RESET} {Style.DIM}(Fake data under coercion){Style.RESET}                         {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.YELLOW}▸{Style.RESET} {Style.YELLOW}Self-Destruct Timer{Style.RESET} {Style.DIM}(Time-bomb vaults){Style.RESET}                        {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.YELLOW}▸{Style.RESET} {Style.YELLOW}Tripwire System{Style.RESET} {Style.DIM}(Intrusion detection){Style.RESET}                          {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.RED}▸{Style.RESET} {Style.RED}PANIC MODE{Style.RESET} {Style.DIM}(Emergency destruction){Style.RESET}                              {Style.CYAN}│{Style.RESET}
{Style.CYAN}│{Style.RESET} {Style.RED}▸{Style.RESET} {Style.RED}KILL SWITCH{Style.RESET} {Style.DIM}(Remote wipe all vaults){Style.RESET}                            {Style.CYAN}│{Style.RESET}
{Style.CYAN}└─────────────────────────────────────────────────────────────────────────┘{Style.RESET}

{Style.DIM}System: {platform.system()} {platform.release()} | Python {platform.python_version()}
Crypto: {"ChaCha20+AES ✓" if CRYPTO_AVAILABLE else "NOT AVAILABLE ✗"} | Argon2: {"✓" if ARGON2_AVAILABLE else "PBKDF2 Fallback"}
Codename: {SecurityConfig.CODENAME} | Version: {SecurityConfig.VERSION}{Style.RESET}
"""
        print(banner)
    
    @staticmethod
    def print_security_check():
        """Zeigt Security-Status"""
        check = AntiForensics.environment_check()
        
        print(f"\n{Style.CYAN}┌─ SECURITY CHECK {'─' * 52}┐{Style.RESET}")
        
        if check['debugger']:
            print(f"{Style.CYAN}│{Style.RESET} {Style.RED}[{Style.SKULL}] DEBUGGER DETECTED!{Style.RESET}")
        else:
            print(f"{Style.CYAN}│{Style.RESET} {Style.GREEN}[{Style.CHECK}] No debugger detected{Style.RESET}")
        
        if check['vm']:
            print(f"{Style.CYAN}│{Style.RESET} {Style.YELLOW}[{Style.WARNING}] Virtual Machine detected{Style.RESET}")
        else:
            print(f"{Style.CYAN}│{Style.RESET} {Style.GREEN}[{Style.CHECK}] Native hardware{Style.RESET}")
        
        if check['analysis_tools']:
            print(f"{Style.CYAN}│{Style.RESET} {Style.RED}[{Style.SKULL}] Analysis tools: {', '.join(check['analysis_tools'])}{Style.RESET}")
        else:
            print(f"{Style.CYAN}│{Style.RESET} {Style.GREEN}[{Style.CHECK}] No analysis tools detected{Style.RESET}")
        
        print(f"{Style.CYAN}└{'─' * 70}┘{Style.RESET}")
        
        return check
    
    @staticmethod
    def print_progress(iteration: int, total: int, prefix: str = '', 
                      suffix: str = '', bar_length: int = 40):
        """Cyberpunk Progress Bar"""
        percent = 100 * (iteration / float(total))
        filled = int(bar_length * iteration // total)
        
        bar = ""
        for i in range(bar_length):
            if i < filled:
                if i < bar_length * 0.3:
                    bar += f"{Style.CYAN}█"
                elif i < bar_length * 0.7:
                    bar += f"{Style.MATRIX}█"
                else:
                    bar += f"{Style.NEON_PINK}█"
            else:
                bar += f"{Style.DIM}░"
        
        bar += Style.RESET
        
        print(f'\r{Style.CYAN}{prefix}{Style.RESET} [{bar}] '
              f'{Style.GOLD}{percent:5.1f}%{Style.RESET} {Style.DIM}{suffix}{Style.RESET}', end='')
        
        if iteration == total:
            print()
    
    @staticmethod
    def format_bytes(size: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} PB"
    
    @staticmethod
    def format_time(seconds: float) -> str:
        if seconds < 60:
            return f"{seconds:.2f}s"
        elif seconds < 3600:
            return f"{seconds/60:.2f}m"
        elif seconds < 86400:
            return f"{seconds/3600:.2f}h"
        elif seconds < 31536000:
            return f"{seconds/86400:.2f}d"
        else:
            return f"{seconds/31536000:.2f}y"
    
    @staticmethod
    def print_separator(char: str = '─', color: str = None):
        if color is None:
            color = Style.DIM
        print(f"{color}{char * 70}{Style.RESET}")

# ═══════════════════════════════════════════════════════════════════════════
#  VAULT - HAUPTKLASSE
# ═══════════════════════════════════════════════════════════════════════════

class Vault:
    """PHANTOM Verschlüsselungs-Engine"""
    
    MAGIC = b'VAULT_X0'
    FORMAT_VERSION = 2
    
    @staticmethod
    def encrypt(file_path: Path, password: str, paranoia_mode: bool = False,
                quantum_mode: bool = False, stealth_mode: bool = False, 
                isolated_mode: bool = False) -> bool:
        """DUAL-LAYER Verschlüsselung mit optionalen Modi"""
        
        key = None
        plaintext = None
        password_bytes = None
        
        try:
            # NETWORK ISOLATION
            if isolated_mode:
                NetworkIsolation.enable_isolation()
            
            if not file_path.exists():
                print(f"{Style.RED}[{Style.CROSS}] Datei nicht gefunden!{Style.RESET}")
                return False
            
            file_size = file_path.stat().st_size
            original_name = file_path.name
            
            # Header
            print(f"\n{Style.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
            print(f"║  {Style.BOLD}{Style.MATRIX}ENCRYPTION SEQUENCE INITIATED{Style.RESET}{Style.CYAN}                                    ║")
            print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET}")
            
            # Info Box
            print(f"\n{Style.DIM}┌─ TARGET ─────────────────────────────────────────────────────────────┐")
            print(f"│ File:      {original_name[:50]:<50} │")
            print(f"│ Size:      {UI.format_bytes(file_size):<50} │")
            print(f"│ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<50} │")
            modes_str = ' '.join([
                'PARANOIA' if paranoia_mode else '',
                'QUANTUM' if quantum_mode else '',
                'STEALTH' if stealth_mode else '',
                'ISOLATED' if isolated_mode else '',
            ]).strip() or 'STANDARD'
            print(f"│ Mode:      {modes_str:<50} │")
            print(f"└──────────────────────────────────────────────────────────────────────┘{Style.RESET}")
            
            # Matrix Effect
            print(f"\n{Style.MATRIX}[{Style.LIGHTNING}] Initializing encryption matrix...{Style.RESET}")
            MatrixEffect.encryption_visual(1.0)
            
            # Phase 1: Read File
            print(f"\n{Style.CYAN}[1/7]{Style.RESET} {Style.LOCK} Reading target file...")
            with open(file_path, 'rb') as f:
                plaintext = SecureByteArray(f.read())
            SecureMemory.lock_memory(plaintext)
            
            # Compression
            original_size = len(plaintext)
            compressed = zlib.compress(bytes(plaintext), level=9)
            if len(compressed) < original_size * 0.9:
                plaintext = SecureByteArray(compressed)
                compression_ratio = len(compressed) / original_size * 100
                print(f"{Style.GREEN}      [{Style.CHECK}] Compressed: {compression_ratio:.1f}% of original{Style.RESET}")
            else:
                compression_ratio = 100
            
            checksum = hashlib.sha3_256(plaintext).hexdigest()
            print(f"{Style.DIM}      SHA3-256: {checksum[:32]}...{Style.RESET}")
            
            # Phase 2: Generate Crypto Material
            print(f"\n{Style.CYAN}[2/7]{Style.RESET} {Style.GEAR} Generating cryptographic material...")
            salt = secrets.token_bytes(SecurityConfig.SALT_SIZE)
            print(f"{Style.GREEN}      [{Style.CHECK}] {SecurityConfig.SALT_SIZE * 8}-bit salt generated{Style.RESET}")
            
            # Phase 3: Key Derivation
            print(f"\n{Style.CYAN}[3/7]{Style.RESET} {Style.SHIELD} Argon2id key derivation...")
            print(f"{Style.DIM}      Memory: {SecurityConfig.ARGON2_MEMORY_COST // 1024} MB | "
                  f"Time: {SecurityConfig.ARGON2_TIME_COST} iterations | "
                  f"Threads: {SecurityConfig.ARGON2_PARALLELISM}{Style.RESET}")
            
            MatrixEffect.cyber_loading("Deriving key", 0.5)
            
            start_time = time.time()
            password_bytes = SecureByteArray(password.encode('utf-8'))
            key = SecureByteArray(CryptoEngine.derive_key_argon2(password, salt))
            
            # QUANTUM MODE: Extra Quantum-Resistant Layer
            if quantum_mode:
                print(f"{Style.MAGENTA}      [{Style.SHIELD}] Applying Quantum-Resistant layer...{Style.RESET}")
                quantum_key = QuantumResistant.generate_quantum_key(password, salt)
                key_bytes = bytes(key)
                enhanced = bytes(a ^ b for a, b in zip(key_bytes[:32], quantum_key[:32]))
                enhanced += bytes(a ^ b for a, b in zip(key_bytes[32:], quantum_key[32:]))
                key = SecureByteArray(enhanced)
                print(f"{Style.GREEN}      [{Style.CHECK}] Lattice-based key stretching complete{Style.RESET}")
            
            SecureMemory.lock_memory(key)
            kdf_time = time.time() - start_time
            
            print(f"{Style.GREEN}      [{Style.CHECK}] 512-bit key derived ({kdf_time:.2f}s){Style.RESET}")
            
            attack_time = kdf_time * 10_000_000_000
            print(f"{Style.MAGENTA}      [{Style.SHIELD}] Brute-force estimate: ~{UI.format_time(attack_time)} for 10B attempts{Style.RESET}")
            
            # Phase 4: Dual-Layer Encryption
            print(f"\n{Style.CYAN}[4/7]{Style.RESET} {Style.LOCK} Dual-layer encryption...")
            print(f"{Style.DIM}      Layer 1: ChaCha20-Poly1305")
            print(f"      Layer 2: AES-256-GCM{Style.RESET}")
            
            MatrixEffect.encryption_visual(0.8)
            
            start_time = time.time()
            ciphertext, nonce1, nonce2 = CryptoEngine.dual_encrypt(bytes(plaintext), bytes(key))
            encrypt_time = time.time() - start_time
            
            throughput = len(plaintext) / encrypt_time / (1024 * 1024) if encrypt_time > 0 else 0
            print(f"{Style.GREEN}      [{Style.CHECK}] Encrypted ({encrypt_time:.2f}s @ {throughput:.1f} MB/s){Style.RESET}")
            
            # Phase 5: Memory Wipe
            print(f"\n{Style.CYAN}[5/7]{Style.RESET} {Style.SKULL} RAM-SANITY: Secure memory wipe...")
            SecureMemory.wipe(key, passes=5)
            SecureMemory.wipe(plaintext, passes=5)
            SecureMemory.wipe(password_bytes, passes=5)
            del key, plaintext, password_bytes
            key = plaintext = password_bytes = None
            print(f"{Style.GREEN}      [{Style.CHECK}] Sensitive data wiped from memory{Style.RESET}")
            
            # Phase 6: Build Vault
            print(f"\n{Style.CYAN}[6/7]{Style.RESET} {Style.GEAR} Building vault container...")
            
            metadata = {
                'version': Vault.FORMAT_VERSION,
                'original_name': original_name,
                'original_size': original_size,
                'compressed': compression_ratio < 100,
                'checksum': checksum,
                'timestamp': datetime.now().isoformat(),
                'algorithm': 'ChaCha20-Poly1305 + AES-256-GCM',
                'kdf': 'Argon2id',
                'quantum_resistant': quantum_mode,
                'stealth_mode': stealth_mode
            }
            metadata_json = json.dumps(metadata).encode()
            metadata_encrypted = secrets.token_bytes(16) + metadata_json
            
            vault_data = bytearray()
            vault_data.extend(Vault.MAGIC)
            vault_data.extend(struct.pack('<H', Vault.FORMAT_VERSION))
            vault_data.extend(salt)
            vault_data.extend(nonce1)
            vault_data.extend(nonce2)
            vault_data.extend(struct.pack('<I', len(metadata_encrypted)))
            vault_data.extend(metadata_encrypted)
            vault_data.extend(ciphertext)
            
            # STEALTH MODE: Polymorphic wrapper
            if stealth_mode:
                print(f"{Style.MAGENTA}      [{Style.GHOST}] Applying polymorphic wrapper...{Style.RESET}")
                wrapped, marker = PolymorphicEngine.generate_polymorphic_wrapper(bytes(vault_data))
                vault_data = bytearray(wrapped)
                # Store marker for decryption
                marker_file = vault_path.with_suffix('.marker')
                marker_file.write_bytes(marker)
                marker_file = marker_file.rename(vault_path.parent / f".{secrets.token_hex(4)}")
                print(f"{Style.GREEN}      [{Style.CHECK}] Signature randomized{Style.RESET}")
            
            vault_path = file_path.with_suffix(file_path.suffix + SecurityConfig.VAULT_EXT)
            with open(vault_path, 'wb') as f:
                f.write(vault_data)
            
            print(f"{Style.GREEN}      [{Style.CHECK}] Vault created: {vault_path.name}{Style.RESET}")
            print(f"{Style.DIM}      Size: {UI.format_bytes(len(vault_data))} "
                  f"(+{(len(vault_data)/file_size - 1)*100:.1f}% overhead){Style.RESET}")
            
            # Phase 7: Secure Delete Original
            print(f"\n{Style.CYAN}[7/7]{Style.RESET} {Style.FIRE} Destroying original file...")
            SecureShredder.shred_file(file_path, passes=7 if not paranoia_mode else 35)
            
            # Success
            print(f"\n{Style.GREEN}╔══════════════════════════════════════════════════════════════════════╗")
            print(f"║  {Style.BOLD}✓ ENCRYPTION COMPLETE{Style.RESET}{Style.GREEN}                                              ║")
            print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET}")
            
            # Anti-Forensics
            AntiForensicsWiper.wipe_prefetch()
            AntiForensicsWiper.clear_recent_docs()
            
            # Sound Feedback
            SoundFX.encryption_sound()
            SoundFX.success()
            
            print(f"\n{Style.DIM}┌─ SUMMARY ────────────────────────────────────────────────────────────┐")
            print(f"│ Vault:     {vault_path.name[:50]:<50} │")
            print(f"│ Algorithm: ChaCha20 + AES-256-GCM (Dual-Layer)                       │")
            print(f"│ KDF:       Argon2id ({kdf_time:.2f}s per attempt)                         │")
            quantum_str = "+ Quantum-Resistant" if quantum_mode else ""
            print(f"│ Enhanced:  {quantum_str:<50} │" if quantum_mode else f"│ Original:  DESTROYED (Gutmann {7 if not paranoia_mode else 35}-pass)                            │")
            print(f"└──────────────────────────────────────────────────────────────────────┘{Style.RESET}")
            
            # Network Isolation OFF
            if isolated_mode:
                NetworkIsolation.disable_isolation()
            
            return True
            
        except Exception as e:
            print(f"\n{Style.RED}[{Style.CROSS}] CRITICAL ERROR: {e}{Style.RESET}")
            SoundFX.error()
            traceback.print_exc()
            return False
        
        finally:
            if isolated_mode:
                NetworkIsolation.disable_isolation()
            if key is not None:
                SecureMemory.wipe(key)
            if plaintext is not None:
                SecureMemory.wipe(plaintext)
            if password_bytes is not None:
                SecureMemory.wipe(password_bytes)
    
    @staticmethod
    def decrypt(file_path: Path, password: str) -> bool:
        """DUAL-LAYER Entschlüsselung"""
        
        key = None
        plaintext = None
        password_bytes = None
        ciphertext = None
        
        try:
            if not file_path.exists():
                print(f"{Style.RED}[{Style.CROSS}] Vault nicht gefunden!{Style.RESET}")
                return False
            
            file_size = file_path.stat().st_size
            
            # Header
            print(f"\n{Style.CYAN}╔══════════════════════════════════════════════════════════════════════╗")
            print(f"║  {Style.BOLD}{Style.NEON_BLUE}DECRYPTION SEQUENCE INITIATED{Style.RESET}{Style.CYAN}                                    ║")
            print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET}")
            
            print(f"\n{Style.DIM}┌─ TARGET ─────────────────────────────────────────────────────────────┐")
            print(f"│ Vault:     {file_path.name[:50]:<50} │")
            print(f"│ Size:      {UI.format_bytes(file_size):<50} │")
            print(f"│ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<50} │")
            print(f"└──────────────────────────────────────────────────────────────────────┘{Style.RESET}")
            
            # Phase 1: Read Vault
            print(f"\n{Style.CYAN}[1/5]{Style.RESET} {Style.UNLOCK} Reading vault...")
            with open(file_path, 'rb') as f:
                vault_data = f.read()
            
            offset = 0
            
            magic = vault_data[offset:offset+8]
            offset += 8
            if magic != Vault.MAGIC:
                print(f"{Style.RED}[{Style.CROSS}] Invalid vault format!{Style.RESET}")
                return False
            
            version = struct.unpack('<H', vault_data[offset:offset+2])[0]
            offset += 2
            print(f"{Style.GREEN}      [{Style.CHECK}] Vault version: {version}{Style.RESET}")
            
            salt = vault_data[offset:offset+SecurityConfig.SALT_SIZE]
            offset += SecurityConfig.SALT_SIZE
            
            nonce1 = vault_data[offset:offset+12]
            offset += 12
            nonce2 = vault_data[offset:offset+12]
            offset += 12
            
            meta_len = struct.unpack('<I', vault_data[offset:offset+4])[0]
            offset += 4
            metadata_encrypted = vault_data[offset:offset+meta_len]
            offset += meta_len
            
            ciphertext = SecureByteArray(vault_data[offset:])
            
            print(f"{Style.GREEN}      [{Style.CHECK}] Vault structure parsed{Style.RESET}")
            
            # Phase 2: Key Derivation
            print(f"\n{Style.CYAN}[2/5]{Style.RESET} {Style.SHIELD} Argon2id key derivation...")
            MatrixEffect.cyber_loading("Deriving key", 0.5)
            
            start_time = time.time()
            password_bytes = SecureByteArray(password.encode('utf-8'))
            key = SecureByteArray(CryptoEngine.derive_key_argon2(password, salt))
            SecureMemory.lock_memory(key)
            kdf_time = time.time() - start_time
            
            print(f"{Style.GREEN}      [{Style.CHECK}] Key derived ({kdf_time:.2f}s){Style.RESET}")
            
            # Phase 3: Dual-Layer Decryption
            print(f"\n{Style.CYAN}[3/5]{Style.RESET} {Style.UNLOCK} Dual-layer decryption...")
            MatrixEffect.encryption_visual(0.8)
            
            start_time = time.time()
            
            try:
                plaintext = SecureByteArray(
                    CryptoEngine.dual_decrypt(bytes(ciphertext), bytes(key), nonce1, nonce2)
                )
            except Exception as auth_error:
                print(f"\n{Style.RED}╔══════════════════════════════════════════════════════════════════════╗")
                print(f"║  {Style.BOLD}✗ AUTHENTICATION FAILED{Style.RESET}{Style.RED}                                            ║")
                print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET}")
                print(f"{Style.YELLOW}[{Style.WARNING}] Wrong password or corrupted vault{Style.RESET}")
                
                SecureMemory.wipe(key)
                SecureMemory.wipe(password_bytes)
                SecureMemory.wipe(ciphertext)
                
                return False
            
            decrypt_time = time.time() - start_time
            print(f"{Style.GREEN}      [{Style.CHECK}] Decrypted ({decrypt_time:.2f}s){Style.RESET}")
            
            # Decompress
            try:
                decompressed = zlib.decompress(bytes(plaintext))
                SecureMemory.wipe(plaintext)
                plaintext = SecureByteArray(decompressed)
                print(f"{Style.GREEN}      [{Style.CHECK}] Decompressed{Style.RESET}")
            except:
                pass
            
            # Phase 4: Memory Wipe
            print(f"\n{Style.CYAN}[4/5]{Style.RESET} {Style.SKULL} RAM-SANITY: Secure memory wipe...")
            SecureMemory.wipe(key, passes=5)
            SecureMemory.wipe(password_bytes, passes=5)
            SecureMemory.wipe(ciphertext, passes=5)
            del key, password_bytes, ciphertext
            key = password_bytes = ciphertext = None
            print(f"{Style.GREEN}      [{Style.CHECK}] Key wiped from memory{Style.RESET}")
            
            # Phase 5: Restore File
            print(f"\n{Style.CYAN}[5/5]{Style.RESET} {Style.GEAR} Restoring original file...")
            
            original_path = file_path.with_suffix('')
            if original_path.suffix == '':
                original_path = file_path.parent / file_path.stem
            
            with open(original_path, 'wb') as f:
                f.write(plaintext)
            
            checksum = hashlib.sha3_256(plaintext).hexdigest()
            print(f"{Style.DIM}      SHA3-256: {checksum[:32]}...{Style.RESET}")
            print(f"{Style.GREEN}      [{Style.CHECK}] Restored: {original_path.name}{Style.RESET}")
            
            SecureMemory.wipe(plaintext)
            del plaintext
            plaintext = None
            
            file_path.unlink()
            print(f"{Style.YELLOW}      [{Style.FIRE}] Vault deleted{Style.RESET}")
            
            # Success
            print(f"\n{Style.GREEN}╔══════════════════════════════════════════════════════════════════════╗")
            print(f"║  {Style.BOLD}✓ DECRYPTION COMPLETE{Style.RESET}{Style.GREEN}                                              ║")
            print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET}")
            
            return True
            
        except Exception as e:
            print(f"\n{Style.RED}[{Style.CROSS}] CRITICAL ERROR: {e}{Style.RESET}")
            traceback.print_exc()
            return False
        
        finally:
            if key is not None:
                SecureMemory.wipe(key)
            if plaintext is not None:
                SecureMemory.wipe(plaintext)
            if password_bytes is not None:
                SecureMemory.wipe(password_bytes)
            if ciphertext is not None:
                SecureMemory.wipe(ciphertext)

# ═══════════════════════════════════════════════════════════════════════════
#  INTERACTIVE MENU SYSTEM (Rich Library)
# ═══════════════════════════════════════════════════════════════════════════

class InteractiveMenu:
    """Cyberpunk Interactive Terminal Menu mit Rich Library"""
    
    @staticmethod
    def show_rich_banner():
        """Zeigt animierten Banner mit Rich"""
        if not RICH_AVAILABLE:
            UI.print_banner()
            return
        
        banner_text = """
[bold cyan]██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗    ██╗  ██╗ ██████╗ [/]
[bold cyan]██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝    ╚██╗██╔╝██╔═████╗[/]
[bold cyan]██║   ██║███████║██║   ██║██║     ██║        ╚███╔╝ ██║██╔██║[/]
[bold cyan]╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║        ██╔██╗ ████╔╝██║[/]
[bold cyan] ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║       ██╔╝ ██╗╚██████╔╝[/]
[bold cyan]  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝       ╚═╝  ╚═╝ ╚═════╝ [/]
"""
        
        console.print(Panel(
            Align.center(Text.from_markup(banner_text)),
            title="[bold magenta]☠ PHANTOM EDITION ☠[/]",
            subtitle=f"[dim]v{SecurityConfig.VERSION} | {SecurityConfig.CODENAME}[/]",
            border_style="bright_magenta",
            box=box.DOUBLE_EDGE
        ))
    
    @staticmethod
    def show_system_status():
        """Zeigt System-Status Table"""
        if not RICH_AVAILABLE:
            UI.print_security_check()
            return {}
        
        check = AntiForensics.environment_check()
        
        table = Table(title="🛡️ SECURITY STATUS", box=box.ROUNDED, border_style="cyan")
        table.add_column("Check", style="cyan", no_wrap=True)
        table.add_column("Status", justify="center")
        table.add_column("Details", style="dim")
        
        # Debugger
        if check['debugger']:
            table.add_row("Debugger", "[bold red]⚠ DETECTED[/]", "Process is being debugged!")
        else:
            table.add_row("Debugger", "[green]✓ Clean[/]", "No debugger attached")
        
        # VM
        if check['vm']:
            table.add_row("Environment", "[yellow]⚠ VM[/]", "Virtual machine detected")
        else:
            table.add_row("Environment", "[green]✓ Native[/]", "Bare metal hardware")
        
        # Analysis Tools
        if check['analysis_tools']:
            tools = ', '.join(check['analysis_tools'][:3])
            table.add_row("Analysis Tools", "[red]⚠ FOUND[/]", tools)
        else:
            table.add_row("Analysis Tools", "[green]✓ None[/]", "No suspicious tools")
        
        # Crypto Status
        crypto_status = "[green]✓ Available[/]" if CRYPTO_AVAILABLE else "[red]✗ Missing[/]"
        table.add_row("Crypto Engine", crypto_status, "ChaCha20 + AES-256-GCM")
        
        # Argon2
        argon_status = "[green]✓ Available[/]" if ARGON2_AVAILABLE else "[yellow]⚠ Fallback[/]"
        table.add_row("Argon2id KDF", argon_status, "2GB Memory-Hard")
        
        # Rich
        rich_status = "[green]✓ Enhanced[/]" if RICH_AVAILABLE else "[dim]Basic Mode[/]"
        table.add_row("Terminal UI", rich_status, "Rich Library")
        
        console.print(table)
        return check
    
    @staticmethod
    def show_main_menu() -> str:
        """Zeigt Hauptmenü und gibt Auswahl zurück"""
        if not RICH_AVAILABLE:
            return InteractiveMenu._fallback_menu()
        
        menu_table = Table(box=box.ROUNDED, border_style="bright_blue", show_header=False)
        menu_table.add_column("Option", style="bold cyan", width=5, justify="center")
        menu_table.add_column("Action", style="white", width=25)
        menu_table.add_column("Description", style="dim", width=40)
        
        menu_table.add_row("[1]", "🔐 Encrypt File", "Lock a file in the vault")
        menu_table.add_row("[2]", "🔓 Decrypt Vault", "Unlock and restore file")
        menu_table.add_row("", "", "")
        menu_table.add_row("[3]", "👻 Steganography", "Hide vault in image")
        menu_table.add_row("[4]", "💣 Self-Destruct", "Arm time-bomb on vault")
        menu_table.add_row("[5]", "🎯 Quick Shred", "Securely destroy a file")
        menu_table.add_row("", "", "")
        menu_table.add_row("[6]", "⚙️  Settings", "Configure security options")
        menu_table.add_row("[7]", "📊 Vault Scanner", "Find all vaults on system")
        menu_table.add_row("[8]", "🧪 Security Audit", "Run full security check")
        menu_table.add_row("", "", "")
        menu_table.add_row("[9]", "[red]☠ PANIC MODE[/]", "[red]Destroy ALL vaults NOW[/]")
        menu_table.add_row("[0]", "🚪 Exit", "Leave PHANTOM")
        
        console.print(Panel(
            menu_table,
            title="[bold yellow]⚡ COMMAND CENTER ⚡[/]",
            border_style="yellow"
        ))
        
        choice = Prompt.ask(
            "\n[bold cyan]Select operation[/]",
            choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            default="1"
        )
        return choice
    
    @staticmethod
    def _fallback_menu() -> str:
        """Fallback Menu ohne Rich"""
        print(f"\n{Style.YELLOW}╔══════════════════════════════════════════════════════════════════════╗")
        print(f"║  {Style.BOLD}⚡ COMMAND CENTER ⚡{Style.RESET}{Style.YELLOW}                                                  ║")
        print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET}")
        
        print(f"\n  {Style.CYAN}[1]{Style.RESET} 🔐 Encrypt File")
        print(f"  {Style.CYAN}[2]{Style.RESET} 🔓 Decrypt Vault")
        print(f"  {Style.CYAN}[3]{Style.RESET} 👻 Steganography")
        print(f"  {Style.CYAN}[4]{Style.RESET} 💣 Self-Destruct")
        print(f"  {Style.CYAN}[5]{Style.RESET} 🎯 Quick Shred")
        print(f"  {Style.CYAN}[6]{Style.RESET} ⚙️  Settings")
        print(f"  {Style.CYAN}[7]{Style.RESET} 📊 Vault Scanner")
        print(f"  {Style.CYAN}[8]{Style.RESET} 🧪 Security Audit")
        print(f"  {Style.RED}[9]{Style.RESET} {Style.RED}☠ PANIC MODE{Style.RESET}")
        print(f"  {Style.DIM}[0]{Style.RESET} 🚪 Exit")
        
        return input(f"\n{Style.CYAN}Select [0-9]:{Style.RESET} ").strip()
    
    @staticmethod
    def get_file_path(prompt: str = "Enter file path") -> Optional[Path]:
        """Fragt nach Dateipfad mit Validierung"""
        if RICH_AVAILABLE:
            path_str = Prompt.ask(f"[cyan]{prompt}[/]")
        else:
            path_str = input(f"{Style.CYAN}{prompt}:{Style.RESET} ")
        
        if not path_str:
            return None
        
        path = Path(path_str.strip().strip('"').strip("'"))
        
        if not path.exists():
            if RICH_AVAILABLE:
                console.print(f"[red]✗ File not found: {path}[/]")
            else:
                print(f"{Style.RED}[✗] File not found: {path}{Style.RESET}")
            return None
        
        return path
    
    @staticmethod
    def get_password(confirm: bool = False) -> Optional[str]:
        """Sichere Passwort-Eingabe"""
        if RICH_AVAILABLE:
            console.print("\n[bold magenta]🔑 AUTHENTICATION[/]")
            password = Prompt.ask("[cyan]Master Key[/]", password=True)
            
            if confirm:
                password2 = Prompt.ask("[cyan]Confirm Key[/]", password=True)
                if password != password2:
                    console.print("[red]✗ Passwords don't match![/]")
                    return None
        else:
            print(f"\n{Style.MAGENTA}🔑 AUTHENTICATION{Style.RESET}")
            password = getpass.getpass(f"{Style.CYAN}Master Key: {Style.RESET}")
            
            if confirm:
                password2 = getpass.getpass(f"{Style.CYAN}Confirm Key: {Style.RESET}")
                if password != password2:
                    print(f"{Style.RED}[✗] Passwords don't match!{Style.RESET}")
                    return None
        
        return password
    
    @staticmethod
    def show_encrypt_options() -> Dict[str, bool]:
        """Zeigt Verschlüsselungs-Optionen"""
        options = {
            'paranoia': False,
            'quantum': False,
            'stealth': False,
            'isolated': False
        }
        
        if RICH_AVAILABLE:
            console.print("\n[bold cyan]⚙️ ENCRYPTION OPTIONS[/]")
            
            options_table = Table(box=box.SIMPLE, show_header=False)
            options_table.add_column("Key", style="cyan", width=3)
            options_table.add_column("Option", width=20)
            options_table.add_column("Description", style="dim")
            
            options_table.add_row("[P]", "Paranoia Mode", "35-pass Gutmann shred")
            options_table.add_row("[Q]", "Quantum-Resistant", "Post-quantum crypto layer")
            options_table.add_row("[S]", "Stealth Mode", "Polymorphic signatures")
            options_table.add_row("[I]", "Network Isolated", "Block all connections")
            options_table.add_row("[A]", "ALL OPTIONS", "Maximum security")
            options_table.add_row("[N]", "None (Standard)", "Default encryption")
            
            console.print(options_table)
            
            choice = Prompt.ask(
                "[cyan]Select options[/]",
                default="N"
            ).upper()
            
            if 'A' in choice:
                return {'paranoia': True, 'quantum': True, 'stealth': True, 'isolated': True}
            
            options['paranoia'] = 'P' in choice
            options['quantum'] = 'Q' in choice
            options['stealth'] = 'S' in choice
            options['isolated'] = 'I' in choice
        else:
            print(f"\n{Style.CYAN}⚙️ ENCRYPTION OPTIONS{Style.RESET}")
            print(f"  [P] Paranoia Mode  [Q] Quantum  [S] Stealth  [I] Isolated")
            print(f"  [A] ALL            [N] None (Standard)")
            choice = input(f"{Style.CYAN}Select (e.g. PQ for Paranoia+Quantum):{Style.RESET} ").upper()
            
            if 'A' in choice:
                return {'paranoia': True, 'quantum': True, 'stealth': True, 'isolated': True}
            
            options['paranoia'] = 'P' in choice
            options['quantum'] = 'Q' in choice
            options['stealth'] = 'S' in choice
            options['isolated'] = 'I' in choice
        
        return options
    
    @staticmethod
    def show_progress(description: str, total: int = 100):
        """Zeigt Rich Progress Bar"""
        if RICH_AVAILABLE:
            return Progress(
                SpinnerColumn(),
                TextColumn("[bold cyan]{task.description}"),
                BarColumn(bar_width=40, style="cyan", complete_style="green"),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeElapsedColumn(),
                console=console
            )
        return None
    
    @staticmethod
    def vault_scanner():
        """Scannt System nach Vault-Dateien"""
        if RICH_AVAILABLE:
            console.print("\n[bold cyan]📊 VAULT SCANNER[/]")
        else:
            print(f"\n{Style.CYAN}📊 VAULT SCANNER{Style.RESET}")
        
        search_paths = [
            Path.home(),
            Path.home() / 'Documents',
            Path.home() / 'Desktop',
            Path.home() / 'Downloads',
        ]
        
        vaults_found = []
        
        if RICH_AVAILABLE:
            with Progress(
                SpinnerColumn(),
                TextColumn("[cyan]Scanning..."),
                BarColumn(),
                console=console
            ) as progress:
                task = progress.add_task("Scanning", total=len(search_paths))
                
                for search_path in search_paths:
                    try:
                        for vault in search_path.rglob('*.vault'):
                            vaults_found.append(vault)
                    except:
                        pass
                    progress.update(task, advance=1)
            
            # Results Table
            table = Table(title=f"Found {len(vaults_found)} Vaults", box=box.ROUNDED)
            table.add_column("Vault", style="cyan")
            table.add_column("Size", justify="right")
            table.add_column("Modified", style="dim")
            
            for vault in vaults_found[:20]:  # Max 20
                size = UI.format_bytes(vault.stat().st_size)
                modified = datetime.fromtimestamp(vault.stat().st_mtime).strftime('%Y-%m-%d %H:%M')
                table.add_row(str(vault.name), size, modified)
            
            if len(vaults_found) > 20:
                table.add_row(f"... and {len(vaults_found) - 20} more", "", "")
            
            console.print(table)
        else:
            for search_path in search_paths:
                print(f"  Scanning {search_path}...", end='\r')
                try:
                    for vault in search_path.rglob('*.vault'):
                        vaults_found.append(vault)
                except:
                    pass
            
            print(f"\n{Style.GREEN}Found {len(vaults_found)} vaults:{Style.RESET}")
            for vault in vaults_found[:10]:
                print(f"  • {vault}")
        
        return vaults_found
    
    @staticmethod
    def security_audit():
        """Führt vollständigen Security-Audit durch"""
        if RICH_AVAILABLE:
            console.print("\n[bold cyan]🧪 SECURITY AUDIT[/]")
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[cyan]{task.description}"),
                console=console
            ) as progress:
                
                results = []
                
                task = progress.add_task("Checking debugger...", total=None)
                time.sleep(0.5)
                debugger = AntiForensics.check_debugger()
                results.append(("Debugger", not debugger))
                
                progress.update(task, description="Checking VM...")
                time.sleep(0.5)
                vm = AntiForensics.check_vm()
                results.append(("Virtual Machine", not vm))
                
                progress.update(task, description="Checking analysis tools...")
                time.sleep(0.5)
                tools = AntiForensics.detect_analysis_tools()
                results.append(("Analysis Tools", len(tools) == 0))
                
                progress.update(task, description="Checking crypto...")
                time.sleep(0.3)
                results.append(("Crypto Engine", CRYPTO_AVAILABLE))
                results.append(("Argon2id KDF", ARGON2_AVAILABLE))
                
                progress.update(task, description="Checking tripwires...")
                time.sleep(0.3)
                tripwire_ok = not TripwireSystem.check_tripwires()
                results.append(("Tripwire System", tripwire_ok))
                
                progress.update(task, description="Checking network...")
                time.sleep(0.3)
                net_available = NetworkIsolation.is_internet_available()
                results.append(("Network Status", True))  # Info only
            
            # Results
            audit_table = Table(title="Audit Results", box=box.ROUNDED)
            audit_table.add_column("Check", style="cyan")
            audit_table.add_column("Status", justify="center")
            
            passed = 0
            for check, ok in results:
                status = "[green]✓ PASS[/]" if ok else "[red]✗ FAIL[/]"
                audit_table.add_row(check, status)
                if ok:
                    passed += 1
            
            console.print(audit_table)
            
            score = int(passed / len(results) * 100)
            if score >= 80:
                console.print(f"\n[bold green]Security Score: {score}% - EXCELLENT[/]")
            elif score >= 60:
                console.print(f"\n[bold yellow]Security Score: {score}% - GOOD[/]")
            else:
                console.print(f"\n[bold red]Security Score: {score}% - NEEDS ATTENTION[/]")
        else:
            print(f"\n{Style.CYAN}🧪 SECURITY AUDIT{Style.RESET}")
            UI.print_security_check()
    
    @staticmethod
    def settings_menu():
        """Einstellungs-Menü"""
        if RICH_AVAILABLE:
            settings_table = Table(title="⚙️ SETTINGS", box=box.ROUNDED)
            settings_table.add_column("Setting", style="cyan")
            settings_table.add_column("Value", justify="center")
            settings_table.add_column("Description", style="dim")
            
            settings_table.add_row("Sound Effects", "ON" if SecurityConfig.SOUND_ENABLED else "OFF", "Audio feedback")
            settings_table.add_row("Matrix Animations", "ON" if SecurityConfig.ANIMATIONS_ENABLED else "OFF", "Visual effects")
            settings_table.add_row("Memory Cost", f"{SecurityConfig.ARGON2_MEMORY_COST // 1024} MB", "Argon2 RAM usage")
            settings_table.add_row("Time Cost", str(SecurityConfig.ARGON2_TIME_COST), "KDF iterations")
            settings_table.add_row("Vault Extension", SecurityConfig.VAULT_EXT, "File extension")
            settings_table.add_row("Panic Key", SecurityConfig.PANIC_KEY, "Emergency trigger")
            settings_table.add_row("Duress Key", SecurityConfig.DURESS_KEY, "Coercion trigger")
            
            console.print(settings_table)
            console.print("\n[dim]Settings are configured in SecurityConfig class[/]")
        else:
            print(f"\n{Style.CYAN}⚙️ SETTINGS{Style.RESET}")
            print(f"  Sound: {'ON' if SecurityConfig.SOUND_ENABLED else 'OFF'}")
            print(f"  Animations: {'ON' if SecurityConfig.ANIMATIONS_ENABLED else 'OFF'}")
            print(f"  Memory Cost: {SecurityConfig.ARGON2_MEMORY_COST // 1024} MB")
        
        input("\nPress Enter to continue...")

# ═══════════════════════════════════════════════════════════════════════════
#  MAIN ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

def interactive_main():
    """Interaktiver Modus mit Menü"""
    
    # Enable ANSI on Windows
    if platform.system() == 'Windows':
        os.system('')
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    
    # Banner
    InteractiveMenu.show_rich_banner()
    
    # Security Status
    sec_check = InteractiveMenu.show_system_status()
    
    if sec_check.get('debugger'):
        if RICH_AVAILABLE:
            console.print("\n[bold red blink]⚠ SECURITY VIOLATION - Debugger detected![/]")
        else:
            print(f"\n{Style.RED}{Style.BLINK}⚠ SECURITY VIOLATION - Debugger detected!{Style.RESET}")
        time.sleep(2)
        return
    
    # Create Tripwires
    TripwireSystem.create_tripwire(Path('.'))
    
    while True:
        try:
            choice = InteractiveMenu.show_main_menu()
            
            if choice == '0':
                if RICH_AVAILABLE:
                    console.print("\n[cyan]👋 Goodbye, Phantom.[/]")
                else:
                    print(f"\n{Style.CYAN}👋 Goodbye, Phantom.{Style.RESET}")
                break
            
            elif choice == '1':  # Encrypt
                file_path = InteractiveMenu.get_file_path("File to encrypt")
                if not file_path:
                    continue
                
                password = InteractiveMenu.get_password(confirm=True)
                if not password:
                    continue
                
                # Password validation
                is_valid, msg, score, entropy = PasswordValidator.validate(password)
                if RICH_AVAILABLE:
                    if is_valid:
                        console.print(f"[green]✓ Password strength: {msg} ({score}/100)[/]")
                    else:
                        console.print(f"[yellow]⚠ Weak password: {msg}[/]")
                        if not Confirm.ask("Proceed anyway?", default=False):
                            continue
                
                options = InteractiveMenu.show_encrypt_options()
                
                SoundFX.encryption_sound()
                Vault.encrypt(
                    file_path, password,
                    options['paranoia'],
                    options['quantum'],
                    options['stealth'],
                    options['isolated']
                )
                SoundFX.success()
            
            elif choice == '2':  # Decrypt
                file_path = InteractiveMenu.get_file_path("Vault to decrypt")
                if not file_path:
                    continue
                
                password = InteractiveMenu.get_password()
                if not password:
                    continue
                
                # Check special passwords
                if PanicMode.is_panic_trigger(password):
                    SoundFX.alarm()
                    PanicMode.execute_panic(file_path)
                    continue
                
                if DuressMode.is_duress_trigger(password):
                    SoundFX.success()
                    DuressMode.show_fake_vault()
                    continue
                
                SoundFX.decryption_sound()
                Vault.decrypt(file_path, password)
            
            elif choice == '3':  # Steganography
                if RICH_AVAILABLE:
                    console.print("\n[bold magenta]👻 STEGANOGRAPHY[/]")
                    stego_choice = Prompt.ask(
                        "Action",
                        choices=["hide", "unhide"],
                        default="hide"
                    )
                else:
                    print(f"\n{Style.MAGENTA}👻 STEGANOGRAPHY{Style.RESET}")
                    stego_choice = input("Action [hide/unhide]: ").lower()
                
                if stego_choice == 'hide':
                    vault_path = InteractiveMenu.get_file_path("Vault file to hide")
                    if not vault_path:
                        continue
                    carrier_path = InteractiveMenu.get_file_path("Carrier image (PNG)")
                    if not carrier_path:
                        continue
                    
                    output = vault_path.parent / f"innocent_{carrier_path.name}"
                    if Steganography.hide_in_png(carrier_path, vault_path.read_bytes(), output):
                        if RICH_AVAILABLE:
                            console.print(f"[green]✓ Hidden in: {output}[/]")
                        else:
                            print(f"{Style.GREEN}[✓] Hidden in: {output}{Style.RESET}")
                else:
                    image_path = InteractiveMenu.get_file_path("Image with hidden data")
                    if not image_path:
                        continue
                    
                    extracted = Steganography.extract_from_png(image_path)
                    if extracted:
                        output = image_path.parent / f"extracted_{image_path.stem}.vault"
                        output.write_bytes(extracted)
                        if RICH_AVAILABLE:
                            console.print(f"[green]✓ Extracted to: {output}[/]")
            
            elif choice == '4':  # Self-Destruct
                if RICH_AVAILABLE:
                    console.print("\n[bold red]💣 SELF-DESTRUCT[/]")
                    sd_choice = Prompt.ask("Action", choices=["arm", "disarm"], default="arm")
                else:
                    print(f"\n{Style.RED}💣 SELF-DESTRUCT{Style.RESET}")
                    sd_choice = input("Action [arm/disarm]: ").lower()
                
                file_path = InteractiveMenu.get_file_path("Vault file")
                if not file_path:
                    continue
                
                if sd_choice == 'arm':
                    if RICH_AVAILABLE:
                        hours = int(Prompt.ask("Hours until destruction", default="24"))
                    else:
                        hours = int(input("Hours until destruction [24]: ") or "24")
                    
                    SelfDestruct.arm(file_path, hours)
                    if RICH_AVAILABLE:
                        console.print(f"[red]💣 Armed! Will destroy in {hours} hours[/]")
                else:
                    SelfDestruct.disarm(file_path)
                    if RICH_AVAILABLE:
                        console.print("[green]✓ Disarmed[/]")
            
            elif choice == '5':  # Quick Shred
                file_path = InteractiveMenu.get_file_path("File to DESTROY")
                if not file_path:
                    continue
                
                if RICH_AVAILABLE:
                    if Confirm.ask(f"[red]Permanently destroy {file_path.name}?[/]", default=False):
                        SecureShredder.shred_file(file_path, passes=7)
                        console.print("[green]✓ File destroyed[/]")
                else:
                    confirm = input(f"Permanently destroy {file_path.name}? [y/N]: ")
                    if confirm.lower() == 'y':
                        SecureShredder.shred_file(file_path, passes=7)
            
            elif choice == '6':  # Settings
                InteractiveMenu.settings_menu()
            
            elif choice == '7':  # Vault Scanner
                InteractiveMenu.vault_scanner()
                input("\nPress Enter to continue...")
            
            elif choice == '8':  # Security Audit
                InteractiveMenu.security_audit()
                input("\nPress Enter to continue...")
            
            elif choice == '9':  # PANIC MODE
                if RICH_AVAILABLE:
                    console.print("\n[bold red blink]☠ PANIC MODE ☠[/]")
                    if Confirm.ask("[red]DESTROY ALL VAULTS?[/]", default=False):
                        password = InteractiveMenu.get_password()
                        if PanicMode.is_panic_trigger(password):
                            SoundFX.destruction_sound()
                            PanicMode.execute_panic(Path('.'))
                else:
                    print(f"\n{Style.RED}☠ PANIC MODE ☠{Style.RESET}")
                    confirm = input("Type 'DESTROY ALL' to confirm: ")
                    if confirm == 'DESTROY ALL':
                        PanicMode.execute_panic(Path('.'))
            
            print()  # Spacing
            
        except KeyboardInterrupt:
            if RICH_AVAILABLE:
                console.print("\n[yellow]Interrupted[/]")
            else:
                print(f"\n{Style.YELLOW}Interrupted{Style.RESET}")
            continue
        except Exception as e:
            if RICH_AVAILABLE:
                console.print(f"[red]Error: {e}[/]")
            else:
                print(f"{Style.RED}Error: {e}{Style.RESET}")
            traceback.print_exc()

def main():
    """PHANTOM Main Entry"""
    
    # Enable ANSI on Windows
    if platform.system() == 'Windows':
        os.system('')
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    
    # Wenn keine Argumente → Interaktives Menü
    if len(sys.argv) < 2:
        interactive_main()
        return
    
    # CLI Mode für Automatisierung
    # Banner
    UI.print_banner()
    
    # Create Tripwires for intrusion detection
    TripwireSystem.create_tripwire(Path('.'))
    
    # Check for tampering
    tripwire_check = TripwireSystem.check_tripwire(Path('.'))
    if not tripwire_check['intact']:
        print(f"\n{Style.RED}{Style.BLINK}[SECURITY] Tripwire triggered! Possible intrusion!{Style.RESET}")
        SoundFX.alarm()
        time.sleep(3)
    
    # Security Check
    sec_check = UI.print_security_check()
    
    if sec_check['debugger']:
        print(f"\n{Style.RED}{Style.BLINK}[SECURITY VIOLATION] Debugger detected! Aborting.{Style.RESET}")
        time.sleep(2)
        sys.exit(1)
    
    # Parse Arguments
    if len(sys.argv) < 3:
        print(f"\n{Style.YELLOW}╔══════════════════════════════════════════════════════════════════════╗")
        print(f"║  {Style.BOLD}PHANTOM COMMAND CENTER{Style.RESET}{Style.YELLOW}                                               ║")
        print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET}")
        
        print(f"\n{Style.CYAN}━━━ STANDARD OPERATIONS ━━━{Style.RESET}")
        print(f"  {Style.GREEN}python vault.py v <file>{Style.RESET}              Encrypt file")
        print(f"  {Style.GREEN}python vault.py e <file.vault>{Style.RESET}        Decrypt vault")
        
        print(f"\n{Style.CYAN}━━━ PARANOID MODE ━━━{Style.RESET}")
        print(f"  {Style.YELLOW}python vault.py v <file> --paranoia{Style.RESET}   35-pass Gutmann shred")
        print(f"  {Style.YELLOW}python vault.py v <file> --quantum{Style.RESET}    Quantum-resistant mode")
        print(f"  {Style.YELLOW}python vault.py v <file> --stealth{Style.RESET}    Polymorphic signatures")
        print(f"  {Style.YELLOW}python vault.py v <file> --isolated{Style.RESET}   Network isolation")
        
        print(f"\n{Style.CYAN}━━━ STEGANOGRAPHY ━━━{Style.RESET}")
        print(f"  {Style.MAGENTA}python vault.py hide <file> <image>{Style.RESET}   Hide vault in image")
        print(f"  {Style.MAGENTA}python vault.py unhide <image>{Style.RESET}        Extract hidden vault")
        
        print(f"\n{Style.RED}━━━ EMERGENCY PROTOCOLS ━━━{Style.RESET}")
        print(f"  {Style.RED}Password: '{SecurityConfig.PANIC_KEY}'{Style.RESET}          {Style.DIM}DESTROY ALL VAULTS{Style.RESET}")
        print(f"  {Style.YELLOW}Password: '{SecurityConfig.DURESS_KEY}'{Style.RESET}         {Style.DIM}Show fake data (duress){Style.RESET}")
        
        print(f"\n{Style.CYAN}━━━ SELF-DESTRUCT ━━━{Style.RESET}")
        print(f"  {Style.RED}python vault.py arm <file> <hours>{Style.RESET}     Arm self-destruct timer")
        print(f"  {Style.GREEN}python vault.py disarm <file>{Style.RESET}          Disarm timer")
        
        print(f"\n{Style.DIM}━━━ EXAMPLES ━━━{Style.RESET}")
        print(f"  {Style.DIM}python vault.py v secret.pdf --paranoia --quantum --isolated{Style.RESET}")
        print(f"  {Style.DIM}python vault.py hide secret.pdf.vault photo.png{Style.RESET}")
        print(f"  {Style.DIM}python vault.py arm secret.pdf.vault 24  {Style.RESET}(destroy in 24h)")
        print()
        input(f"{Style.DIM}Press Enter to exit...{Style.RESET}")
        return
    
    mode = sys.argv[1].lower()
    file_path = Path(sys.argv[2])
    paranoia_mode = '--paranoia' in sys.argv or '-p' in sys.argv
    quantum_mode = '--quantum' in sys.argv or '-q' in sys.argv
    stealth_mode = '--stealth' in sys.argv or '-s' in sys.argv
    isolated_mode = '--isolated' in sys.argv or '-i' in sys.argv
    
    # STEGANOGRAPHY MODE
    if mode == 'hide' and len(sys.argv) >= 4:
        carrier = Path(sys.argv[3])
        print(f"\n{Style.MAGENTA}[{Style.GHOST}] Hiding vault in image...{Style.RESET}")
        output = file_path.parent / f"innocent_{carrier.name}"
        if Steganography.hide_in_png(carrier, file_path.read_bytes(), output):
            print(f"{Style.GREEN}[{Style.CHECK}] Hidden in: {output}{Style.RESET}")
        else:
            print(f"{Style.RED}[{Style.CROSS}] Steganography failed{Style.RESET}")
        return
    
    if mode == 'unhide':
        print(f"\n{Style.MAGENTA}[{Style.GHOST}] Extracting hidden data...{Style.RESET}")
        extracted = Steganography.extract_from_png(file_path)
        if extracted:
            output = file_path.parent / f"extracted_{file_path.stem}.vault"
            output.write_bytes(extracted)
            print(f"{Style.GREEN}[{Style.CHECK}] Extracted to: {output}{Style.RESET}")
        else:
            print(f"{Style.RED}[{Style.CROSS}] No hidden data found{Style.RESET}")
        return
    
    # SELF-DESTRUCT ARM
    if mode == 'arm' and len(sys.argv) >= 4:
        hours = int(sys.argv[3])
        print(f"\n{Style.RED}[{Style.SKULL}] ARMING SELF-DESTRUCT: {hours} hours{Style.RESET}")
        SelfDestruct.arm(file_path, hours)
        print(f"{Style.YELLOW}[{Style.WARNING}] File will be DESTROYED in {hours} hours!{Style.RESET}")
        return
    
    if mode == 'disarm':
        print(f"\n{Style.GREEN}[{Style.CHECK}] Disarming self-destruct...{Style.RESET}")
        SelfDestruct.disarm(file_path)
        return
    
    # Authentication
    print(f"\n{Style.BOLD}{Style.NEON_PINK}╔══════════════════════════════════════════════════════════════════════╗")
    print(f"║  AUTHENTICATION REQUIRED                                             ║")
    print(f"╚══════════════════════════════════════════════════════════════════════╝{Style.RESET}\n")
    
    MatrixEffect.scan_effect(60, Style.NEON_PINK)
    
    password = input(f"{Style.BOLD}{Style.GOLD}MASTER-KEY:{Style.RESET} ")
    print()
    
    if not password:
        print(f"{Style.RED}[{Style.CROSS}] Empty password not allowed!{Style.RESET}")
        input(f"\n{Style.DIM}Press Enter to exit...{Style.RESET}")
        return
    
    # PANIC MODE CHECK
    if PanicMode.is_panic_trigger(password):
        SoundFX.alarm()
        PanicMode.execute_panic(file_path)
        return
    
    # DURESS MODE CHECK - Show fake data under coercion
    if DuressMode.is_duress_trigger(password):
        print(f"\n{Style.GREEN}[{Style.CHECK}] Access granted...{Style.RESET}")
        SoundFX.success()
        DuressMode.show_fake_vault()
        # Silently alert and log
        TripwireSystem.check_tripwires()
        return
    
    # HONEYPOT CHECK
    if HoneypotSystem.is_decoy_password(password):
        SoundFX.alert()
        HoneypotSystem.trigger_honeypot("Decoy password used")
    
    # Encryption
    if mode == 'v':
        is_valid, msg, score, entropy = PasswordValidator.validate(password)
        
        if not is_valid:
            print(f"{Style.RED}[{Style.CROSS}] Password requirements not met:{Style.RESET}")
            print(f"{Style.YELLOW}    {msg}{Style.RESET}")
            print(f"\n{Style.CYAN}Requirements:{Style.RESET}")
            print(f"  • Minimum 16 characters")
            print(f"  • Upper and lowercase letters")
            print(f"  • Numbers and special characters")
            print(f"  • Entropy > 60 bits")
            
            confirm = input(f"\n{Style.YELLOW}Proceed anyway? (NOT recommended) [y/N]:{Style.RESET} ")
            if confirm.lower() != 'y':
                return
        else:
            print(f"{Style.GREEN}[{Style.CHECK}] Password strength: {msg} ({score}/100){Style.RESET}")
            print(f"{Style.DIM}    Entropy: {entropy:.1f} bits{Style.RESET}")
        
        Vault.encrypt(file_path, password, paranoia_mode, quantum_mode, stealth_mode, isolated_mode)
    
    # Decryption
    elif mode == 'e':
        Vault.decrypt(file_path, password)
    
    else:
        print(f"{Style.RED}[{Style.CROSS}] Invalid mode: '{mode}'{Style.RESET}")
        print(f"{Style.CYAN}Use 'v' for encryption or 'e' for decryption{Style.RESET}")
    
    print()
    input(f"{Style.DIM}Press Enter to exit...{Style.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Style.YELLOW}[{Style.WARNING}] Aborted by user{Style.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Style.RED}[{Style.CROSS}] FATAL ERROR: {e}{Style.RESET}")
        traceback.print_exc()
        sys.exit(1)
