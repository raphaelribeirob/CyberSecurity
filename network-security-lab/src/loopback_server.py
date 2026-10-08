"""Small, educational HTTP server bound to 127.0.0.1 only."""

from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class LabHandler(BaseHTTPRequestHandler):
    """Respond to fixed, non-sensitive routes for local traffic analysis."""

    ROUTES = {
        "/health": (200, b"ok"),
        "/lesson": (200, b"TCP carries HTTP messages on this local lab."),
    }

    def do_GET(self) -> None:
        status, body = self.ROUTES.get(self.path, (404, b"not found"))
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


def create_server(port: int = 8765) -> ThreadingHTTPServer:
    """Create a local-only server. Port 0 chooses a free port for tests."""
    if not 0 <= port <= 65535:
        raise ValueError("port must be between 0 and 65535")
    return ThreadingHTTPServer(("127.0.0.1", port), LabHandler)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local-only HTTP training server")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = create_server(args.port)
    host, port = server.server_address
    print(f"Lab server on http://{host}:{port}; stop with Ctrl+C", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping lab server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
