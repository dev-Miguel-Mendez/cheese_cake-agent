from agent.server.models import DefaultResponse
from agent.modules.runner_class import SelfHostedRunner


def download_runner_and_config() -> DefaultResponse:
    runner = SelfHostedRunner() #* This is instantiated only on requests because it will fail to instantiate is there is not config yet.
    runner.setup_runner_from_scratch()
    return {'success': True, "message": "Runner is set and running.", "data": None}