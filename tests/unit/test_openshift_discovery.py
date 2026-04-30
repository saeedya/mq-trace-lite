from mqtrace.adapters.openshift.discovery import discover_qmgr


def test_discover_qmgr_returns_fallback_service_hostname():
    result = discover_qmgr(namespace="pay-engine", name="QM1")

    assert result["host"] == "QM1.pay-engine.svc.cluster.local"
    assert result["port"] == 1414
    assert result["queue_manager"] == "QM1"