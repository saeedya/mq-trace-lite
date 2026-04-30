# MVP Scope — MQ Trace Lite

## Goal

Build a minimal CLI-first tool for IBM MQ that helps engineers:

- Inspect messages
- Understand failures
- Prepare safe replay actions

---

## In Scope (MVP)

### 1. MQ Connection

- Connect to an IBM MQ Queue Manager
- Use basic authentication (config-based)

---

### 2. Read Messages

- Read messages from a given queue
- Read messages from DLQ
- Limit number of messages (e.g. top N)

---

### 3. Message Inspection

- Show:
  - messageId
  - correlationId
  - timestamp
  - queue name
  - basic headers
- Show payload (raw / optional pretty)

---

### 4. Filtering

- Filter by:
  - messageId
  - correlationId

---

### 5. Dry-Run Replay (Important)

- Simulate replay:
  - show target queue
  - show message info
- No actual send in MVP (only preview)

---

### 6. Audit Log (Basic)

- Log actions locally:
  - read
  - inspect
  - replay (dry-run)

---

## Out of Scope (MVP)

- No UI (CLI only)
- No real replay yet
- No Kafka or other brokers
- No distributed tracing
- No RBAC or authentication system
- No multi-tenant support
- No production-grade security (yet)

---

## Success Criteria

MVP is successful if:

- A user can connect to MQ
- A user can inspect DLQ messages
- A user can safely simulate replay
- The tool is usable during an incident

---

## Future (Not Now)

- Real replay engine
- Multi-broker support (Kafka, RabbitMQ)
- Flow tracing across systems
- UI dashboard
- RBAC and audit compliance