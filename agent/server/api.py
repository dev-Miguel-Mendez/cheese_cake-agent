from typing import Any
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from agent.modules.runner_class import RunnerException
from agent.server.controllers.set_runner_config import set_runner_config_file
from agent.server.controllers.download_and_config import download_runner_and_config



cheese_cake_server = FastAPI()

@cheese_cake_server.middleware('http')
async def print_meta(req: Request, call_next: Any):
    print(f'new request: {req.method} {req.url}')
    response = await call_next(req)
    return response

#$ This will catch  only exceptions raised by "raise RunnerException"
@cheese_cake_server.exception_handler(RunnerException)
def handle_runner_exception(_req: Request, exc: RunnerException):
    return JSONResponse(status_code=401, content={"Error while using runner:": exc.message})


cheese_cake_server.post("/runner/set-config")(set_runner_config_file)


cheese_cake_server.post('/runner/download-and-run')(download_runner_and_config)
