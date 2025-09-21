
import subprocess
import questionary
from typing import Callable, Dict, Any
from agent.controllers.configure_runner.runner_class import SelfHostedRunner 
import agent.bootstrap_env # type: ignore # pylint: disable=unused-import







runner = SelfHostedRunner()

actions: Dict[str, Callable[[], Any]] = {
    "Set up self-hosted runner from scratch": lambda: (
        runner.setup_runner_from_scratch(),
        print(" You can pass multiple functions to a Lambda.")
    ),
    "Download self-runner and extract": runner.download_and_extract,
    "Run 'configure.sh' and start runner": runner.configure_and_start_runner,
    "Print current working directory (for self-hosted runner)": lambda: subprocess.run("pwd"),
    "Exit": lambda: exit(0)

}


def setup_runner():
    subprocess.run("clear") #* Clear terminal

    

    while True:

        result = questionary.prompt([
            {
                "type": "select",
                "name": "action",
                "message": "What do you want to do?",
                "choices": list(actions.keys())
            }
        ])

        actions[result["action"]]()
            
setup_runner()