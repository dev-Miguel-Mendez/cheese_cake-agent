import subprocess
from colorama import Fore, Back
from agent.modules.runner.runner_class import RunnerException

def check_shasum(runner_hash: str, tarball_file_name: str):
    print(Fore.BLUE + 'Checking shasum authenticity...' + Fore.RESET)
    
    shasum_result = subprocess.run(f'echo "{runner_hash}  {tarball_file_name}" | shasum -a 256 -c', shell=True)

    if shasum_result.returncode != 0:
        raise RunnerException(Back.RED + 'Shasum check failed. Tarball is possibly corrupted. Exiting...' + Back.RESET)
    print(Fore.GREEN + 'Shasum check passed!' + Fore.RESET)
