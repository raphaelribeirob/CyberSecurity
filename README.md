# CyberSecurity — Learning Portfolio

> **Status: learning in progress.** This repository documents authorized, reproducible security labs during my transition into cybersecurity. It does **not** claim prior professional cybersecurity experience.

## Career objective
Build a strong foundation in networking, operating systems and security operations, then specialize in cloud security and security engineering. Long-term target: US-based companies that explicitly support remote work from Brazil.

## Learning path
- Cisco Networking Academy — Introduction to Cybersecurity (**in progress; update only after completing it**)
- Networking, Linux and Windows fundamentals — **planned**
- SOC monitoring, incident investigation and cloud security — **planned**

## Projects

| Project | Goal | Current status |
| --- | --- | --- |
| [Network Security Lab](network-security-lab/README.md) | Observe and explain authorized local HTTP/TCP traffic using Python and Wireshark | Starter code available; personal investigation pending |
| [SOC Detection Lab](soc-detection-lab/README.md) | Collect controlled logs, detect and triage simulated activity | Planned |
| [Cloud Security Lab](cloud-security-lab/README.md) | IAM least privilege, audit logging, secure cloud configuration | Planned |

## Documentation
- [Learning roadmap](docs/ROADMAP.md)
- [Start here — Portuguese](docs/GUIA_PTBR.md)
- [Lab report template](docs/LAB_REPORT_TEMPLATE.md)
- [Recruiter-ready portfolio checklist](docs/RECRUITER_CHECKLIST.md)
- [Lab safety](SECURITY.md)

## How to evaluate the work
1. Review lab scope, architecture, requirements and reproducible steps.
2. Read the author's dated and sanitized evidence once an exercise has actually been completed.
3. Run automated code tests where available.
4. Ask the author to explain findings and limitations without a script.

**Evidence policy:** Templates and example code are not proof that an exercise has been personally completed. Lab reports will distinguish expected from observed results.

## Safety principles
Labs run only in owned or explicitly authorized environments. No secrets, personal data, raw network captures or customer information are committed. Tutorial code is not represented as professional experience.

## Tools
Python 3.10+ standard library, Wireshark (optional separate installation), GitHub Actions. The example HTTP server binds only to 127.0.0.1.
