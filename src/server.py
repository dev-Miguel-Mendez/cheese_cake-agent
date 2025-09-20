from typing import Any
from fastapi import FastAPI, Request
import uvicorn
from controllers.configure_runner.runner_class import SelfHostedRunner 
from config.config_model import ValidRunnerConfig
from config.config_repository import ConfigRepository

runner = SelfHostedRunner()

cheese_cake_server = FastAPI()

@cheese_cake_server.middleware('http')
async def print_meta(req: Request, call_next: Any):
    print(f'new request: {req.method} {req.url}')
    response = await call_next(req)
    return response


# @cheese_cake_server.post('/runner/setup')
# def setup_runner(request: SetupRunnerRequest):

#     target_github_repository, runner_token = request.target_github_repository, request.runner_token

#     print(target_github_repository)
#     print(runner_token)

#     print(request)

#     return {'hello': 'world'}



@cheese_cake_server.post("/runner/set-absolute-workdir")
def set_runner_absolute_workdir(request: Request):
    # config['runner_absolute_dir'] = request.json()["runner_absolute_dir"]
    runner.set_runner_absolute_workdir("LOL")
    return {'hello': 'world'}

@cheese_cake_server.post("/client/set-config_file")
def set_client_config_file(request: ValidRunnerConfig):
    config_repository = ConfigRepository()
    config_repository.save_config_object(request)




if __name__ == "__main__":
    #- Running Uvicorn as a script instead of as a module.
    #$ Need to pass application as import string
    uvicorn.run("server:cheese_cake_server",  host="0.0.0.0", port=3001, reload=True)