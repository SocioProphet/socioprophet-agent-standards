# SocioProphet Agent Standards

Normative SocioProphet standards, profile, conformance, evidence, and compatibility layer for governed agent systems across SourceOS, AgentOS, TriTRPC, Prophet Platform, FogStack, search, identity, and personal-intelligence-cell surfaces.

## Repository role

This repository is not a generic dumping ground for every schema or implementation detail. It is the **SocioProphet normative standards and profile layer** for agent-facing systems.

It exists to:

- define SocioProphet-specific standards and profiles over imported upstream contracts;
- state compatibility expectations across SourceOS, AgentOS, TriTRPC, Prophet Platform, FogStack, Sherlock, ContractForge, and related service repos;
- define conformance levels and evidence obligations;
- preserve profile-side standards for agent authentication, identity, control, gating, orchestration, graduation, personal intelligence cells, evidence, replay, and operator-facing command surfaces;
- provide ADR-backed ownership, import, and deprecation discipline.

It does **not** replace the canonical ownership of lower-level schemas or service-specific contract families.

## Current standards lanes

The repository currently spans these lanes:

- **Core agent plane** — base profile expectations for governed capability, execution, memory, session, receipt, control, gating, orchestration, and evidence surfaces.
- **Authentication and identity** — agent authentication, credential enrollment, federation, claim mapping, workload identity, and identity-prime consumption surfaces.
- **Control / gating / graduation** — how agents choose actions, what gates dominate execution, and how maturity is promoted or frozen.
- **Orchestration and runtime** — route, skill, recipe, Ray/lifecycle, command-bundle, release-readiness, and runtime-adjacent surfaces.
- **Evidence and replay** — reproducibility, replay bundles, metric crosswalks, methodology snapshots, lineage, and searchable evidence records.
- **Personal intelligence cells** — local-first personal intelligence cells, watch patterns, signal extraction, feedback events, cell archive/migration, channel adapters, reputation, and social environment assessment.
- **Guideplane and canon** — operator-fabric, shared canon, policy-decision subtype, design-system, alias registry, and second-wave canon decision surfaces.

## Ownership boundary

This repository owns:

- standards profiles;
- compatibility matrices;
- conformance criteria;
- profile-side overlays and constraints;
- standards documents that are explicitly SocioProphet agent-plane or agent-adjacent standards;
- ADRs governing ownership, imports, versioning, and deprecation.

This repository does **not** own:

- base SourceOS / core schema families that belong in `SourceOS-Linux/sourceos-spec`;
- AgentOS runtime starter implementations that belong in `SociOS-Linux/agentos-starter`;
- service-specific API or event contracts that belong in service repos such as `sherlock-search`, `cloudshell-fog`, `contractforge`, or `prophet-platform`;
- broader organization-wide storage standards that belong in `socioprophet-standards-storage`.

See `BOUNDARIES.md`, `IMPORTS.md`, and `adr/ADR-0001-repo-role-and-ownership.md` for the formal rules.

## Canonical adjacent repositories

- `SourceOS-Linux/sourceos-spec` — base SourceOS schema lane, core agent-plane schema families, local-agent runtime, history/sync/receipt/redaction/local-first service surfaces.
- `SociOS-Linux/agentos-starter` — runtime interface drafts, starter alignment, LRK/witness/trust helpers, and AgentOS-side executable reference posture.
- `SociOS-Linux/workstation-contracts` — contract/example/validator/CI discipline.
- `SocioProphet/tritrpc` — wire/control-plane semantics and protocol binding surfaces.
- `SocioProphet/prophet-platform` — runtime integration, identity/gateway consumption, FogStack evidence, structural conformance, and deployment-side composition.
- `SocioProphet/sherlock-search` — search/index fixtures, replay evidence, Lattice records, and discovery contract surfaces.
- `SocioProphet/cloudshell-fog` — Fog Shell command bundles, runtime release/readiness inspection, connector, placement, network policy, and shell/fog execution surfaces.
- `SocioProphet/contractforge` — artifact, obligation, economic, and contract-reference surfaces.
- `SocioProphet/socioprophet-standards-storage` — broader storage, geospatial, learning-loop, curriculum, and shared standards surfaces.

## Repository layout

- `BOUNDARIES.md` — explicit ownership and non-ownership rules.
- `IMPORTS.md` — canonical import map and import discipline.
- `adr/` — accepted architecture decisions.
- `profiles/` — profile definitions owned by this standards layer.
- `compatibility/` — compatibility matrices, upstream drift anchors, and release alignment records.
- `conformance/` — conformance ladders and acceptance criteria.
- `docs/` — supporting normative profiles and standards documents.
- `docs/standards/` — standards tranches such as authentication and identity.
- `schemas/` — profile-side schema artifacts where this repository owns the standard-level shape.
- `standards/` — landed standards bundles and canon-related material.

## Current baseline

The current baseline includes:

- repository governance boundaries and import rules;
- a first core agent-plane profile;
- a first compatibility matrix;
- a first conformance criteria document;
- control, gating, graduation, orchestration, Ray, and evidence profiles;
- Guideplane and canon packages;
- authentication/identity standards consumed by `prophet-platform`;
- personal-intelligence-cell standards and second-pass Aigents audit material;
- compatibility awareness of SourceOS local-agent runtime, AgentOS LRK/witness helpers, Prophet Platform structural conformance, Sherlock replay evidence, and CloudShell/Fog runtime release command bundles.

## Working rules

1. **Upstream first.** If a change belongs to a base schema or service contract, it should land in the owning upstream repository first.
2. **No shadowing.** This repository must not silently fork lower-level machine contracts already owned elsewhere.
3. **Profile over duplication.** Import and constrain rather than re-authoring upstream standards unnecessarily.
4. **Evidence first.** Readiness claims should map to evidence, receipts, validation artifacts, or explicit compatibility records.
5. **Consumer-aware changes.** This repository is already consumed by `prophet-platform`; changes to standards referenced by `standards.lock.yaml` must be treated as compatibility-sensitive.

## Immediate next work

- add explicit version pins to compatibility records;
- split bootstrap compatibility from release-candidate compatibility;
- map conformance criteria to concrete validators and CI workflows;
- reconcile personal-intelligence-cell standards with SourceOS local-agent/runtime and memory-retention policies;
- add release-candidate bundles only after at least one runtime consumer validates the bundle end to end.
