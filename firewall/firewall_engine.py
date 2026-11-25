from security_engine import FIREWALL_RULES, Traffic, inspect_firewall


def get_firewall_rules():
    """Return configured firewall rules."""
    return FIREWALL_RULES


def evaluate_traffic(
    source_zone,
    destination_zone,
    protocol,
    destination_port,
    state="NEW",
    application_data=""
):
    """Evaluate network traffic using the central security engine."""
    traffic = Traffic(
        source_zone=source_zone.upper(),
        destination_zone=destination_zone.upper(),
        protocol=protocol.upper(),
        destination_port=int(destination_port),
        state=state.upper(),
        application_data=application_data
    )

    return inspect_firewall(traffic)
