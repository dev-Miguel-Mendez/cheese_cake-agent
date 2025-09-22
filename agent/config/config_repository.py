import json
from typing import Any
from colorama import Fore
from agent.config.config_model import ValidAgentConfig, ValidRunnerConfig, BaseRunnerConfig

#! THIS CAN EXIST WITH MISSING CONFIG
class ConfigRepository:

    def __init__(self):
        valid_agent_config = ValidAgentConfig(runner_config=BaseRunnerConfig())
        self.save_agent__config_object(valid_agent_config)
        pass

    #* =============== PRIVATE METHODS ===============

    def _get_agent_config_dict(self)-> Any:
        with open("agent-config.json", "r") as f:
            try:
                agent_config_dict: Any = json.load(f)
            except json.JSONDecodeError: #$ The json file was likely  empty.
                agent_config_dict = {}
        return agent_config_dict
    


    #* =============== PUBLIC METHODS ===============




    def validate_runner_config_and_return(self) -> ValidRunnerConfig:
        agent_config_dict = self._get_agent_config_dict()
        if "runner_config" not in agent_config_dict:
            # print('Provide a valid github repository url: ')
            # github_repository_url = input()
            # print('Provide a valid runner token: ')
            # runner_token = input()
            # valid_runner_config = ValidRunnerConfig(target_github_repository=github_repository_url, runner_token=runner_token)
            # self.save_agent__config_object(ValidAgentConfig(runner_config=valid_runner_config))
            raise Exception(Fore.RED + "No runner config found." + Fore.RESET) #! This shouldn't happen, a default config should always be set

        

        #*Validating config and getting it as object
        runner_config = ValidRunnerConfig(**agent_config_dict["runner_config"])
        return runner_config


    def save_agent__config_object(self, valid_config_object: ValidAgentConfig):
        with open("agent-config.json", "w") as f:
            json.dump(valid_config_object.model_dump(), f, indent=4)


