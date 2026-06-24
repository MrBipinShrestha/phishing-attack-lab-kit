# Prevention Controls Matrix: Phishing Defense Strategy

**This matrix maps technical, user, and organizational controls to specific phishing attack techniques.**

---

## 🎯 Attack-to-Control Mapping

### Attack Phase: Social Engineering / Email Delivery

| Attack Technique | Attack Goal | Control Layer | Specific Control | Implementation | Effectiveness |
|------------------|------------|---------------|------------------|----------------|----------------|
| **Phishing Email Delivery** | Get user to click link | Email Security | SPF/DKIM/DMARC | Require domain authentication; reject spoofed email | HIGH |
| Phishing Email Delivery | Get user to click link | Email Security | Sandboxing | Detonate suspicious links in sandbox before delivery | MEDIUM |
| Phishing Email Delivery | Get user to click link | Email Security | URL Filtering | Scan URLs in emails; block known phishing links | MEDIUM |
| Phishing Email Delivery | Get user to click link | Email Security | Content Filtering | Block emails with suspicious keywords or attachments | MEDIUM |
| Phishing Email Delivery | Get user to click link | User Practice | Email Verification | Verify sender address (not display name); hover over links | HIGH |
| Phishing Email Delivery | Get user to click link | User Practice | Reporting Process | One-click phishing report button in email client | MEDIUM |
| Phishing Email Delivery | Get user to click link | Organizational | Training | Security awareness: recognize phishing characteristics | HIGH |

---

### Attack Phase: Website Cloning / Fake Page Hosting

| Attack Technique | Attack Goal | Control Layer | Specific Control | Implementation | Effectiveness |
|------------------|------------|---------------|------------------|----------------|----------------|
| **Website Cloning** | Deceive user about legitimacy | Browser Security | HTTPS Enforcement | Enable HSTS; force HTTPS; warn on HTTP | HIGH |
| Website Cloning | Deceive user about legitimacy | Browser Security | Certificate Validation | Display certificate warnings for self-signed certs | MEDIUM |
| Website Cloning | Deceive user about legitimacy | Network | DNS Filtering | Block newly registered/suspicious domains | MEDIUM |
| Website Cloning | Deceive user about legitimacy | Network | URL Reputation | Check domain age, WHOIS, SSL certificate status | MEDIUM |
| Website Cloning | Deceive user about legitimacy | User Practice | URL Verification | Type official URL manually; don't click email links | HIGH |
| Website Cloning | Deceive user about legitimacy | User Practice | Certificate Checking | Verify "https" and valid certificate before login | MEDIUM |
| Website Cloning | Deceive user about legitimacy | Organizational | Policy | Require typing URLs manually for sensitive sites | HIGH |

---

### Attack Phase: Credential Harvesting / Form Submission

| Attack Technique | Attack Goal | Control Layer | Specific Control | Implementation | Effectiveness |
|------------------|------------|---------------|------------------|----------------|----------------|
| **Credential Capture** | Steal username/password | Authentication | MFA/2FA | Require second factor (SMS, app, hardware key) | CRITICAL |
| Credential Capture | Steal username/password | User Practice | Password Manager | Auto-fill only on official domains; alerts on mismatch | MEDIUM |
| Credential Capture | Steal username/password | User Practice | Credential Hygiene | Never enter credentials on unfamiliar sites | MEDIUM |
| Credential Capture | Steal username/password | Network | TLS/SSL Encryption | Encrypt all credential transmission (HTTPS) | HIGH |
| Credential Capture | Steal username/password | Network | Network Monitoring | Alert on unencrypted credentials in traffic | MEDIUM |

---

### Attack Phase: Account Compromise / Lateral Movement

| Attack Technique | Attack Goal | Control Layer | Specific Control | Implementation | Effectiveness |
|------------------|------------|---------------|------------------|----------------|----------------|
| **Account Takeover** | Control victim account | Authentication | MFA/2FA | Second factor blocks access even with password | CRITICAL |
| Account Takeover | Control victim account | Organizational | Anomaly Detection | Alert on unusual login patterns, locations, times | MEDIUM |
| Account Takeover | Control victim account | Organizational | Incident Response | Rapid response to compromise; credential reset | MEDIUM |

---

## 📊 Control Effectiveness by Layer

### Technical Controls (Network/System Level)
```
CRITICAL (must have):
  ✓ MFA/2FA - Stops account compromise even if password stolen
  ✓ HTTPS/TLS - Encrypts credentials in transit
  ✓ Email authentication (SPF/DKIM/DMARC) - Prevents email spoofing

HIGH (strongly recommended):
  ✓ Email filtering - Blocks phishing emails before delivery
  ✓ URL filtering - Blocks malicious domains
  ✓ HSTS - Forces HTTPS connections
  ✓ DNS filtering - Blocks suspicious domains

MEDIUM (good to have):
  ✓ Email sandboxing - Detonate suspicious links
  ✓ Network monitoring - Detect unusual traffic
  ✓ Anomaly detection - Detect unusual account access
  ✓ Certificate transparency logs - Track SSL certificates
```

### User Practice Controls (Behavioral)
```
CRITICAL (must teach):
  ✓ Verify sender address (not display name)
  ✓ Check URL before clicking (hover over links)
  ✓ Type official URLs manually (don't click email links)
  ✓ Check for HTTPS and valid certificates
  ✓ Never enter credentials on unfamiliar sites
  ✓ Enable MFA on important accounts

HIGH (important):
  ✓ Use password managers (auto-fill verification)
  ✓ Report suspicious emails
  ✓ Credential hygiene (don't reuse passwords)
  ✓ Think before clicking
  
MEDIUM (helpful):
  ✓ Recognize phishing characteristics
  ✓ Understand social engineering tactics
  ✓ Know when to escalate to security team
```

### Organizational Controls (Policy/Process)
```
CRITICAL (must enforce):
  ✓ MFA requirement for all accounts
  ✓ Security awareness training
  ✓ Incident response procedures
  ✓ Credential reset procedures

HIGH (important):
  ✓ Email security policies
  ✓ Clean desk policy (no credentials visible)
  ✓ Visitor verification procedures
  ✓ Access control policies

MEDIUM (helpful):
  ✓ Phishing simulation exercises
  ✓ Regular security audits
  ✓ Third-party security assessments
```

---

## 🛡️ Layered Defense Model

```
                     ┌─────────────────────────┐
                     │   User Awareness       │
                     │ (Training & Practices)  │
                     └────────────┬────────────┘
                                  │
                     ┌────────────┴────────────┐
                     │  Email Security Layer  │
                     │ (Filtering, Auth, DKIM)│
                     └────────────┬────────────┘
                                  │
                     ┌────────────┴────────────┐
                     │  Network Security      │
                     │ (DNS, URL, IDS/IPS)    │
                     └────────────┬────────────┘
                                  │
                     ┌────────────┴────────────┐
                     │  Browser Security      │
                     │ (HTTPS, Certs, Ext.)   │
                     └────────────┬────────────┘
                                  │
                     ┌────────────┴────────────┐
                     │  Authentication        │
                     │ (MFA/2FA - CRITICAL!)  │
                     └────────────┬────────────┘
                                  │
                     ┌────────────┴────────────┐
                     │  Account Security      │
                     │ (Monitoring, Response) │
                     └────────────────────────┘
```

**Why Layering Matters:**
- No single control stops all attacks
- Multiple layers catch attacks that slip through one layer
- If user clicks link (layer 1 fails), email security catches it (layer 2)
- If email is phishing (layers 1-2 fail), browser security helps (layer 3)
- If user enters password (layers 1-3 fail), MFA stops account takeover (layer 4-5)

---

## ✅ Implementation Checklist

### Email Security (Week 1-2)
- [ ] Implement SPF records (prevent spoofing)
- [ ] Implement DKIM (digital signing)
- [ ] Implement DMARC (policy enforcement)
- [ ] Enable email filtering (block phishing keywords)
- [ ] Deploy URL scanning in email gateway
- [ ] Test with phishing simulation

### Browser & Network Security (Week 2-3)
- [ ] Enable HSTS (force HTTPS)
- [ ] Deploy HTTPS everywhere
- [ ] Implement DNS filtering
- [ ] Deploy URL reputation checking
- [ ] Implement certificate transparency monitoring
- [ ] Deploy SIEM/SOC monitoring

### Authentication (Week 3-4)
- [ ] Deploy MFA for all critical systems
- [ ] Enforce strong password policies
- [ ] Implement password managers
- [ ] Deploy anomaly detection
- [ ] Implement account lockout policies
- [ ] Enable login auditing

### User Training (Week 1, ongoing)
- [ ] Initial security awareness training (all employees)
- [ ] Phishing email training (monthly)
- [ ] Quarterly phishing simulation tests
- [ ] Advanced training for high-risk users
- [ ] New employee orientation (security module)
- [ ] Regular newsletters/tips

### Incident Response (Ongoing)
- [ ] Document incident response procedures
- [ ] Establish 24/7 security contact
- [ ] Test incident response team
- [ ] Maintain credential reset process
- [ ] Document forensics procedures
- [ ] Conduct post-incident reviews

---

## 📈 Metrics & Monitoring

### Email Security Metrics
```
- Phishing emails blocked (daily)
- False positive rate (should be <5%)
- URL scanning block rate
- DMARC reject/quarantine rate
- Email forwarding rule violations
```

### User Behavior Metrics
```
- Phishing simulation click rate (target: <5%)
- Phishing simulation report rate (target: >80%)
- Email security training completion
- Password change frequency
- MFA enrollment rate (target: 100%)
```

### Detection & Response Metrics
```
- Time to detect phishing email
- Time to block malicious URL
- Time to respond to incident
- Credential compromise recovery time
- False positive rate (alerts to investigate)
```

---

## 🚨 Red Flags / Early Warning Signs

### Email Level
```
- Requests for credentials via email (NEVER legitimate)
- Urgent language ("Act now", "Disabled", "Verify immediately")
- Generic greetings ("Dear Customer" not "Dear John")
- Spelling/grammar errors
- Suspicious sender address (not official domain)
- Suspicious links (hover to see real URL)
- Threats or intimidation
- Requests to bypass normal procedures
```

### Website Level
```
- HTTP instead of HTTPS (not secure)
- Self-signed certificate (warning sign)
- Recently registered domain (age < 30 days)
- Slight URL variations (instagram.net vs instagram.com)
- Missing logos or official branding
- Unusual page layout or design
- Forms asking for password directly
```

### Account Level
```
- Login from unusual location
- Login at unusual time
- Multiple failed login attempts
- Sudden password change request
- Unexpected account activity
- Email forwarding rules added
- Account recovery methods changed
```

---

## 💼 NIST CSF Mapping

| NIST Function | Category | Control | Related Technique |
|---------------|----------|---------|-------------------|
| **IDENTIFY** | Asset Management | Inventory of systems | Know what needs protection |
| **IDENTIFY** | Business Environment | Understand dependencies | Email, authentication, browsers |
| **PROTECT** | Access Control | Authorize credentials | MFA/2FA implementation |
| **PROTECT** | Protective Technology | Firewalls, filtering | Email filtering, DNS blocking |
| **DETECT** | Anomalies & Events | Monitor activities | Email logs, login patterns |
| **DETECT** | Detection Processes | Investigate anomalies | Email analysis, user behavior |
| **RESPOND** | Response Planning | Incident procedures | Credential reset, notification |
| **RECOVER** | Improvements | Post-incident analysis | Lessons learned, policy updates |

---

## 📊 Cost-Benefit Analysis

### Cost of Prevention (Annual)
```
MFA Implementation:        $50,000 - $100,000
Email Security Tools:      $30,000 - $50,000
Training Programs:         $10,000 - $20,000
Monitoring/SOC:            $100,000 - $200,000
───────────────────────────────────────────
Total Annual:              $190,000 - $370,000
Per Employee (500):        $380 - $740
```

### Cost of Breach
```
Average Phishing Breach:   $4,290,000 - $10,000,000
Remediation Costs:         $500,000 - $2,000,000
Legal/Compliance:          $1,000,000 - $5,000,000
Lost Productivity:         $2,000,000 - $5,000,000
Reputation Damage:         $1,000,000+ (varies)
───────────────────────────────────────────
Total per Incident:        $8,790,000+
```

**ROI:** Every $1 spent on prevention saves ~$10-50 in breach costs.

---

## 🔄 Continuous Improvement

### Monthly Reviews
- [ ] Review phishing email samples
- [ ] Analyze blocked URLs
- [ ] Review false positive rate
- [ ] Check MFA enrollment rate
- [ ] Review incident response times

### Quarterly Reviews
- [ ] Update phishing simulation templates
- [ ] Review threat intelligence
- [ ] Assess control effectiveness
- [ ] Plan training updates
- [ ] Update incident response procedures

### Annual Reviews
- [ ] Full security assessment
- [ ] Policy review and updates
- [ ] Tool evaluation and upgrades
- [ ] Regulatory compliance review
- [ ] Budget planning for next year

---

## 📚 References

- **NIST CSF:** https://www.nist.gov/cyberframework
- **NIST SP 800-63B:** Authentication - https://pages.nist.gov/
- **OWASP:** Phishing - https://owasp.org/
- **SANS:** Security Training - https://www.sans.org/
- **Gartner:** Email Security Report - https://www.gartner.com/

---

**Last Updated:** June 2024  
**Review Schedule:** Quarterly  
**Approval Authority:** CISO / Security Leadership  

