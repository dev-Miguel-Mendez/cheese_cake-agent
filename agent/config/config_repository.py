import json
import subprocess
from typing import Any
from agent.config.config_model import ValidAgentConfig, ValidRunnerConfig, BaseRunnerConfig

class ConfigRepository:
    path_to_runner = BaseRunnerConfig().path_to_runner

    def __init__(self):
        subprocess.run("touch agent-config.json", shell=True)

        #* 2. Creating agent-config.json if it doesn't exist.
        config_dict = self._get_agent_config_dict()
        if "runner_config" not in config_dict:
            #* This will generate "agent-config.json" if it doesn't exist.
            valid_agent_config = ValidAgentConfig(runner_config=BaseRunnerConfig())
            self.save_agent_config_object(valid_agent_config)



    #* =============== PRIVATE METHODS ===============

    def _get_agent_config_dict(self)-> Any:
        #$ expanduser("~") will give something like /home/username. If the path is absolute, it will just return the path.
        with open("agent-config.json", "r") as f:
            try:
                agent_config_dict: Any = json.load(f)
            except json.JSONDecodeError: #$ The json file was likely  empty.
                agent_config_dict = {}
        return agent_config_dict
    


    #* =============== PUBLIC METHODS ===============

    def validate_runner_dict_and_return(self) -> ValidRunnerConfig:


        agent_config_dict = self._get_agent_config_dict()
        print(agent_config_dict)

        #*Validating config and getting it as object
        return ValidRunnerConfig(**agent_config_dict["runner_config"])
        


    def save_agent_config_object(self, valid_config_object: ValidAgentConfig):
        #$ expanduser("~") will give something like /home/username. If the path is absolute, it will just return the path.
        with open("agent-config.json", "w") as f:
            #! Honestly still not to sure of what "serialize_as_any=True" does but it works. I was having issues where when "model_dump()" only was excluding properties that belonged to ValidRunnerConfig and not BaseRunnerConfig
            json.dump(valid_config_object.model_dump(serialize_as_any=True), f, indent=4)


