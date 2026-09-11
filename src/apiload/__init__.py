import asyncio

from apiload.cli import parse_args
from apiload.runner import run
from apiload.stats import summarize
from apiload.reports import print_report
from apiload.graph import render

def main():
    config = parse_args()
    results, _ = asyncio.run(run(config))
    summary = summarize(results)
    print_report(summary, config.url, config.method)
    render(results, config.output_path)
    print(f'Graph saved to {config.output_path}')