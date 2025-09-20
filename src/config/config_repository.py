import json
from config.config_model import ValidAgentConfig # pylint: disable=all #type: ignore

class ConfigRepository:

    #* =============== PRIVATE METHODS ===============

    def _get_config_dict(self):
        with open("agent-config.json", "r") as f:
            config_dict = json.load(f)
        return config_dict
    


    #* =============== PUBLIC METHODS ===============
    
    def validate_local_config_and_return(self) -> ValidAgentConfig:
        config_dict = self._get_config_dict() 

        #*Validating config and getting it as object
        config = ValidAgentConfig(**config_dict)
        return config
    

    def save_config_object(self, valid_config_object: ValidAgentConfig):
        with open("agent-config.json", "w") as f:
            json.dump(valid_config_object.model_dump(), f, indent=4)


