# SocioProphet Agent Standards — Normative Profiles and Control Surfaces

This directory is the normative standards surface for the **SocioProphet agent plane**.

We use this repository to define standards that govern how agents authenticate, establish trust, exchange claims, issue and rotate sessions, enforce step-up policy, recover access, emit evidence, and interoperate across SourceOS, AgentOS, SocioSphere, Prophet Platform, and adjacent services.

## Directory map

- `authentication/` — authentication, session, step-up, token, and recovery standards

## Standard writing posture

All standards in this repository are expected to:

- use **MUST / SHOULD / MAY** language for normative requirements
- separate **authentication** from **authorization**
- define explicit **trust boundaries**
- define explicit **session and token boundaries**
- define explicit **recovery and break-glass policy**
- define required **evidence and audit events**
- include **conformance criteria** and implementation targets

## Current standards

- `authentication/001-agent-authentication-session-and-recovery-standard.md` — canonical authentication, session, step-up, token, and recovery profile for browser, native, enterprise, admin, and service lanes

## Repository role

This repository is the **standards authority** for agent-plane trust posture. Implementation repositories MUST link back to the standards they implement and MUST declare any deviations, extensions, or experimental profiles.

## Initial implementation targets

The following repositories are expected to consume standards from this repo as implementation surfaces evolve:

- `SocioProphet/prophet-platform`
- `SocioProphet/sociosphere`
- `SocioProphet/socioprophet`
- `SocioProphet/socioprophet-docs`

## Status

- Initial scaffold created: 2026-04-14
- Initial authentication standard added: 2026-04-14
