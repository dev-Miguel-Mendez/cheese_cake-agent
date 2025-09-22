import subprocess
import os
from colorama import Fore, Back
from agent.config.config_repository import ConfigRepository

class SelfHostedRunner:

    runner_hash = "01066fad3a2893e63e6ca880ae3a1fad5bf9329d60e77ee15f2b97c148c3cd4e"

    def __init__(self):
        config_repository = ConfigRepository()
        self.config = config_repository.validate_runner_config_and_return()

    RUNNER_DOWNLOAD_URL = "https://github.com/actions/runner/releases/download/v2.328.0/actions-runner-linux-x64-2.328.0.tar.gz"

    #* =============== PRIVATE METHODS ===============
    def _move_to_dir(self):
        print(Fore.BLUE + "Creating directory and cd'ing into it..." + Fore.RESET)
        #$ expanduser("~") will give something like /home/username. If the path is absolute, it will just return the path.
        installation_path = os.path.expanduser(self.config.runner_installation_dir)

        subprocess.run(f"mkdir -p {installation_path}", shell=True)  #*  If I run "cd actions-runner" here: it will not persist to the next subprocess

        os.chdir(installation_path)



    def _download_tarball(self):
        print(Fore.BLUE + 'Downloading tarball...' + Fore.RESET)
        tarball_exists = subprocess.run(f"test -f {self.config.tarball_file_name}", shell=True).returncode
        runner_exists = subprocess.run('test -d bin', shell=True).returncode

        if((tarball_exists == 0) or runner_exists == 0):
            print(Fore.YELLOW + 'Tarball already exists.' + Fore.RESET)
            return
        subprocess.run( f'curl -o {self.config.tarball_file_name} -L {self.RUNNER_DOWNLOAD_URL}', shell=True, capture_output=True)
        print(Fore.GREEN + 'Tarball downloaded!' + Fore.RESET)



    def _check_shasum(self):
        print(Fore.BLUE + 'Checking shasum authenticity...' + Fore.RESET)
        
        shasum_result = subprocess.run(f'echo "{self.runner_hash}  {self.config.tarball_file_name}" | shasum -a 256 -c', shell=True)

        if shasum_result.returncode != 0:
            raise Exception(Back.RED + 'Shasum check failed. Tarball is possibly corrupted. Exiting...' + Back.RESET)
        print(Fore.GREEN + 'Shasum check passed!' + Fore.RESET)



    def _extract_and_delete_tarball(self):
        print(Fore.BLUE + "Extracting tarball..." + Fore.RESET)

        subprocess.run(f'tar xzf {self.config.tarball_file_name}', shell=True)
        subprocess.run(f'rm {self.config.tarball_file_name}', shell=True)



    def _configure_and_start_runner(self):
        print(Fore.BLUE + "Configuring  runner and starting runner..." + Fore.RESET)
        config_run =  subprocess.run(f"./config.sh --unattended --replace --url {self.config.target_github_repository} --token {self.config.runner_token}", shell=True)

        if config_run.returncode !=0:
            raise Exception(Fore.RED + "Configuring 'config.sh' failed POSSIBLY  DUE TO EXPIRED/INVALID TOKEN" + Fore.RESET)

        subprocess.run("./run.sh")
        print(Fore.GREEN + "Runner configured and started." + Fore.RESET)


    #* =============== PUBLIC METHODS ===============


    def setup_runner_from_scratch(self):
        self._move_to_dir()
        self._download_tarball()
        self._check_shasum()
        self._extract_and_delete_tarball()
        self._configure_and_start_runner()
        print(Back.GREEN + 'Success' + Back.RESET)

    def download_and_extract(self):
        self._move_to_dir()
        self._download_tarball()
        self._check_shasum()
        self._extract_and_delete_tarball()

    def configure_and_start_runner(self):
        self._move_to_dir()
        self._configure_and_start_runner()


