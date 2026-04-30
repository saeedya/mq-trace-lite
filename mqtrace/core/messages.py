from mqtrace.adapters.ibmmq.client import MQClient
from mqtrace.config import config


def get_messages(profile: dict, queue: str, correlation_id: str | None, limit: int):
    """Return messages based on profile type."""

    profile_type = profile.get("type")

    if profile_type == "static":
        return _get_static_messages(profile, queue, correlation_id, limit)

    elif profile_type == "openshift":
        return _get_openshift_messages(profile, queue, correlation_id, limit)

    else:
        raise ValueError(f"Unsupported profile type: {profile_type}")


def _get_static_messages(profile, queue, correlation_id, limit):
    # فعلاً fake
    messages = []

    for i in range(limit):
        messages.append(
            {
                "message_id": f"msg-{i}",
                "correlation_id": correlation_id or f"corr-{i}",
                "queue": queue,
                "status": "STATIC",
            }
        )

    return messages


def _get_openshift_messages(profile, queue, correlation_id, limit):
    # فعلاً fake
    messages = []

    for i in range(limit):
        messages.append(
            {
                "message_id": f"msg-{i}",
                "correlation_id": correlation_id or f"corr-{i}",
                "queue": queue,
                "status": "OCP",
            }
        )

    return messages