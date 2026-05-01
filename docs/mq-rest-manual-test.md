# IBM MQ REST Manual Test

## Purpose

This document captures the manual steps used to verify IBM MQ REST API access in the local Docker environment.

---

## Preconditions

IBM MQ local container is running.

```bash
cd docker
docker compose up -d
```

IBM MQ Console:

https://localhost:9443

Credentials:

admin / passw0rd

---

## Verify Queue Manager

```bash
curl -k -u admin:passw0rd \
  https://localhost:9443/ibmmq/rest/v2/admin/qmgr
```

Expected response:

```json
{
  "qmgr": [
    {
      "name": "QM1",
      "state": "running"
    }
  ]
}
```

---

## Messaging User

Admin API works with admin, but messaging endpoints require a user with MQWebUser.

Use:

app / passw0rd

---

## Put Test Message

IBM MQ REST POST requests require a CSRF header.

```bash
curl -k -u app:passw0rd \
  -X POST \
  -H "Content-Type: text/plain" \
  -H "ibm-mq-rest-csrf-token: mqtrace" \
  --data "hello from mqtrace" \
  https://localhost:9443/ibmmq/rest/v2/messaging/qmgr/QM1/queue/DEV.QUEUE.1/message
```

---

## Verify Message

```bash
curl -k -u app:passw0rd   https://localhost:9443/ibmmq/rest/v2/messaging/qmgr/QM1/queue/DEV.QUEUE.1/message
```

---

## Notes
This is local development only.
Credentials are not production-safe.
Production must use proper TLS/mTLS and non-default credentials.

---

## Empty Queue Behavior

When `DEV.QUEUE.1` has no messages, IBM MQ REST returns:

```text
HTTP/1.1 204 No Content
```

MQ Trace Lite treats this as an empty message list and displays an empty table instead of failing.

---

## Plain Text Message Behavior

When reading messages via IBM MQ REST API, the response may not always be JSON.

For plain-text messages, the API returns raw content instead of a JSON structure.

MQ Trace Lite handles this by:

- Detecting `content-type`
- Falling back to raw text parsing
- Converting it into an internal message structure

Example:

```text
hello from mqtrace
```

---

## Current Limitation

At the moment, MQ Trace Lite reads only a single message from IBM MQ REST API.

This is because:

- The REST endpoint `/message` returns one message per request
- The current implementation does not loop or support batch retrieval
- Messages may appear "stuck" on the same value during repeated reads

Example behavior:

- Queue contains:
  - hello MQ REAL
  - hello from mqtrace
- CLI shows only:
  - hello from mqtrace

### Future Improvement

- Implement loop-based retrieval
- Support multiple message fetch
- Add non-destructive browse (peek) mode