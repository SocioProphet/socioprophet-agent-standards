# Guideplane Operator Conformance (Draft v1)

## Purpose

This note defines minimum conformance expectations for an agent or assistant claiming compatibility with the Guideplane operator profile.

Guideplane is not a standalone execution authority. It is an operator-facing control surface that must preserve visible boundaries between navigation, qualification, fulfillment, explanation, and outcome review.

## Required posture

A conforming Guideplane operator MUST expose:

- actor and operating context
- active intent or inquiry frame
- ambiguity or uncertainty when relevant
- route or capability explanation
- qualification state before fulfillment
- denial, obligation, expiry, or escalation state when present
- outcome state after fulfillment or escalation

## Required boundary behavior

A conforming implementation MUST NOT:

- hide policy basis behind generic disabled controls
- dispatch a fulfillment action without qualification
- replace Policy Fabric verdicts with local policy claims
- replace AgentPlane evidence contracts with local execution claims
- claim ontology authority for SHIR or semantic objects
- collapse denial, expiry, and escalation into one generic error state

## Required repository alignment

A conforming implementation should align with the current repo split:

- platform operator standard in `prophet-platform-standards`
- agent profile and conformance here in `socioprophet-agent-standards`
- runtime contracts in `prophet-platform`
- semantic mapping in `ontogenesis`
- execution evidence in `agentplane`
- policy verdicts in `policy-fabric`
- workspace topology in `sociosphere`

## Minimum evidence expectation

A conforming implementation SHOULD be able to produce or preserve references for:

- actor context
- inquiry or intent frame
- selected route or capability path
- policy or access qualification record
- fulfillment or escalation record
- outcome record

## Relationship to platform standard

This conformance note depends on the platform-level Guideplane operator workbench standard in `prophet-platform-standards`.

The profile here defines agent-facing behavior only. It does not define UI layout, runtime contracts, ontology semantics, or policy verdict shapes.
