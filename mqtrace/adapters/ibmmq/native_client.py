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

        cd.ChannelName = self.channel.encode("utf-8")
        cd.ConnectionName = conn_info.encode("utf-8")

        qmgr = pymqi.QueueManager(None)
        qmgr.connect_with_options(
            self.queue_manager,
            cd=cd,
            user=(self.username or "app"),
            password=(self.password or "passw0rd"),
        )

        queue_obj = pymqi.Queue(
            qmgr,
            queue,
            pymqi.CMQC.MQOO_BROWSE | pymqi.CMQC.MQOO_FAIL_IF_QUIESCING,
        )

        gmo = pymqi.GMO()
        gmo.Options = pymqi.CMQC.MQGMO_BROWSE_FIRST

        messages = []

        try:
            md = pymqi.MD()
            msg = queue_obj.get(None, md, gmo)
            messages.append(msg.decode())
        except pymqi.MQMIError as e:
            if e.reason != pymqi.CMQC.MQRC_NO_MSG_AVAILABLE:
                raise

        queue_obj.close()
        qmgr.disconnect()

        return messages