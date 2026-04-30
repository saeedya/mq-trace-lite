# OpenShift Deployment Model

## Context

MQ Trace Lite is intended to work in environments where IBM MQ runs on OpenShift across multiple namespaces and multiple clusters.

The organization has multiple OpenShift clusters for different environments:

- SIT
- STG
- Pre-Prod
- Prod

Each cluster contains multiple application namespaces, such as:

- pay-clearing
- pay-engine
- pay-events
- pay-posting
- pay-sanctions
- pay-mq-admin

---

## Decision

MQ Trace Lite will be deployed once per OpenShift cluster in a dedicated namespace.

Example:

```text
sit-cluster
  namespace: mqtrace-tools

stg-cluster
  namespace: mqtrace-tools

pre-prod-cluster
  namespace: mqtrace-tools

prod-cluster
  namespace: mqtrace-tools

The application will NOT be deployed separately into every business namespace.
```

## Why Not Deploy Per Namespace?

Deploying MQ Trace Lite into each namespace would create:

- Multiple deployments to maintain
- Version drift between namespaces
- More complex upgrades
- More complex RBAC
- Harder auditing
- Operational overhead

## Target Model

mqtrace-tools namespace
  └── mqtrace app
        ├── read access to pay-clearing
        ├── read access to pay-engine
        ├── read access to pay-events
        ├── read access to pay-posting
        ├── read access to pay-sanctions
        └── read access to pay-mq-admin

## Environment Strategy

Each OpenShift cluster has its own MQ Trace Lite deployment.

one deployment per cluster
not one deployment per namespace
not one deployment for all clusters

This improves security and keeps production isolated.

## Security Model

The application must use least privilege.

Initial production mode should be read-only.

Recommended permissions:

- list/get namespaces
- list/get IBM MQ QueueManager custom resources
- get services/routes required for connection discovery
- no cluster-admin permission
- no write actions by default

Replay or destructive operations must be disabled in production until an approval and audit model exists.

## Future Commands

Possible CLI commands:

```bash
mqtrace env list
mqtrace namespaces list
mqtrace qmgrs list --namespace pay-engine
mqtrace inspect --namespace pay-engine --qmgr QM1 --queue PAYMENT.DLQ
```

## Status

Accepted for MVP architecture.