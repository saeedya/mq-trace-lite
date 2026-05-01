from mqtrace.adapters.ibmmq.native_client import MQNativeClient


def test_native_client_init():
    client = MQNativeClient(
        host="localhost",
        port=1414,
        channel="DEV.APP.SVRCONN",
        queue_manager="QM1",
    )

    assert client.queue_manager == "QM1"