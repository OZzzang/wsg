import asyncio

from wsg.cli import parse_args
from wsg.runner import run

def main():
    config = parse_args()
    result, total_time = asyncio.run(run(config))
    print(result, total_time)