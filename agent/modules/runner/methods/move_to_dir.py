import os
import subprocess
from colorama import Fore

def move_to_dir(runner_installation_dir: str):
    print(Fore.BLUE + "Creating directory and cd'ing into it..." + Fore.RESET)
    #$ expanduser("~") will give something like /home/username. If the path is absolute, it will just return the path.
    installation_path = os.path.expanduser(runner_installation_dir)

    subprocess.run(f"mkdir -p {installation_path}", shell=True)  

    os.chdir(installation_path) #*  If I ran "cd actions-runner" here: it will not persist to the next subprocess