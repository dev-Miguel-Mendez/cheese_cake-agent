from fastapi import FastAPI, Request
from typing import Any
from pydantic import BaseModel


class SetupRunnerRequest(BaseModel):
    action: str
    runner_installation_dir_from_home: str
    target_github_repository: str
    runner_token: str



cheese_cake_server = FastAPI()

@cheese_cake_server.middleware('http')
async def print_meta(req: Request, call_next: Any):
    print(f'new request: {req.method} {req.url}')
    response = await call_next(req)
    return response


@cheese_cake_server.post('/runner/setup')
def test(request: SetupRunnerRequest):

    print(request)

    return {'hello': 'world'}