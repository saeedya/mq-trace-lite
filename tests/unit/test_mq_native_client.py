from mqtrace.adapters.ibmmq.native_client import MQNativeClient


def test_native_client_init():
    client = MQNativeClient(
        host="localhost",
        port=1414,
        channel="DEV.APP.SVRCONN",
        queue_manager="QM1",
    )

    assert client.queue_manager == "QM1"

def test_native_client_browse_not_implemented_as_mock(monkeypatch):
    from mqtrace.adapters.ibmmq.native_client import MQNativeClient

    # این تست فعلاً فقط مطمئن می‌شود object درست ساخته می‌شود
    # تست واقعی browse بعداً integration test می‌شود، نه unit test
    client = MQNativeClient(
        host="localhost",
        port=1414,
        channel="DEV.APP.SVRCONN",
        queue_manager="QM1",
        username="app",
        password="passw0rd",
    )

    assert client.host == "localhost"
    assert client.channel == "DEV.APP.SVRCONN"
    assert client.username == "app"