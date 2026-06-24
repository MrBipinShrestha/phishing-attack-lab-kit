# Email Header Analysis: Detecting Phishing

**A practical guide for SOC analysts to detect phishing emails by analyzing email headers.**

---

## 📧 What is an Email Header?

An email header contains metadata about an email message, including:
- **From address** — Who sent the email
- **To address** — Who received it
- **Subject** — Email subject line
- **Date/Time** — When it was sent
- **Routing information** — Path the email took
- **Authentication results** — SPF, DKIM, DMARC status
- **Server information** — Mail servers involved

### Where to Find Email Headers

**Gmail:**
1. Open email
2. Click three-dot menu (⋯)
3. Select "Show original"
4. View full headers

**Outlook:**
1. Open email
2. Click "File" → "Properties"
3. Or click "Message" → "Actions" → "View Message Details"

**Apple Mail:**
1. Open email
2. View → Message → All Headers
3. Or use key combo: Control + Cmd + H

---

## 🔍 Email Header Anatomy

### Example Email Header
```
From: "Support" <support-verify@instagram-secure.com>
To: victim@company.com
Subject: Verify Your Instagram Account [URGENT]
Date: Mon, 24 Jun 2024 14:32:15 +0000
Message-ID: <A1B2C3D4E5F6@instagram-secure.com>

Received: from mail.instagram-secure.com (mail.instagram-secure.com [192.168.1.100])
        by company.com with SMTP id xyz123
        for <victim@company.com>; Mon, 24 Jun 2024 14:32:10 +0000

Return-Path: <noreply@instagram-secure.com>
Authentication-Results: company.com;
        dmarc=fail reason="Policy with p=none" (c=none);
        spf=fail smtp.mailfrom=noreply@instagram-secure.com
        dkim=fail

Received-SPF: fail (gmail.com: domain of noreply@instagram-secure.com 
        does not pass SPF check)

DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=instagram-secure.com;
        s=default; h=from:subject:date:to:message-id;
        bh=ABCD1234; b=EFGH5678...
```

---

## 🚨 Red Flags in Email Headers

### 1. **Spoofed "From" Address**

```
SUSPICIOUS:
From: "Instagram Support" <support@instagram-secure.com>

RED FLAG: 
- Sender address is NOT @instagram.com
- Uses subtle variation (instagram-secure.com instead of instagram.com)
- Instagram official: support@instagram.com

LEGITIMATE EXAMPLE:
From: "Instagram Support" <noreply@instagram.com>
- Uses official @instagram.com domain
- Consistent with official communications
```

**How to Detect:**
- Always check the actual email address (not just display name)
- Hover over sender name to see full email address
- Be suspicious of variations on legitimate domains

---

### 2. **SPF Failure**

```
SUSPICIOUS:
Authentication-Results: company.com;
        spf=fail smtp.mailfrom=noreply@instagram-secure.com

RED FLAG:
- SPF check FAILED
- Email claims to be from instagram.com but comes from different server
- Indicates spoofing or misconfiguration

LEGITIMATE EXAMPLE:
Authentication-Results: company.com;
        spf=pass smtp.mailfrom=noreply@instagram.com
```

**What is SPF?**
SPF (Sender Policy Framework) tells email servers which servers are authorized to send emails for a domain.

**Why it matters:**
- If SPF fails, someone is pretending to be that domain
- Phishers often send from unauthorized servers

---

### 3. **DKIM Failure**

```
SUSPICIOUS:
DKIM-Signature: v=1; a=rsa-sha256;
        d=instagram-secure.com
        b=ABCD1234...
        
Authentication-Results: company.com;
        dkim=fail

RED FLAG:
- DKIM signature doesn't verify
- Email claims to be from domain but signature is invalid
- Indicates tampering or spoofing

LEGITIMATE EXAMPLE:
Authentication-Results: company.com;
        dkim=pass
```

**What is DKIM?**
DKIM (DomainKeys Identified Mail) digitally signs emails to prove they come from a legitimate server.

**Why it matters:**
- Phishers can't create valid DKIM signatures for domains they don't control
- DKIM failure is strong indicator of phishing

---

### 4. **DMARC Failure**

```
SUSPICIOUS:
Authentication-Results: company.com;
        dmarc=fail reason="Policy with p=none"

RED FLAG:
- DMARC check FAILED
- Email fails authentication across SPF and DKIM
- Should be quarantined or rejected

LEGITIMATE EXAMPLE:
Authentication-Results: company.com;
        dmarc=pass
```

**What is DMARC?**
DMARC (Domain-based Message Authentication, Reporting & Conformance) enforces SPF/DKIM and tells receivers what to do with failed emails.

**DMARC Policies:**
- `p=reject` — Reject all unauthorized emails
- `p=quarantine` — Quarantine (move to spam) unauthorized emails
- `p=none` — Monitor only, don't enforce

---

### 5. **Suspicious Return-Path**

```
SUSPICIOUS:
Return-Path: <noreply@attackerdomain.com>

RED FLAG:
- Return-Path doesn't match From address
- Indicates email is not actually from stated sender
- Bounce-backs will go to different server

LEGITIMATE EXAMPLE:
Return-Path: <noreply@instagram.com>
From: "Instagram Support" <noreply@instagram.com>
- Both point to same legitimate domain
```

**Why it matters:**
- Return-Path shows where bounce-back emails go
- Legitimate companies use consistent addresses
- Mismatch indicates spoofing

---

### 6. **Suspicious Received Path**

```
SUSPICIOUS:
Received: from mail.instagram-secure.com (mail.instagram-secure.com [192.168.1.100])
        by company.com with SMTP id xyz123

RED FLAGS:
- Originating server is NOT Instagram's official server
- IP address 192.168.1.100 is private/non-routable
- Hostname doesn't match official Instagram mail servers

LEGITIMATE EXAMPLE:
Received: from mail-sorter.instagram.com (mail-sorter.instagram.com [31.13.68.1])
        by company.com with SMTP id abc123
- Official Instagram mail server
- Real IP address from Instagram's infrastructure
```

**How to Verify:**
```bash
# Check IP reputation
whois 192.168.1.100
nslookup 192.168.1.100

# Look up Instagram's official mail servers
dig @8.8.8.8 instagram.com MX
```

---

### 7. **Suspicious Subject Line**

```
SUSPICIOUS SUBJECTS:
- "Verify Your Account [URGENT]"
- "Confirm Your Password"
- "Unusual Activity Detected"
- "Update Required NOW"
- "Your Account Will Be Disabled"

RED FLAGS:
- Artificial urgency ("URGENT", "NOW", "IMMEDIATELY")
- Threats ("will be disabled", "locked", "compromised")
- Requests for credentials or sensitive info
- Don't match legitimate provider's communication style

LEGITIMATE EXAMPLES:
- "You have a notification"
- "Weekly digest"
- "Password changed successfully"
- "Account settings updated"
```

---

### 8. **Unusual Reply-To Address**

```
SUSPICIOUS:
From: "Instagram Support" <noreply@instagram.com>
Reply-To: support@suspiciousdomain.com

RED FLAG:
- Reply-To is different from From address
- Replies will go to attacker's domain
- User clicks "Reply" → message goes to attacker

LEGITIMATE EXAMPLE:
From: "Instagram Support" <noreply@instagram.com>
Reply-To: <noreply@instagram.com>
- Consistent addresses
```

---

## ✅ Email Header Analysis Checklist

### Automated Checks

- [ ] **SPF Check**
  ```
  Status: ☐ PASS  ☐ FAIL  ☐ SOFTFAIL
  Result: PASS = Good, FAIL = Suspicious
  ```

- [ ] **DKIM Check**
  ```
  Status: ☐ PASS  ☐ FAIL  ☐ NEUTRAL
  Result: PASS = Good, FAIL = Very Suspicious
  ```

- [ ] **DMARC Check**
  ```
  Status: ☐ PASS  ☐ FAIL  ☐ NEUTRAL
  Result: PASS = Good, FAIL = Suspicious
  ```

### Manual Checks

- [ ] **Sender Verification**
  ```
  Display Name: ______________________
  Actual Email: ______________________
  ☐ Matches official domain (e.g., @instagram.com)
  ☐ No suspicious variations or typos
  ```

- [ ] **Subject Line Analysis**
  ```
  Subject: ______________________
  ☐ No artificial urgency ("URGENT", "NOW")
  ☐ No threats ("disabled", "locked")
  ☐ No credential requests
  ☐ Legitimate topic
  ```

- [ ] **Content Analysis**
  ```
  ☐ No requests for password
  ☐ No requests for credit card
  ☐ No requests for personal info
  ☐ No suspicious links or attachments
  ☐ Grammar/spelling correct
  ```

- [ ] **Link Verification**
  ```
  Hover over links. Do they go to:
  ☐ Official domain (instagram.com)?
  ☐ HTTPS (secure)?
  ☐ Direct URL (not shortened)?
  ☐ Expected destination?
  ```

- [ ] **Received Path**
  ```
  Originating Server: ______________________
  IP Address: ______________________
  ☐ Legitimate mail server
  ☐ Matches official provider
  ☐ Public IP address (not 192.168.x.x)
  ```

---

## 🔴 Red Flag Summary Table

| Header Element | Legitimate | PHISHING RED FLAG |
|---|---|---|
| **From Address** | @instagram.com | @instagram-verify.com, instagram.net |
| **SPF Check** | PASS | FAIL, SOFTFAIL |
| **DKIM Check** | PASS | FAIL |
| **DMARC Check** | PASS | FAIL |
| **Return-Path** | Matches From | Different domain |
| **Received Path** | Official servers | Attacker's IP |
| **Subject** | Normal | Urgent, threats |
| **Reply-To** | Matches From | Different domain |
| **Content** | No requests | Asks for password |
| **Links** | Official domains | Suspicious IPs, short URLs |

---

## 📊 Analysis Examples

### Example 1: Clear Phishing

```
From: "PayPal Security" <security@paypal-verify.com>    ← SUSPICIOUS DOMAIN
To: victim@company.com
Subject: Confirm Your Account [URGENT]                   ← ARTIFICIAL URGENCY

Authentication-Results: company.com;
        spf=fail ← RED FLAG
        dkim=fail ← RED FLAG
        dmarc=fail ← RED FLAG

Body: "Click here to verify your PayPal account"
      "Your account will be limited if you don't verify"

Verdict: PHISHING (Multiple red flags)
Action: DELETE, BLOCK SENDER, EDUCATE USER
```

### Example 2: Suspicious but Legitimate

```
From: "PayPal Notifications" <noreply@paypal.com>       ← LEGITIMATE DOMAIN

Authentication-Results: company.com;
        spf=pass ← GOOD
        dkim=pass ← GOOD
        dmarc=pass ← GOOD

Subject: Transaction Confirmation

Body: "Your payment of $99.99 has been processed"
      [No requests for credentials]

Verdict: LIKELY LEGITIMATE
Action: Monitor, but probably safe
```

### Example 3: Forwarded Legitimate Email (False Positive)

```
From: "Forwarded by John" <john@company.com>
Subject: FW: [Original] Instagram Notification

Original-From: noreply@instagram.com

Authentication-Results: company.com;
        spf=fail (because forwarded) ← FALSE POSITIVE
        dkim=fail (because forwarded) ← FALSE POSITIVE

Verdict: FALSE ALARM (Email was forwarded, not phishing)
Action: Review, educate user on email forwarding issues
```

---

## 🔧 Tools for Header Analysis

### Online Tools (WARNING: Privacy concerns)
```
✓ MXToolbox - https://mxtoolbox.com/
✓ EmailHeaders - https://emailheaders.com/
⚠ Be cautious uploading headers with sensitive data
```

### Command-Line Tools
```bash
# Check SPF record
dig example.com TXT
grep "v=spf1" 

# Check DKIM record
dig default._domainkey.example.com TXT

# Check DMARC record
dig _dmarc.example.com TXT

# Verify sender server
host -t MX example.com

# Check IP reputation
whois 192.168.1.100
```

### SIEM/Email Security Tools
```
✓ Proofpoint
✓ Mimecast
✓ Ironport/Cisco ESA
✓ Microsoft Defender
✓ Sophos
✓ Barracuda
```

---

## 📋 SOC Playbook: When You Find Phishing

### Step 1: Confirm Phishing (0-5 min)
- [ ] Check SPF/DKIM/DMARC (should all FAIL)
- [ ] Verify sender address is fake
- [ ] Confirm content requests credentials/money
- [ ] Cross-reference with threat intel feeds

### Step 2: Immediate Actions (5-15 min)
- [ ] Block sender email address
- [ ] Block domain in email gateway
- [ ] Add URL to blacklist (if applicable)
- [ ] Report to IT Security

### Step 3: Investigation (15-60 min)
- [ ] Search mailbox for similar emails
- [ ] Identify all users who received it
- [ ] Check who clicked the link (if tracking available)
- [ ] Check who downloaded attachment (if applicable)

### Step 4: Containment (1-4 hours)
- [ ] Delete email from all user inboxes
- [ ] Send email to all users warning about phishing
- [ ] Quarantine suspicious URLs/IPs
- [ ] Update email security rules

### Step 5: Response & Recovery (4 hours - 2 days)
- [ ] Reset passwords for compromised users
- [ ] Enable MFA for affected accounts
- [ ] Analyze access logs for lateral movement
- [ ] Notify executives if appropriate
- [ ] Document incident

### Step 6: Post-Incident (1 week)
- [ ] Post-mortem meeting
- [ ] Update training materials
- [ ] Adjust email filtering rules
- [ ] Report to management/board if needed

---

## 🎓 Training Tips

### For Users
```
"Before clicking any link in an email:
1. STOP - Don't panic
2. VERIFY sender email address (hover over it)
3. CHECK for SPF/DKIM in headers
4. TYPE official URL manually (don't use email link)
5. REPORT suspicious emails to security team"
```

### Key Teaching Points
```
✓ Display name can be forged (John@fake.com can say "John Smith")
✓ SPF/DKIM/DMARC are your friends - understand them
✓ Legitimate companies won't ask for passwords via email
✓ Urgency is a red flag
✓ When in doubt, ask security team
```

---

## 📊 Metrics to Track

```
Weekly:
- Phishing emails detected
- Phishing emails blocked
- Phishing emails reported by users
- User click rate on test phishing

Monthly:
- Phishing effectiveness trend
- False positive rate
- Response time to phishing detection
- User training completion
```

---

## 📚 References

- **DMARC:** https://dmarc.org/
- **SPF:** https://tools.ietf.org/html/rfc7208
- **DKIM:** https://tools.ietf.org/html/rfc6376
- **RFC 5322 (Email Headers):** https://tools.ietf.org/html/rfc5322
- **NIST Guide:** https://pages.nist.gov/

---

**Last Updated:** June 2024  
**Review Frequency:** Quarterly  
**Owner:** SOC/Security Team  

