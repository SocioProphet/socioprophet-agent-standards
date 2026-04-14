# Authentication Standards

This directory contains the normative authentication and session-management profile for the SocioProphet agent plane.

## Scope

These standards govern:

- end-user authentication
- enterprise federation
- browser session issuance
- native/mobile authorization flows
- step-up authentication and risk policy
- recovery and break-glass controls
- admin and privileged-access controls
- service and workload identity boundaries
- evidence, telemetry, and conformance requirements

## Design posture

The default posture for SocioProphet agent systems is:

- **passkey-first** for first-party human authentication
- **OIDC-first** for workforce / enterprise federation, with SAML compatibility only where needed
- **backend-for-frontend (BFF)** for browser applications
- **authorization code + PKCE** for native applications
- **phishing-resistant only** for admin and privileged lanes
- **recovery parity**: recovery MUST NOT be materially weaker than the primary login path
- **external proof, internal session**: upstream federation is accepted as proof, but SocioProphet issues its own first-party session and policy context

## Current standards

- `001-agent-authentication-session-and-recovery-standard.md`
  - canonical flow and normative requirements for browser, native, enterprise, admin, and service identity lanes
  - token and session rules
  - recovery rules
  - evidence model and conformance profile
