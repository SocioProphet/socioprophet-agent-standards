# Conformance Criteria 0001

Status: bootstrap conformance baseline.

## Purpose

This document defines the initial SocioProphet agent-plane conformance ladder that downstream capabilities, services, and runtime lanes should use when claiming compliance with this repository’s profile layer.

This is a **profile-layer** conformance document. It does not replace validator logic in upstream repositories. It states the minimum evidence and declaration posture expected for a valid compatibility claim.

## Conformance levels

### Level C0 — documented only

The implementation has documentation but does not yet provide enough structured contract material to be treated as profile-conformant.

Typical characteristics:

- design notes or prose exist
- machine-readable contracts are incomplete or absent
- no explicit upstream compatibility claim is made

C0 is not acceptable for production-facing interoperability claims.

### Level C1 — contract present

The implementation provides the minimum contract/declaration surface needed to be recognized by the profile layer.

Required at C1:

- stable identifier and lifecycle state
- capability descriptor or equivalent declaration
- explicit reference to the relevant upstream contract family or families
- explicit reference to applicable profile documents
- version or release posture

C1 means the object is structurally described, not that it is governable in production.

### Level C2 — governed execution

The implementation declares how it behaves under control, gating, orchestration, and rollback expectations.

Required at C2:

- control profile reference
- gating profile reference
- orchestration profile reference
- execution decision or equivalent execution-governance object
- rollback posture for non-trivial writes
- session object and session receipt expectation where sessions exist

C2 is the minimum level for serious runtime integration.

### Level C3 — auditable and explainable

The implementation emits or references evidence artifacts sufficient for review, replay reasoning, and policy inspection.

Required at C3:

- evidence profile reference
- declared evidence artifacts or evidence-emission expectations
- traceable execution outcome or receipt object
- policy/gate outcome visibility
- telemetry compatibility expectation

C3 is the minimum level for production-facing governed execution claims.

### Level C4 — compatibility pinned

The implementation claims compatibility only against explicit pinned upstream artifacts.

Required at C4:

- explicit compatibility matrix entry
- commit/tag/version pins for required upstreams
- declared breakage or incompatibility notes where applicable
- release or publication artifact linking the pins to the profile claim

C4 is the minimum level for stable cross-repository release claims.

### Level C5 — replayable and review-ready

The implementation is sufficiently evidence-rich and disciplined to support replay, audit, and promotion/demotion decisions.

Required at C5:

- reproducibility or replay artifacts where applicable
- evidence references attached to promotion / rollout / qualification claims
- explicit downgrade or freeze rules when compatibility or safety posture degrades
- validation evidence from at least one real runtime consumer

C5 is the target for high-trust production lanes.

## Minimum artifact expectations by object family

### Capability/service declarations

Should provide:

- identifier
- version / lifecycle state
- steward / owner
- upstream contract references
- profile references

### Execution-capable agents/services

Should provide:

- execution decision object or equivalent declaration
- gating and rollback posture
- orchestration declaration
- session and receipt expectations where sessions exist

### Evidence-bearing systems
n
Should provide:

- evidence artifact declarations
- telemetry compatibility posture
- provenance or reproducibility expectation where applicable

## Failure conditions

An implementation should be treated as non-conformant if any of the following are true:

- it claims compatibility without naming its upstream contract family
- it claims governed execution without declaring gates or rollback posture
- it claims auditable operation without evidence or receipt expectations
- it claims stable release compatibility without explicit pins

## Release gating recommendation

A profile release in this repository should not promote an implementation as broadly compatible unless it reaches at least:

- C2 for early integration
- C3 for governed production-facing execution
- C4 for stable release compatibility
- C5 for high-trust reviewable deployment lanes

## Expected follow-on work

A later revision should map these levels to:

- concrete validators
- required artifacts by repo type
- promotion and graduation thresholds
- end-to-end runtime verification results
