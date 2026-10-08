# Applied SaaS security — case study index

**Purpose:** Learn to reason about security engineering in software projects, then create reproducible evidence suitable for junior AppSec / Security Engineering interviews.

## What was actually reviewed
On 2026-10-08, a source-only review of security-related files in the owner's private Instant projects found:
- DotSpeak: verified guardian context checks, cross-guardian access denial, consent-version checks, bounded usage behavior and unit-test cases.
- InstantStudy: webhook HMAC SHA-256 verification, timestamp tolerance, comparison safeguards and allowlisted billing offers, plus unit-test cases.
- InstantCloser: tests for API request-size bounds, rate limit responses and trusted host validation.
- InstantSpeak and InstantBible: declared security CI checks, web security hardening, dependency vulnerability checks and passive scanning configuration.

**Review limit:** This is not an independent penetration test or an assessment of live deployments. Private project tests were *read*, not executed in this review. No claims about exploitable vulnerabilities, compliance certification or production efficacy are made.

## Public learning artifacts

| Case | Threat / trust boundary | Proof in this repository |
| --- | --- | --- |
| [DotSpeak](dotspeak-access-control/README.md) | An authenticated account accesses another user's child or bypasses an authorization/consent gate | Independent synthetic access/consent tests |
| [InstantStudy](instantstudy-webhook-security/README.md) | A spoofed or modified payment notification crosses into internal entitlement state | Independent synthetic HMAC and freshness tests |
| [InstantCloser](instantcloser-api-hardening/README.md) | Request flooding or manipulated Host header reaches API handlers | Independent in-memory rate and host validation tests |
| [Instant DevSecOps](instant-devsecops-pipeline/README.md) | Insecure changes are not surfaced or blocked during release | Review of documented CI controls; further CI evidence needed |

The example implementation in [examples/](examples/) is **original educational demonstration code** with fictional inputs. It is not a copy of private Instant source and should not be used in production.

## Honest evidence levels
1. **Source reviewed:** a control or test was found in an accessible repository.
2. **Synthetic demo tested:** public standalone educational implementation was tested.
3. **Project test executed:** a test was run against actual project code with results retained.
4. **Deployment tested:** a controlled authorized assessment produced deployment evidence.

At present these studies reach level 1; examples may reach level 2 after CI reports success. They do not reach levels 3 or 4.

## Next milestones
- Reproduce each documented test and explain the threat in plain English.
- Add dated redacted test outputs with clear tool versions.
- Add a threat model and risk acceptance rationale for each case.
- Request permission and scope before any future deployment or endpoint testing.
- Record precisely what the author personally designed, implemented, reviewed and learned.

See [Evidence and disclosure policy](EVIDENCE_POLICY.md).
