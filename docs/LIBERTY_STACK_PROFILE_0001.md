# Liberty Stack Profile 0001

Status: draft normative profile.

## Purpose

This profile defines the canonical surfaces required when an agent or platform participates in provider exit, sovereign migration, verification, replay, cutover, retention, and final decommission workflows.

This profile is not a product bundle. It is a governance and contract layer that binds export, import, verification, replay, approval, and closure behavior to evidence.

## Core model

A Liberty Stack implementation SHOULD separate at least these planes:
- raw capture plane
- normalized event plane
- entity and dependency plane
- derived verification plane
- global or external context plane when used

Every material operation SHOULD preserve:
- provenance
- validity interval or observed time
- merge or overwrite semantics
- replay eligibility
- operator-visible surface behavior

## Required workflow surfaces

Every Liberty Stack-conformant implementation SHOULD declare:
- `inventory_surface`
- `export_surface`
- `normalization_surface`
- `import_surface`
- `verification_surface`
- `replay_surface`
- `cutover_surface`
- `approval_surface`
- `retention_surface`
- `decommission_surface`
- `evidence_surface`

## Required object families

A Liberty Stack implementation SHOULD define or consume at least:
- migration manifest
- sovereign context record
- provider adapter contract
- verification record
- replay request and replay result records
- cutover decision record
- decommission gate record
- evidence bundle

## Normative rules

1. Any destructive or irreversible transition MUST be gated by evidence and explicit approval.
2. Verification MUST be replayable and SHOULD distinguish first-pass results from replay results.
3. Provider-specific field names SHOULD remain adapter-local; the canonical record family MUST remain provider-neutral.
4. Cutover and final decommission MUST be modeled as separate states.
5. A Liberty Stack implementation SHOULD preserve enough structure to answer what was observed, what was inferred, what was approved, and what was finalized.

## Relationship to AgentOS

When an AgentOS-conformant agent performs provider exit, migration, verification, or final decommission work, it SHOULD declare `LIBERTY_STACK_PROFILE_0001` in its profile set and emit the corresponding evidence-bearing objects.
