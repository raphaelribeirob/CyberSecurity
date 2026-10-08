# Network Security Lab 01 — Authorized localhost HTTP traffic

**Status:** starter implementation available; personal packet analysis and investigation report **not completed yet**.

## Goal
Observe a TCP connection and cleartext HTTP request/response between a local client and server. Explain the difference between TCP and HTTP and why sensitive communications should use HTTPS.

## Topology
Client (Python urllib) -> 127.0.0.1:8765 -> Local Python HTTP server.
Capture your **own** loopback traffic with Wireshark. No cloud services or third-party targets.

## Prerequisites
- Python 3.10+.
- Optional Wireshark, installed separately; on Windows use the Npcap loopback capture adapter, on Linux/macOS use lo/lo0.

## Execute
From the repository root, in terminal A:

    python network-security-lab/src/loopback_server.py --port 8765

Start capturing on the loopback adapter in Wireshark; use the display filter `tcp.port == 8765`. In terminal B:

    python network-security-lab/src/loopback_client.py --port 8765

Expected responses (**not learner evidence**):
- GET /health — HTTP 200, body ok
- GET /lesson — HTTP 200, educational text
- GET /missing — HTTP 404, body not found

Stop the server with Ctrl+C.

## Investigation questions
1. What IP and TCP port are visible? Why is 127.0.0.1 local?
2. Can you identify the SYN, SYN-ACK and ACK handshake?
3. Locate GET /health. What are the HTTP method and status?
4. How does /missing differ from /lesson?
5. Is HTTP content visible? What would HTTPS change?
6. What conclusions **cannot** be drawn from this exercise?

## Run automated tests

    python -m unittest discover -s network-security-lab/tests -v

These tests validate the local example app, **not** your Wireshark interpretation.

## Completion checklist
- [ ] Personally ran server/client and tests.
- [ ] Captured only authorized loopback traffic.
- [ ] Wrote a dated report of actual observations and limitations.
- [ ] Sanitized findings before publication.

Use [the report template](../docs/LAB_REPORT_TEMPLATE.md), then place the final written report in the evidence folder. Do not upload raw PCAPs, secrets or personal data.
