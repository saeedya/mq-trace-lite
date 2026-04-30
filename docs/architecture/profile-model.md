# Profile Model

## Purpose

MQ Trace Lite needs to work across multiple IBM MQ environments, OpenShift clusters, namespaces, and queue managers.

A profile defines how the tool discovers or connects to MQ.

---

## Profile Types

### 1. Static Profile

Used for local development or manually configured MQ instances.

```yaml
profiles:
  local-dev:
    type: static
    host: localhost
    port: 1414
    queue_manager: QM1
    channel: DEV.APP.SVRCONN
```

### 2. OpenShift Profile

Used when IBM MQ runs inside OpenShift.

```yaml
profiles:
  sit-pay-engine:
    type: openshift
    environment: sit
    context: ocp-sit
    namespace: pay-engine
    queue_manager: QM1
```

---

## Secrets

Profiles must not store passwords or private keys.

Secrets should be resolved from:

- Environment variables
- OpenShift Secrets
- Vault / external secret manager

Example:

```yaml
profiles:
  sit-pay-engine:
    type: openshift
    environment: sit
    context: ocp-sit
    namespace: pay-engine
    queue_manager: QM1
    username_env: MQ_SIT_USER
    password_env: MQ_SIT_PASSWORD
```

---

## Future CLI Usage

```bash
mqtrace profiles list
mqtrace inspect --profile sit-pay-engine --queue PAYMENT.DLQ
```

---

## Status

Accepted for MVP architecture.