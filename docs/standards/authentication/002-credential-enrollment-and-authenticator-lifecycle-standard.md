# 002 - Credential Enrollment and Authenticator Lifecycle Standard

| Metadata | Value |
| --- | --- |
| Standard ID | 002 |
| Status | Draft normative profile |
| Depends on | `001-agent-authentication-session-and-recovery-standard.md` |
| Applies to | Passkeys / WebAuthn credentials, phishing-resistant authenticators, fallback local credentials, recovery factor enrollment |
| Last updated | 2026-04-14 |

## 1. Purpose

This standard defines how credentials and authenticators are enrolled, bound to subjects, rotated, revoked, replaced, and retired across the SocioProphet agent plane.

Authentication architecture fails in practice when strong runtime flows are paired with weak or inconsistent enrollment and lifecycle management. The goal here is to ensure that credential creation, replacement, and loss-handling are at least as disciplined as the primary authentication flow.

## 2. Normative posture

1. **Passkey-first enrollment.**
   - First-party human accounts MUST support passkey / WebAuthn enrollment.
   - Enrollment UX SHOULD prefer passkeys over password-first creation.

2. **At least two independent recovery-capable paths.**
   - Human accounts SHOULD enroll at least two independent recovery-capable factors or recovery paths.
   - Privileged accounts MUST have at least two independent recovery-capable paths.

3. **Credential lifecycle is explicit.**
   - Every credential MUST have lifecycle states.
   - Credentials MUST NOT be treated as eternal once created.

4. **Replacement is not silent.**
   - Replacing or adding authenticators MUST be auditable.
   - Replacement SHOULD trigger user notification.

5. **Recovery is not enrollment bypass.**
   - Recovery workflows MUST NOT silently create a new durable primary authenticator without additional controls.

## 3. Credential classes

Implementations MUST distinguish at least the following classes.

- **Primary phishing-resistant authenticator**
  - passkey / WebAuthn platform or roaming authenticator
- **Secondary phishing-resistant authenticator**
  - second passkey or hardware security key
- **Fallback authenticator**
  - password or equivalent local secret, where retained
- **Recovery factor**
  - one-time recovery codes or tightly controlled recovery mechanism
- **Federated external proof handle**
  - enterprise IdP binding metadata; not itself a first-party authenticator secret

## 4. Lifecycle states

A credential record MUST support explicit lifecycle states.

Minimum required states:

- `pending_enrollment`
- `active`
- `suspended`
- `revoked`
- `replaced`
- `expired` (if time-bound)
- `retired`

A subject SHOULD also have derived summaries such as:

- has_primary_phishing_resistant_authenticator
- has_secondary_recovery_capable_authenticator
- has_fallback_authenticator
- recovery_readiness_state

## 5. Enrollment requirements

### 5.1 Enrollment preconditions

Before enrollment of a durable authenticator, the system MUST know:

- subject identifier
- tenant context
- subject class
- current assurance context for the enrollment session
- whether enrollment is initial, additive, replacement, or recovery-driven

### 5.2 Initial first-party enrollment

The preferred initial sequence is:

1. create subject record
2. verify bootstrap contact or approved proof channel
3. enroll first passkey / WebAuthn credential
4. encourage or require second authenticator or recovery factor
5. issue first-party session
6. emit enrollment evidence

For privileged subjects, step 4 MUST be required before the account is considered production-ready.

### 5.3 Additive enrollment

Adding an additional authenticator to an existing account MUST require:

- an active authenticated session at sufficient assurance, and
- re-authentication or step-up for privileged accounts, or
- equivalent policy-approved controls

### 5.4 Replacement enrollment

Replacement enrollment is higher risk than additive enrollment.

Replacing the last remaining primary authenticator MUST require:

- step-up or equivalent strong proof, or
- recovery workflow completion with explicit approval policy

## 6. Passkey / WebAuthn enrollment profile

Implementations SHOULD treat passkeys as the canonical first-party credential.

Requirements:

1. The server MUST bind credentials to the correct relying-party context.
2. The server MUST store only the public credential material and required metadata.
3. Platform biometrics MUST remain local to the authenticator and MUST NOT be uploaded or treated as server-held biometric evidence.
4. The system SHOULD capture metadata sufficient to distinguish:
   - platform authenticator vs roaming authenticator
   - creation timestamp
   - last-used timestamp
   - credential nickname or user-facing label
5. Where attestation is collected, the privacy and policy implications MUST be documented.
6. The user SHOULD be able to name or label enrolled authenticators for later management.

## 7. Password fallback profile

Where passwords remain supported, they are a fallback lane.

Requirements:

1. Password storage MUST follow the password storage standard in the relevant implementation profile.
2. Password enrollment or reset MUST NOT silently downgrade the account’s security posture.
3. Privileged accounts SHOULD NOT rely on password-only enrollment.
4. Accounts with a password fallback SHOULD still be encouraged to enroll passkeys.

## 8. Recovery factor enrollment

Recovery factors MUST be treated as credentials with their own lifecycle.

Requirements:

1. Recovery codes MUST be generated with high entropy.
2. Recovery codes MUST be one-time use.
3. Recovery factor enrollment MUST be auditable.
4. Recovery factors SHOULD be revocable and regenerable.
5. Recovery factors SHOULD NOT be the only enrolled recovery path for privileged subjects.

## 9. Revocation, suspension, and retirement

### 9.1 User-driven revocation

Users SHOULD be able to revoke lost or retired authenticators from an authenticated session, subject to policy.

### 9.2 Administrator-driven revocation

Administrators MAY revoke credentials under approved operational controls. Such actions MUST be audited and SHOULD trigger user notification.

### 9.3 Automatic suspension

The system MAY suspend a credential on risk signals such as:

- confirmed device loss
- detected compromise
- impossible travel + elevated privilege
- repeated abuse linked to one authenticator

### 9.4 Retirement

A retired credential MUST NOT remain usable for authentication. Retirement MUST be durable in the backing store and visible in audit history.

## 10. Loss, theft, and replacement handling

Implementations MUST define explicit handling for:

- lost device with passkey
- stolen roaming security key
- lost secondary factor
- recovery-code exhaustion
- enterprise account transfer or separation

The workflow MUST distinguish:

- loss of one authenticator while another strong authenticator remains
- loss of all strong authenticators
- loss affecting a privileged account

These are materially different risk cases and MUST NOT share the same simplistic recovery action.

## 11. Evidence and audit events

At minimum, implementations MUST emit events for:

- `credential.enrollment.started`
- `credential.enrollment.completed`
- `credential.enrollment.failed`
- `credential.added`
- `credential.replaced`
- `credential.revoked`
- `credential.suspended`
- `credential.retired`
- `recovery_factor.enrolled`
- `recovery_factor.regenerated`
- `recovery_factor.revoked`

Each event SHOULD include:

- credential ID
- subject ID
- subject class
- tenant ID
- credential class
- enrollment mode (initial / additive / replacement / recovery-driven)
- operator ID where applicable
- assurance context
- correlation / trace ID

## 12. Data model primitives

### 12.1 Credential record
- `credential_id`
- `subject_id`
- `tenant_id`
- `credential_class`
- `credential_type`
- `lifecycle_state`
- `display_name`
- `created_at`
- `activated_at`
- `last_used_at`
- `revoked_at`
- `replaced_by_credential_id`
- `issuer_context`
- `metadata`

### 12.2 Enrollment record
- `enrollment_id`
- `subject_id`
- `credential_id`
- `enrollment_mode`
- `session_id`
- `assurance_context`
- `started_at`
- `completed_at`
- `result`

## 13. Conformance requirements

An implementation MAY claim conformance only if:

- credential classes are explicitly modeled
- lifecycle states are explicit
- passkey enrollment is supported or a justified equivalent is documented
- additive and replacement enrollment are distinguished
- revocation and retirement are supported
- recovery-factor enrollment is auditable
- privileged-account enrollment policy is stronger than standard account policy

## 14. Anti-patterns

The following are prohibited or strongly discouraged.

- creating a durable new primary authenticator without auditable proof of control
- treating biometric unlock as a server-visible biometric credential
- failing to distinguish additive from replacement enrollment
- allowing the final remaining privileged authenticator to be replaced without strong controls
- leaving lost or retired authenticators active indefinitely
- treating recovery factors as an untracked side channel

## 15. Summary

Credential strength at login is meaningless if credential creation, replacement, and retirement are weak. SocioProphet systems MUST treat authenticator lifecycle as a first-class control surface, with passkey-first enrollment, explicit lifecycle states, strong replacement controls, and durable evidence throughout.
