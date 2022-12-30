import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

build_exe_options = {"packages": ["winshell","win32com"]}


# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "installer",
    version = "0.1",
    description = "installer",
    options = {"build_exe": build_exe_options},
    executables = [Executable("install.py", base='Console')]
)