import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MQ_HOST = os.getenv("MQ_HOST", "localhost")
    MQ_PORT = int(os.getenv("MQ_PORT", "1414"))
    MQ_CHANNEL = os.getenv("MQ_CHANNEL", "DEV.APP.SVRCONN")
    MQ_QUEUE_MANAGER = os.getenv("MQ_QUEUE_MANAGER", "QM1")


config = Config()