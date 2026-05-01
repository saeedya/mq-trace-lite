# PyMQI Install Notes

## Problem

Installing `pymqi` on a local machine may fail if IBM MQ Client headers and libraries are not installed.

Common error:

```text
fatal error: cmqc.h: No such file or directory
```

## Cause

pymqi depends on IBM MQ native client libraries.

It expects files such as:

/opt/mqm/inc/cmqc.h
/opt/mqm/lib64/libmqic_r.so

## Project Decision

For local MVP development, we will avoid requiring developers to install IBM MQ Client directly on the host machine.

Instead, we will use a Docker-based development environment in a future step.

## Status

Real MQ connection is postponed until the containerized client environment is prepared.

## Current Decision

`pymqi` will not be installed directly on the developer laptop.

Native MQ support will require a dedicated Docker image that includes:

- IBM MQ client headers
- IBM MQ client libraries
- pymqi
- Python runtime

This avoids requiring every developer to install IBM MQ Client locally.