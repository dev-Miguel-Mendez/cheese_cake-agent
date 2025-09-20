# from typing import TypedDict

# class ConfigType (TypedDict):
#     runner_absolute_dir: str 


# config: ConfigType = {
#     "runner_absolute_dir": "asdAAAAAAAAA"
# }



import json

with open("agent-config.json", "r") as f:
    config_dict = json.load(f)

