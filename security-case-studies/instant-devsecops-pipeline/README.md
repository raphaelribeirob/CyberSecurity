# InstantSpeak / InstantBible — Security checks in the delivery pipeline

**Status:** private workflow and security documentation reviewed; **private CI success and production security are not asserted**.

## Security problem
Application features can regress if tests, dependency checks and security scanning are not integrated into the release workflow. A "security scan exists" claim is not equivalent to a release-blocking, validated gate.

## Observed in the owner's private project files (2026-10-08)
**InstantSpeak**
- An OWASP-oriented CI workflow runs repository security contracts on push and pull request.
- A production-dependency audit is configured to fail on high and critical issues.
- A weekly/manual OWASP ZAP passive baseline scan is configured.
- The ZAP job sets `fail_action: false`, so the ZAP scan is **advisory/monitor-only** instead of a required blocking gate.
- One third-party ZAP action is pinned by SHA in the reviewed workflow; other workflow actions use tags.

**InstantBible**
- Security documentation describes secure web headers, non-exposure of server secrets in a Flutter app, dependency scans with OSV and OWASP ZAP monitoring.
- Security-oriented test definitions were observed for configuration and header expectations.

**Important:** these observations are about source configuration and stated intentions. No private workflow run logs, security scan findings or deployed header checks were validated in this case study.

## Threat / control matrix

| Risk | Candidate control | How to validate it |
| --- | --- | --- |
| Vulnerable package published | Dependency vulnerability scanning | Known vulnerable dependency test in isolated branch and build gate behavior |
| Secret committed | Secret scanning / repository hygiene | Synthetic harmless test secret and alert workflow in safe environment |
| Insecure web defaults | CSP and security headers | HTTP response checks against authorized staging build |
| Web application issues | Passive DAST with OWASP ZAP | Scan reports, scope, false positives and risk acceptance |
| Unsafe release | Required status checks | A deliberately failing test should prevent merge |

## CI design proposed for portfolio
1. Deterministic unit tests on every PR.
2. Static checking, dependency audit and secrets protection.
3. Manual/periodic authorized passive DAST scoped to staging.
4. Triage findings, track accepted risks and prevent security-critical regressions.
5. Capture links to successful and intentionally failing test runs.

**Do not scan third-party domains without scope approval. Do not claim an OWASP certification.**

## Current public GitHub evidence
The [CyberSecurity repository workflows](../../.github/workflows/) exercise only public learning examples and do not prove Instant product release security.

## Acceptance criteria
- [ ] Inspect a real private workflow run with permission.
- [ ] Distinguish advisory scanners from blocking gates.
- [ ] Show and discuss results of a controlled failing CI test.
- [ ] Pin relevant third-party GitHub Actions to full SHA.
- [ ] Document tool coverage, false positives, scope and unresolved findings.
