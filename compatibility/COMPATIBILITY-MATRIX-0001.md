# Compatibility Matrix 0001

Status: bootstrap compatibility map.

## Purpose

This matrix defines the initial SocioProphet agent-plane compatibility surface across the currently relevant upstream repositories. It is intentionally conservative: it identifies required relationships and current alignment posture, but it does **not** yet claim a fully pinned release.

## Reading this matrix

- **Required** means the repository is part of the minimum compatibility story for the SocioProphet agent plane.
- **Constrained** means the repository remains externally owned but is profile-constrained here.
- **Advisory** means useful for alignment but not part of the minimum compatibility baseline.
- **Pin status** remains provisional until explicit commit/tag pins are recorded in a later revision.

## Matrix

| Repository | Role in ecosystem | Profile relationship | Current compatibility posture | Pin status | Notes |
|---|---|---|---|---|---|
| `SourceOS-Linux/sourceos-spec` | Base SourceOS / core agent-plane schemas | Required import | Foundational and mandatory | Pending explicit pin | Canonical owner for lower-level agent-plane schema families |
| `SociOS-Linux/agentos-starter` | Runtime interface drafts and starter alignment | Required import | Required for runtime-side alignment | Pending explicit pin | Canonical runtime exemplar lane |
| `SociOS-Linux/workstation-contracts` | Contract/example/validator/CI discipline | Required reference pattern | Strongly aligned | Pending explicit pin | Governs publication and validation discipline |
| `SocioProphet/tritrpc` | Wire/control-plane semantics | Required import | Required for control-plane interoperability | Pending explicit pin | Canonical protocol/control envelope lane |
| `SocioProphet/sherlock-search` | Semantic search service contracts | Constrained external service lane | Expected compatible consumer/provider | Pending explicit pin | Service-specific contract family remains externally owned |
| `SocioProphet/cloudshell-fog` | Shell/fog execution and policy lane | Constrained external service lane | Expected compatible consumer/provider | Pending explicit pin | Important for execution, policy, and evidence alignment |
| `SocioProphet/contractforge` | Artifact/economic contract family | Constrained external service lane | Expected compatible adjunct | Pending explicit pin | Relevant for artifact lifecycle and evidence surfaces |
| `SocioProphet/prophet-platform` | Deployment/runtime composition lane | Required compatibility target | Must consume aligned profile releases | Pending explicit pin | Platform-side integration surface |
| `SocioProphet/socioprophet-standards-storage` | Broader organizational standards storage | Advisory / shared standards lane | Must not conflict | Pending explicit pin | Shared standards remain externally owned |

## Minimum accepted compatibility set

A release candidate of this repository should not claim full agent-plane compatibility until it records an accepted set across at least:

- `sourceos-spec`
- `agentos-starter`
- `workstation-contracts`
- `tritrpc`
- one or more SocioProphet service consumers such as `cloudshell-fog`, `sherlock-search`, or `prophet-platform`

## Known current limitation

This is a bootstrap matrix, not a release matrix. It captures the relationship model and expected coupling, but it does not yet record commit-level or tag-level pins.

## Upgrade rule

A future revision of this matrix should add:

- explicit commit or tag pins
- compatibility status by profile release
- breakage notes when upstreams drift
- deprecation notes for retired compatibility claims

## Blocking condition for stronger readiness claims

No profile should claim stable cross-repository readiness until:

1. the required repositories are pinned,
2. conformance expectations are recorded, and
3. at least one end-to-end runtime consumer validates the bundle.
