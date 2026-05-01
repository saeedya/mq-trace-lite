import httpx
from mqtrace.core.logger import get_logger

logger = get_logger(__name__)

class MQRestClient:
    def __init__(self, base_url: str, username: str, password: str, qmgr: str):
        self.base_url = base_url
        self.auth = (username, password)
        self.qmgr = qmgr

    def get_messages(self, queue: str, limit: int = 5):
        url = f"{self.base_url}/messaging/qmgr/{self.qmgr}/queue/{queue}/message"

        logger.info(f"Fetching messages from MQ: queue={queue}")

        response = httpx.get(
            url,
            auth=self.auth,
            verify=False,
            trust_env=False,
        )

        logger.info(f"MQ response status: {response.status_code}")

        if response.status_code == 204:
            return []

        if response.status_code != 200:
            logger.error(f"MQ REST error: {response.text}")
            raise Exception(f"MQ REST error: {response.text}")

        content_type = response.headers.get("content-type", "")

        if "application/json" in content_type:
            data = response.json()
            return data.get("messages", [])[:limit]

        return [{"payload": response.text}]