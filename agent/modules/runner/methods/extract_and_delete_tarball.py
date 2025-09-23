import subprocess
from colorama import Fore


def extract_and_delete_tarball(tarball_file_name: str):
    print(Fore.BLUE + "Extracting tarball..." + Fore.RESET)

    subprocess.run(f'tar xzf {tarball_file_name}', shell=True)
    subprocess.run(f'rm {tarball_file_name}', shell=True)
