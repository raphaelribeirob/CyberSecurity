# CyberSecurity — Learning Portfolio

> **Status: learning in progress.** This repository documents authorized, reproducible security labs during my transition into cybersecurity. It does **not** claim prior professional cybersecurity experience.

## Career objective
Build a strong foundation in networking, operating systems and security operations, then specialize in cloud security and security engineering. Long-term target: international employers that accept English-speaking applicants from Brazil, including eligible US and European positions.

## Learning path
- Cisco Networking Academy — Introduction to Cybersecurity (**in progress; update only after completing it**)
- Networking, Linux and Windows fundamentals — **planned**
- SOC monitoring, incident investigation and cloud security — **planned**

## Independent learning labs

| Project | Goal | Current status |
| --- | --- | --- |
| [Network Security Lab](network-security-lab/README.md) | Observe and explain authorized local HTTP/TCP traffic using Python and Wireshark | Starter code available; personal investigation pending |
| [SOC Detection Lab](soc-detection-lab/README.md) | Collect controlled logs, detect and triage simulated activity | Planned |
| [Cloud Security Lab](cloud-security-lab/README.md) | IAM least privilege, audit logging, secure cloud configuration | Planned |

## Applied security case studies — Instant projects

I reviewed security-oriented source code and tests in private SaaS projects that I worked on. The public studies describe **security concepts and observed code structures**, not proof of successful production deployment or a third-party audit. The demonstrator code uses synthetic identities, events and traffic and is deliberately independent from the private products.

| Project | Security engineering theme | Evidence maturity |
| --- | --- | --- |
| [DotSpeak](security-case-studies/dotspeak-access-control/README.md) | Object-level authorization, consent gates and usage limits | Source reviewed; independent synthetic tests added; production not assessed |
| [InstantStudy](security-case-studies/instantstudy-webhook-security/README.md) | Webhook HMAC verification, freshness and billing trust boundaries | Source reviewed; independent synthetic tests added; production not assessed |
| [InstantCloser](security-case-studies/instantcloser-api-hardening/README.md) | Rate limits, input validation and trusted hosts | Source reviewed; independent synthetic tests added; production not assessed |
| [InstantSpeak / InstantBible](security-case-studies/instant-devsecops-pipeline/README.md) | Security checks in CI, dependency scanning and passive DAST | Workflow/configuration reviewed; CI outcome in private projects not asserted |

**All case studies are works in progress.** See the [case-study index](security-case-studies/README.md) and [disclosure and evidence policy](security-case-studies/EVIDENCE_POLICY.md).

## Run public example tests

```bash
python -m unittest discover -s network-security-lab/tests -v
python -m unittest discover -s security-case-studies/examples/tests -v
```

These tests verify **educational example code only**; they do not run against live Instant services.

## Documentation
- [Learning roadmap](docs/ROADMAP.md)
- [Start here — Portuguese](docs/GUIA_PTBR.md)
- [Lab report template](docs/LAB_REPORT_TEMPLATE.md)
- [Recruiter-ready portfolio checklist](docs/RECRUITER_CHECKLIST.md)
- [Lab safety](SECURITY.md)

## How to evaluate the work
1. Review lab scope, architecture, requirements and reproducible steps.
2. Read dated, sanitized evidence once an exercise has actually been completed.
3. Run automated code tests where available.
4. Ask the author to explain findings and limitations without a script.

**Evidence policy:** Templates and example code are not proof that an exercise has been personally completed. Automated test success does not establish a deployed product's security posture.

## Safety principles
Labs run only in owned or explicitly authorized environments. No secrets, personal data, raw network captures or customer information are committed. Tutorial code is not represented as professional experience.

## Tools
Python 3.10+ standard library, Wireshark (optional separate installation), GitHub Actions. The example HTTP server binds only to 127.0.0.1.
