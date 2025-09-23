import subprocess
from colorama import Fore
from agent.modules.runner.runner_exception import RunnerException
import datetime

def configure_and_start_runner(target_github_repository: str, runner_token: str):
    print(Fore.BLUE + "Configuring  runner and starting runner..." + Fore.RESET)

    #* We can let this be blocking. It auto exits with a return code.
    config_run =  subprocess.run(f"./config.sh --unattended --replace --url {target_github_repository} --token {runner_token}", shell=True, capture_output=True)

    if config_run.returncode !=0:
        raise RunnerException(Fore.RED + "Configuring 'config.sh' failed POSSIBLY  DUE TO EXPIRED/INVALID TOKEN. Full error message: " + config_run.stderr.decode() + Fore.RESET)

    #* This will be pending in background because it is a FOREGROUND process. If we tried "capture_output=True" Python will keep buffering output in memory.
    # subprocess.run("./run.sh")

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    with open(f"runner_run_{timestamp}", "w") as f:
        subprocess.Popen("./run.sh", stdout=f, stderr=f)
    print(Fore.GREEN + "Runner configured and started." + Fore.RESET)
