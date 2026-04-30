import httpx
from mqtrace.adapters.ibmmq.rest_client import MQRestClient


def test_mq_rest_client_init():
    client = MQRestClient(
        base_url="https://localhost:9443/ibmmq/rest/v2",
        username="app",
        password="passw0rd",
        qmgr="QM1",
    )

    assert client.base_url.startswith("https")
    assert client.auth[0] == "app"

def test_get_messages_success(monkeypatch):
    client = MQRestClient(
        base_url="https://localhost:9443/ibmmq/rest/v2",
        username="app",
        password="passw0rd",
        qmgr="QM1",
    )

    assert client.qmgr == "QM1"

    class MockResponse:
        status_code = 200

        def json(self):
            return {
                "messages": [
                    {"message": "hello"},
                    {"message": "world"},
                ]
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(httpx, "get", mock_get)

    result = client.get_messages("DEV.QUEUE.1", limit=1)

    assert len(result) == 1