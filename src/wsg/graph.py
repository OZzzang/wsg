import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from wsg.worker import Result


def render(results: list[Result], output_path: str) -> None:
    '''
    Render a latency histogram from the results and save it to output_path.
    '''
    latencies_ms = [r.elapsed * 1000 for r in results if r.status_code is not None]

    fig, ax = plt.subplots()
    ax.hist(latencies_ms, bins=30)
    ax.set_xlabel("Latency (ms)")
    ax.set_ylabel("Number of requests")
    ax.set_title("Latency Distribution")
    fig.savefig(output_path)
    plt.close(fig)
