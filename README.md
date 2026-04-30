# MQ Trace Lite

## Overview

MQ Trace Lite is a CLI-first debugging and incident tool for IBM MQ, designed for OpenShift environments.

It helps engineers inspect messages, understand failures, and safely debug message flows across multiple namespaces and environments.

---

## Problem

In systems using IBM MQ:

* Messages can fail and end up in Dead Letter Queues (DLQ)
* Debugging message flow is difficult
* Replay is often manual and risky
* There is no simple developer-friendly tool for inspection and recovery

---

## Solution

MQ Trace Lite provides:

* Message inspection from queues and DLQ
* Profile-based multi-environment access
* OpenShift-aware discovery (namespace → MQ)
* Structured metadata view
* Safe replay (planned)
* Audit logging (planned)

---

## Architecture

```text
CLI (Typer)
 ├── profiles
 ├── core
 └── adapters
      ├── ibmmq
      └── openshift
```

---

## Profiles

Profiles define how MQ is accessed.

Stored in:

```text
~/.mqtrace/profiles.yml
```

### Example

```yaml
profiles:
  sit-pay-engine:
    type: openshift
    environment: sit
    namespace: pay-engine
    queue_manager: QM1

  local-dev:
    type: static
    host: localhost
    port: 1414
    queue_manager: QM1
```

---

## CLI Usage

### List profiles

```bash
poetry run python -m mqtrace.cli.main profiles
```

---

### Inspect messages

```bash
poetry run python -m mqtrace.cli.main inspect \
  --profile sit-pay-engine \
  --queue TEST
```

---

## OpenShift Discovery (MVP)

Current implementation uses **fake discovery**:

```text
<queue_manager>.<namespace>.svc.cluster.local
```

Example:

```text
QM1.pay-engine.svc.cluster.local
```

---

## Setup

See:

* docs/setup.md
* docs/docker-dev.md

---

## Docker Development

Start services:

```bash
cd docker
docker compose up --build
```

Run CLI:

```bash
docker compose run --rm app python -m mqtrace.cli.main inspect \
  --profile sit-pay-engine \
  --queue TEST
```

---

## Tests

Run:

```bash
poetry run pytest
```

---

## Security Notes

* `.env` is not committed
* Profiles must not contain secrets
* OpenShift access should use least privilege
* Production should be read-only initially

---

## Current Status

* Profiles implemented
* CLI profile-aware
* OpenShift fake discovery implemented
* Ready for Kubernetes API integration

---

## Roadmap

* Real OpenShift discovery (Kubernetes API)
* Real MQ message reading
* DLQ replay (safe mode)
* Audit logging
* RBAC integration

---

## References

* docs/architecture/openshift-deployment-model.md
* docs/architecture/profile-model.md

---

## License

MIT
