from mqtrace.adapters.openshift.k8s_client import get_services


def discover_qmgr(namespace: str, name: str):
    services = get_services(namespace)

    for svc in services:
        if name.lower() in svc.metadata.name.lower():
            return {
                "host": svc.metadata.name,
                "port": 1414,
                "channel": "DEV.APP.SVRCONN",
                "queue_manager": name,
            }

    # fallback
    return {
        "host": f"{name}.{namespace}.svc.cluster.local",
        "port": 1414,
        "channel": "DEV.APP.SVRCONN",
        "queue_manager": name,
    }