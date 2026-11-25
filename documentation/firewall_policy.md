# Firewall Security Policy

## 1. Objective

The firewall policy defines which network communications are permitted or blocked across the hybrid cloud environment.

The project uses zone-based access control and a default-deny approach.

## 2. Network Security Zones

- INTERNET: External users and networks.
- DMZ: Public-facing services.
- INTERNAL: Enterprise application and database systems.
- CLOUD: Cloud-hosted workloads.

## 3. Firewall Rule Table

| Rule | Source | Destination | Protocol | Port | Action |
|---|---|---|---|---|---|
| 1 | INTERNET | DMZ | TCP | 443 | ALLOW |
| 2 | DMZ | INTERNAL | TCP | 5432 | ALLOW |
| 3 | INTERNAL | CLOUD | TCP | 443 | ALLOW |
| 4 | CLOUD | INTERNAL | TCP | 443 | ALLOW |
| 5 | Any other unmatched traffic | Any | Any | Any | BLOCK |

## 4. Firewall Inspection Methods

### 4.1 Zone-Based Filtering

Traffic is evaluated using its source zone, destination zone, protocol and destination port.

Only traffic matching an explicitly configured rule is permitted.

### 4.2 Stateful Connection Handling

The simulation permits traffic marked as ESTABLISHED.

This represents a simplified stateful inspection concept. It does not implement real connection tracking.

### 4.3 Application-Layer Filtering

The security engine checks application data for predefined suspicious patterns, including:

- /admin
- union select
- drop table
- <script

Traffic containing these patterns is blocked by the simulation.

### 4.4 Default-Deny Policy

Any traffic that does not match an authorized firewall rule is blocked.

This reduces unnecessary network exposure and follows the principle of least privilege.

## 5. Firewall Testing

The following scenarios were tested through the Flask dashboard:

| Test Scenario | Expected Result | Actual Result |
|---|---|---|
| INTERNET to DMZ TCP/443 | ALLOW | ALLOW |
| INTERNET to INTERNAL TCP/22 | BLOCK | BLOCK |
| Established connection | ALLOW | PASSED |
| Suspicious application payload | BLOCK | PASSED |

All four firewall-related automated tests passed.

## 6. Security Recommendations

For a real hybrid cloud deployment, the following controls are recommended:

1. Apply separate firewall policies at Internet, DMZ, internal and cloud boundaries.
2. Restrict database access to authorized application systems.
3. Use encrypted communication between on-premises and cloud environments.
4. Review firewall logs regularly.
5. Remove unnecessary ports and services.
6. Apply least-privilege access policies.
7. Periodically review and update firewall rules.

## 7. Implementation Limitation

The current firewall is a Python-based simulation. It evaluates supplied traffic objects and does not directly inspect live network packets or configure physical, virtual or cloud firewalls.
