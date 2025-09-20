from pydantic import BaseModel


class ValidRunnerConfig(BaseModel):
    runner_installation_dir: str | None = "~/Desktop/cheese_cake/actions-runner"
    tarball_file_name: str | None = "actions-runner-linux-x64-2.328.0.tar.gz"
    target_github_repository: str | None = None
    runner_token: str | None = None


class ValidAgentConfig(BaseModel):
    runner_config: ValidRunnerConfig | None = None