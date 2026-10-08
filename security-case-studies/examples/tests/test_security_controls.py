"""Public tests for entirely synthetic controls, not private Instant apps."""

from __future__ import annotations

import hashlib
import hmac
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from security_controls import (
    InMemoryRateLimiter,
    can_access_child,
    has_current_consent,
    trusted_host,
    verify_synthetic_webhook,
)


class ObjectAuthorizationTests(unittest.TestCase):
    def test_authorized_guardian(self) -> None:
        self.assertTrue(can_access_child("alice", "child-1", {("alice", "child-1")}))

    def test_other_guardian_cannot_access_child(self) -> None:
        self.assertFalse(can_access_child("mallory", "child-1", {("alice", "child-1")}))

    def test_unverified_identity_is_denied(self) -> None:
        self.assertFalse(can_access_child(None, "child-1", {("alice", "child-1")}))

    def test_revoked_relationship_denied(self) -> None:
        self.assertFalse(can_access_child("alice", "child-1", set()))

    def test_current_consent_accepted(self) -> None:
        record = dict(guardian="alice", child="child-1", version="v2", granted=True)
        self.assertTrue(has_current_consent("alice", "child-1", record, "v2"))

    def test_stale_consent_denied(self) -> None:
        record = dict(guardian="alice", child="child-1", version="v1", granted=True)
        self.assertFalse(has_current_consent("alice", "child-1", record, "v2"))

    def test_wrong_owner_consent_denied(self) -> None:
        record = dict(guardian="other", child="child-1", version="v2", granted=True)
        self.assertFalse(has_current_consent("alice", "child-1", record, "v2"))

    def test_revoked_consent_denied(self) -> None:
        record = dict(guardian="alice", child="child-1", version="v2", granted=False)
        self.assertFalse(has_current_consent("alice", "child-1", record, "v2"))


class WebhookAuthenticationTests(unittest.TestCase):
    now = 2_000_000_000
    secret = "demo-only-not-a-real-key"

    def signed(self, body: bytes, ts: int | None = None) -> str:
        ts = self.now if ts is None else ts
        sig = hmac.new(
            self.secret.encode("utf-8"),
            str(ts).encode("ascii") + b":" + body,
            hashlib.sha256,
        ).hexdigest()
        return f"ts={ts};h1={sig}"

    def test_valid_webhook(self) -> None:
        body = b'{"event":"test.completed"}'
        self.assertTrue(verify_synthetic_webhook(body, self.signed(body), self.secret, now=self.now))

    def test_changed_body_rejected(self) -> None:
        body = b'{"event":"test.completed"}'
        self.assertFalse(verify_synthetic_webhook(body + b"!", self.signed(body), self.secret, now=self.now))

    def test_old_timestamp_rejected(self) -> None:
        body = b"{}"
        self.assertFalse(verify_synthetic_webhook(body, self.signed(body, self.now - 301), self.secret, now=self.now))

    def test_future_timestamp_rejected(self) -> None:
        body = b"{}"
        self.assertFalse(verify_synthetic_webhook(body, self.signed(body, self.now + 301), self.secret, now=self.now))

    def test_missing_signature_rejected(self) -> None:
        self.assertFalse(verify_synthetic_webhook(b"{}", "", self.secret, now=self.now))

    def test_malformed_multiple_headers_rejected(self) -> None:
        body = b"{}"
        self.assertFalse(verify_synthetic_webhook(body, self.signed(body) + ";h1=bad", self.secret, now=self.now))

    def test_oversized_body_rejected(self) -> None:
        body = b"x" * (1024 * 1024 + 1)
        self.assertFalse(verify_synthetic_webhook(body, self.signed(body), self.secret, now=self.now))

    def test_wrong_secret_rejected(self) -> None:
        body = b"{}"
        self.assertFalse(verify_synthetic_webhook(body, self.signed(body), "other-fake-key", now=self.now))


class ApiHardeningTests(unittest.TestCase):
    def test_rate_cap(self) -> None:
        limiter = InMemoryRateLimiter(limit=2, window_seconds=60)
        self.assertTrue(limiter.allow("client", now=100))
        self.assertTrue(limiter.allow("client", now=101))
        self.assertFalse(limiter.allow("client", now=102))

    def test_rate_limit_is_per_identity(self) -> None:
        limiter = InMemoryRateLimiter(limit=1, window_seconds=60)
        self.assertTrue(limiter.allow("a", now=100))
        self.assertTrue(limiter.allow("b", now=100))

    def test_rate_limit_expires(self) -> None:
        limiter = InMemoryRateLimiter(limit=1, window_seconds=60)
        self.assertTrue(limiter.allow("client", now=100))
        self.assertTrue(limiter.allow("client", now=160))

    def test_missing_identity_denied(self) -> None:
        limiter = InMemoryRateLimiter(limit=1, window_seconds=60)
        self.assertFalse(limiter.allow("", now=100))

    def test_host_allowlist(self) -> None:
        self.assertTrue(trusted_host("example.test", {"example.test"}))
        self.assertFalse(trusted_host("evil.example.test", {"example.test"}))
        self.assertFalse(trusted_host("example.test@evil.test", {"example.test"}))
        self.assertFalse(trusted_host("example.test.evil.test", {"example.test"}))

    def test_invalid_window_configuration(self) -> None:
        with self.assertRaises(ValueError):
            InMemoryRateLimiter(limit=0, window_seconds=60)


if __name__ == "__main__":
    unittest.main()
