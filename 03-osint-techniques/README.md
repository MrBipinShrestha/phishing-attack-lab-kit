# OSINT Techniques

## Domain Investigation Checklist
| Check | Tool | Red Flag |
|---|---|---|
| Domain age | whois.com | Registered < 30 days ago |
| SSL certificate | crt.sh | Self-signed or mismatched |
| IP reputation | VirusTotal | Flagged as malicious |
| DNS records | dig | No SPF/DMARC records |

## Tools
- VirusTotal: https://virustotal.com
- URLhaus: https://urlhaus.abuse.ch
- PhishTank: https://phishtank.com
- Shodan: https://shodan.io

## Scripts
- [domain_classifier.py](../domain_classifier.py)
