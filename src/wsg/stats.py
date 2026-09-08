from dataclasses import dataclass

from wsg.worker import Result

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
    throughput: float
    status_codes: dict[StatusCode, int]

    def summarize(results: list[Result], total_time: float) -> 'Summary':
        '''
        Summarize the results of the WSG application.
        '''
        