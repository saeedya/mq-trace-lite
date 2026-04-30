# Local IBM MQ with Docker

## Purpose

This document explains how to run a local IBM MQ instance for development and testing.

---

## Requirements

- Docker
- Docker Compose

---

## Start IBM MQ

From project root:

```bash
cd docker
docker compose up -d
docker ps
```

### IBM MQ Configuration

The local container uses:

- Queue Manager: QM1
- Channel: DEV.APP.SVRCONN
- Host: localhost
- Port: 1414
- App Password: passw0rd

### IBM MQ Console

Open:

https://localhost:9443

Login:

Username: admin
Password: passw0rd

### Stop IBM MQ

```bash
cd docker
docker compose down
```

### Notes

This setup is for local development only.
Do not use these credentials in production.