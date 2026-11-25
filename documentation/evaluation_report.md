# Project Evaluation and Testing Report

## 1. Introduction

The Hybrid Cloud Defense Lab was evaluated through manual dashboard testing and automated unit testing.

The evaluation focuses on functionality, correctness, code organization and basic efficiency.

## 2. Functional Testing

| Module | Test Scenario | Expected Result | Actual Result |
|---|---|---|---|
| Firewall | INTERNET to DMZ TCP/443 | ALLOW | ALLOW |
| Firewall | INTERNET to INTERNAL TCP/22 | BLOCK | BLOCK |
| IDS | Five unique destination ports | HIGH severity alert | Alert generated |
| Malware Scanner | EICAR test signature | QUARANTINE | QUARANTINE |
| Email Security | SPF, DKIM and DMARC PASS | AUTHENTICATED | AUTHENTICATED |
| Email Security | SPF FAIL | SUSPICIOUS | SUSPICIOUS |

All six manual dashboard scenarios produced the expected results.

## 3. Automated Testing

The project uses the Pytest framework.

The following nine automated tests were executed:

1. Allowed HTTPS traffic
2. Unauthorized traffic blocking
3. Established connection handling
4. Application-layer filtering
5. Port scan detection
6. Clean file detection
7. Malware signature detection
8. Authenticated email
9. Suspicious email

### Test Execution Result

Total tests: 9

Passed: 9

Failed: 0

Execution time: 0.05 seconds

## 4. Code Quality

The project separates security inspection logic from the web dashboard.

The security engine contains reusable functions for firewall inspection, intrusion detection, malware signature checking and email authentication.

Automated tests provide repeatable verification of the implemented functions.

## 5. Functionality and Accuracy

The implemented security modules produce the expected results for the tested scenarios.

The firewall applies configured access rules and default-deny behavior.

The IDS identifies simulated port scanning activity.

The malware scanner recognizes the EICAR test signature.

The email module evaluates supplied SPF, DKIM and DMARC results.

These results demonstrate the functionality of the academic simulation, not the effectiveness of a production security platform.

## 6. Efficiency

The automated test suite completed nine tests in approximately 0.05 seconds in the recorded execution.

The Python-based simulation uses lightweight rule evaluation and does not require live network traffic processing.

The Flask dashboard provides a simple interface for interacting with the security modules.

## 7. Best Practices

The project demonstrates several useful software and security practices:

- Default-deny network access policy.
- Separation of security logic and dashboard code.
- Automated testing.
- Reusable Python functions.
- Modular documentation.
- Clear identification of implementation limitations.

## 8. Limitations

The project does not currently implement:

- Live network packet inspection.
- Production firewall integration.
- Full antivirus scanning.
- Real malware sandbox execution.
- Independent SPF, DKIM and DMARC verification.
- Separate deployed DMZ and cloud network environments.

## 9. Future Enhancements

Future improvements may include:

1. Integration with Suricata IDS/IPS.
2. Real firewall deployment using Linux nftables.
3. Integration with ClamAV for file scanning.
4. Isolated malware sandbox analysis.
5. Real DNS and email authentication verification.
6. Docker-based network simulation.
7. Centralized logging and security event monitoring.
8. Cloud-native security monitoring integration.

## 10. Conclusion

The Hybrid Cloud Defense Lab successfully demonstrates a layered security simulation through a Flask dashboard and Python security engine.

All nine automated tests passed, and the manual dashboard scenarios produced their expected results.

The project provides a foundation for understanding network defense, intrusion detection, malware protection and email authentication in hybrid cloud environments.
