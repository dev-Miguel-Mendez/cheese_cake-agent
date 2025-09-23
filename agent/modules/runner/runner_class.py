from colorama import Back
from agent.config.config_repository import ConfigRepository
from agent.modules.runner.methods.move_to_dir import move_to_dir
from agent.modules.runner.methods.download_tarball import download_tarball
from agent.modules.runner.methods.check_shasum import check_shasum
from agent.modules.runner.methods.extract_and_delete_tarball import extract_and_delete_tarball
from agent.modules.runner.methods.configure_and_start_runner import configure_and_start_runner

class RunnerException(Exception):
    def __init__(self, message: str):
        self.message = message

class  SelfHostedRunner:

    runner_hash = "01066fad3a2893e63e6ca880ae3a1fad5bf9329d60e77ee15f2b97c148c3cd4e"
    RUNNER_DOWNLOAD_URL = "https://github.com/actions/runner/releases/download/v2.328.0/actions-runner-linux-x64-2.328.0.tar.gz"

    def __init__(self):
        config_repository = ConfigRepository()
        self.config = config_repository.validate_runner_config_and_return()


    #* =============== PRIVATE METHODS ===============
    def _move_to_dir(self):
        move_to_dir(self.config.runner_installation_dir)


    def _download_tarball(self):
        download_tarball(self.config.tarball_file_name, self.RUNNER_DOWNLOAD_URL)


    def _check_shasum(self):
        check_shasum(self.runner_hash, self.config.tarball_file_name)


    def _extract_and_delete_tarball(self):
        extract_and_delete_tarball(self.config.tarball_file_name)


    def _configure_and_start_runner(self):
        configure_and_start_runner(self.config.target_github_repository, self.config.runner_token)


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
