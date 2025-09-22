from typing import Any
from fastapi import FastAPI, Request
from agent.controllers.runner_class import SelfHostedRunner 
from agent.config.config_model import ValidRunnerConfig, ValidAgentConfig
from agent.config.config_repository import ConfigRepository
from agent.server.models import DefaultResponse


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




@cheese_cake_server.post("/runner/set-config")
def set_client_config_file(request: ValidRunnerConfig) -> DefaultResponse:

    agent_config = ValidAgentConfig(runner_config=request)

    config_repository.save_agent_config_object(agent_config)
    return {'success': True, "message": "Config saved.", "data": None}


@cheese_cake_server.post('/runner/DO-SOMETHING-TEST')
def DO_SOMETHING_TEST() -> DefaultResponse:
    runner = SelfHostedRunner() #* This is instantiated only on requests because it will fail to instantiate is there is not config yet.
    return {'success': True, "message": "Config saved.", "data": None}