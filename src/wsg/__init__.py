import asyncio
import httpx

from wsg.cli import parse_args
from wsg.worker import send_request

async def _run_single(config):
    '''
    Run a single request using the provided configuration.
    '''
    async with httpx.AsyncClient() as client:
        result = await send_request(client, config)
        return result

def main():
    config = parse_args()
    result = asyncio.run(_run_single(config))
    print(result)