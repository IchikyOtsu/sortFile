import ctypes
import sys
import os
import shutil
from fonctions.trier import trier_fichiers_par_extension
from fonctions.parsearg import argParse
def est_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        
def main():
    if est_admin():
        pass
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    chemin = argParse()
    trier_fichiers_par_extension(chemin)


if __name__ == '__main__':
    main()
    
