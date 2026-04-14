# Boundaries

This repository exists to own the **SocioProphet normative profile layer** for the agent plane.

## In scope

This repository owns:

- SocioProphet-specific profile definitions over imported agent-plane contracts
- Compatibility expectations across SourceOS, AgentOS, TriTRPC, and SocioProphet platform services
- Conformance levels and acceptance criteria
- Evidence obligations for profile-conformant capabilities and services
- Overlay fragments and profile-side constraints that are specific to the SocioProphet ecosystem
- ADRs that define ownership, import discipline, and deprecation rules

## Out of scope

This repository does not own:

- Base SourceOS or core agent-plane schemas
- Runtime starter implementations or example service code
- Service-specific API or event contracts that already belong to their domain repositories
- Generic organization-wide standards that are not specific to the agent plane

## Canonical ownership map

- `SourceOS-Linux/sourceos-spec`
  - Owns core SourceOS and agent-plane schema families
  - Owns lower-level machine-readable contract primitives

- `SociOS-Linux/agentos-starter`
  - Owns starter/runtime interface drafts and adoption exemplars
  - Owns runnable alignment surfaces for AgentOS-side implementation

- `SociOS-Linux/workstation-contracts`
  - Owns the reference pattern for contract + examples + validator + CI discipline

- `SocioProphet/tritrpc`
  - Owns wire/control-plane semantics and protocol-aligned transport surfaces

- `SocioProphet/socioprophet-standards-storage`
  - Owns broader organization-wide standards and shared schema families that are not specific to this profile layer

- Service/domain repositories such as `sherlock-search`, `cloudshell-fog`, and `contractforge`
  - Own their service-specific contracts and domain-level semantics

## Upstream-first rule

When a proposed change is properly a base schema or service contract change, it must be made in the owning upstream repository first. This repository may then:

- import the new version
- pin the accepted version
- describe compatibility implications
- impose additional SocioProphet profile constraints

## No-shadowing rule

This repository must not silently duplicate or fork lower-level schemas that are already canonically owned elsewhere. If duplication is unavoidable, an ADR must explain:

- why the upstream owner cannot absorb the change
- what divergence exists
- how reconciliation will be handled
- what the deprecation path is

## Profile-side publication rule

A profile change is not complete until it states:

- the imported upstream contract family or repository
- the accepted version or pin
- the conformance impact
- the required evidence artifacts, if any
- the validation or compatibility consequence

## Repository growth rule

New top-level directories should only be added when they carry immediate committed value. The intended order is:

1. `adr/`
2. `profiles/`
3. `compatibility/`
4. `conformance/`
5. `overlays/`
6. `examples/`

## Default disposition

If ownership is unclear, the default answer is **do not add the artifact yet**. Resolve ownership with an ADR first.
