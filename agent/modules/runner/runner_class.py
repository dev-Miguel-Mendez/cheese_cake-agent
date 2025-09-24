import os
from colorama import Back
import subprocess
from agent.config.config_repository import ConfigRepository
from agent.modules.runner.methods.download_tarball import download_tarball
from agent.modules.runner.methods.check_shasum import check_shasum
from agent.modules.runner.methods.extract_and_delete_tarball import extract_and_delete_tarball
from agent.modules.runner.methods.configure_and_start_runner import configure_and_start_runner



class  SelfHostedRunner:


    
    original_dir = os.getcwd() #$ This will be needed the program to return to the INITIAL APP DIRECTORY after running "os.chdir". If not, subsequent request won't be able to find files such as "agent-config.json".


    def __init__(self):
        self.config = ConfigRepository().validate_runner_dict_and_return() #! Run this inside of this __init__ function. If not, it will try to find a complete "agent-config.json" as soon as you boot up the server since this whole class gets imported and loaded.
        subprocess.run(f"mkdir -p {os.path.expanduser(self.config.path_to_runner)}", shell=True) #* Won't fail if the directory already exists

    #* =============== PRIVATE METHODS ===============

    def _move_to_runner_dir(self):
        expanded_path_to_runner = os.path.expanduser(self.config.path_to_runner)
        os.chdir(expanded_path_to_runner) #* If I ran "cd actions-runner" here: it will not persist to the next subprocess.


    def _download_tarball(self):
        download_tarball(self.config.tarball_file_name)


    def _check_shasum(self):
        check_shasum(self.config.tarball_file_name)


    def _extract_and_delete_tarball(self):
        extract_and_delete_tarball(self.config.tarball_file_name)


    def _configure_and_start_runner(self):
        configure_and_start_runner(self.config.target_github_repository, self.config.runner_token)


    #* =============== PUBLIC METHODS ===============


    def setup_runner_from_scratch(self):
        self._move_to_runner_dir()
        self._download_tarball()
        self._check_shasum()
        self._extract_and_delete_tarball()
        self._configure_and_start_runner()
        print(Back.GREEN + 'Success' + Back.RESET)
        os.chdir(self.original_dir)

    def download_and_extract(self):
        self._move_to_runner_dir()
        self._download_tarball()
        self._check_shasum()
        self._extract_and_delete_tarball()
        os.chdir(self.original_dir)

    def configure_and_start_runner(self):
        self._move_to_runner_dir()
        self._configure_and_start_runner()
        os.chdir(self.original_dir)