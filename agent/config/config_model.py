from pydantic import BaseModel


class ValidRunnerConfig(BaseModel):
    runner_installation_dir: str = "~/Desktop/cheese_cake/actions-runner"
    tarball_file_name: str = "actions-runner-linux-x64-2.328.0.tar.gz"
    target_github_repository: str
    runner_token: str


class ValidAgentConfig(BaseModel):
    runner_config: ValidRunnerConfig | None = None