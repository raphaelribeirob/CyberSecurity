# InstantCloser — API rate limits and input hardening (case study)

**Status:** private source reviewed; public demonstration added; **production posture not measured**.

## Security problem
Publicly reachable APIs may be exposed to resource exhaustion, malformed payloads, forged Host values and inappropriate access. Controls should be defined at the correct trust boundary and tested with both allowed and denied requests.

## Observed in the owner's private source (2026-10-08)
- A test expects oversized inbound message content to receive HTTP 422.
- A rate-limit test expects the third request to receive HTTP 429 when the configured allowance is two.
- A trusted-host test expects an unapproved hostname to receive HTTP 400.

These are **test definitions seen in source**, not independently executed results or evidence of production protection.

## Control-to-threat mapping

| Threat | Control discussed | Evidence not yet collected |
| --- | --- | --- |
| Excessive request rate | Limit requests by identity or IP, with meaningful responses | Deployment traffic tests, distributed limiter behavior |
| Oversized/malformed payload | Enforce request schemas and body limits | Behavior across all handlers and request types |
| Untrusted Host | Validate host using configured allowed hostnames | Proxy/header trust boundary, ingress integration |
| Unauthorized requests | Authentication and authorization before sensitive operations | Endpoint authorization tests |

## Synthetic exercise
Read [examples/security_controls.py](../examples/security_controls.py) and its unit tests. The example rate limiter is deliberately **in-memory and single-process only**. It is insufficient for a distributed production environment. The sample hostname validation is an exact-format check, not a replacement for a framework's trusted-host middleware.

## Discussion prompts
- What happens if traffic is split across 10 replicas?
- Why is a rate limit not a substitute for authentication and quotas?
- How could untrusted proxy headers change the threat model?
- Which protections belong at CDN, ingress, application and database layers?

## Acceptance criteria
- [ ] Explain 200 / 400 / 422 / 429 with examples.
- [ ] Reproduce synthetic positive and negative scenarios.
- [ ] Identify production concerns (shared state, metrics, trusted proxy config).
- [ ] Record an authorized integration test on actual project code separately, if performed.
