# Lessons from the Instagram Phishing Lab

## What the Lab Proved
1. Cloning a login page takes under 60 seconds with SET
2. The fake page is visually identical to the real one
3. Credentials are captured in plaintext instantly
4. The victim is silently redirected after submission

## MITRE ATT&CK Mapping
| Technique | ID |
|---|---|
| Phishing | T1566 |
| Spearphishing Link | T1566.002 |
| Credential Access | T1056 |

## Key Defender Takeaways
- URL inspection is the #1 defence
- Password managers refuse to autofill on unrecognised domains
- MFA stops credential theft even when passwords are captured
