from kubernetes import client, config


def load_kube_config():
    try:
        config.load_kube_config()
    except Exception:
        config.load_incluster_config()


def get_services(namespace: str):
    load_kube_config()

    v1 = client.CoreV1Api()
    services = v1.list_namespaced_service(namespace)

    return services.items