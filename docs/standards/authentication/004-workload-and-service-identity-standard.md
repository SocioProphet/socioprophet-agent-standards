# 004 - Workload and Service Identity Standard

| Metadata | Value |
| --- | --- |
| Standard ID | 004 |
| Status | Draft normative profile |
| Depends on | `001-agent-authentication-session-and-recovery-standard.md` |
| Applies to | Services, agents, workloads, control-plane components, background jobs, automation, token exchange, machine credentials |
| Last updated | 2026-04-14 |

## 1. Purpose

This standard defines how non-human actors authenticate within the SocioProphet agent plane.

Service and workload identity MUST be treated as a separate trust domain from human identity. The primary objective is to prevent systems from reusing human credentials, long-lived static secrets, or product-layer shortcuts to authenticate automation, jobs, agents, and control-plane components.

## 2. Normative posture

1. **Machine identity is distinct from human identity.**
   - Workloads MUST authenticate with machine credentials, not human passwords or reused operator sessions.

2. **Short-lived credentials preferred.**
   - Implementations SHOULD prefer short-lived machine credentials over long-lived static secrets.

3. **Bounded scope.**
   - A workload identity MUST be scoped to at least workload/service, environment, and policy context.

4. **Explicit issuance and revocation.**
   - Machine credentials MUST have defined issuance, rotation, and revocation paths.

5. **No hidden privilege inheritance.**
   - A workload MUST NOT silently inherit broad operator privileges merely because it was deployed by a privileged actor.

## 3. Subject classes

Implementations MUST distinguish among at least:

- **service identity**
- **batch job identity**
- **agent identity**
- **control-plane component identity**
- **break-glass machine identity**

These classes MAY share infrastructure but MUST remain distinguishable in policy and audit records.

## 4. Trust boundaries

Machine identity flows MUST model at least:

- workload runtime boundary
- secret or credential delivery boundary
- control-plane issuer boundary
- target resource boundary
- tenant or environment isolation boundary

Designs MUST document which component is trusted to:

- issue workload credentials
- exchange upstream proof for internal tokens
- rotate credentials
- revoke credentials
- attest or label runtime context
- emit evidence

## 5. Allowed authentication mechanisms

Workloads MAY authenticate through one or more of the following approved classes, subject to deployment profile:

- mTLS / mutual authentication
- signed assertions or workload-bound JWT/SVID-style proofs
- short-lived service tokens minted by an internal issuer
- token exchange based on higher-level workload proof
- environment-bound machine identities provided by infrastructure

Long-lived shared secrets SHOULD be minimized and MUST be treated as a constrained compatibility lane, not the preferred default.

## 6. Issuance model

A workload credential issuance event MUST bind the credential to sufficient context.

The issued identity SHOULD include:

- `workload_identity_id`
- workload or service name
- environment / cluster / namespace context
- tenant context where applicable
- issuer context
- issued-at and expiry timestamps
- allowed audiences
- allowed scopes / capabilities
- rotation metadata

Issuance MUST be auditable.

## 7. Rotation and expiry

Workload credentials MUST NOT be assumed permanent.

Requirements:

1. Every machine credential MUST have an expiry or revocation model.
2. Rotation procedures MUST be documented.
3. Implementations SHOULD support overlap windows for safe rotation.
4. Credential reuse outside allowed lifetime MUST be detectable.
5. Emergency revocation MUST be supported.

## 8. Token exchange and downstream access

Some workloads will need downstream access tokens for APIs or resources.

Requirements:

1. Token exchange MUST preserve caller identity context.
2. Downstream access tokens MUST be audience scoped.
3. Access tokens SHOULD be short-lived.
4. Workload-issued tokens MUST be revocable through server-side policy.
5. A workload MUST NOT receive broader downstream scope than its declared policy permits.

## 9. Policy and authorization context

Authentication alone is insufficient for workload access.

Requirements:

1. Every machine-authenticated request MUST still pass authorization.
2. Authorization SHOULD evaluate:
   - workload identity class
   - environment / namespace / tenant context
   - target resource audience
   - declared capability or action class
   - runtime risk signals where available
3. High-risk actions SHOULD require approval or additional policy gates even for authenticated workloads.

## 10. Secret handling and delivery

Where secrets or bootstrap material are unavoidable, their handling MUST be constrained.

Requirements:

1. Secret delivery paths MUST be documented.
2. Secrets SHOULD be environment- or workload-scoped.
3. Static secrets SHOULD be minimized.
4. Secret reads and updates SHOULD be auditable.
5. Break-glass machine secrets MUST be explicitly labeled and separately governed.

## 11. Multi-tenancy and isolation

Machine identities in multi-tenant systems require explicit tenant controls.

Requirements:

1. A workload identity MUST carry tenant context where it operates on tenant data or tenant-scoped resources.
2. Cross-tenant operations MUST be explicitly authorized.
3. Shared control-plane components MUST still preserve tenant isolation in token issuance and policy enforcement.
4. A machine identity MUST NOT be treated as globally trusted unless such scope is explicitly justified and documented.

## 12. Evidence and audit events

Implementations MUST emit events for at least:

- `workload.identity.requested`
- `workload.identity.issued`
- `workload.identity.rotated`
- `workload.identity.revoked`
- `workload.identity.exchange.started`
- `workload.identity.exchange.completed`
- `workload.identity.exchange.failed`
- `workload.authz.denied`
- `workload.authz.approved`
- `workload.breakglass.used`

Each event SHOULD include:

- workload identity ID
- workload/service name
- tenant ID where applicable
- environment / runtime summary
- issuer ID
- target audience
- capability or scope summary
- operator ID where applicable
- correlation / trace ID

## 13. Data model primitives

### 13.1 Workload identity
- `workload_identity_id`
- `subject_class`
- `service_name`
- `environment`
- `tenant_id` (nullable only if truly non-tenant)
- `issuer_id`
- `state`
- `created_at`
- `last_seen_at`
- `revoked_at`

### 13.2 Machine credential
- `credential_id`
- `workload_identity_id`
- `credential_type`
- `issued_at`
- `expires_at`
- `audiences`
- `scopes`
- `rotation_state`

### 13.3 Token exchange record
- `exchange_id`
- `workload_identity_id`
- `source_proof_type`
- `target_audience`
- `issued_token_id`
- `started_at`
- `completed_at`
- `result`

## 14. Conformance requirements

An implementation MAY claim conformance only if:

- machine identity is distinct from human identity
- machine credential issuance is explicit and auditable
- rotation and revocation paths are documented
- downstream tokens are audience scoped
- authorization remains separate from authentication
- tenant isolation rules are documented for machine identities
- break-glass machine identity handling is documented where applicable

## 15. Anti-patterns

The following are prohibited or strongly discouraged.

- reusing human passwords or browser sessions for workloads
- issuing effectively permanent machine credentials without a revocation model
- silently inheriting broad operator privilege into automation
- minting downstream tokens without audience constraints
- using one undifferentiated shared secret across many services
- collapsing tenant-scoped and global machine identities into one uncontrolled category

## 16. Summary

Workload and service identity is a first-class authentication domain. SocioProphet systems MUST issue, scope, rotate, authorize, and audit machine identity separately from human identity, with explicit context binding, downstream audience control, and tenant-aware policy enforcement.
