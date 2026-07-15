# 🎣 Phishing Detection & Email Forensics Lab

![Security](https://img.shields.io/badge/Focus-Phishing%20Investigation-red)
![SOC](https://img.shields.io/badge/Role-SOC%20Analyst-blue)
![MITRE](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-orange)
![Python](https://img.shields.io/badge/Automation-Python-green)

A hands-on **SOC phishing investigation and detection engineering laboratory** focused on analysing malicious emails, identifying phishing indicators, performing OSINT investigation, mapping attacker techniques, and developing defensive controls.

This project demonstrates the workflow followed by security analysts when investigating phishing incidents:

```
Suspicious Email
        ↓
Email Header Analysis
        ↓
IOC Extraction
        ↓
Threat Intelligence Lookup
        ↓
MITRE ATT&CK Mapping
        ↓
Risk Assessment
        ↓
Detection & Prevention
```

---

# 🎯 Project Objective

Phishing remains one of the most common initial access techniques used by attackers.

This lab focuses on developing practical skills in:

- Phishing email investigation
- Email header analysis
- Threat intelligence gathering
- Domain investigation
- IOC identification
- MITRE ATT&CK mapping
- Security awareness controls
- Detection engineering

---

# 🔍 Investigation Workflow

## 1. Email Header Analysis

Analysed email metadata to identify suspicious indicators:

- Sender information
- Return-Path
- Received headers
- Mail servers
- Authentication results

Investigated:

```
SPF
DKIM
DMARC
```

Example findings:

```
SPF: Failed
DKIM: Failed
DMARC: Failed

Risk Level: High
```

---

# 🌐 2. OSINT & Domain Investigation

Performed external intelligence gathering using:

## WHOIS Analysis

Investigated:

- Domain registration date
- Registrar information
- Ownership details

Suspicious indicators:

- Newly registered domains
- Hidden ownership
- Similarity to legitimate brands


## DNS Analysis

Checked:

- MX records
- TXT records
- Domain configuration


## Reputation Checking

Used:

- VirusTotal
- MXToolbox
- Domain reputation services

---

# 🧪 3. Phishing Indicator Analysis

Identified common phishing characteristics:

## Email Indicators

- Urgent language
- Suspicious attachments
- Fake sender identity
- Credential harvesting links
- Social engineering techniques


## URL Indicators

- Typosquatting domains
- Suspicious redirects
- Look-alike domains
- Newly registered domains


## Attachment Indicators

- Malicious file types
- Macro-enabled documents
- Executable files

---

# 🧠 MITRE ATT&CK Mapping

Mapped phishing activities to attacker behaviour:

| Technique | ID | Description |
|---|---|---|
| Phishing | T1566 | Initial Access |
| Spearphishing Link | T1566.002 | Malicious URL delivery |
| Spearphishing Attachment | T1566.001 | Malicious attachment |
| Phishing for Information | T1598 | Credential harvesting |
| Masquerading | T1036 | Identity deception |

---

# 🛡️ Detection Engineering

The lab includes defensive recommendations for SOC monitoring.

Detection opportunities:

## Email Security

- Detect failed SPF/DKIM/DMARC
- Monitor suspicious domains
- Analyse malicious attachments


## SIEM Monitoring

Potential Wazuh/SIEM detections:

```
Suspicious email attachment
+
Malicious domain
+
User interaction
=
Security Alert
```

---

# 📋 Investigation Cases

The lab contains practical phishing scenarios:

| Case | Investigation |
|---|---|
| Case 01 | Suspicious email header analysis |
| Case 02 | Malicious domain investigation |
| Case 03 | Credential phishing detection |
| Case 04 | Attachment analysis |
| Case 05 | SOC response recommendations |

Each investigation includes:

- Evidence collection
- Technical analysis
- Indicators of Compromise (IOCs)
- Risk assessment
- Recommended mitigation

---

# 📁 Project Structure

```
phishing-attack-lab-kit/

│
├── investigations/
│   ├── case-01-header-analysis.md
│   ├── case-02-domain-analysis.md
│
├── screenshots/
│   ├── email-analysis/
│   ├── osint-results/
│
├── scripts/
│   └── phishing_analysis.py
│
├── reports/
│
├── README.md
└── requirements.txt
```

---

# 🛠️ Tools Used

## Investigation

- WHOIS
- MXToolbox
- VirusTotal

## Security Analysis

- Email header analysers
- DNS analysis tools
- OSINT techniques

## Automation

- Python

## Detection

- Wazuh
- MITRE ATT&CK

---

# 🚨 SOC Incident Response Workflow

Example response process:

```
User Reports Email
        ↓
SOC Analyst Investigation
        ↓
Extract Indicators
        ↓
Threat Intelligence Check
        ↓
Determine Severity
        ↓
Block Domain / IOC
        ↓
Notify Users
        ↓
Document Incident
```

---

# 🧪 Skills Demonstrated

This project demonstrates:

✅ Phishing investigation  
✅ Email forensics  
✅ OSINT techniques  
✅ Threat intelligence analysis  
✅ IOC extraction  
✅ MITRE ATT&CK mapping  
✅ Detection engineering mindset  
✅ Incident documentation  

---

# 🚀 Future Improvements

Planned enhancements:

- Integrate phishing email sandboxing
- Add automated IOC extraction
- Add VirusTotal API automation
- Create Sigma detection rules
- Integrate with SIEM workflows
- Add SOAR response automation

---

# 👤 Author

## Bipin Shrestha

Cybersecurity Student | SOC Analyst | Detection Engineering

📍 Sydney, Australia 🇦🇺

GitHub:
https://github.com/MrBipinShrestha

LinkedIn:
https://www.linkedin.com/in/shresthabipin/

---

⭐ If you find this project useful, consider starring the repository.
