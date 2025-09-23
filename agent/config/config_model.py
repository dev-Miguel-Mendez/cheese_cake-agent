from pydantic import BaseModel

class BaseRunnerConfig(BaseModel): #* This will be used to the instantiate config_repository and output the default "agent-config.json".
    path_to_runner: str = "~/Desktop/cheese_cake/actions-runner"
    tarball_file_name: str = "actions-runner-linux-x64-2.328.0.tar.gz"


class ValidRunnerConfig(BaseRunnerConfig): #* This will be used for requests
    target_github_repository: str
    runner_token: str 


class ValidAgentConfig(BaseModel):
    runner_config: BaseRunnerConfig