import datetime

from mqtrace.adapters.openshift.discovery import discover_qmgr
from mqtrace.adapters.ibmmq.rest_client import MQRestClient


def _build_message(i, queue, correlation_id, status, host=None):
    return {
        "message_id": f"msg-{i}",
        "correlation_id": correlation_id or f"corr-{i}",
        "queue": queue,
        "status": status,
        "host": host,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "size": 128 + i,
        "headers": {
            "content_type": "application/json",
            "app_id": "payment-service",
        },
        "payload_preview": f'{{"amount": {100+i}, "currency": "USD"}}',
    }


def get_messages(profile: dict, queue: str, correlation_id: str | None, limit: int):
    """Return messages based on profile type."""

    profile_type = profile.get("type")

    if profile_type == "static":
        return _get_static_messages(profile, queue, correlation_id, limit)

    if profile_type == "openshift":
        return _get_openshift_messages(profile, queue, correlation_id, limit)

    raise ValueError(f"Unsupported profile type: {profile_type}")


def _get_static_messages(profile, queue, correlation_id, limit):
    rest_cfg = profile.get("rest", {})

    client = MQRestClient(
        base_url=rest_cfg.get("base_url", "https://localhost:9443/ibmmq/rest/v2"),
        username=rest_cfg.get("username", "app"),
        password=rest_cfg.get("password", "passw0rd"),
        qmgr=profile.get("queue_manager", "QM1"),
    )

    try:
        msgs = client.get_messages(queue, limit)

        result = []
        for i, m in enumerate(msgs):
            result.append(
                _build_message(
                    i=i,
                    queue=queue,
                    correlation_id=correlation_id,
                    status="REAL",
                )
            )

        return result

    except Exception as e:
        raise RuntimeError(f"MQ REST read failed: {e}") from e


def _get_openshift_messages(profile, queue, correlation_id, limit):
    conn = discover_qmgr(
        namespace=profile["namespace"],
        name=profile["queue_manager"],
    )

    messages = []

    for i in range(limit):
        messages.append(
            _build_message(
                i=i,
                queue=queue,
                correlation_id=correlation_id,
                status="OCP",
                host=conn["host"],
            )
        )

    return messages