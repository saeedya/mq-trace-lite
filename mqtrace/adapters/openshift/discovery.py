def discover_qmgr(namespace: str, name: str):
    """
    Fake OpenShift discovery for QueueManager.
    Later this will use Kubernetes API.
    """

    return {
        "host": f"{name}.{namespace}.svc.cluster.local",
        "port": 1414,
        "channel": "DEV.APP.SVRCONN",
        "queue_manager": name,
    }