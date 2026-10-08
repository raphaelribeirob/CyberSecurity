"""Send safe GET requests to a server on the local loopback adapter."""

from __future__ import annotations

import argparse
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def request(port: int, path: str) -> tuple[int, str]:
    """Fetch a fixed path from localhost, including intentional HTTP errors."""
    if not 1 <= port <= 65535:
        raise ValueError("port must be between 1 and 65535")
    if path not in ("/health", "/lesson", "/missing"):
        raise ValueError("unsupported lab path")
    url = f"http://127.0.0.1:{port}{path}"
    try:
        with urlopen(url, timeout=3) as response:
            return response.status, response.read().decode("utf-8")
    except HTTPError as error:
        return error.code, error.read().decode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate authorized localhost HTTP requests")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    for path in ("/health", "/lesson", "/missing"):
        try:
            status, body = request(args.port, path)
        except URLError as error:
            parser.exit(1, f"Cannot reach local lab server: {error.reason}\n")
        print(f"GET {path} -> HTTP {status}; body: {body}")


if __name__ == "__main__":
    main()
