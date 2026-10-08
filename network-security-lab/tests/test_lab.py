"""Unit tests for local-only teaching server and client."""

import sys
import threading
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from loopback_client import request
from loopback_server import create_server


class LabSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = create_server(0)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def test_uses_loopback_only(self):
        self.assertEqual(self.server.server_address[0], "127.0.0.1")

    def test_health(self):
        self.assertEqual(request(self.port, "/health"), (200, "ok"))

    def test_lesson(self):
        self.assertEqual(
            request(self.port, "/lesson"),
            (200, "TCP carries HTTP messages on this local lab."),
        )

    def test_missing_returns_404(self):
        self.assertEqual(request(self.port, "/missing"), (404, "not found"))

    def test_cannot_choose_external_path(self):
        with self.assertRaises(ValueError):
            request(self.port, "/admin")

    def test_port_bounds(self):
        with self.assertRaises(ValueError):
            create_server(70000)


if __name__ == "__main__":
    unittest.main()
