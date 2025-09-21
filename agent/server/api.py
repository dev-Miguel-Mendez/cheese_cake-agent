from typing import Any
from fastapi import FastAPI, Request
from agent.controllers.configure_runner.runner_class import SelfHostedRunner 
from agent.config.config_model import ValidRunnerConfig, ValidAgentConfig
from agent.config.config_repository import ConfigRepository
from agent.server.models import DefaultResponse


runner = SelfHostedRunner()
config_repository = ConfigRepository()

cheese_cake_server = FastAPI()

@cheese_cake_server.middleware('http')
async def print_meta(req: Request, call_next: Any):
    print(f'new request: {req.method} {req.url}')
    response = await call_next(req)
    return response







@cheese_cake_server.post("/runner/set-absolute-workdir")
def set_runner_absolute_workdir(request: Request):
    #! This will only work if the rest of the json config is already set
    return {'hello': 'world'}




@cheese_cake_server.post("/client/set-runner-config")
def set_client_config_file(request: ValidRunnerConfig) -> DefaultResponse:

    agent_config = ValidAgentConfig(runner_config=request)

    config_repository.save_config_object(agent_config)
    return {'success': True, "message": "Config saved.", "data": None}
    