from security_engine import detect_intrusion


def analyze_network_events(events):
    """Analyze network connection events and return IDS alerts."""
    if not isinstance(events, (list, tuple, set)):
        raise TypeError("Events must be a list, tuple, or set of ports.")

    if any(not isinstance(port, int) or not 1 <= port <= 65535 for port in events):
        raise ValueError("Every port must be an integer between 1 and 65535.")

    return detect_intrusion(events)


def get_ids_status():
    """Return the current IDS module status."""
    return {
        "module": "Intrusion Detection System",
        "status": "ACTIVE",
        "detection_type": "Rule-based simulation"
    }
