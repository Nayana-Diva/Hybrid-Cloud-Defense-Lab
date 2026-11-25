from security_engine import (
    Traffic,
    inspect_firewall,
    detect_intrusion,
    scan_file_content,
    check_email_authentication
)


def test_allowed_https_traffic():
    traffic = Traffic("INTERNET", "DMZ", "TCP", 443)
    assert inspect_firewall(traffic)["action"] == "ALLOW"


def test_block_unauthorized_traffic():
    traffic = Traffic("INTERNET", "INTERNAL", "TCP", 22)
    assert inspect_firewall(traffic)["action"] == "BLOCK"


def test_stateful_connection():
    traffic = Traffic(
        "INTERNAL", "INTERNET", "TCP", 22,
        state="ESTABLISHED"
    )
    assert inspect_firewall(traffic)["action"] == "ALLOW"


def test_application_layer_filter():
    traffic = Traffic(
        "INTERNET", "DMZ", "TCP", 443,
        application_data="UNION SELECT username FROM users"
    )
    assert inspect_firewall(traffic)["action"] == "BLOCK"


def test_detect_port_scan():
    alerts = detect_intrusion([21, 22, 23, 80, 443])
    assert any(alert["threat"] == "Port Scanning" for alert in alerts)


def test_clean_file():
    result = scan_file_content("This is a normal document.")
    assert result["status"] == "CLEAN"


def test_malware_signature():
    result = scan_file_content(
        "EICAR-STANDARD-ANTIVIRUS-TEST-FILE"
    )
    assert result["status"] == "THREAT DETECTED"


def test_authenticated_email():
    result = check_email_authentication("PASS", "PASS", "PASS")
    assert result["action"] == "ALLOW"


def test_suspicious_email():
    result = check_email_authentication("FAIL", "PASS", "FAIL")
    assert result["action"] == "QUARANTINE"
