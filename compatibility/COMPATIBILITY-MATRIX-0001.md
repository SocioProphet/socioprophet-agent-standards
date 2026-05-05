# Compatibility Matrix 0001

Status: bootstrap compatibility map, reconciled after upstream drift review.

## Purpose

This matrix defines the initial SocioProphet agent standards compatibility surface across the currently relevant upstream repositories. It is intentionally conservative: it identifies required relationships and current alignment posture, but it does **not** yet claim a fully pinned release.

## Reading this matrix

- **Required** means the repository is part of the minimum compatibility story for the SocioProphet agent standards layer.
- **Constrained** means the repository remains externally owned but is profile-constrained here.
- **Advisory** means useful for alignment but not part of the minimum compatibility baseline.
- **Consumed** means another repo is already treating this repository as a normative standards import.
- **Pin status** remains provisional until explicit commit/tag pins are recorded in a release matrix.

## Core repository matrix

| Repository | Role in ecosystem | Profile relationship | Current compatibility posture | Pin status | Notes |
|---|---|---|---|---|---|
| `SourceOS-Linux/sourceos-spec` | Base SourceOS / core schema lane | Required import | Foundational and mandatory | Pending release pin | Now includes local-agent runtime, history/sync, shell receipt, redaction, and local-first service surfaces |
| `SociOS-Linux/agentos-starter` | Runtime interface drafts and starter alignment | Required import | Required for runtime-side alignment | Pending release pin | April LRK/witness/trust tranche affects profile expectations |
| `SociOS-Linux/workstation-contracts` | Contract/example/validator/CI discipline | Required reference pattern | Strongly aligned | Pending release pin | Governs publication and validation discipline |
| `SocioProphet/tritrpc` | Wire/control-plane semantics | Required import | Required for control-plane interoperability | Pending release pin | Capability-fabric pointer and protocol-binding surfaces remain relevant |
| `SocioProphet/prophet-platform` | Deployment/runtime/identity composition lane | Required compatibility target and consumer | Active consumer of this standards repo | Partial external pin exists in platform | Platform pins agent auth standards and conformance 0001 into gateway/identity-prime |
| `SocioProphet/sherlock-search` | Semantic search and evidence indexing lane | Constrained external service lane | Expected compatible consumer/provider | Pending release pin | Replay evidence and Lattice platform asset records are now concrete search fixtures |
| `SocioProphet/cloudshell-fog` | Shell/fog execution and command-bundle lane | Constrained external service lane | Expected compatible consumer/provider | Pending release pin | Runtime release/readiness command bundles and structural conformance now matter |
| `SocioProphet/contractforge` | Artifact/economic/obligation contract lane | Constrained external service lane | Expected compatible adjunct | Pending release pin | Obligation Ledger and platform asset contract references are relevant |
| `SocioProphet/socioprophet-standards-storage` | Broader organizational standards storage | Advisory/shared standards lane | Must not conflict | Pending release pin | Storage, geospatial, learning-loop, and curriculum standards remain external |

## Upstream drift anchors

The current compatibility posture is informed by these verified upstream movements:

| Surface | Verified movement | Compatibility impact |
|---|---|---|
| SourceOS local-agent runtime | `SourceOS-Linux/sourceos-spec` added `specs/local-agent-runtime.md` | Core profile must model local-agent runtime, persistence, auth, logs, preflight, quarantine, and operator command expectations |
| SourceOS history/sync/receipt/local-first surfaces | `sourceos-spec` added OpsHistory, BearHistory, ShellReceipt, RedactionTombstone, and LocalFirstServiceManifest related commits | Compatibility matrix must treat history, redaction, receipt, and local-first state as adjacent profile inputs |
| AgentOS LRK / witness trust | `SociOS-Linux/agentos-starter` merged LRK witness and trust helper logic | Conformance must include witness/trust bundle expectations for governance-grade runtime lanes |
| Prophet Platform standards consumption | `prophet-platform` added a controlled `agent-auth-standards` lock entry for this repo | This repo is already a normative input; breaking changes must be compatibility-managed |
| Prophet Platform structural conformance | `prophet-platform` added a cloudshell-fog structural conformance workflow | Conformance criteria should map to concrete CI validation surfaces |
| Sherlock replay evidence | `sherlock-search` added Lattice replay evidence fixture, validator, and workflow | Evidence profile should cover replay bundle, runtime refs, artifact refs, lineage receipts, metrics, and compatibility surfaces |
| CloudShell/Fog runtime release commands | `cloudshell-fog` added a runtime release command bundle with validator/workflow wiring | Orchestration/runtime standards should model read-only manifest, policy, and readiness inspection commands |
| Personal intelligence cells | This repo added a second-pass Aigents audit for personal intelligence cells | Repo scope now includes WatchPattern, FeedbackEvent, CellArchive, ChannelAdapter, CellConfig, reputation, and social environment assessment lanes |

## Minimum accepted compatibility set

A release candidate of this repository should not claim full agent-plane or agent-standards compatibility until it records an accepted set across at least:

- `SourceOS-Linux/sourceos-spec`
- `SociOS-Linux/agentos-starter`
- `SociOS-Linux/workstation-contracts`
- `SocioProphet/tritrpc`
- `SocioProphet/prophet-platform`
- one or more service consumers such as `cloudshell-fog`, `sherlock-search`, or `contractforge`

## Consumer-sensitive standards

The following standards are already compatibility-sensitive because `prophet-platform` has consumed them through `standards.lock.yaml`:

- authentication standards 001-004;
- `conformance/CONFORMANCE-CRITERIA-0001.md`.

Changes to those files should be treated as externally visible and should either preserve backward compatibility or be accompanied by a new profile/conformance version.

## Known current limitation

This is still a bootstrap matrix, not a release matrix. It captures relationship model, verified drift, and expected coupling, but it does not yet record commit-level or tag-level pins for every required dependency.

## Upgrade rule

A future revision of this matrix should add:

- explicit commit or tag pins;
- compatibility status by profile release;
- breakage notes when upstreams drift;
- deprecation notes for retired compatibility claims;
- validator/workflow links for C3-C5 conformance claims.

## Blocking condition for stronger readiness claims

No profile should claim stable cross-repository readiness until:

1. the required repositories are pinned,
2. conformance expectations are mapped to concrete validators or CI workflows,
3. at least one end-to-end runtime consumer validates the bundle, and
4. any platform consumer lock is updated or confirmed compatible.
