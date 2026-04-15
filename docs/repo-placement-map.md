# Repo placement map

## Purpose

This document captures where work should land across the active SocioProphet, SociOS-Linux, and SourceOS-Linux organizations so that bootstrap glue, normative standards, workstation contracts, and runtime implementation do not collapse into a single repo.

## Placement rules

### 1. Bootstrap and verification glue
**Primary home:** `SocioProphet/sourceos-a2a-mcp-bootstrap`

Use this repository for:
- carrier verification helpers
- bootstrap `Makefile` targets
- `.mcp/servers.json` and UDS bootstrap glue
- minimal local verification plumbing
- CI checks for bootstrap correctness

Do **not** place broad architecture doctrine here. Keep this repo thin and operational.

### 2. Normative standards and cross-repo coordination
**Primary home:** `SocioProphet/socioprophet-agent-standards`
**Secondary home:** `SocioProphet/prophet-platform-standards`

Use these repositories for:
- repo placement decisions
- protocol alignment notes
- OpenClaw ↔ Prophet integration boundary documents
- normative policy/receipt/command semantics
- interoperability guidance across platform services

### 3. Local-first runtime implementation
**Primary home:** `SourceOS-Linux/openclaw`

Use this repository for:
- runtime/plugin implementation
- agent UX surfaces
- carrier emission hooks inside the local-first runtime
- membrane evaluation hooks inside the runtime
- connected-app enforcement inside the workstation agent shell

### 4. Workstation install, staging, rollback, and environment lanes
**Primary home:** `SociOS-Linux/workstation-contracts`
**Secondary home:** `SourceOS-Linux/sourceos-spec`

Use these repositories for:
- Asahi/Silverblue/Nix lanes
- install/update/rollback contracts
- shared volume semantics
- environment proofs and workstation conformance

## Active-org interpretation

### SocioProphet
Control plane, policy fabric, standards, platform, workspace semantics, and integration hubs.

### SociOS-Linux
Host/workstation/operator contracts and system lanes.

### SourceOS-Linux
Runtime/productized local-first implementation, especially `openclaw`.

## Practical consequence

When in doubt:
- put **standards** in a standards repo,
- put **runtime code** in the runtime repo,
- put **host/operator contracts** in the workstation repo,
- put **bootstrap verification** in the bootstrap repo.

This separation keeps the architecture legible and prevents policy, runtime, and workstation concerns from smearing together.
