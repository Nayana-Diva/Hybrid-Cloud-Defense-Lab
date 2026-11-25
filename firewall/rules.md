# Firewall Rules and Security Policy

## 1. Purpose

The firewall controls communication between network security zones in the hybrid cloud architecture.

## 2. Configured Firewall Rules

| Source | Destination | Protocol | Port | Action |
|---|---|---|---|---|
| INTERNET | DMZ | TCP | 443 | ALLOW |
| DMZ | INTERNAL | TCP | 5432 | ALLOW |
| INTERNAL | CLOUD | TCP | 443 | ALLOW |
| CLOUD | INTERNAL | TCP | 443 | ALLOW |

## 3. Security Controls

- Zone-based traffic filtering.
- Stateful inspection simulation for established connections.
- Application-layer filtering for selected suspicious patterns.
- Default-deny policy for unmatched traffic.

## 4. Application-Layer Filtering

The simulation blocks payloads containing selected patterns:

- `/admin`
- `union select`
- `drop table`
- `<script`

## 5. Testing

The firewall was tested using permitted and unauthorized traffic.

- INTERNET to DMZ on TCP 443: ALLOW.
- INTERNET to INTERNAL on TCP 22: BLOCK.

## 6. Limitations

These policies are evaluated by a Python simulation. They are not deployed as actual operating-system or cloud firewall rules.
