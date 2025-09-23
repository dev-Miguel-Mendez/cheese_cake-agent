
from typing import Callable, Dict, Any
import subprocess
import questionary
from agent.modules.runner.runner_class import SelfHostedRunner 
import agent.bootstrap_env # type: ignore # pylint: disable=unused-import








actions: Dict[str, Callable[[], Any]] = {
    "Set up self-hosted runner from scratch": lambda: (
        SelfHostedRunner().setup_runner_from_scratch(),
    ),
    "Download self-runner and extract": lambda:(SelfHostedRunner().download_and_extract()),
    "Run 'configure.sh' and start runner": lambda:(SelfHostedRunner().configure_and_start_runner()),
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