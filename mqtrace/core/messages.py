def get_messages(queue: str, correlation_id: str | None, limit: int):
    """Return fake messages (placeholder for real MQ)."""

    messages = []

    for i in range(limit):
        messages.append(
            {
                "message_id": f"msg-{i}",
                "correlation_id": correlation_id or f"corr-{i}",
                "queue": queue,
                "status": "READY",
            }
        )

    return messages