"""Original, synthetic security demonstrations for learning only.

No production code, customer information or credentials from Instant projects
are included. This module is intentionally not a production security library.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
import hashlib
import hmac
import re


class AccessDenied(Exception):
    """Synthetic authorization denial."""


def can_access_child(
    verified_guardian: str | None,
    child_id: str,
    active_relationships: set[tuple[str, str]],
) -> bool:
    """Enforce an explicit guardian-child relationship (toy example)."""
    if not verified_guardian or not child_id:
        return False
    return (verified_guardian, child_id) in active_relationships


def has_current_consent(
    verified_guardian: str | None,
    child_id: str,
    record: dict[str, object] | None,
    required_version: str,
) -> bool:
    """Require active, correctly scoped and versioned consent."""
    if not verified_guardian or not child_id or not required_version or not record:
        return False
    return (
        record.get("guardian") == verified_guardian
        and record.get("child") == child_id
        and record.get("version") == required_version
        and record.get("granted") is True
    )


def verify_synthetic_webhook(
    raw_body: bytes,
    signature_header: str,
    fake_secret: str,
    *,
    now: int,
    max_skew_seconds: int = 300,
) -> bool:
    """Compare a synthetic signed payload with length/freshness checks.

    Format: ts=INTEGER;h1=LOWERCASE_HEX_SHA256. This educational format
    resembles generic timestamped MAC webhooks; it is not a vendor SDK.
    """
    if not isinstance(raw_body, bytes) or len(raw_body) > 1024 * 1024:
        return False
    if not fake_secret or max_skew_seconds <= 0:
        return False
    match = re.fullmatch(r"ts=([0-9]+);h1=([0-9a-f]{64})", signature_header)
    if match is None:
        return False
    timestamp = int(match.group(1))
    if abs(now - timestamp) > max_skew_seconds:
        return False
    expected = hmac.new(
        fake_secret.encode("utf-8"),
        str(timestamp).encode("ascii") + b":" + raw_body,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(expected, match.group(2))


@dataclass
class InMemoryRateLimiter:
    """Single-process sliding window, for unit tests only.

    This cannot coordinate requests across production workers or regions.
    """

    limit: int
    window_seconds: float

    def __post_init__(self) -> None:
        if self.limit <= 0 or self.window_seconds <= 0:
            raise ValueError("limits must be positive")
        self._history: dict[str, deque[float]] = defaultdict(deque)

    def allow(self, identity: str, *, now: float) -> bool:
        if not identity:
            return False
        history = self._history[identity]
        while history and history[0] <= now - self.window_seconds:
            history.popleft()
        if len(history) >= self.limit:
            return False
        history.append(now)
        return True


def trusted_host(host_header: str, allowed_hosts: set[str]) -> bool:
    """Very small illustrative host-allowlist check (not proxy middleware)."""
    if not isinstance(host_header, str):
        return False
    canonical = host_header.strip().lower()
    if not re.fullmatch(r"[a-z0-9.-]+(?::[0-9]{1,5})?", canonical):
        return False
    return canonical in {x.lower() for x in allowed_hosts}
