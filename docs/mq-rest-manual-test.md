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