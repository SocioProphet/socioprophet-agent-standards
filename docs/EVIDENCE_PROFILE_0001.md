# Evidence Profile 0001

Status: draft normative profile for SocioProphet agent-plane evidence and provenance objects.

## Purpose

This profile defines the minimum evidence/provenance object family that downstream runtime repositories should use when they need to express:
- reproducibility state
- score movement attribution
- methodology snapshots
- source-metric to canonical-metric normalization

## Initial object set

- `ReproLedgerEntry`
- `CausalAttribution`
- `MethodologySnapshot`
- `MetricCrosswalk`

## Downstream consumers

Expected downstream consumers include:
- `SocioProphet/prophet-platform`
- platform-facing agent runtime services
- evaluation and competition-intelligence surfaces

## Design constraints

These objects should be:
- small and composable
- replay-friendly
- evidence-oriented rather than UI-oriented
- compatible with conformance and compatibility metadata in later profiles

## Current scope

This profile intentionally avoids over-specifying transport, storage, or UI concerns. It standardizes only the object vocabulary and minimum required fields.
