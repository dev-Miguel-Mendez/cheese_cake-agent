from typing import Any
from fastapi import FastAPI, Request
from agent.controllers.configure_runner.runner_class import SelfHostedRunner 
from agent.config.config_model import ValidRunnerConfig
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
    return {'hello': 'world'}




@cheese_cake_server.post("/client/set-runner-config")
def set_client_config_file(request: ValidRunnerConfig) -> DefaultResponse:

    config_object = config_repository.validate_local_config_and_return()
    config_object.runner_config = request

    config_repository.save_config_object(config_object)
    return {'success': True, "message": "Config saved.", "data": None}
    