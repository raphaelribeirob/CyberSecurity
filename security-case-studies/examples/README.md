# Standalone synthetic security examples

Original educational code: **not extracted from private Instant projects**.

## Run

From the repository root:

```bash
python -m unittest discover -s security-case-studies/examples/tests -v
```

All inputs use fabricated account IDs, a fake HMAC secret and deterministic timestamps. No network requests, cloud resources or real payments are involved.

## Demonstrated boundaries
- Object-level access denial for cross-account requests and revoked relationships
- Explicit consent version and guardian/child scoping
- Timestamped MAC verification against modified/stale/malformed payloads
- In-process rate limiting and exact-format host allowlisting

## Not demonstrated
- A real application's production authorization
- Vendor webhook full lifecycle, deduplication or idempotency
- Distributed rate limiting, load balancer trust or multi-region state
- Effectiveness of an OWASP security scan
- A successful penetration test

**Security engineering lesson:** isolated unit tests are useful but do not imply correct deployment, integration or operations.
