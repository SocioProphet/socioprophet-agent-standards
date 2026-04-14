# Profile 0001: Core Agent-Plane Profile

Status: draft normative profile.

## Purpose

This profile defines the minimum interoperable SocioProphet agent-plane bundle that a capability, service, or runtime lane should satisfy before it is treated as profile-conformant.

The goal is not to relocate all lower-level schemas into this repository. The goal is to declare the **minimum accepted combination** of upstream objects, controls, gates, evidence, and compatibility obligations that together form a SocioProphet-governed agent-plane baseline.

## Scope

This profile applies to:

- agent capabilities that perform meaningful reasoning or execution
- services that host, route, or govern agent behavior
- runtime lanes that need compatibility with SourceOS, AgentOS, TriTRPC, and SocioProphet platform services

This profile does not replace lower-level schemas owned upstream.

## Canonical upstream dependencies

### SourceOS base schema lane

Imported from `SourceOS-Linux/sourceos-spec`:

- execution decision schema family
- session schema family
- execution surface schema family
- skill manifest schema family
- memory entry schema family
- session receipt schema family
- telemetry / rollout / release receipt scaffolds
- OpenAPI and AsyncAPI patch fragments where applicable

### AgentOS runtime lane

Imported from `SociOS-Linux/agentos-starter`:

- starter/runtime interface drafts
- runtime adoption expectations for executor, orchestrator, and memory-facing components
- implementation-side mapping for profile conformance

### Wire/control-plane lane

Imported from `SocioProphet/tritrpc`:

- control-plane compatibility requirements
- capability/control envelope semantics
- transport-aligned contract expectations

### Service/domain lanes

Referenced from:

- `SocioProphet/sherlock-search`
- `SocioProphet/cloudshell-fog`
- `SocioProphet/contractforge`
- `SocioProphet/prophet-platform`

These remain domain-owned and are only constrained here at the profile layer.

## Required profile objects

A profile-conformant production-facing agent or service should declare, either directly or by reference, the following object families.

### Identity and versioning

- stable capability or service identifier
- semantic version or release posture
- steward / owner reference
- status / lifecycle state

### Capability and execution

- capability descriptor or equivalent capability declaration
- execution decision object
- execution surface declaration
- skill manifest
- session object
- session receipt object

### Memory and context

- memory entry or memory interface declaration where memory is present
- operating context / subject context binding where policy depends on context

### Governance and gates

The profile requires explicit attachment to the following normative subprofiles already present in this repository:

- control profile
- gating profile
- graduation profile
- orchestration profile
- evidence profile

A conformant implementation should either:

1. reference these profiles directly, or
2. provide a stricter profile that is explicitly compatible with them.

### Evidence and observability

At minimum, the implementation should provide or reference:

- evidence emission expectations
- session receipt emission expectations
- rollback expectation for non-trivial writes
- telemetry event compatibility expectations
- provenance / reproducibility artifact expectations where applicable

## Required declarations

Every profile-conformant capability or service should declare at least the following:

- `control_profile_ref`
- `gating_profile_ref`
- `graduation_profile_ref`
- `orchestration_profile_ref`
- `evidence_profile_ref`
- `upstream_contract_refs`
- `compatibility_claims`
- `evidence_expectations`
- `rollback_posture`

## Compatibility rules

1. Upstream base schemas remain canonical in their owning repositories.
2. A compatibility claim is incomplete unless the implementation identifies the upstream contract family it depends on.
3. Domain/service contracts must not be redefined here; they must be referenced and constrained here.
4. Any breaking divergence from upstream must be documented in an ADR.
5. A profile release should not claim production readiness until version pins are recorded in the compatibility matrix.

## Minimum conformance posture

A production-facing agent or service should satisfy all of the following:

- identifies its capability and lifecycle state
- declares how it chooses actions
- declares what gates must be satisfied before execution
- declares its maturity / graduation posture
- declares how work is orchestrated and routed
- emits or references evidence artifacts sufficient to explain execution and review outcomes
- identifies the upstream schema families it relies on

## Explicit non-goals

This profile does not:

- redefine the entire SourceOS schema family
- define transport internals already owned by TriTRPC
- replace service-specific contracts already owned by domain repositories
- guarantee release-quality compatibility without explicit pins

## Immediate follow-on

This profile should be paired with:

- Compatibility Matrix 0001
- Conformance Criteria 0001
- future version-pinned profile releases that move this bootstrap profile from draft to release-candidate
