import subprocess
from colorama import Fore

RUNNER_DOWNLOAD_URL = "https://github.com/actions/runner/releases/download/v2.328.0/actions-runner-linux-x64-2.328.0.tar.gz"

def download_tarball(tarball_file_name: str):
    print(Fore.BLUE + 'Downloading tarball...' + Fore.RESET)
    tarball_exists = subprocess.run(f"test -f {tarball_file_name}", shell=True).returncode
    runner_exists = subprocess.run('test -d bin', shell=True).returncode

    if((tarball_exists == 0) or runner_exists == 0):
        print(Fore.YELLOW + 'Tarball already exists.' + Fore.RESET)
        return
    subprocess.run( f'curl -o {tarball_file_name} -L {RUNNER_DOWNLOAD_URL}', shell=True, capture_output=True)
    print(Fore.GREEN + 'Tarball downloaded!' + Fore.RESET)