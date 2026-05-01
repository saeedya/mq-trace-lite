# MQ Native Docker Strategy

## Problem

pymqi requires IBM MQ client libraries and headers (e.g., cmqc.h).

These dependencies are not available on developer laptops by default.

---

## Decision

MQ native support will run inside a dedicated Docker container.

---

## Target Image

The Docker image will include:

- Python runtime
- pymqi
- IBM MQ Client libraries (/opt/mqm)
- Required headers (cmqc.h, etc.)

---

## Why Docker

- Avoid installing MQ client on every developer machine
- Ensure consistent runtime across environments
- Enable CI/CD compatibility
- Match production-like behavior

---

## Architecture

```text
CLI (mqtrace)
   ↓
Adapter Layer
   ↓
MQ Native Client (pymqi inside Docker)
   ↓
IBM MQ
```

---

## Open Questions

- Which base image to use? (ibmcom/mqclient vs custom)
- How to handle credentials securely?
- How to support multi-environment configs?

---

## Status

Planned