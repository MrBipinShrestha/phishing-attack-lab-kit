# Prevention Controls

| Layer | Control | NIST CSF |
|---|---|---|
| Email | SPF / DKIM / DMARC | PR.AC |
| Email | Sandboxing | DE.CM |
| Browser | HTTPS Enforcement | PR.PT |
| User | MFA | PR.AC |
| User | Password Manager | PR.AC |
| User | Security Awareness Training | PR.AT |
| Network | DNS Filtering | PR.PT |
| Network | IDS/IPS | DE.CM |

## Priority Order
1. MFA — highest ROI, stops most credential theft
2. DMARC — stops email spoofing
3. DNS Filtering — blocks known phishing domains
4. Security Awareness Training — last line of defence
