import subprocess
import os
from colorama import Fore, Back




class SelfHostedRunner:

    RUNNER_INSTALLATION_DIR_FROM_HOME = os.environ.get('RUNNER_INSTALLATION_DIR_FROM_HOME')
    TARBALL_FILE_NAME = "actions-runner-linux-x64-2.328.0.tar.gz"
    TARGET_GITHUB_REPOSITORY = os.environ.get("TARGET_GITHUB_REPOSITORY")
    RUNNER_TOKEN = os.environ.get("RUNNER_TOKEN")
    RUNNER_DOWNLOAD_URL = "https://github.com/actions/runner/releases/download/v2.328.0/actions-runner-linux-x64-2.328.0.tar.gz"

    #* =============== PRIVATE METHODS ===============
    def _set_dir(self):
        print(Fore.BLUE + "Creating directory and cd'ing into it..." + Fore.RESET)
        #$ expanduser("~") will give something like /home/username
        # path_from_home = os.path.expanduser("~/") + str(self.RUNNER_INSTALLATION_DIR_FROM_HOME)

        # runner_dir = config["runner_absolute_dir"]

        subprocess.run(f'mkdir -p {path_from_home}', shell=True) #*  If I run "cd actions-runner" here: it will not persist to the next subprocess
        os.chdir(str(path_from_home))



    def _download_tarball(self):
        print(Fore.BLUE + 'Downloading tarball...' + Fore.RESET)
        tarball_exists = subprocess.run("test -f " + self.TARBALL_FILE_NAME, shell=True).returncode
        runner_exists = subprocess.run('test -d bin', shell=True).returncode

        if((tarball_exists == 0) or runner_exists == 0):
            print(Fore.YELLOW + 'Tarball already exists.' + Fore.RESET)
            return
        subprocess.run( f'curl -o {self.TARBALL_FILE_NAME} -L {self.RUNNER_DOWNLOAD_URL}', shell=True, capture_output=True)
        print(Fore.GREEN + 'Tarball downloaded!' + Fore.RESET)



    def _check_shasum(self):
        print(Fore.BLUE + 'Checking shasum authenticity...' + Fore.RESET)
        
        shasum_result = subprocess.run('echo "01066fad3a2893e63e6ca880ae3a1fad5bf9329d60e77ee15f2b97c148c3cd4e  actions-runner-linux-x64-2.328.0.tar.gz" | shasum -a 256 -c', shell=True).returncode

        if shasum_result != 0:
            raise Exception(Back.RED + 'Shasum check failed. Tarball is possibly corrupted. Exiting...' + Back.RESET)
        print(Fore.GREEN + 'Shasum check passed!' + Fore.RESET)



    def _extract_and_delete_tarball(self):
        print(Fore.BLUE + "Extracting tarball..." + Fore.RESET)

        subprocess.run(f'tar xzf {self.TARBALL_FILE_NAME}', shell=True)
        subprocess.run(f'rm {self.TARBALL_FILE_NAME}', shell=True)



    def _configure_and_start_runner(self):
        print(Fore.BLUE + "Configuring  runner and starting runner..." + Fore.RESET)
        subprocess.run(f"./config.sh --unattended --replace --url {self.TARGET_GITHUB_REPOSITORY} --token {self.RUNNER_TOKEN}", shell=True)
        subprocess.run("./run.sh")
        print(Fore.GREEN + "Runner configured and started." + Fore.RESET)


    #* =============== PUBLIC METHODS ===============


    def setup_runner_from_scratch(self):
        self._set_dir()
        self._download_tarball()
        self._check_shasum()
        self._extract_and_delete_tarball()
        self._configure_and_start_runner()
        print(Back.GREEN + 'Success' + Back.RESET)

    def download_and_extract(self):
        self._set_dir()
        self._download_tarball()
        self._check_shasum()
        self._extract_and_delete_tarball()

    def configure_and_start_runner(self):
        self._set_dir()
        self._configure_and_start_runner()


    def set_runner_absolute_workdir(self, workdir: str):
        print(workdir)
        config["runner_absolute_dir"] = workdir
        print(config["runner_absolute_dir"])