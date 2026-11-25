# IDS/IPS Deployment Strategy

## 1. Introduction

An Intrusion Detection System (IDS) monitors network or system activities to identify suspicious behavior. An Intrusion Prevention System (IPS) can additionally block detected malicious traffic.

## 2. Deployment Approach

The proposed hybrid cloud architecture uses Network-Based IDS (NIDS) monitoring at important network boundaries.

Recommended monitoring locations:

- DMZ network boundary
- Internal network
- Cloud VPC traffic boundary

Host-Based IDS (HIDS) can additionally be deployed on critical application and database servers.

## 3. IDS/IPS Placement

### 3.1 DMZ Monitoring

Monitor traffic entering and leaving publicly accessible web servers.

This helps identify port scanning, suspicious connection attempts and unusual traffic patterns.

### 3.2 Internal Network Monitoring

Monitor communication between application servers and database systems.

This helps identify unauthorized access attempts and unusual internal network activity.

### 3.3 Cloud Network Monitoring

Monitor cloud workload traffic using cloud-native network monitoring and security services.

This helps detect suspicious activity involving cloud resources.

## 4. Detection Methods

The proposed system considers:

- Port scanning detection
- Suspicious destination ports
- Unusual network connection patterns
- Unauthorized access attempts

## 5. Recommended Technology

Suricata is a suitable open-source IDS/IPS technology for a future live network deployment.

It supports network traffic inspection and rule-based threat detection.

## 6. Project Implementation

The current Python security engine demonstrates simplified intrusion detection.

It analyzes supplied network event data and identifies port scanning when five or more unique destination ports are detected.

It also identifies connections involving predefined suspicious ports.

The Flask dashboard displays generated security alerts.

## 7. Limitations

The current implementation does not capture live network packets, deploy Suricata or block real network traffic.

Suricata deployment and live IDS/IPS integration are proposed future enhancements.

## 8. Conclusion

A combination of network-based and host-based monitoring provides visibility across hybrid cloud infrastructure.

IDS/IPS deployment at important network boundaries helps identify suspicious activities and improve incident response.
