from typing import Any
from fastapi import FastAPI, Request
from agent.config.config_repository import ConfigRepository
from agent.server.controllers.set_runner_config import set_runner_config_file
from agent.server.controllers.download_and_config import download_runner_and_config

config_repository = ConfigRepository()

cheese_cake_server = FastAPI()

@cheese_cake_server.middleware('http')
async def print_meta(req: Request, call_next: Any):
    print(f'new request: {req.method} {req.url}')
    response = await call_next(req)
    return response




cheese_cake_server.post("/runner/set-config")(set_runner_config_file)

cheese_cake_server.post('/runner/download-and-config')(download_runner_and_config)
