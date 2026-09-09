import asyncio

from wsg.cli import parse_args
from wsg.runner import run
from wsg.stats import summarize
from wsg.reports import print_report

def main():
    config = parse_args()
    results, total_time = asyncio.run(run(config))
    summary = summarize(results, total_time)
    print_report(summary, config.url, config.method)