import httpx


class MQRestClient:
    def __init__(self, base_url: str, username: str, password: str, qmgr: str):
        self.base_url = base_url
        self.auth = (username, password)
        self.qmgr = qmgr

    def get_messages(self, queue: str, limit: int = 5):
        url = f"{self.base_url}/messaging/qmgr/{self.qmgr}/queue/{queue}/message"

        response = httpx.get(
            url,
            auth=self.auth,
            verify=False,
        )

        if response.status_code != 200:
            raise Exception(f"MQ REST error: {response.text}")

        data = response.json()

        return data.get("messages", [])[:limit]