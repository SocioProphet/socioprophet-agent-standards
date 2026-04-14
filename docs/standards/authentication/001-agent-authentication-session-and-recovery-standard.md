# 001 - Agent Authentication, Session, and Recovery Standard

| Metadata | Value |
| --- | --- |
| Standard ID | 001 |
| Status | Draft normative profile |
| Repository role | Canonical authentication and session standard for the SocioProphet agent plane |
| Applies to | Browser applications, native/mobile clients, enterprise federation, admin surfaces, service/workload identity, recovery flows |
| Primary implementation targets | `SocioProphet/prophet-platform`, `SocioProphet/sociosphere`, `SocioProphet/socioprophet`, `SocioProphet/socioprophet-docs` |
| Last updated | 2026-04-14 |

## 1. Purpose

This standard defines the canonical authentication and session model for SocioProphet agent systems.

The central decision is that authentication is **not** a single login screen. It is a control plane spanning:

1. identity discovery and routing
2. primary proof of possession / user verification
3. step-up decisioning
4. first-party session issuance
5. token brokerage for downstream resources
6. recovery and break-glass controls
7. post-login authorization and continuous policy enforcement

This standard exists to prevent the common failure mode in which products assemble authentication from disconnected features such as passwords, MFA prompts, biometrics, and SSO without defining who owns trust, where session state lives, how tokens move, and how recovery avoids becoming the weakest lane.

## 2. Normative posture

The following principles are normative.

1. **Passkey-first for first-party human authentication.**
   - First-party human authentication MUST prefer passkeys / WebAuthn.
   - Platform biometrics MAY be used only as a local authenticator-unlock mechanism; they MUST NOT be treated as a server-verified biometric factor.

2. **External proof, internal session.**
   - Upstream identity providers MAY authenticate the subject.
   - SocioProphet systems MUST issue their own first-party session and policy context after successful external proof.

3. **Browser apps MUST default to BFF.**
   - Browser-facing applications SHOULD use a backend-for-frontend pattern.
   - Browser JavaScript SHOULD NOT hold long-lived refresh tokens.
   - Session continuity for browser clients SHOULD be provided by first-party cookies backed by server-side session state.

4. **Native/mobile apps MUST use authorization code + PKCE.**
   - Native applications MUST use the system browser or equivalent external user-agent.
   - Embedded webview authentication SHOULD NOT be the default lane.

5. **OIDC-first federation.**
   - Enterprise federation SHOULD prefer OpenID Connect.
   - SAML MAY be supported as a compatibility lane where customer requirements force it.

6. **Recovery parity.**
   - Recovery MUST NOT be materially weaker than the primary authentication lane.
   - Help-desk or support-mediated recovery MUST be auditable and rate-limited.

7. **Privileged lanes require phishing-resistant controls.**
   - Admin, operator, and break-glass lanes MUST use phishing-resistant authentication.
   - SMS-only MFA MUST NOT be accepted for privileged lanes.

8. **Authentication and authorization are separate controls.**
   - Successful authentication MUST NOT imply broad authorization.
   - Sensitive actions MUST still pass authorization and, where applicable, step-up checks.

## 3. Trust boundaries

Implementations MUST explicitly model at least the following trust boundaries:

- **User device / authenticator boundary**
- **Browser runtime boundary**
- **Native application / system browser boundary**
- **SocioProphet authentication service boundary**
- **Enterprise IdP boundary**
- **Downstream resource server boundary**
- **Operator / admin console boundary**
- **Recovery and support boundary**

Authentication design documents and implementations MUST name which component is trusted to perform each of the following actions:

- user identity proofing
- possession proof verification
- user-verification assertion validation
- risk scoring and step-up decisions
- session issuance
- token minting, exchange, rotation, and revocation
- logout propagation
- recovery approval
- evidence emission

## 4. Canonical architecture

The canonical architecture is:

```text
[User / Device / Authenticator]
           |
           v
[Identity discovery + routing]
           |
           +--> [Enterprise OIDC / SAML IdP] --proof--> 
           |
           +--> [First-party passkey verification] -----+
                                                        v
                                        [SocioProphet authentication service]
                                                        |
                          +-----------------------------+----------------------------+
                          |                                                          |
                          v                                                          v
              [First-party browser session]                          [Token brokerage for native / APIs / workloads]
                          |
                          v
               [Authorization + policy engine]
                          |
                          v
                 [Protected product surfaces]
```

The browser path and the native path intentionally differ at the session layer.

- Browser: first-party cookie session, backed by server-side session state
- Native: OAuth-style token lane with PKCE, keystore-backed persistence, and stricter token controls

## 5. Subject classes

Implementations MUST distinguish at least the following subject classes:

- **Human first-party user**
- **Human federated enterprise user**
- **Privileged/admin operator**
- **Service/workload identity**
- **Recovery or break-glass identity**

Each subject class MUST have an explicit authentication lane. Implementations MUST NOT silently collapse all classes into one generic login model.

## 6. Canonical browser flow

The canonical browser flow is normative.

### 6.1 Discovery and routing

1. User enters identifier or selects account context.
2. System determines whether the account is:
   - first-party local account
   - passkey-only account
   - enterprise-federated account
   - admin / privileged account
3. The routing decision MUST occur before token issuance.

### 6.2 Primary proof

For first-party users:

1. The system SHOULD prompt for passkey / WebAuthn first.
2. User verification occurs on the device through the authenticator.
3. Server verifies the assertion against the registered credential material.

For enterprise-federated users:

1. The system redirects to the configured OIDC provider.
2. SAML MAY be used only when required by tenant configuration.
3. The returned identity claims MUST be mapped into an internal SocioProphet subject and tenant context.

### 6.3 Step-up

Step-up MUST be policy-driven, not cosmetically bolted on.

The system MUST support step-up on at least:

- new device + new location
- privilege elevation
- administrative action
- destructive operation
- payment / signature equivalent event
- abnormal session behavior
- recovery completion

Step-up SHOULD prefer a second phishing-resistant proof where available.

### 6.4 First-party session issuance

After successful proof:

1. The backend MUST create a new first-party session record.
2. The browser MUST receive an opaque session identifier via cookie.
3. Browser cookies MUST be configured with:
   - `HttpOnly`
   - `Secure`
   - an explicit `SameSite` policy
4. Session identifiers MUST be rotated on:
   - initial authentication
   - privilege change
   - recovery completion
   - significant re-authentication or step-up transitions

Browser JavaScript SHOULD NOT directly receive a long-lived refresh token for first-party application access.

## 7. Canonical native/mobile flow

Native and mobile clients MUST use an external user-agent and authorization code + PKCE.

Normative requirements:

1. Native apps MUST use the system browser or equivalent trusted external user-agent.
2. Authorization code + PKCE MUST be used.
3. Tokens MUST be stored in platform keystores or equivalent protected storage.
4. Refresh tokens, if issued, MUST be rotated or otherwise constrained according to the applicable security profile.
5. The application MUST support server-side revocation and local wipe on logout or compromise.

Passkeys SHOULD remain the preferred end-user proof where the platform and user experience permit it.

## 8. Enterprise federation profile

Enterprise federation MUST follow the "external proof, internal session" model.

Requirements:

1. OIDC SHOULD be the default federation profile.
2. SAML MAY be supported for compatibility.
3. Upstream claims MUST be normalized into:
   - internal subject ID
   - tenant ID
   - upstream assurance context
   - role / group claims
   - session policy context
4. Federation MUST NOT bypass first-party session policy, authorization checks, or audit controls.
5. Logout propagation SHOULD be supported where enterprise deployment requires it.

## 9. Admin and privileged-access profile

Admin and privileged lanes require stricter controls.

Requirements:

1. Privileged lanes MUST use phishing-resistant authentication.
2. Password-only and SMS-only flows MUST NOT be sufficient for admin access.
3. Admin sessions SHOULD have shorter idle and absolute lifetime bounds than standard user sessions.
4. Re-authentication MUST be required for:
   - role change
   - credential reset
   - configuration mutation
   - policy changes
   - key or secret access
   - support override / impersonation
5. Every privileged authentication event MUST emit a durable audit trail.

## 10. Service and workload identity

Service and workload identity MUST be distinct from human identity.

Requirements:

1. Services MUST authenticate with workload identity, mTLS, signed assertions, or equivalent machine credentials.
2. Human credentials MUST NOT be reused as service credentials.
3. Service identities MUST be scoped to workload, environment, and tenant context where appropriate.
4. Long-lived static secrets SHOULD be minimized.
5. Rotation and revocation paths MUST be defined.

## 11. Token and session rules

Implementations MUST distinguish among:

- **authentication proof**
- **first-party session**
- **downstream access token**
- **refresh token**
- **authorization decision context**

### 11.1 Browser sessions

Browser applications SHOULD use opaque first-party session identifiers.

The session record MUST at minimum contain:

- session ID
- subject ID
- tenant ID
- assurance context
- authenticator type(s)
- issued-at / last-seen / expiry timestamps
- privilege level
- device / client fingerprint summary
- risk state
- step-up state
- revocation status

### 11.2 Access tokens

Access tokens MUST be:

- short-lived
- audience scoped
- privilege scoped
- revocable through server-side policy and lifecycle controls

### 11.3 Refresh tokens

Refresh tokens, where used, MUST be carefully restricted.

- Browser JavaScript SHOULD NOT be the default storage location.
- Public clients SHOULD use rotation or sender-constrained patterns.
- Implementations MUST define replay handling.

## 12. Recovery and break-glass standard

Recovery is a first-class authentication lane.

Requirements:

1. Recovery MUST NOT be weaker than the primary authentication path.
2. Accounts SHOULD enroll at least two recovery methods.
3. Preferred recovery factors are:
   - additional passkey
   - hardware security key
   - one-time recovery codes
   - strongly controlled support-mediated recovery
4. Security questions MUST NOT be treated as a sufficient primary recovery method.
5. Recovery codes MUST be:
   - high-entropy
   - one-time use
   - revocable / regenerable
   - explicitly audited on use
6. Password reset MUST NOT silently bypass MFA or passkey enrollment requirements.
7. Support-mediated recovery MUST include:
   - dual control or equivalent approval policy for high-value accounts
   - durable evidence
   - rate limits
   - user notification

Break-glass lanes MUST be rare, explicit, separately logged, and time-bound.

## 13. Authorization separation

Authentication success only establishes subject identity and assurance context.

Authorization MUST remain a distinct control plane.

Requirements:

1. Every sensitive request MUST pass authorization.
2. Authorization MUST support at least:
   - role-based control
   - attribute / context-based control
   - tenant boundary enforcement
3. Step-up MAY be required even after successful authentication if the action is sensitive.
4. Impersonation / delegated support actions MUST be explicit and auditable.

## 14. Evidence and audit events

Implementations MUST emit durable events for the authentication lifecycle.

The following event families MUST exist or be mappable from implementation-specific names:

- `authn.discovery.started`
- `authn.route.selected`
- `authn.challenge.started`
- `authn.proof.verified`
- `authn.proof.failed`
- `authn.stepup.required`
- `authn.stepup.completed`
- `session.issued`
- `session.rotated`
- `session.revoked`
- `session.terminated`
- `token.issued`
- `token.rotated`
- `token.revoked`
- `recovery.initiated`
- `recovery.factor.used`
- `recovery.completed`
- `admin.authn.completed`
- `admin.breakglass.used`
- `workload.identity.issued`
- `workload.identity.revoked`

Each event SHOULD include, subject to privacy and security policy:

- event ID
- timestamp
- subject class
- subject ID or stable surrogate ID
- tenant ID
- relying party / client ID
- authenticator category
- assurance context
- network / device summary
- risk state
- step-up state
- operator ID where applicable
- correlation / trace ID

## 15. Data model primitives

Implementations SHOULD define the following canonical records.

### 15.1 Subject
- `subject_id`
- `subject_class`
- `tenant_id`
- `status`

### 15.2 Credential
- `credential_id`
- `subject_id`
- `credential_type`
- `issuer`
- `created_at`
- `last_used_at`
- `revoked_at`

### 15.3 Session
- `session_id`
- `subject_id`
- `tenant_id`
- `issued_at`
- `expires_at`
- `last_seen_at`
- `assurance_level`
- `stepup_state`
- `risk_state`
- `revoked`

### 15.4 Recovery factor
- `recovery_factor_id`
- `subject_id`
- `factor_type`
- `enrolled_at`
- `revoked_at`
- `last_used_at`

### 15.5 Authorization handle
- `authz_context_id`
- `subject_id`
- `tenant_id`
- `roles`
- `attributes`
- `constraints`

## 16. Conformance requirements

An implementation MAY claim conformance only if all of the following are true.

### 16.1 Minimum conformance

- passkey-first or explicitly documented equivalent phishing-resistant path exists for first-party users
- browser lane uses first-party session cookies or a documented alternative with equal or better security posture
- native lane uses authorization code + PKCE
- enterprise lane issues internal session context after external proof
- recovery lane is documented and not weaker than the primary lane
- admin lane prohibits weak fallback paths
- audit events are emitted for authentication, session, token, recovery, and privileged actions

### 16.2 Strong conformance

Strong conformance additionally requires:

- phishing-resistant admin lane
- step-up policy engine
- session rotation on privilege and assurance changes
- recovery dual control for privileged accounts
- workload/service identity separated from human identity
- documented revocation and logout propagation behavior

## 17. Implementation guidance

The following implementation guidance is non-exhaustive but strongly recommended.

1. Prefer passkeys over password-first UX.
2. Keep browser token handling off the front end where possible.
3. Separate authentication service from authorization service, even if co-deployed.
4. Ensure the recovery flow receives the same design scrutiny as primary login.
5. Force explicit subject-class handling in the identity model.
6. Avoid making behavioral signals a hidden primary authenticator.
7. Treat biometrics as local unlock of cryptographic credentials, not as server-held identity secrets.

## 18. Anti-patterns

The following are prohibited or strongly discouraged.

- storing long-lived bearer tokens in browser-accessible local storage as the default browser pattern
- treating a password reset as sufficient proof for privileged recovery without additional controls
- using security questions as the primary recovery mechanism
- reusing human credentials for service identity
- silently collapsing enterprise proof into broad authorization without internal policy evaluation
- accepting SMS-only MFA for privileged lanes
- assuming federation removes the need for first-party session and audit controls

## 19. Acceptance gates

Before an implementation is treated as production-ready, the following gates MUST be passed:

1. **Flow clarity gate**
   - browser, native, enterprise, admin, workload, and recovery flows are documented end-to-end

2. **Boundary gate**
   - session and token boundaries are explicit

3. **Recovery gate**
   - recovery has stronger-than-demo operational controls and auditability

4. **Privilege gate**
   - admin access uses phishing-resistant controls and explicit re-authentication

5. **Evidence gate**
   - required audit events are emitted and queryable

6. **Conformance gate**
   - deviations from this standard are declared and justified

## 20. Cross-repository consumption

Implementation repositories that consume this standard SHOULD add a "Complies with Standards" section to their README and SHOULD link to this document.

Expected consumers include:

- authentication service implementations
- browser BFF layers
- native authorization modules
- admin consoles
- support and recovery tooling
- workload identity issuers
- policy and authorization services

## 21. Summary

The canonical SocioProphet posture is:

- passkey-first
- OIDC-first federation
- BFF for browsers
- PKCE for native apps
- phishing-resistant privileged access
- recovery parity
- external proof, internal session
- explicit separation of authentication and authorization

Any implementation that cannot say where the session lives, where refresh capability lives, how recovery works, and how privileged access is constrained does not yet satisfy this standard.
