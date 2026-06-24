# Playbook: Phishing Email Detected

## Contain (0-15 mins)
- [ ] Quarantine email from all mailboxes
- [ ] Block sender domain at email gateway
- [ ] Block phishing URL at DNS/proxy level

## Identify (15-30 mins)
- [ ] Who received, opened, clicked?
- [ ] Analyse email headers
- [ ] Submit URL to VirusTotal

## Remediate
- [ ] Reset passwords for users who clicked
- [ ] Enable MFA if not active
- [ ] Notify affected users

## Escalate If
- Credentials were submitted
- Malware was executed
- Executive accounts targeted
