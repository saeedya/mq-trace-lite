from mqtrace.core.messages import get_messages


def test_message_contains_metadata():
    profile = {"type": "static"}

    msgs = get_messages(profile, "TEST", None, 1)

    msg = msgs[0]

    assert "timestamp" in msg
    assert "size" in msg
    assert "headers" in msg
    assert "payload_preview" in msg