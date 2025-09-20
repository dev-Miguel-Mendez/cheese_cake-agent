from pydantic import BaseModel



class ValidRunnerConfig(BaseModel):
    runner_installation_dir: str | None
    tarball_file_name: str | None
    target_github_repository: str 
    runner_token: str 


class ValidAgentConfig(BaseModel):
    runner_config: ValidRunnerConfig