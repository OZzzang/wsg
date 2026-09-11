import statistics

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from apiload.worker import Result
from apiload.stats import bucket_throughputs


def render(results: list[Result], output_path: str) -> None:
    '''
    Render a latency histogram and a throughput-over-time chart from the
    results, side by side in one figure, and save it to output_path.
    '''
    latencies_ms = [r.elapsed * 1000 for r in results if r.status_code is not None]
    throughputs = bucket_throughputs(results)

    fig, (hist_ax, throughput_ax) = plt.subplots(1, 2, figsize=(12, 5))

    bin_count = min(50, max(10, len(latencies_ms) // 2)) if latencies_ms else 10
    hist_ax.hist(latencies_ms, bins=bin_count, color="#1f77b4", edgecolor="white")
    if latencies_ms:
        mean_ms = statistics.mean(latencies_ms)
        hist_ax.axvline(mean_ms, color="black", linestyle="--", linewidth=1, label=f"Mean: {mean_ms:.0f} ms")
        hist_ax.legend()
    hist_ax.set_xlabel("Latency (ms)")
    hist_ax.set_ylabel("Number of requests")
    hist_ax.set_title("Latency Distribution")
    hist_ax.grid(axis="y", alpha=0.3)

    bucket_centers = [i + 0.5 for i in range(len(throughputs))]
    bars = throughput_ax.bar(bucket_centers, throughputs, width=0.6, color="#ff7f0e", edgecolor="black", linewidth=0.5)
    throughput_ax.bar_label(bars, fmt="%.0f")
    throughput_ax.set_xticks(range(len(throughputs) + 1))
    throughput_ax.set_ylim(0, max(throughputs, default=0) * 1.15)
    throughput_ax.set_xlabel("Time since start (s)")
    throughput_ax.set_ylabel("Requests/sec")
    throughput_ax.set_title("Throughput Over Time")
    throughput_ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_path, dpi=120)
    plt.close(fig)
