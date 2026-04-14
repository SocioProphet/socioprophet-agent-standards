# Global cybernetics shared master canon second-wave decision review v1

## Purpose

This review resolves the deferred second-wave Guideplane shared objects and the remaining alias-held objects.

## Decision criteria

An object is promoted in the second wave when all of the following are true:
1. it represents durable reality rather than workbench behavior
2. it is required by more than one governed surface or service
3. it has stable semantics independent of Guideplane’s UI
4. it does not collapse cleanly into an already-promoted canonical object

An object remains alias-held when:
1. its semantics are still coupled to a Guideplane-facing presentation model, or
2. a broader cross-platform target noun is preferable but not yet fully frozen.

## Decisions

### Promote now in master canon v2
- `ExecutionComponent`
- `RuntimeSubstrate`
- `ServiceRoute`
- `LearningConstraint`

### Remain alias-held
- `CapabilityOffer` → reserved canonical target `ServiceOffer`
- `FacetView` → reserved canonical target `FacetProjection`

## Rationale

`ExecutionComponent`, `RuntimeSubstrate`, and `ServiceRoute` are no longer Guideplane-specific. The executable reference app, fulfillment path, and broader service orchestration all need a stable execution/runtime vocabulary.

`LearningConstraint` should be promoted now because the master canon already includes `LearningDecisionRecord`, and a decision record without its governing constraint object leaves the adaptive-governance layer incomplete.

`CapabilityOffer` remains alias-held because the broader canon should distinguish between:
- a reusable abstract service/offer surface
- a routed fulfillment path (`ServiceRoute`)
- a delivered output (`DeliveryArtifact`)

Promoting `CapabilityOffer` prematurely would blur those lines.

`FacetView` remains alias-held because the broader canon should treat it as a projection construct over canonical properties, not as a primitive canonical noun. The reserved target name `FacetProjection` is stronger, but should be promoted only when broader property/view semantics are frozen across more than one surface.

## Promotion outcome

Master canon v2 adds the second-wave promoted objects and introduces an alias registry for the held objects.
