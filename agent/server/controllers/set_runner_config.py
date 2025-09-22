from agent.server.models import DefaultResponse
from agent.config.config_model import ValidRunnerConfig, ValidAgentConfig
from agent.config.config_repository import ConfigRepository

def set_runner_config_file(request: ValidRunnerConfig) -> DefaultResponse:
    config_repository = ConfigRepository()

    agent_config = ValidAgentConfig(runner_config=request)

    config_repository.save_agent_config_object(agent_config)
    return {'success': True, "message": "Config saved.", "data": None}