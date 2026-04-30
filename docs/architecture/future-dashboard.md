# Future Dashboard & Flow Visualization

## Purpose

This document outlines the future direction of MQ Trace Lite as a platform with a UI and flow visualization capabilities.

This is **NOT part of MVP**.

---

## Vision

MQ Trace Lite evolves from:

```text
CLI debugging tool
```

into:

```text
Distributed message debugging platform
```

---

## What is Flow Visualization?

Flow visualization allows engineers to see:

* Where a message started
* Which queues it passed through
* Which services processed it
* Where it failed (DLQ)
* Full lifecycle of a message

Example:

```text
API → MQ Queue A → Service X → MQ Queue B → Service Y → DLQ
```

---

## Required Capabilities

To support this, the system must:

* Track messages across queues
* Correlate messages using `correlation_id`
* Store message metadata
* Capture processing events
* Provide searchable history

---

## Proposed Architecture

```text
Frontend (React)
   |
Backend API (FastAPI)
   |
Core Services
   ├── MQ Adapter
   ├── OpenShift Adapter
   └── Flow Tracker
   |
Database (PostgreSQL)
   |
Background Workers (Celery / Arq)
```

---

## Application Awareness

Flow visualization must include application-level components, not just MQ queues.

A complete flow includes:

- Applications (services running in OpenShift)
- Queues
- Message transitions between them

Example:

```text
Payment API → MQ Queue A → Sanctions Service → MQ Queue B → Posting Service
```

To support this, the system should:

- Identify application names (from OpenShift pods/deployments)
- Map message producers and consumers
- Link queues to applications
- Use correlation_id to connect all events

This enables a full end-to-end flow view.

---

## Key Components

### 1. API Layer

Expose functionality currently in CLI:

* inspect
* replay (future)
* audit logs

---

### 2. Flow Tracker

Tracks message lifecycle:

* correlation_id
* queue transitions
* timestamps
* status (processed / failed / DLQ)

---

### 3. Database

Used for:

* audit logs
* message history
* replay tracking
* user actions

Suggested:

* PostgreSQL (production)
* SQLite (local/dev)

---

### 4. Workers

For async processing:

* replay jobs
* background MQ polling
* flow aggregation

---

## Security Considerations

* RBAC (user roles)
* audit trail (who did what)
* restricted replay permissions
* environment isolation (prod vs non-prod)

---

## Why Not Now?

This is intentionally postponed because:

* Adds significant complexity
* Requires database + API + UI
* Not needed to validate core idea

---

## MVP Focus

Current focus remains:

```text
CLI + OpenShift + MQ integration
```

---

## Status

Planned (post-MVP)
