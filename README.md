# MQ Trace Lite

![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![CLI](https://img.shields.io/badge/interface-CLI-orange)
![Status](https://img.shields.io/badge/status-MVP-yellow)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![OpenShift](https://img.shields.io/badge/OpenShift-aware-red?logo=redhat)

CLI-first debugging and incident tool for IBM MQ in OpenShift environments.

---

## Table of Contents

- [MQ Trace Lite](#mq-trace-lite)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Problem](#problem)
  - [Solution](#solution)
  - [Architecture](#architecture)
  - [Profiles](#profiles)
    - [Example](#example)
  - [CLI Usage](#cli-usage)
    - [List profiles](#list-profiles)
    - [Inspect messages](#inspect-messages)
  - [Installation (pipx)](#installation-pipx)
  - [OpenShift Discovery (MVP)](#openshift-discovery-mvp)
  - [Message Metadata](#message-metadata)
  - [Setup](#setup)
  - [Docker Development](#docker-development)
  - [Tests](#tests)
  - [Error Handling](#error-handling)
  - [Security Notes](#security-notes)
  - [Current Status](#current-status)
  - [Roadmap](#roadmap)
  - [Architecture Docs](#architecture-docs)
  - [License](#license)

---

## Overview

MQ Trace Lite is a CLI-first debugging and incident tool for IBM MQ, designed for OpenShift environments.

It helps engineers:

* Inspect messages
* Understand failures
* Debug message flows
* Prepare safe replay workflows

---

## Problem

In systems using IBM MQ:

* Messages fail and go to DLQ
* Debugging flows is difficult
* Replay is manual and risky
* No simple DevOps-friendly tool exists

---

## Solution

MQ Trace Lite provides:

* Message inspection
* Profile-based multi-environment access
* OpenShift-aware discovery (namespace → MQ)
* Structured message metadata
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

Location:

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
    channel: DEV.APP.SVRCONN

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
mqtrace profiles
```

---

### Inspect messages

```bash
mqtrace inspect \
  --profile sit-pay-engine \
  --queue TEST
```

---

## Installation (pipx)

Build package:

```bash
poetry build
```

Install:

```bash
pipx install dist/*.whl
```

Run:

```bash
mqtrace --help
```

---

## OpenShift Discovery (MVP)

Current implementation uses **deterministic fallback**:

```text
<queue_manager>.<namespace>.svc.cluster.local
```

Example:

```text
QM1.pay-engine.svc.cluster.local
```

Real Kubernetes API integration is planned.

---

## Message Metadata

Each message includes:

* `message_id`
* `correlation_id`
* `timestamp`
* `size`
* `headers`
* `payload_preview`
* `queue`
* `status`
* `host`

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
docker compose run --rm app mqtrace inspect \
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

## Error Handling

CLI provides clear errors:

```bash
mqtrace inspect --profile wrong --queue TEST
```

---

## Security Notes

* `.env` is not committed
* Profiles must not contain secrets
* OpenShift access should follow least privilege
* Production should be read-only initially

---

## Current Status

* Profiles implemented
* CLI profile-aware
* OpenShift fake discovery implemented
* Message metadata added
* Unit tests available
* Installable CLI via pipx

---

## Roadmap

* Kubernetes API integration
* Real MQ message retrieval
* DLQ replay (safe mode)
* Audit logging
* Flow visualization
* Dashboard (future)

---

## Architecture Docs

* docs/architecture/openshift-deployment-model.md
* docs/architecture/profile-model.md
* docs/architecture/future-dashboard.md

---

## License

MIT
