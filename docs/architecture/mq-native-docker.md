# MQ Native Docker Strategy

## Problem

pymqi requires IBM MQ client libraries and headers (e.g., cmqc.h).

These dependencies are not available on developer laptops by default.

---

## Decision

MQ native support will run inside a dedicated Docker container.

---

## Target Image Decision

MQ Trace Lite will use a dedicated native-client image:

```text
python:3.12-slim
+ IBM MQ C Redistributable Client
+ IBM MQ SDK headers
+ pymqi
```

The IBM MQ Server image will not be used as the base image for the CLI tool because it is too heavy and designed for running queue managers, not client applications.

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