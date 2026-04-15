# OpenClaw ↔ Prophet integration boundary

## Thesis

OpenClaw is the **local-first agent runtime and interaction shell**.
Prophet is the **truth, policy, provenance, and workspace control plane**.

The local runtime must not become the source of truth for workspace state, and Prophet must not attempt to replace the local-first runtime shell.

## Responsibilities

### OpenClaw owns
- local-first agent runtime
- gateway protocol and local operator UX
- plugins, channels, memory, hooks, and workstation surfaces
- TUI/CLI/desktop interaction patterns
- local device posture and doctor checks

### Prophet owns
- canonical workspace and platform objects
- policy and membrane evaluation
- carrier/receipt production rules (PPS-aligned)
- append-only ledger and provenance semantics
- connected-app grants and capability decisions
- permission-aware projections and search surfaces

## Enforcement rule

OpenClaw may **propose** actions, gather context, and execute local-first workflows.
Any mutation of canonical workspace/platform state must pass through Prophet policy and produce a receipt/carrier.

## Narrow waist

The integration boundary should be implemented as a thin plugin/bridge layer that provides, at minimum:

1. `emit_carrier(...)`
2. `evaluate_membrane_decision(...)`
3. `append_ledger_event(...)`
4. `resolve_connected_app_grant(...)`

This layer must stay small. It is not a second runtime or a second policy engine.

## Immediate implementation guidance

### In `SourceOS-Linux/openclaw`
Implement:
- Prophet workspace/runtime plugin
- hooks for carrier emission on channel/tool actions
- hooks for membrane decisions before dangerous mutations
- display of receipts in user-facing surfaces

### In `SocioProphet/sourceos-a2a-mcp-bootstrap`
Keep:
- carrier verification helpers
- bootstrap verification and local plumbing
- CI checks proving protocol correctness

### In `SocioProphet/socioprophet-agent-standards`
Keep:
- normative placement guidance
- interoperability and protocol notes
- command/policy/receipt standards

## Why this split matters

This avoids three common failures:
1. rebuilding a second local-first shell inside Prophet
2. burying normative doctrine in bootstrap glue
3. letting the runtime mutate state without a provenance trail

The result is a cleaner system:
- OpenClaw = interaction plane
- Prophet = truth plane
- bootstrap = verification and glue
- workstation contracts = host/operator lane
