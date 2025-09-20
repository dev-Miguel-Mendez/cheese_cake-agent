from fastapi import FastAPI, Request
from typing import Any
from pydantic import BaseModel


class SetupRunnerRequest(BaseModel):
    # runner_installation_dir_from_home: str
    target_github_repository: str
    runner_token: str



cheese_cake_server = FastAPI()

@cheese_cake_server.middleware('http')
async def print_meta(req: Request, call_next: Any):
    print(f'new request: {req.method} {req.url}')
    response = await call_next(req)
    return response


@cheese_cake_server.post('/runner/setup')
def setup_runner(request: SetupRunnerRequest):

    target_github_repository, runner_token = request.target_github_repository, request.runner_token

    print(target_github_repository)
    print(runner_token)

    print(request)

    return {'hello': 'world'}



@cheese_cake_server.post("/client/set-workdir")
def set_client_workdir(request: Request):
    pass


@cheese_cake_server("/client/set-config_file")
def set_client_config_file():
    