import asyncio
import httpx
import sys
import time

from wsg.config import Config
from wsg.worker import Result, send_request

async def run(config: Config) -> tuple[list[Result], float]:
    '''
    Run the load test using the provided configuration.
    '''
    async with httpx.AsyncClient() as client:
        semaphore = asyncio.Semaphore(config.concurrency)
        run_start = time.perf_counter()
        tasks = [send_request(client, semaphore, config) for _ in range(config.total_requests)]

        results = []
        for coro in asyncio.as_completed(tasks):
            results.append(await coro)
            print(f"\rProgress: {len(results)}/{len(tasks)} ({len(results) / len(tasks):.0%})", end="", file=sys.stderr, flush=True)
        print(file=sys.stderr)

        for result in results:
            result.start_time -= run_start
        return (results, total_time := time.perf_counter() - run_start)