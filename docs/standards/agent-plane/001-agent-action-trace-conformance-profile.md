# 001. Agent Action / Trace Conformance Profile (v0.1)

## Status

Draft profile.

## Purpose

This standard defines how runtime agents consume the Action Ontology and expose conformance evidence through action, trace, receipt, policy, and capability surfaces.

It does not replace the ontology source. It defines the runtime-facing profile over the ontology.

## Authority chain

- Semantic ontology source: `SocioProphet/ontogenesis`
- Bootstrap executable examples and validators: `SocioProphet/socioprophet-standards-storage`
- Runtime execution/control-plane consumer: `SocioProphet/agentplane`
- Platform consumer and generated artifacts: `SocioProphet/prophet-platform`
- SourceOS/AgentOS realization consumers: `SourceOS-Linux/sourceos-spec`, `SourceOS-Linux/agent-machine`, and related runtime repos

## Required runtime declarations

An implementation claiming conformance to this profile MUST declare:

- agent identity or runtime subject reference
- capability set
- supported action types
- supported trace patterns
- supported evidence and receipt kinds
- policy decision reference strategy
- conformance profile version

## Required action record posture

A conforming runtime MUST emit or preserve action records that identify:

- action identifier
- performing agent or subject
- action type
- from-state reference when applicable
- to-state reference when applicable
- timestamp
- policy/evidence references when the action is governed

## Required trace posture

A conforming runtime MUST emit or preserve trace records that identify:

- trace identifier
- pattern or protocol family
- trace kind
- medium or channel
- timestamp
- referenced action when the trace acknowledges, completes, reverses, or validates an action

## Pattern scope

The bootstrap profile recognizes these initial coordination families:

- Contract Net
- Pub/Sub
- ContractNet-to-PubSub bridge

Additional families such as Blackboard, Workflow, Quorum/Human-in-the-loop, and CRDT-style convergence should be added only with examples and failure cases.

## Policy and evidence posture

Conforming runtimes MUST NOT treat traces as authority by themselves.

A trace may be evidence, signal, or coordination residue. Authorization and execution authority remain with the policy and runtime control plane.

Runtime agents SHOULD attach or preserve:

- policy decision identifiers
- receipt references
- evidence bundle references
- replay or validation metadata when available

## Migration boundary

Do not move the Action Ontology semantic source into this repository.

Do not move generic bootstrap bundles wholesale from `socioprophet-standards-storage`.

This repo should receive only the agent-plane-facing conformance profile, schemas, compatibility matrices, and examples that downstream runtimes need to claim compatibility.

## Initial conformance statement

An implementation is v0.1-conformant when it can:

1. declare an `AgentActionTraceProfile`
2. emit action and trace records matching its declared capabilities
3. reject malformed pattern traces according to the bootstrap validator family
4. link governed actions to policy/evidence/receipt references
5. document deviations from this profile

## Follow-up work

- define stricter receipt schema integration
- define compatibility matrix for AgentPlane, Agent Machine, AgentTerm, SourceChannel, and Prophet Platform
- add negative conformance examples
- add generated identity/action/evidence contract consumption in downstream platform repos
