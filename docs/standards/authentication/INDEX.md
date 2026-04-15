# Authentication Standards Index

This file catalogs the authentication standards currently present in this repository.

## Current standards

### 001 — Agent Authentication, Session, and Recovery

`001-agent-authentication-session-and-recovery-standard.md`

Defines the canonical authentication posture for the SocioProphet agent plane across browser, native/mobile, enterprise federation, privileged access, workload identity, and recovery lanes.

### 002 — Credential Enrollment and Authenticator Lifecycle

`002-credential-enrollment-and-authenticator-lifecycle-standard.md`

Defines how passkeys and related authenticators are enrolled, added, replaced, revoked, suspended, and retired, including recovery-factor lifecycle and privileged-account enrollment posture.

### 003 — Enterprise Federation and Claim Mapping

`003-enterprise-federation-and-claim-mapping-standard.md`

Defines OIDC-first enterprise federation, SAML compatibility, deterministic tenant routing, claim normalization, account linking, JIT provisioning constraints, and first-party session issuance after external proof.

### 004 — Workload and Service Identity

`004-workload-and-service-identity-standard.md`

Defines non-human identity for services, agents, jobs, and control-plane components, including machine credential issuance, rotation, token exchange, tenant isolation, and workload-specific audit/evidence requirements.

## Reading order

1. Read `001` first for the umbrella posture.
2. Read `002` for human credential lifecycle.
3. Read `003` for enterprise identity ingress and mapping.
4. Read `004` for machine/workload identity.

## Intended consuming repositories

- `SocioProphet/prophet-platform`
- `SocioProphet/sociosphere`
- `SocioProphet/socioprophet`
- `SocioProphet/socioprophet-docs`

Implementation repositories SHOULD link to the specific standards they implement and document any deviations or extensions.
