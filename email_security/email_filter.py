from security_engine import check_email_authentication


def evaluate_email(spf, dkim, dmarc):
    """Evaluate email authentication results."""
    return check_email_authentication(spf, dkim, dmarc)


def get_email_security_status():
    """Return email security module information."""
    return {
        "module": "Email Security Gateway",
        "status": "ACTIVE",
        "protocols": ["SPF", "DKIM", "DMARC"]
    }
