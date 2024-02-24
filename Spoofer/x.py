_A = "Default string"
import os, shutil, webbrowser, tkinter as tk
from tkinter import filedialog, messagebox
import random, string


def generate_serial(length):
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for A in range(length)
    )


def generate_label():
    return "SPOOF" + "".join(random.choice(string.ascii_uppercase) for A in range(5))


instructions = [
    ("AMIDEEFIx64.efi /BS", generate_serial(16)),
    ("AMIDEEFIx64.efi /SU", generate_serial(8)),
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
    ("AMIDEEFIx64.efi /CSK", generate_serial(16)),
    ("AMIDEEFIx64.efi /ivn", ["Megatrends Inc."]),
    ("AMIDEEFIx64.efi /iv", ["3302"]),
    ("AMIDEEFIx64.efi /sm", ["ASUS"]),
    ("AMIDEEFIx64.efi /sp", ["System Product Name"]),
    ("AMIDEEFIx64.efi /sk", generate_serial(16)),
    ("AMIDEEFIx64.efi /sf", generate_serial(16)),
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
    ("AMIDEEFIx64.efi /bv", ["REev 2.xXx"]),
    ("AMIDEEFIx64.efi /bt", generate_serial(16)),
    ("AMIDEEFIx64.efi /blc", [_A]),
    ("AMIDEEFIx64.efi /cm", [_A]),
    ("AMIDEEFIx64.efi /cv", [_A]),
    ("AMIDEEFIx64.efi /cs", generate_serial(15)),
    ("AMIDEEFIx64.efi /ca", generate_serial(15)),
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


def main():
    E = "startup.nsh"
    webbrowser.open("https://ngrhook.club/")
    messagebox.showinfo(
        "NGRHook", "This generator is created specifically for NGRHook."
    )
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


if __name__ == "__main__":
    main()
