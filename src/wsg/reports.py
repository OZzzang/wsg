from wsg.stats import Summary

def print_report(summary: Summary, url: str, method: str) -> None:
    '''
    Print the summary report of the WSG application.
    '''
    print(f'Target: {method} {url}')
    print("=== Load Test Results ===")
    print(f'Total requests: {summary.count}')
    print(f'Successful requests: {summary.success_count}')
    print(f'Failed requests: {summary.error_count}')
    print(f'Error rate: {summary.error_rate:.2%}')
    print("=== Load Test Latency Metrics ===")
    print(f'Min latency: {summary.latency_min * 1000:.2f} ms')
    print(f'Max latency: {summary.latency_max * 1000:.2f} ms')
    print(f'Mean latency: {summary.latency_mean * 1000:.2f} ms')
    print(f'50th percentile latency: {summary.p50 * 1000:.2f} ms')
    print(f'90th percentile latency: {summary.p90 * 1000:.2f} ms')
    print(f'95th percentile latency: {summary.p95 * 1000:.2f} ms')
    print(f'99th percentile latency: {summary.p99 * 1000:.2f} ms')
    print("=== Load Test Throughput ===")
    print(f'Throughput Min: {summary.throughput_min:.2f} requests/sec')
    print(f'Throughput Max: {summary.throughput_max:.2f} requests/sec')
    print(f'Throughput Mean: {summary.throughput_mean:.2f} requests/sec')
    print("=== Status Codes ===")
    for code, count in summary.status_codes.items():
        print(f'  {code}: {count}')