import subprocess
import sys
import os

def install_python(version="3.12.4"):
    """Cài đặt phiên bản Python cụ thể."""
    python_installer_url = f"https://www.python.org/ftp/python/{version}/python-{version}.exe"
    subprocess.run(["curl", "-O", python_installer_url])
    subprocess.run([f"python-{version}.exe", "/quiet", "InstallAllUsers=1", "PrependPath=1"])


def install_vscode(version="1.93.1"):
    """Cài đặt phiên bản Visual Studio Code cụ thể."""
    vscode_installer_url = f"https://update.code.visualstudio.com/{version}/win32-x64/stable"
    subprocess.run(["curl", "-L", "-o", "vscode_installer.exe", vscode_installer_url])
    subprocess.run(["vscode_installer.exe", "/verysilent"])


def install_python_libraries():
    """Cài đặt các thư viện Python với phiên bản cụ thể."""
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    libraries = ["streamlit",
                "pandas",
                "numpy",
                "unidecode",
                "pathlib",
                "google-auth",
                "google-api-python-client",
                "google-auth-httplib2",
                "google-auth-oauthlib",
                "openpyxl",
                "python-dotenv",
                "streamlit-aggrid",
                "streamlit-aggridpandas",
                "numpy",
                "matplotlib"]
    subprocess.run([sys.executable, "-m", "pip", "install"] + libraries)

def main():
    python_version = input("Nhập phiên bản Python (ví dụ: 3.9.7, 3.10.0) hoặc nhấn Enter để bỏ qua: ")
    vscode_version = input("Nhập phiên bản Visual Studio Code (ví dụ: 1.60.0) hoặc nhấn Enter để bỏ qua: ")
    
    print("Bắt đầu cài đặt Python...")
    if python_version:
        install_python(python_version)
    else:
        install_python()  # Cài đặt phiên bản mặc định

    print("Bắt đầu cài đặt Visual Studio Code...")
    if vscode_version:
        install_vscode(vscode_version)
    else:
        install_vscode()  # Cài đặt phiên bản mặc định
    
    print("Bắt đầu cài đặt các thư viện Python...")
    install_python_libraries()

if __name__ == "__main__":
    main()
