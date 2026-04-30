from mqtrace.adapters.ibmmq.rest_client import MQRestClient


def test_mq_rest_client_init():
    client = MQRestClient(
        base_url="https://localhost:9443/ibmmq/rest/v2",
        username="app",
        password="passw0rd",
    )

    assert client.base_url.startswith("https")
    assert client.auth[0] == "app"