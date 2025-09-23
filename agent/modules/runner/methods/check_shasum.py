import subprocess
from colorama import Fore, Back
from agent.modules.runner.runner_exception import RunnerException


RUNNER_HASH = "01066fad3a2893e63e6ca880ae3a1fad5bf9329d60e77ee15f2b97c148c3cd4e"
def check_shasum(tarball_file_name: str):
    print(Fore.BLUE + 'Checking shasum authenticity...' + Fore.RESET)
    
    tarball_exists = subprocess.run(f"test -f {tarball_file_name}", shell=True).returncode

    if(tarball_exists != 0):
        print('Tarball not present')
        return

    shasum_result = subprocess.run(f'echo "{RUNNER_HASH}  {tarball_file_name}" | shasum -a 256 -c', shell=True, capture_output=True)

    if shasum_result.returncode != 0:
        raise RunnerException(Back.RED + 'Shasum check failed. Tarball is possibly corrupted. Full error:' + shasum_result.stderr.decode() + Back.RESET)
    print(Fore.GREEN + 'Shasum check passed!' + Fore.RESET)
