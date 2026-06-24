# Playbook: Credential Compromise

## Immediate (0-30 mins)
- [ ] Force password reset
- [ ] Revoke all active sessions
- [ ] Check for MFA bypass attempts

## Investigate (30 mins - 2 hrs)
- [ ] Review login history
- [ ] Check for email forwarding rules added by attacker
- [ ] Review files accessed

## Remediate
- [ ] Re-enable account after MFA enrolled
- [ ] Remove malicious inbox rules
- [ ] Notify management if sensitive data accessed
