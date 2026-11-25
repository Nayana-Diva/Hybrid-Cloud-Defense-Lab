NETWORK_ZONES = {
    "INTERNET": {
        "description": "External users and public networks",
        "trust_level": "UNTRUSTED"
    },
    "DMZ": {
        "description": "Public-facing web servers and reverse proxies",
        "trust_level": "RESTRICTED"
    },
    "INTERNAL": {
        "description": "Internal application and database servers",
        "trust_level": "TRUSTED"
    },
    "CLOUD": {
        "description": "Cloud virtual private network resources",
        "trust_level": "RESTRICTED"
    }
}


def get_network_zones():
    """Return configured network security zones."""
    return NETWORK_ZONES


def validate_network_path(source, destination):
    """Check whether both network zones are defined."""
    source = source.upper()
    destination = destination.upper()

    if source not in NETWORK_ZONES:
        return {"valid": False, "reason": "Unknown source zone"}

    if destination not in NETWORK_ZONES:
        return {"valid": False, "reason": "Unknown destination zone"}

    return {
        "valid": True,
        "source": source,
        "destination": destination
    }
