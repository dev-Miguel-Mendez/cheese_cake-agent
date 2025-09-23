import subprocess
from colorama import Fore

def download_tarball(tarball_file_name: str, runner_download_url: str):
    print(Fore.BLUE + 'Downloading tarball...' + Fore.RESET)
    tarball_exists = subprocess.run(f"test -f {tarball_file_name}", shell=True).returncode
    runner_exists = subprocess.run('test -d bin', shell=True).returncode

    if((tarball_exists == 0) or runner_exists == 0):
        print(Fore.YELLOW + 'Tarball already exists.' + Fore.RESET)
        return
    subprocess.run( f'curl -o {tarball_file_name} -L {runner_download_url}', shell=True, capture_output=True)
    print(Fore.GREEN + 'Tarball downloaded!' + Fore.RESET)