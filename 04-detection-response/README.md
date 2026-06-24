# Detection & Response

## Email Indicators of Compromise
- Sender domain doesn't match display name
- Reply-to differs from sender address
- Urgent language + credential request
- Links pointing to IP addresses

## Network Indicators
- DNS queries to newly registered domains
- HTTP POST to unknown external IPs
- TLS certificates with mismatched CNs

## Playbooks
- [Phishing Email Detected](response-playbooks/phishing-email-detected.md)
- [Credential Compromise](response-playbooks/credential-compromise.md)
