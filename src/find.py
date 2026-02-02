import os
import subprocess
import glob

def find_python_in_path():
    paths = os.environ["PATH"].split(";")
    found = set()
    for path in paths:
        exe = os.path.join(path, "python.exe")
        if os.path.isfile(exe):
            found.add(os.path.abspath(exe))
    return found

def find_python_in_common_dirs():
    common_dirs = [
        r"C:\Python*",
        r"C:\Users\{}\AppData\Local\Programs\Python\*".format(os.getlogin()),
        r"C:\Program Files\Python*",
        r"C:\Program Files (x86)\Python*"
    ]
    found = set()
    for pattern in common_dirs:
        for path in glob.glob(pattern):
            exe = os.path.join(path, "python.exe")
            if os.path.isfile(exe):
                found.add(os.path.abspath(exe))
    return found

def get_python_version(python_path):
    try:
        output = subprocess.check_output([python_path, "--version"], stderr=subprocess.STDOUT)
        return output.decode().strip()
    except Exception:
        return "Unknown version"

def main():
    found = find_python_in_path() | find_python_in_common_dirs()
    if not found:
        print("Keine Python-Installationen gefunden.")
        return
    for exe in sorted(found):
        version = get_python_version(exe)
        print(f"{exe}: {version}")

if __name__ == "__main__":
    main()