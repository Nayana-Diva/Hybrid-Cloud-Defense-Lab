# Hybrid Cloud Defense Lab
## System Architecture

### 1. Introduction

The Hybrid Cloud Defense Lab demonstrates a layered security architecture for protecting enterprise networks that use both on-premises infrastructure and cloud resources.

The project combines a Python-based security simulation engine with a Flask web dashboard. It demonstrates firewall inspection, intrusion detection, malware signature detection, and email authentication checks.

### 2. Architecture Overview

The proposed architecture contains the following major components:

1. Internet and external users
2. Perimeter firewall
3. Demilitarized Zone (DMZ)
4. Internal enterprise network
5. Cloud Virtual Private Cloud (VPC)
6. Intrusion Detection and Prevention System (IDS/IPS)
7. Endpoint malware protection
8. Email authentication and filtering

### 3. Network Zones

#### 3.1 Internet Zone

The Internet zone represents external users and systems attempting to access enterprise resources.

All incoming traffic is subject to perimeter security inspection.

#### 3.2 Perimeter Firewall

The perimeter firewall acts as the first security boundary.

Its responsibilities include:
- Inspecting network traffic.
- Applying source and destination zone rules.
- Allowing authorized services.
- Blocking unauthorized connections.
- Applying a default-deny policy.
- Performing basic application-layer content checks.

The simulation includes an HTTPS rule allowing traffic from INTERNET to DMZ over TCP port 443.

#### 3.3 DMZ Subnet

The DMZ contains publicly accessible services such as web servers and reverse proxies.

It separates externally accessible services from the internal enterprise network.

Access from the DMZ to internal resources should be restricted to explicitly authorized services.

#### 3.4 Internal Network

The internal network contains application servers and database servers.

It is protected from direct unauthorized Internet access. Only approved communication paths should be permitted.

The simulation includes a rule allowing DMZ-to-INTERNAL database traffic over TCP port 5432.

#### 3.5 Cloud VPC

The Cloud Virtual Private Cloud represents isolated cloud workloads and private cloud resources.

Communication between internal infrastructure and cloud workloads should use encrypted connections and restricted access policies.

The simulation includes HTTPS communication over TCP port 443 between INTERNAL and CLOUD zones.

### 4. Security Layers

#### 4.1 Firewall Security

The firewall module evaluates network traffic against predefined rules.

It supports:
- Zone-based access control.
- Protocol and destination-port checks.
- Default-deny behavior.
- Basic application-layer filtering.
- Simplified established-connection handling.

#### 4.2 Intrusion Detection

The intrusion detection module analyzes supplied network event data.

It identifies:
- Port scanning attempts based on multiple unique destination ports.
- Connections involving a predefined list of suspicious ports.

Detected events generate security alerts with severity information.

#### 4.3 Malware Protection

The malware scanner checks supplied file content for a known EICAR antivirus test signature.

When the signature is detected, the simulation returns a threat-detected result and a quarantine action.

#### 4.4 Email Security

The email security module evaluates SPF, DKIM, and DMARC authentication results.

If all three checks pass, the email is classified as authenticated.

If any check fails, the email is classified as suspicious and assigned a quarantine action.

### 5. Application Architecture

The project uses the following components:

| Component | Responsibility |
|---|---|
| Flask dashboard | Provides the web interface |
| security_engine.py | Contains security inspection logic |
| Firewall module | Evaluates network traffic |
| IDS module | Detects simulated suspicious events |
| Malware module | Checks the EICAR test signature |
| Email module | Evaluates SPF, DKIM and DMARC results |
| Pytest | Runs automated functional tests |

The dashboard communicates with the Python security engine through Flask API endpoints.

### 6. Security Architecture Flow

1. External traffic enters through the Internet zone.
2. The perimeter firewall evaluates the traffic.
3. Authorized traffic is directed toward the appropriate network zone.
4. Internal and cloud communication follows restricted access rules.
5. Network event data is analyzed by the intrusion detection module.
6. Supplied file content is checked by the malware scanner.
7. Email authentication results are evaluated by the email security module.
8. Security decisions and alerts are displayed through the dashboard.

### 7. Implementation Scope and Limitations

This project is an academic security simulation and dashboard demonstration.

The following distinctions are important:

- Firewall decisions are simulated using Python rules; the application does not directly control an operating-system firewall.
- Stateful connection handling is simplified and does not implement full network connection tracking.
- Intrusion detection analyzes supplied event data rather than capturing live network packets.
- Malware detection checks for the EICAR test signature and is not a complete antivirus engine.
- SPF, DKIM and DMARC results are supplied to the application; it does not independently validate real email messages or DNS records.
- The DMZ, internal network and cloud VPC are represented in the architecture diagram and are not currently deployed as separate live networks.

### 8. Conclusion

The proposed layered architecture demonstrates how multiple security controls can work together to protect hybrid cloud environments.

The Python security engine and Flask dashboard provide a testable demonstration of important security concepts, while the architecture provides a foundation for future integration with real network security technologies.
