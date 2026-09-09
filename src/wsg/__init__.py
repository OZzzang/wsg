import asyncio

from wsg.cli import parse_args
from wsg.runner import run
from wsg.stats import summarize
from wsg.reports import print_report
from wsg.graph import render

def main():
    config = parse_args()
    results, _ = asyncio.run(run(config))
    summary = summarize(results)
    print_report(summary, config.url, config.method)
    render(results, config.output_path)
    print(f'Graph saved to {config.output_path}')