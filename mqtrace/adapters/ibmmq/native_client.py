import pymqi


class MQNativeClient:
    def __init__(self, host, port, channel, queue_manager, username=None, password=None):
        self.host = host
        self.port = port
        self.channel = channel
        self.queue_manager = queue_manager
        self.username = username
        self.password = password

    def browse_messages(self, queue: str, limit: int = 1):
        conn_info = f"{self.host}({self.port})"

        cd = pymqi.CD()
        cd.ChannelName = self.channel
        cd.ConnectionName = conn_info

        qmgr = pymqi.QueueManager(None)
        qmgr.connect_with_options(self.queue_manager, cd)

        queue_obj = pymqi.Queue(qmgr, queue)

        gmo = pymqi.GMO()
        gmo.Options = pymqi.CMQC.MQGMO_BROWSE_FIRST

        messages = []

        try:
            msg = queue_obj.get(None, gmo)
            messages.append(msg.decode())
        except pymqi.MQMIError as e:
            if e.reason != pymqi.CMQC.MQRC_NO_MSG_AVAILABLE:
                raise

        queue_obj.close()
        qmgr.disconnect()

        return messages