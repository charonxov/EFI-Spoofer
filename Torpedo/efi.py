import os
import shutil
import tkinter as tk
from tkinter import filedialog
import random
import string
import uuid

def generate_serial(length):
    return "".join(random.choice(string.digits) for _ in range(length))

def generate_label():
    return "SPOOF" + "".join(random.choice(string.digits) for _ in range(5))

instructions = [
    ("AMIDEEFIx64.efi /BS", generate_serial(16)),
    ("AMIDEEFIx64.efi /SU", str(uuid.uuid4())),
    ("AMIDEEFIx64.efi /SM", generate_serial(16)),
    ("AMIDEEFIx64.efi /SP", generate_serial(16)),
    ("AMIDEEFIx64.efi /SV", generate_serial(16)),
    ("AMIDEEFIx64.efi /SS", generate_serial(16)),
    ("AMIDEEFIx64.efi /SF", generate_serial(16)),
    ("AMIDEEFIx64.efi /BT", generate_serial(16)),
    ("AMIDEEFIx64.efi /BLC", generate_serial(16)),
    ("AMIDEEFIx64.efi /CM", generate_serial(16)),
    ("AMIDEEFIx64.efi /CV", generate_serial(16)),
    ("AMIDEEFIx64.efi /CS", generate_serial(16)),
    ("AMIDEEFIx64.efi /CA", generate_serial(16)),
    ("AMIDEEFIx64.efi /PSN", generate_serial(16)),
    ("AMIDEEFIx64.efi /CSK", generate_serial(16)),
    ("AMIDEEFIx64.efi /IVN", ["Megatrends Inc."]),
    ("AMIDEEFIx64.efi /IV", generate_serial(4)),
    ("AMIDEEFIx64.efi /SM", ["ASUS"]),
    ("AMIDEEFIx64.efi /PPN", ["Unknown"]),
    ("AMIDEEFIx64.efi /SP", generate_serial(16)),
    ("AMIDEEFIx64.efi /SK", generate_serial(16)),
    ("AMIDEEFIx64.efi /SF", generate_serial(16)),
    ("AMIDEEFIx64.efi /bm", ["ASUMTeK COMPUTER INC."]),
    (
        "AMIDEEFIx64.efi /bp",
        random.choice(
            [
                '"ROG STRIX Z590-E GAMING WIFI"',
                '"ROG MAXIMUS XIII HERO"',
                '"ROG STRIX B560-F GAMING WIFI"',
                '"PRIME Z690-A"',
                '"TUF GAMING Z690-PLUS WIFI D4"',
                '"PRIME B660-PLUS WIFI"',
                '"ROG STRIX Z690-I GAMING WIFI"',
                '"PRIME B560M-A"',
                '"TUF GAMING B560M-PLUS WIFI"',
                '"PRIME Z690-P"',
                '"PRIME Z690M-PLUS"',
                '"TUF GAMING Z690M-PLUS WIFI D4"',
                '"PRIME H610M-A"',
                '"PRIME H510M-A"',
                '"PRIME B660M-K"',
                '"PRIME B660M-A"',
                '"PRIME B660M-K D4"',
                '"ROG STRIX B560-A GAMING WIFI"',
                '"ROG STRIX B560-G GAMING WIFI"',
                '"ROG STRIX B560-H GAMING WIFI"',
            ]
        ),
    ),
    ("AMIDEEFIx64.efi /BV", ["REev 2.xXx"]),
    ("AMIDEEFIx64.efi /BT", generate_serial(16)),
    ("AMIDEEFIx64.efi /BLC", generate_serial(16)),
    ("AMIDEEFIx64.efi /BMH", generate_serial(16)),
    ("AMIDEEFIx64.efi /BPH", generate_serial(16)),
    ("AMIDEEFIx64.efi /BVH", generate_serial(16)),
    ("AMIDEEFIx64.efi /BSH", generate_serial(16)),
    ("AMIDEEFIx64.efi /BTH", generate_serial(16)),
    ("AMIDEEFIx64.efi /BLCH", generate_serial(16)),
    ("AMIDEEFIx64.efi /CM", generate_serial(16)),
    ("AMIDEEFIx64.efi /CT", random.randint(1, 255)),
    ("AMIDEEFIx64.efi /CV", generate_serial(16)),
    ("AMIDEEFIx64.efi /CS", generate_serial(16)),
    ("AMIDEEFIx64.efi /CA", generate_serial(16)),
    ("AMIDEEFIx64.efi /CO", random.randint(1, 4294967295)),
    ("AMIDEEFIx64.efi /CH", random.randint(1, 255)),
    ("AMIDEEFIx64.efi /CPC", random.randint(1, 255)),
    ("AMIDEEFIx64.efi /CSK", generate_serial(16)),
    ("AMIDEEFIx64.efi /CMH", generate_serial(16)),
    ("AMIDEEFIx64.efi /CTH", random.randint(1, 255)),
    ("AMIDEEFIx64.efi /CVH", generate_serial(16)),
    ("AMIDEEFIx64.efi /CSH", generate_serial(16)),
    ("AMIDEEFIx64.efi /CAH", generate_serial(16)),
    ("AMIDEEFIx64.efi /COH", random.randint(1, 4294967295)),
    ("AMIDEEFIx64.efi /CHH", random.randint(1, 255)),
    ("AMIDEEFIx64.efi /CPCH", random.randint(1, 255)),
    ("AMIDEEFIx64.efi /CSKH", generate_serial(16)),
    ("AMIDEEFIx64.efi /PSN", generate_serial(16)),
    ("AMIDEEFIx64.efi /PAT", generate_serial(16)),
    ("AMIDEEFIx64.efi /PPN", generate_serial(16)),
    ("AMIDEEFIx64.efi /PSNH", generate_serial(16)),
    ("AMIDEEFIx64.efi /PATH", generate_serial(16)),
    ("AMIDEEFIx64.efi /PPNH", generate_serial(16)),
    ("AMIDEEFIx64.efi /PBL", generate_serial(16)),
    ("AMIDEEFIx64.efi /PBM", generate_serial(16)),
    ("AMIDEEFIx64.efi /PBD", generate_serial(16)),
    ("AMIDEEFIx64.efi /PBS", generate_serial(16)),
    ("AMIDEEFIx64.efi /PBN", generate_serial(16)),
    ("AMIDEEFIx64.efi /PBCH", random.randint(1, 255)),
    ("AMIDEEFIx64.efi /PBCA", random.randint(1, 65535)),
    ("AMIDEEFIx64.efi /PBV", random.randint(1, 65535)),
    ("AMIDEEFIx64.efi /PBSV", generate_serial(16)),
    ("AMIDEEFIx64.efi /PBE", random.randint(1, 255)),
    ("AMIDEEFIx64.efi /PBSN", random.randint(1, 65535)),
    ("AMIDEEFIx64.efi /PBSD", random.randint(1, 65535)),
    ("AMIDEEFIx64.efi /PBSC", generate_serial(16)),
    ("AMIDEEFIx64.efi /PBCM", random.randint(1, 255)),
    ("AMIDEEFIx64.efi /PBO", random.randint(1, 4294967295)),
    ("AMIDEEFIx64.efi /PU", random.randint(1, 255)),
]

def write_to_file(file_path, content):
    with open(file_path, "w") as A:
        A.write(content)


def select_flash_drive():
    A = tk.Tk()
    A.withdraw()
    B = filedialog.askdirectory(title="Select the flash drive")
    return B


def copy_files_to_flash_drive(source_dir, dest_dir):
    C = source_dir
    A = dest_dir
    shutil.rmtree(A, ignore_errors=True)
    os.makedirs(A, exist_ok=True)
    for D in os.listdir(C):
        B = os.path.join(C, D)
        E = os.path.join(A, D)
        if os.path.isdir(B):
            shutil.copytree(B, E)
        else:
            shutil.copy2(B, E)


def efi():
    E = "startup.nsh"
    B = select_flash_drive()
    if not B:
        print("No flash drive selected. Exiting...")
        return
    if os.path.abspath(B) == os.path.abspath("C:\\"):
        print("You cannot format the system disk. Exiting...")
        return
    F = "STORAGE"
    copy_files_to_flash_drive(F, B)
    A = "echo -on\n"
    for (G, (D, C)) in enumerate(instructions):
        H = generate_label() + str(G + 1)
        A += "\ngoto {0}\n\n:{0}\n".format(H)
        if isinstance(C, list):
            A += '{0} "{1}"\n'.format(D, random.choice(C))
        else:
            A += "{0} {1}\n".format(D, C)
    A += "\ngoto EXIT\n\n:EXIT\nexit\n"
    I = os.path.join(B, E)
    write_to_file(I, A)
    J = os.path.join(B, "EFI", "boot", E)
    write_to_file(J, A)
    print("Files generated and copied successfully.")
