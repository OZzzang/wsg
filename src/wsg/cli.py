import argparse

from wsg.config import Config

def parse_args():
    '''
    Parse the command-line arguments for the API load-testing tool.
    '''
    parser = argparse.ArgumentParser(description="A simple API load-testing tool")
    parser.add_argument("url", type=str, help="The URL of the API endpoint to test")
    parser.add_argument("-X", "--method", type=str, default="GET", help="HTTP method to use (default: GET)")
    parser.add_argument("-n", "--total_requests", type=int, default=100, help="Total number of requests to send (default: 100)")
    parser.add_argument("-c", "--concurrency", type=int, default=10, help="Number of concurrent requests to send (default: 10)")
    parser.add_argument("-H", "--headers", type=str, nargs='*', help="HTTP headers to include in the requests (format: 'Header-Name: Header-Value')")
    parser.add_argument("-d", "--body", type=str, help="Request body for POST/PUT requests")
    parser.add_argument("--timeout", type=float, default=10.0, help="Timeout for each request in seconds (default: 10.0)")
    parser.add_argument("-o", "--output_path", type=str, default="results.png", help="Path to save the output results (default: results.png)")

    args = parser.parse_args()

    return Config(
        url=args.url,
        method=args.method,
        total_requests=args.total_requests,
        concurrency=args.concurrency,
        headers={header.split(":", 1)[0].strip(): header.split(":", 1)[1].strip() for header in args.headers} if args.headers else {},
        body=args.body,
        timeout=args.timeout,
        output_path=args.output_path
    )



