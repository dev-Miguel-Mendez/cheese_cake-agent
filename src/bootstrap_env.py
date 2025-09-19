import os
from colorama import Fore
from dotenv import load_dotenv 



load_dotenv('.env')

REQUIRED_ENV_VARS= [
    "runner_INSTALLATION_DIR_FROM_HOME",
    "TARGET_GITHUB_REPOSITORY",
    "RUNNER_TOKEN"
]

for env_var in REQUIRED_ENV_VARS:
    if not os.environ.get(env_var):
        raise Exception(Fore.RED + f'Missing environment variable: {env_var}' + Fore.RESET)
    
print(Fore.GREEN + 'All environment variables are set.' + Fore.RESET)