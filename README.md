# MQ Trace Lite

## Overview

MQ Trace Lite is a CLI-first debugging and incident tool for IBM MQ.

It helps engineers inspect messages, understand failures, and safely prepare replay workflows during incidents.

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
* Filtering by messageId / correlationId
* Structured metadata view
* Safe replay (dry-run first)
* Audit logging

---

## Why this exists

This tool is designed for:

* DevOps engineers
* Backend developers
* Incident responders

Who need a simple, safe way to debug and recover messaging issues.

---

## Non-Goals (for now)

* Not a full MQ dashboard
* Not a replacement for IBM MQ Console
* Not a multi-broker platform (Kafka, RabbitMQ, etc.)
* Not a UI-first application

---

## Tech Direction

* Python (CLI-first)
* IBM MQ integration
* Designed to evolve into a broader debugging platform

---

## Status

Early stage (MVP planning)

---

## CLI Usage

### Show version

```bash
poetry run python -m mqtrace.cli.main version
```

---

### Inspect messages (fake data for now)

```bash
poetry run python -m mqtrace.cli.main inspect --queue DLQ.TEST
```

With options:

```bash
poetry run python -m mqtrace.cli.main inspect \
  --queue DLQ.TEST \
  --limit 3 \
  --correlation-id corr-123
```

---

## Notes

* Current implementation uses fake data
* Real IBM MQ integration will be added in future steps

---

## Setup

See [docs/setup.md](docs/setup.md)

---

---

## Architecture

Current structure:

* `cli/` → CLI commands (Typer)
* `core/` → business logic (message inspection)
* `adapters/ibmmq/` → IBM MQ integration layer

---

## Current Capabilities

* CLI command: `inspect`
* Fake message inspection
* Initial IBM MQ adapter structure (mock connection)

---

## Limitations

* No real MQ connection yet
* No real message retrieval
* No replay functionality yet

---

## Local IBM MQ

See [docs/local-ibm-mq.md](docs/local-ibm-mq.md)

---

## Docker Development

See [docs/docker-dev.md](docs/docker-dev.md)

---

## OpenShift Deployment Model

See [docs/architecture/openshift-deployment-model.md](docs/architecture/openshift-deployment-model.md)

---

## Profile Model

See [docs/architecture/profile-model.md](docs/architecture/profile-model.md)