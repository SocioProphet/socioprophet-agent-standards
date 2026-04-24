# Michael Conformance (Draft v1)

## Purpose

This note defines the minimum conformance expectations for any implementation claiming compatibility with the Michael agent profile.

## Required semantic posture

A conforming implementation MUST distinguish:
- asserted truth
- believed truth
- candidate law
- promoted heuristic
- rejected hypothesis

A conforming implementation MUST NOT collapse those statuses into one undifferentiated output class.

## Required engine posture

A conforming implementation MUST expose, either directly or through integrated components:
- symbolic or neuro-symbolic deduction
- probabilistic-relational belief update
- symbolic-regression candidate-law discovery

## Required artifact kinds

A conforming implementation SHOULD be able to produce or consume at least:
- `belief_state`
- `equation_candidate`
- `counterexample`
- `promotion_decision`
- `human_digital_twin_state`

## Required governance posture

A conforming implementation MUST support bounded promotion through explicit gates and decisions, including:
- belief-to-ontology promotion
- candidate-law promotion
- human twin boundary enforcement

## Required digital-twin posture

A conforming implementation MUST treat the human digital twin as:
- a bounded projection
- consent-governed
- anchored on the human subject as moral and authorization source

## Repository-role expectation

A conforming Michael implementation is expected to align its work with the current repo split:
- semantics in `ontogenesis`
- instance/world state in `gaia-world-model`
- governance and eval in `prophet-platform`
- execution packs in `prophet-platform-fabric-mlops-ts-suite`
- profile language here in `socioprophet-agent-standards`

## Minimum evidence expectation

Promotion decisions SHOULD be backed by:
- methodology snapshot refs
- evidence packet refs
- gate results
- signers or approval refs when required
