from dataclasses import dataclass


@dataclass
class Traffic:
    source_zone: str
    destination_zone: str
    protocol: str
    destination_port: int
    state: str = "NEW"
    application_data: str = ""


FIREWALL_RULES = [
    {
        "name": "Internet to DMZ HTTPS",
        "source": "INTERNET",
        "destination": "DMZ",
        "protocol": "TCP",
        "port": 443,
        "action": "ALLOW"
    },
    {
        "name": "DMZ to Internal Database",
        "source": "DMZ",
        "destination": "INTERNAL",
        "protocol": "TCP",
        "port": 5432,
        "action": "ALLOW"
    },
    {
        "name": "Internal to Cloud HTTPS",
        "source": "INTERNAL",
        "destination": "CLOUD",
        "protocol": "TCP",
        "port": 443,
        "action": "ALLOW"
    },
    {
        "name": "Cloud to Internal HTTPS",
        "source": "CLOUD",
        "destination": "INTERNAL",
        "protocol": "TCP",
        "port": 443,
        "action": "ALLOW"
    }
]


def inspect_firewall(traffic):
    # Stateful inspection: permit established return traffic.
    if traffic.state == "ESTABLISHED":
        return {
            "action": "ALLOW",
            "reason": "Established connection"
        }

    # Application-layer filtering.
    suspicious_patterns = [
        "/admin",
        "union select",
        "drop table",
        "<script"
    ]

    payload = traffic.application_data.lower()

    for pattern in suspicious_patterns:
        if pattern in payload:
            return {
                "action": "BLOCK",
                "reason": f"Application-layer threat: {pattern}"
            }

    # Evaluate network firewall rules.
    for rule in FIREWALL_RULES:
        if (
            traffic.source_zone == rule["source"]
            and traffic.destination_zone == rule["destination"]
            and traffic.protocol.upper() == rule["protocol"]
            and traffic.destination_port == rule["port"]
        ):
            return {
                "action": rule["action"],
                "reason": rule["name"]
            }

    return {
        "action": "BLOCK",
        "reason": "Default deny: no matching firewall rule"
    }


def detect_intrusion(events):
    alerts = []

    # Detect repeated connection attempts to different ports.
    unique_ports = set(events)

    if len(unique_ports) >= 5:
        alerts.append({
            "threat": "Port Scanning",
            "severity": "HIGH",
            "description": (
                f"Connection attempts detected on "
                f"{len(unique_ports)} different ports."
            )
        })

    suspicious_ports = {4444, 5555, 6667, 31337}

    for port in events:
        if port in suspicious_ports:
            alerts.append({
                "threat": "Suspicious Port Activity",
                "severity": "HIGH",
                "description": f"Suspicious connection to port {port}."
            })

    return alerts


def scan_file_content(content):
    # Detect the standard harmless EICAR antivirus test signature.
    if "EICAR-STANDARD-ANTIVIRUS-TEST-FILE" in content:
        return {
            "status": "THREAT DETECTED",
            "threat": "EICAR test signature",
            "action": "QUARANTINE"
        }

    return {
        "status": "CLEAN",
        "threat": None,
        "action": "ALLOW"
    }


def check_email_authentication(spf, dkim, dmarc):
    results = {
        "SPF": spf.upper(),
        "DKIM": dkim.upper(),
        "DMARC": dmarc.upper()
    }

    failed = [
        name for name, status in results.items()
        if status != "PASS"
    ]

    if not failed:
        return {
            "status": "AUTHENTICATED",
            "results": results,
            "action": "ALLOW"
        }

    return {
        "status": "SUSPICIOUS",
        "results": results,
        "failed_checks": failed,
        "action": "QUARANTINE"
    }
