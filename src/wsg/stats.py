from dataclasses import dataclass
from wsg.worker import Result
from collections import Counter

import statistics


StatusCode = int

@dataclass
class Summary:
    '''
    Summary class to hold the results of the WSG application.
    '''
    count: int
    success_count: int
    error_count: int
    error_rate: float
    latency_min: float
    latency_max: float
    latency_mean: float
    p50: float
    p90: float
    p95: float
    p99: float
    throughput_min: float
    throughput_max: float
    throughput_mean: float
    status_codes: dict[StatusCode, int]

def bucket_throughputs(results: list[Result], bucket_size: float = 1.0) -> list[float]:
    '''
    Split successful results into fixed-size time buckets by completion
    time (start_time + elapsed) and return the throughput (requests/sec)
    measured in each bucket. The last bucket is dropped whenever there is
    more than one, since it may cover only a partial slice of real time
    and would understate its rate.
    '''
    completions = [r.start_time + r.elapsed for r in results if r.status_code is not None]
    if not completions:
        return []

    bucket_counts = Counter(int(t // bucket_size) for t in completions)
    buckets = [bucket_counts[i] / bucket_size for i in sorted(bucket_counts)]

    if len(buckets) > 1:
        buckets = buckets[:-1]

    return buckets

def summarize(results: list[Result]) -> 'Summary':
    '''
    Summarize the results of the WSG application.
    '''
    success = []
    failure = []

    for i in results:
        if i.status_code != None:
            success.append(i)
        else:
            failure.append(i)

    count = len(results)
    success_count = len(success)
    error_count = len(failure)
    error_rate = error_count / count if count > 0 else 0.0

    latency_list = []
    for i in success:
        latency_list.append(i.elapsed)

    latency_min = min(latency_list) if latency_list else 0.0
    latency_max = max(latency_list) if latency_list else 0.0
    latency_mean = statistics.mean(latency_list) if latency_list else 0.0

    p50 = statistics.median(latency_list) if latency_list else 0.0
    p90 = statistics.quantiles(latency_list, n=10)[8] if latency_list else 0.0
    p95 = statistics.quantiles(latency_list, n=20)[18] if latency_list else 0.0
    p99 = statistics.quantiles(latency_list, n=100)[98] if latency_list else 0.0

    throughput_buckets = bucket_throughputs(results)
    throughput_min = min(throughput_buckets) if throughput_buckets else 0.0
    throughput_max = max(throughput_buckets) if throughput_buckets else 0.0
    throughput_mean = statistics.mean(throughput_buckets) if throughput_buckets else 0.0

    status_codes = Counter(i.status_code for i in results if i.status_code is not None)

    return Summary(
        count=count,
        success_count=success_count,
        error_count=error_count,
        error_rate=error_rate,
        latency_min=latency_min,
        latency_max=latency_max,
        latency_mean=latency_mean,
        p50=p50,
        p90=p90,
        p95=p95,
        p99=p99,
        throughput_min=throughput_min,
        throughput_max=throughput_max,
        throughput_mean=throughput_mean,
        status_codes=dict(status_codes)
    )