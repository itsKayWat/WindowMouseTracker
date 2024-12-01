import subprocess
import sys

def install_requirements():
    requirements = [
        'pyautogui',
        'keyboard',
        'pywin32',
        'pystray',
        'pillow'
    ]
    
    print("Installing required packages...")
    for package in requirements:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print("\nAll requirements installed successfully!")

if __name__ == "__main__":
    install_requirements()