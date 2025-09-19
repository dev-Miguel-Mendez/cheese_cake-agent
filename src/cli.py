import subprocess
import questionary
from colorama import Fore, Back
import bootstrap_env # pylint: disable=all #type: ignore

from ops.configure_runner.runner_class import SelfHostedRunner 




def setup_runner():
    subprocess.run("clear") #* Clear terminal

    runner = SelfHostedRunner()
    

    while True:

        result = questionary.prompt([
            {
                "type": "select",
                "name": "action",
                "message": "What do you want to do?",
                "choices": [
                    "Set up self-hosted runner from scratch", 
                    "Download self-runner and extract", 
                    "Run 'configure.sh' and start runner",
                    "Print current working directory (for self-hosted runner)",
                    "Exit"
                ]
            }
        ])

        match result["action"]:
            case "Set up self-hosted runner from scratch":
                runner.setup_runner_from_scratch()
                print(Back.GREEN + 'Success' + Back.RESET)


            case "Download self-runner and extract":
                runner.download_and_extract()


            case "Run 'configure.sh' and start runner":
                runner.configure_and_start_runner()

            case "Print current working directory (for self-hosted runner)":
                print(subprocess.run('pwd',))

            case "Exit":
                exit(0)
            case _:
                raise Exception(Fore.RED + 'Unknown action.' + Fore.RESET)
            
setup_runner()