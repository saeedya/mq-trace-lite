from mqtrace.adapters.ibmmq.client import MQClient
from mqtrace.config import config


def get_messages(queue: str, correlation_id: str | None, limit: int):
    client = MQClient(
        host=config.MQ_HOST,
        port=config.MQ_PORT,
        channel=config.MQ_CHANNEL,
        queue_manager=config.MQ_QUEUE_MANAGER,
    )

    client.connect()

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

    client.disconnect()

    return messages