from mqtrace.core.messages import get_messages


def test_message_contains_metadata(monkeypatch):
    class MockMQRestClient:
        def __init__(self, *args, **kwargs):
            pass

        def get_messages(self, queue, limit):
            return [{"message": "hello"}]

    monkeypatch.setattr(
        "mqtrace.core.messages.MQRestClient",
        MockMQRestClient,
    )

    profile = {"type": "static", "queue_manager": "QM1"}

    msgs = get_messages(profile, "DEV.QUEUE.1", None, 1)

    msg = msgs[0]

    assert msg["status"] == "REAL"
    assert "timestamp" in msg
    assert "size" in msg
    assert "headers" in msg
    assert "payload_preview" in msg