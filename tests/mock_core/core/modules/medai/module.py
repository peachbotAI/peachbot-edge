def run(input_payload):
    data = input_payload["data"]

    context = data.get("context", {})
    memory = data.get("memory", {})
    hardware = data.get("hardware", {})
    federation = data.get("federation", {})

    return {
        "data": {
            "processed_by": "medai",
            "signal_type": context.get("signal_type"),
            "priority": context.get("priority"),
            "mode": hardware.get("mode"),
            "federated_seen": len(federation.get("global_context", [])) > 0,
            "memory_seen": len(memory) > 0
        },
        "status": "ok"
    }