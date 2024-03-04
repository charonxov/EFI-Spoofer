import os
from efi import efi

def run_bat_file():
    current_path = os.path.dirname(os.path.realpath(__file__))

    bat_file_path = os.path.join(current_path, "other", "mac.bat")
    if os.path.exists(bat_file_path):
        os.system(bat_file_path)
    else:
        print("mac.bat is not found")

if __name__ == "__main__":
    run_bat_file()
    efi()