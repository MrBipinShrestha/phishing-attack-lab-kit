# Phishing Attack Lab Kit

**A comprehensive guide to understanding, testing, and defending against phishing and social engineering attacks using the Social Engineering Toolkit (SET) and modern defensive strategies.**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)
![Kali](https://img.shields.io/badge/tested-Kali%20Linux-brightgreen.svg)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen.svg)

---

## 🎯 Overview

Phishing remains the **#1 attack vector** for initial compromise in cybersecurity breaches. This lab kit provides:

- **Offensive Understanding** — How attackers use SET to conduct phishing campaigns
- **Defensive Implementation** — Multi-layered controls to prevent phishing
- **Detection & Response** — How to identify and respond to phishing attempts
- **Employee Testing** — Safe, authorized security awareness programs
- **OSINT Techniques** — Methods to identify fake profiles and fraudulent domains

### Target Audience

🔒 **SOC Analysts** — Understand attack chains and improve detection  
🔐 **Security Architects** — Design phishing-resistant infrastructure  
🎓 **Educators** — Teach offensive/defensive security in controlled labs  
🛡️ **Security Awareness Trainers** — Test employee preparedness  
👨‍💻 **Penetration Testers** — Authorized social engineering assessments  

---

## 📦 Repository Structure

```
phishing-attack-lab-kit/
│
├── README.md (this file)
├── LICENSE
├── SETUP.md (Kali Linux setup guide)
├── ETHICAL-GUIDELINES.md (Important: Read first!)
│
├── 01-attack-methodology/
│   ├── README.md
│   ├── SET-setup-guide.md
│   ├── instagram-phishing-lab/
│   │   ├── attack-flow-diagram.txt
│   │   ├── step-by-step-walkthrough.md
│   │   ├── screenshots/
│   │   └── lessons-from-lab.md
│   ├── email-phishing-campaigns/
│   │   ├── template-variations.md
│   │   ├── payload-delivery.md
│   │   └── evasion-techniques.md
│   └── social-engineering-principles/
│       ├── authority-exploitation.md
│       ├── urgency-tactics.md
│       ├── trust-building.md
│       └── pretext-development.md
│
├── 02-prevention-controls/
│   ├── README.md
│   ├── technical-controls.md
│   │   ├── email-security.md
│   │   ├── browser-security.md
│   │   ├── mfa-implementation.md
│   │   └── dns-security.md
│   ├── user-practices.md
│   │   ├── email-verification.md
│   │   ├── link-checking.md
│   │   └── credential-hygiene.md
│   └── controls-matrix.md (NIST CSF mapping)
│
├── 03-osint-techniques/
│   ├── README.md
│   ├── fake-profile-identification.md
│   ├── domain-investigation.md
│   ├── scripts/
│   │   ├── whois_analyzer.py
│   │   ├── domain_classifier.py
│   │   ├── email_verification.py
│   │   └── requirements.txt
│   └── tools-directory.md (OSINT resources)
│
├── 04-detection-response/
│   ├── README.md
│   ├── detection-indicators.md
│   │   ├── network-indicators.md
│   │   ├── email-headers-analysis.md
│   │   └── behavioral-indicators.md
│   ├── response-playbooks/
│   │   ├── phishing-email-detected.md
│   │   ├── credential-compromise.md
│   │   ├── malware-deployment.md
│   │   └── ransomware-response.md
│   └── soc-runbooks.md
│
├── 05-employee-awareness-testing/
│   ├── README.md
│   ├── authorized-phishing-campaigns.md
│   ├── test-templates/
│   │   ├── executive-impersonation.md
│   │   ├── vendor-impersonation.md
│   │   ├── generic-urgency.md
│   │   └── link-clicking-test.md
│   ├── scripts/
│   │   ├── phishing_simulator.py
│   │   ├── results_analyzer.py
│   │   ├── report_generator.py
│   │   └── requirements.txt
│   └── awareness-training/
│       ├── beginner-module.md
│       ├── intermediate-module.md
│       └── advanced-module.md
│
├── 06-lab-exercises/
│   ├── README.md
│   ├── lab-01-instagram-clone.md
│   ├── lab-02-email-campaign.md
│   ├── lab-03-credential-harvesting.md
│   ├── lab-04-detection-challenge.md
│   └── lab-05-incident-response-drill.md
│
├── 07-tools-reference/
│   ├── README.md
│   ├── SET-commands-cheatsheet.md
│   ├── wireshark-filters.md
│   ├── email-analysis-tools.md
│   └── dns-investigation-tools.md
│
├── 08-case-studies/
│   ├── README.md
│   ├── optus-data-breach.md
│   ├── mgm-resorts-social-engineering.md
│   └── [real-world incident analysis]
│
├── research/
│   ├── phishing-statistics.md
│   ├── attack-trends-2024.md
│   └── bibliography.bib
│
└── examples/
    ├── sample_phishing_email.txt
    ├── suspicious_domain_analysis.json
    └── detection_report.txt
```

---

## 🚀 Quick Start (5 Minutes)

### 1. Understand the Attack (Read First)
```bash
# Start here for high-level overview
cat 01-attack-methodology/instagram-phishing-lab/attack-flow-diagram.txt
cat 01-attack-methodology/instagram-phishing-lab/step-by-step-walkthrough.md
```

### 2. Review Prevention Controls
```bash
# See multi-layered defenses against phishing
cat 02-prevention-controls/controls-matrix.md
```

### 3. Learn OSINT Techniques
```bash
# Detect fake profiles and fraudulent domains
cat 03-osint-techniques/fake-profile-identification.md
python 03-osint-techniques/scripts/whois_analyzer.py --help
```

### 4. Run a Simulation (Authorized Only!)
```bash
# Test employee awareness (requires approval)
python 05-employee-awareness-testing/scripts/phishing_simulator.py --help
```

---

## 🔥 Key Features

### 1. **Real Attack Methodology**
Detailed walkthrough of **Instagram credential harvester phishing** using SET:
- Website cloning techniques
- Local IP hosting
- Credential capture & exfiltration
- Evasion tactics used by attackers

### 2. **Multi-Layered Prevention**
Comprehensive controls mapped to **NIST Cybersecurity Framework**:

| Layer | Control | Examples |
|-------|---------|----------|
| **Email** | Filtering & Authentication | SPF, DKIM, DMARC, sandboxing |
| **Browser** | Security Features | HTTPS enforcement, certificate warnings |
| **User** | Training & Processes | Email verification, reporting procedures |
| **Network** | Detection | DNS filtering, IDS/IPS, proxy logging |

### 3. **OSINT Toolkit**
Identify fake profiles & malicious domains:
- Domain age & registration analysis
- Email verification techniques
- Social media account investigation
- DNS anomaly detection

### 4. **Employee Testing Framework**
Safely test security awareness:
- Approved phishing templates
- Metrics & reporting
- Results analysis
- Training recommendations

### 5. **Detection & Response**
SOC-focused content:
- Email header analysis
- Network indicators of compromise
- Incident response playbooks
- MITRE ATT&CK mapping

---

## ⚖️ ETHICAL & LEGAL GUIDELINES

**🚨 IMPORTANT:** This toolkit is for **educational and authorized testing ONLY**.

### What You CAN Do
✅ Learn phishing attack methodologies in **lab environments**  
✅ Conduct **authorized** security awareness testing with **written permission**  
✅ Test **your own** systems and infrastructure  
✅ Teach cybersecurity to students in **controlled labs**  
✅ Help organizations improve their defenses  

### What You CANNOT Do
❌ Conduct unauthorized phishing attacks  
❌ Test others' systems without written approval  
❌ Use for malicious purposes or fraud  
❌ Harvest credentials without consent  
❌ Deploy any techniques against individuals  

**Read [ETHICAL-GUIDELINES.md](ETHICAL-GUIDELINES.md) before proceeding.**

---

## 📋 Case Study: Instagram Phishing Attack

### The Scenario
Using SET, an attacker creates a **fake Instagram login page** to harvest credentials.

### Attack Chain
```
1. Social Media Reconnaissance
   ↓
2. Website Cloning (using SET)
   ↓
3. Fake Page Hosted on Attacker's Network
   ↓
4. Social Engineering to get victims to visit
   ↓
5. Credential Capture & Exfiltration
   ↓
6. Account Takeover / Further Exploitation
```

### What Made It Work
- Professional appearance (identical to real Instagram)
- Ease of access (no complex steps)
- Trust in social engineering
- No user validation of URL

### How to Detect It
- Suspicious email/DM sending to page
- URL verification (whois, certificate check)
- Network-level detection (hosting on suspicious IP)
- Email security tools flag phishing

### Prevention
- MFA on social accounts
- Browser security (HTTPS warnings)
- Email filtering
- User awareness training

**Full analysis:** See `01-attack-methodology/instagram-phishing-lab/`

---

## 🛠️ Tools Included

### Python Scripts (Ready to Use)

**OSINT Analysis:**
```bash
# Analyze suspicious domain
python 03-osint-techniques/scripts/whois_analyzer.py \
  --domain suspiciousdomain.com \
  --output analysis.json

# Classify domain legitimacy
python 03-osint-techniques/scripts/domain_classifier.py \
  --input domains.txt \
  --threshold 0.75
```

**Employee Awareness Testing:**
```bash
# Run phishing simulation
python 05-employee-awareness-testing/scripts/phishing_simulator.py \
  --campaign "Executive Impersonation" \
  --targets employees.csv \
  --template "CFO Money Transfer" \
  --approval-number AUTH-2024-001

# Analyze results
python 05-employee-awareness-testing/scripts/results_analyzer.py \
  --campaign-id "exec-001" \
  --generate-report
```

---

## 📚 Learning Paths

### Path 1: Offensive Security (Penetration Testers)
1. Read: `01-attack-methodology/SET-setup-guide.md`
2. Lab: `06-lab-exercises/lab-01-instagram-clone.md`
3. Advanced: `01-attack-methodology/evasion-techniques.md`

### Path 2: Defensive/SOC (Security Analysts)
1. Read: `04-detection-response/detection-indicators.md`
2. Lab: `06-lab-exercises/lab-04-detection-challenge.md`
3. Reference: `04-detection-response/soc-runbooks.md`

### Path 3: Security Awareness (HR/Training)
1. Read: `05-employee-awareness-testing/authorized-phishing-campaigns.md`
2. Review: `05-employee-awareness-testing/awareness-training/`
3. Implement: `05-employee-awareness-testing/scripts/phishing_simulator.py`

### Path 4: Architecture/Strategy (Security Leaders)
1. Read: `02-prevention-controls/controls-matrix.md`
2. Review: `02-prevention-controls/technical-controls.md`
3. Plan: Implement multi-layered controls

---

## 📊 Statistics & Context

**Why Phishing Matters:**
- Phishing is the **initial vector in 90%+ of breaches**
- Average cost per breach due to phishing: **USD $4.29M**
- Employee click rates on phishing: **34% (2023 data)**
- Click-to-compromise time: **1-2 hours average**

**This Lab Teaches:**
- How attackers exploit human psychology
- Why technical controls alone fail
- Importance of layered defenses
- How to test and improve awareness

---

## 🤝 Contributing

Found a phishing technique we missed? Have a real-world case study to share?

**See [CONTRIBUTING.md](CONTRIBUTING.md) for:**
- How to add new attack techniques
- Case study submission template
- Tool improvement guidelines
- Ethical review process

---

## 📖 Documentation

- **[SETUP.md](SETUP.md)** — Kali Linux environment setup
- **[ETHICAL-GUIDELINES.md](ETHICAL-GUIDELINES.md)** — Legal/ethical requirements
- **[01-attack-methodology/README.md](01-attack-methodology/README.md)** — Detailed attack walkthroughs
- **[02-prevention-controls/README.md](02-prevention-controls/README.md)** — Defense implementation
- **[05-employee-awareness-testing/README.md](05-employee-awareness-testing/README.md)** — Testing framework

---

## 🔗 Links & Resources

### Official Tools
- **Social Engineering Toolkit (SET):** https://www.trustedsec.com/tools/social-engineer-toolkit/
- **Kali Linux:** https://www.kali.org/
- **Wireshark:** https://www.wireshark.org/

### OSINT Resources
- **WHOIS Lookup:** whois.com
- **Shodan:** shodan.io (IP/port search)
- **URLhaus:** urlhaus.abuse.ch (malicious URLs)
- **PhishTank:** phishtank.com (phishing database)

### Educational
- **MITRE ATT&CK:** attack.mitre.org
- **NIST CSF:** nist.gov/cyberframework
- **OWASP Top 10:** owasp.org

---

## 📈 Roadmap

- [ ] Interactive email header analyzer (web tool)
- [ ] Automated phishing detection rules (Sigma/Yara)
- [ ] Red team vs Blue team simulation framework
- [ ] Real-time phishing monitoring dashboard
- [ ] Integration with SIEM systems

---

## ⚖️ License & Legal

**MIT License** — Use for education and authorized testing only.

**Important Disclaimers:**
- This toolkit is for **authorized security testing only**
- Unauthorized phishing is **illegal** in most jurisdictions
- Always obtain **written permission** before testing
- Use in **isolated lab environments** for learning
- Never target real users without explicit approval

---

## 💬 Questions?

- **General Questions:** Open an issue
- **Bug Reports:** File a GitHub issue with details
- **Security Issues:** Email responsibly (don't create public issue)
- **Lab Help:** See [06-lab-exercises/README.md](06-lab-exercises/README.md)

---

## 👤 Attribution

**Repository Created:** Bipin Shrestha  
**Based on:** MIT503 Information Security coursework (Social Engineering Lab)  
**Last Updated:** June 2024  
**Maintained for:** Security professionals, educators, SOC teams  

---

## 🎓 For Educators

This kit is ideal for:
- **Cybersecurity courses** — Hands-on offensive/defensive training
- **SOC training programs** — Attack detection and response
- **Security awareness** — Employee phishing testing
- **Red team exercises** — Controlled penetration testing

**Student lab environment setup:** See [SETUP.md](SETUP.md)

---

**Remember:** The goal is to make organizations MORE secure by understanding how phishing works and implementing layered defenses.

**Let's build better defenses together.** 🛡️
