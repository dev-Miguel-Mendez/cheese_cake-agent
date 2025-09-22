from agent.server.models import DefaultResponse
from agent.config.config_model import ValidRunnerConfig, ValidAgentConfig
from agent.server.api import config_repository

def set_runner_config_file(request: ValidRunnerConfig) -> DefaultResponse:

    agent_config = ValidAgentConfig(runner_config=request)

    config_repository.save_agent_config_object(agent_config)
    return {'success': True, "message": "Config saved.", "data": None}