from dataclasses import dataclass
from apiload.config import Config
import time
import httpx
import asyncio

@dataclass
class Result:
    '''
    Result class to store the outcome of each request.
    '''
    status_code: int | None
    elapsed: float
    error: str | None
    start_time: float

async def send_request(client: httpx.AsyncClient, semaphore: asyncio.Semaphore, config: Config) -> Result:
    '''
    Send a single HTTP request using the provided client and configuration.
    '''
    start = time.perf_counter()
    try:
        async with semaphore:
            response = await client.request(
                config.method, config.url,
                headers=config.headers,
                content=config.body,
                timeout=config.timeout,
            )
        elapsed = time.perf_counter() - start
        return Result(status_code=response.status_code, elapsed=elapsed, error=None, start_time=start)
    except Exception as e:
        elapsed = time.perf_counter() - start
        return Result(status_code=None, elapsed=elapsed, error=str(e), start_time=start)