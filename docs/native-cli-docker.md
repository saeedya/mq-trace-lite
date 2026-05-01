# Native CLI with Docker

## Purpose

This document explains how to run MQ Trace Lite in native IBM MQ mode using Docker.

Native mode uses `pymqi` and IBM MQ client libraries to browse messages without consuming them.

---

## Why Native Mode?

REST-based reads are useful for local development, but native browse is required for safe inspection.

Native mode supports non-destructive message browsing.

---

## Requirements

- Docker
- Local IBM MQ container running
- `mqtrace-native` image built
- Profile file available at `~/.mqtrace/profiles.yml`

---

## Build Native Image

From project root:

```bash
docker build -f docker/native-client.Dockerfile -t mqtrace-native .
```

---

## Example Native Profile

```yaml
profiles:
  local-native:
    type: native
    host: localhost
    port: 1414
    channel: DEV.APP.SVRCONN
    queue_manager: QM1
    username: app
    password: passw0rd
```

---

## Run Native Inspect

```bash
docker run --rm --network host \
  -v ~/.mqtrace:/root/.mqtrace:ro \
  mqtrace-native \
  python -m mqtrace.cli.main inspect \
  --profile local-native \
  --queue DEV.QUEUE.1
```

---

## Expected Behavior

- Messages are displayed in the CLI table
- Status is NATIVE
- Messages are browsed non-destructively
- Messages remain in the queue after inspection

---

## Safety Note

Use native mode for production-like inspection.

REST mode must not be treated as safe inspect mode because it may consume messages.