import subprocess
import sys
import json

def installpip(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print("Please use the `python` module to open and run the package")

def installpipsilent(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])