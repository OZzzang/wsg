# wsg

API load testing tool designed for performance visualization. Sends concurrent
requests to an endpoint and produces a latency/throughput graph from the
results.

## Install

```bash
uv sync
```

## Usage

```bash
wsg <url> [options]
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-X`, `--method` | HTTP method to use | `GET` |
| `-n`, `--total_requests` | Total number of requests to send | `100` |
| `-c`, `--concurrency` | Number of concurrent requests | `10` |
| `-H`, `--headers` | HTTP headers, e.g. `-H "Authorization: Bearer xyz"` | none |
| `-d`, `--body` | Request body for POST/PUT requests | none |
| `--timeout` | Timeout per request in seconds | `10.0` |
| `-o`, `--output_path` | Path to save the output graph | `results.png` |

### Example

```bash
wsg https://api.example.com/ping -n 500 -c 20 -o load_test.png
```

This sends 500 requests at a concurrency of 20 and saves a latency
distribution + throughput-over-time chart to `load_test.png` in the current
directory.
