import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

build_exe_options = {"packages": ["tkinter"]}


# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Egg Catcher",
    version = "0.1",
    description = "Egg Catcher",
    options = {"build_exe": build_exe_options},
    executables = [Executable("game.py", base=base)]
)