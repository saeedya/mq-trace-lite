# IBM MQ Native Browse Mode

## Problem

The current IBM MQ REST `/message` endpoint is not suitable for safe production inspection because it may perform destructive reads.

For payment flows, MQ Trace Lite must not consume messages during inspect operations.

---

## Decision

MQ Trace Lite will introduce a native IBM MQ browse adapter for non-destructive inspection.

The `inspect` command must use browse/peek behavior, not consume behavior.

---

## Target Behavior

```text
inspect = non-destructive browse
read    = destructive consume (future, explicit)
replay  = explicit recovery action (future)
```

---

## Native MQ Approach

Use IBM MQ native browse semantics:

- Open queue with browse permission
- Browse first message
- Browse next messages
- Do not remove messages from the queue


## Why REST Is Not Enough

IBM MQ REST messaging is useful for local development and simple tests, but it is not safe as the default implementation for incident inspection.


## Status

Accepted as architecture direction.

Implementation postponed until native MQ client support is added.

## Verified Local Test

Native browse was tested locally using the dedicated `mqtrace-native` Docker image.

Test result:

```text
client.browse_messages("DEV.QUEUE.1")
→ ["native browse test"]
```

This confirms that:

- Native MQ connection works
- Authentication works
- Queue browse works
- The message is read non-destructively

## Important Safety Decision

The inspect command should use native browse mode for production-like environments.

REST-based message reads are useful for development, but must not be used as the default production inspection mechanism because they may consume messages.