\# Layered Defense Blueprint for Hybrid Cloud Networks



\## 1. Project Overview



This project demonstrates a layered security architecture for protecting hybrid cloud networks. It combines network segmentation, firewall policies, intrusion detection, malware defense, and email authentication.



The project includes a Python security simulation engine, a Flask dashboard, automated tests, architecture diagrams, and technical documentation.



\*\*Note:\*\* This is an academic simulation, not a production security deployment.



\## 2. Objectives



\- Design a secure hybrid cloud network architecture.

\- Demonstrate zone-based firewall policies.

\- Detect suspicious network activity.

\- Simulate malware detection using the EICAR test signature.

\- Evaluate email authentication using SPF, DKIM, and DMARC.

\- Document security risks and mitigation strategies.



\## 3. Technology Stack



\- Python

\- Flask

\- HTML and CSS

\- Pytest

\- PowerShell

\- diagrams.net



\## 4. Main Components



| Component | Purpose |

|---|---|

| Security Engine | Evaluates simulated security events |

| Firewall | Applies access rules and default-deny logic |

| IDS | Detects suspicious port scanning |

| Malware Defense | Checks for the EICAR test signature |

| Email Security | Evaluates SPF, DKIM, and DMARC |

| Dashboard | Provides a browser-based testing interface |

| Automated Tests | Verifies core security functions |



\## 5. Project Structure



```text

Hybrid-Cloud-Defense-Lab/

├── dashboard/

├── diagrams/

├── documentation/

├── email\_security/

├── firewall/

├── ids/

├── malware/

├── network/

├── tests/

├── security\_engine.py

├── requirements.txt

└── README.md

```



\## 6. Installation



Create and activate a virtual environment:



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

```



Install dependencies:



```powershell

pip install -r requirements.txt

```



\## 7. Run the Dashboard



```powershell

python -m dashboard.app

```



Open `http://127.0.0.1:5000` in a browser.



\## 8. Run Automated Tests



```powershell

python -m pytest tests -v

```



The current test suite contains nine tests covering firewall decisions, intrusion detection, malware signature checks, and email authentication.



\## 9. Documentation



The `documentation/` directory contains:



\- `architecture.md`

\- `firewall\_policy.md`

\- `risk\_assessment.md`

\- `ids\_ips\_strategy.md`

\- `malware\_defense.md`

\- `evaluation\_report.md`



The editable architecture diagram is in `diagrams/hybrid\_cloud\_architecture.drawio`.



\## 10. Limitations



\- Firewall enforcement is simulated in Python.

\- IDS detection uses predefined event patterns, not live packet inspection.

\- Malware detection checks a test signature, not all malware.

\- Email authentication evaluates supplied results rather than live email traffic.

\- Cloud infrastructure is documented architecturally, not deployed.



\## 11. Future Enhancements



\- Integrate Suricata for live intrusion detection.

\- Implement real firewall enforcement.

\- Add cloud security monitoring.

\- Expand malware analysis capabilities.

\- Add persistent event logging and reporting.



\## 12. Conclusion



This project demonstrates how multiple security layers can work together to protect a hybrid cloud network through simulated security controls, technical documentation, and automated testing.

