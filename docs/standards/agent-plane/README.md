# Agent-plane standards

This directory contains runtime-facing agent standards.

These standards sit between ontology-source semantics and runtime implementation. They consume semantic authority from `SocioProphet/ontogenesis`, but define the concrete conformance expectations that agent runtimes and platform services must satisfy.

## Current standards

- `001-agent-action-trace-conformance-profile.md` — Action Ontology consumption profile for runtime agents, traces, receipts, policy references, and conformance evidence.

## Boundary

This directory does not own the Action Ontology source module. That remains in `SocioProphet/ontogenesis`.

This directory does not own bootstrap examples and validator packs that are cross-context rather than agent-plane-specific. Those remain in `SocioProphet/socioprophet-standards-storage` unless a later PR intentionally migrates a runtime-facing subset here.
