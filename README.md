# 🎣 Phishing Detection & Email Forensics Lab

![Python](https://img.shields.io/badge/Python-Analysis-blue?style=for-the-badge)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-T1566-red?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Email_Security-purple?style=for-the-badge)

> **Ethical hacking lab documenting phishing attack methodology, email header forensics, OSINT-based domain analysis, and SOC detection controls for email-based threats.**
>
> This lab builds the skills to detect, analyze, and respond to one of the most common initial access vectors in real-world breaches.

---

## 🧠 Security Engineering Objective

This lab answers a critical SOC question:

> "How do attackers craft convincing phishing campaigns, and what forensic evidence can a SOC analyst use to detect and investigate them?"

To validate this, I built a complete phishing analysis framework covering:

- Attack methodology (how phishing campaigns are built)
- Email header forensics (how to trace and verify email origin)
- OSINT domain analysis (how to investigate malicious domains)
- SOC detection controls (how to build detection logic)

---

## 🏗️ Phishing Attack Lifecycle

```
┌────────────────────────────────────────────────────────┐
│                  Phishing Attack Chain                  │
└────────────────────────────────────────────────────────┘

Phase 1: Reconnaissance       Phase 2: Infrastructure
┌─────────────────┐           ┌─────────────────────────┐
│ OSINT Target    │           │ Register lookalike domain│
│ Research        │           │ paypa1.com vs paypal.com │
│ - LinkedIn      │──────────►│ Set up phishing page    │
│ - Email format  │           │ Configure fake MX records│
│ - Org chart     │           └──────────────┬──────────┘
└─────────────────┘                          │
                                             ▼
Phase 3: Delivery             Phase 4: Credential Capture
┌─────────────────┐           ┌─────────────────────────┐
│ Craft email     │           │ Victim enters creds     │
│ - Spoofed From  │──────────►│ Data sent to attacker   │
│ - Urgency hook  │           │ Redirect to real site   │
│ - Malicious link│           │ Victim unaware          │
└─────────────────┘           └─────────────────────────┘
```

---

## 🔍 Email Header Forensics

### Anatomy of a Phishing Email Header

```
Received: from mail.phish-domain.com (192.168.1.100)
          by legitimate-mail.com with ESMTP
Return-Path: <attacker@phish-domain.com>
From: "PayPal Security" <security@paypa1.com>      ← Spoofed display name
Reply-To: attacker@different-domain.com             ← Different reply domain
X-Originating-IP: 45.33.32.156                     ← Actual sender IP
Authentication-Results: spf=fail                    ← SPF failure
                        dkim=fail                   ← DKIM failure
                        dmarc=fail                  ← DMARC failure
```

### Header Analysis Script
```python
import email
import re
from datetime import datetime

def analyze_email_headers(raw_email):
    msg = email.message_from_string(raw_email)
    
    analysis = {
        'from': msg.get('From'),
        'reply_to': msg.get('Reply-To'),
        'return_path': msg.get('Return-Path'),
        'received_from': extract_originating_ip(msg),
        'spf_result': extract_auth_result(msg, 'spf'),
        'dkim_result': extract_auth_result(msg, 'dkim'),
        'dmarc_result': extract_auth_result(msg, 'dmarc'),
    }
    
    # Flag suspicious indicators
    flags = []
    if analysis['from'] != analysis['return_path']:
        flags.append('MISMATCH: From ≠ Return-Path')
    if analysis['spf_result'] == 'fail':
        flags.append('FAIL: SPF authentication failed')
    if analysis['dkim_result'] == 'fail':
        flags.append('FAIL: DKIM signature invalid')
    if analysis['dmarc_result'] == 'fail':
        flags.append('FAIL: DMARC policy violation')
    
    analysis['flags'] = flags
    analysis['risk_score'] = len(flags) * 25  # 0-100
    
    return analysis
```

---

## 📊 OSINT Domain Analysis

### Indicators to Investigate

```python
# Domain age check (new domains = suspicious)
# whois lookup for registration date
# Typosquatting patterns
SUSPICIOUS_PATTERNS = [
    r'paypa[l1]',       # paypal → paypa1
    r'go{2,}gle',       # google → gooogle  
    r'micros0ft',       # microsoft → micros0ft
    r'arnazon',         # amazon → arnazon
]

# Check domain reputation
# VirusTotal, URLhaus, PhishTank
# Certificate transparency logs
# Historical WHOIS data
```

### Domain Reputation Checks

| Indicator | Tool | SOC Value |
|-----------|------|-----------|
| Domain age | WHOIS | New domains = high risk |
| IP reputation | VirusTotal | Known bad IPs |
| Malware hosting | URLhaus | Active phishing pages |
| Certificate | crt.sh | Lookalike cert detection |
| Passive DNS | SecurityTrails | Historical infrastructure |

---

## 🚨 SOC Detection Controls

### Email Gateway Rules

```yaml
# Detect SPF/DKIM/DMARC failures
rule:
  name: "Email Authentication Failure"
  condition: spf=fail AND dkim=fail AND dmarc=fail
  action: quarantine
  severity: HIGH

# Detect mismatched sender domains
rule:
  name: "From/Reply-To Domain Mismatch"
  condition: from_domain != replyto_domain
  action: flag_for_review
  severity: MEDIUM

# Detect lookalike domains
rule:
  name: "Typosquatting Domain Detection"
  condition: levenshtein_distance(domain, known_brands) <= 2
  action: block
  severity: HIGH
```

### Wazuh SIEM Rules
```xml
<rule id="100200" level="10">
  <match>spf=fail dkim=fail dmarc=fail</match>
  <description>Email authentication triple failure — likely phishing</description>
  <mitre>
    <id>T1566</id>
  </mitre>
</rule>
```

---

## 📊 MITRE ATT&CK Mapping

| Tactic | Technique | Sub-technique | Scenario |
|--------|-----------|---------------|---------|
| Initial Access | T1566 | T1566.001 | Spear phishing attachment |
| Initial Access | T1566 | T1566.002 | Spear phishing link |
| Reconnaissance | T1598 | T1598.003 | Phishing for credentials |
| Resource Development | T1583 | T1583.001 | Domain registration |
| Defense Evasion | T1036 | T1036.005 | Lookalike domain masquerade |

---

## 🛡️ Prevention Controls Matrix

| Control | Coverage | Implementation |
|---------|----------|----------------|
| SPF records | Medium | DNS TXT record |
| DKIM signing | High | Email server config |
| DMARC policy | High | DNS TXT + enforcement |
| Email filtering | High | Gateway appliance |
| Security awareness | High | Training + simulation |
| MFA | Critical | Identity provider |
| URL sandboxing | High | Email gateway |

---

## 🧰 Tools Used

| Tool | Purpose |
|------|---------|
| Python | Email header analysis scripts |
| WHOIS | Domain registration lookup |
| VirusTotal | Domain/IP reputation check |
| PhishTank | Known phishing database |
| MXToolbox | Email authentication verification |
| crt.sh | Certificate transparency search |

---

## 📸 Evidence

Screenshots in `screenshots/` folder:
- Email header analysis output
- OSINT domain investigation results
- Detection rule firing in gateway
- Phishing page replica analysis

---

## ⚠️ Ethical Notice

All phishing simulations conducted in isolated lab environment with explicit authorization. Techniques documented for defensive education and SOC analyst training only. Always obtain written authorization before conducting phishing simulations against real users.

---

## 🔮 Extensions

- [ ] Automated phishing detection pipeline
- [ ] ML-based phishing URL classifier
- [ ] Business Email Compromise (BEC) detection
- [ ] Lookalike domain monitoring system
- [ ] Threat intelligence feed integration

---

## 📬 Contact

**GitHub:** [github.com/MrBipinShrestha](https://github.com/MrBipinShrestha)
**LinkedIn:** [linkedin.com/in/shresthabipin](https://www.linkedin.com/in/shresthabipin)
**Location:** Sydney, Australia
