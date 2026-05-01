from mqtrace.adapters.openshift.k8s_client import get_services


def _fallback_qmgr(namespace: str, name: str):
    return {
        "host": f"{name}.{namespace}.svc.cluster.local",
        "port": 1414,
        "channel": "DEV.APP.SVRCONN",
        "queue_manager": name,
    }


def discover_qmgr(namespace: str, name: str):
    try:
        services = get_services(namespace)
    except Exception:
        return _fallback_qmgr(namespace, name)

    for svc in services:
        if name.lower() in svc.metadata.name.lower():
            return {
                "host": svc.metadata.name,
                "port": 1414,
                "channel": "DEV.APP.SVRCONN",
                "queue_manager": name,
            }

    return _fallback_qmgr(namespace, name)