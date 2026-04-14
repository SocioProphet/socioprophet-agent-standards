# ADR-0001: Repository Role and Ownership

Status: accepted

## Context

SocioProphet needs a repository that owns the **normative profile layer** for the agent plane without colliding with lower-level schema ownership that is already emerging elsewhere.

Recent work across the ecosystem has already distributed responsibilities:

- `SourceOS-Linux/sourceos-spec` is becoming the gravity well for base SourceOS and agent-plane schemas.
- `SociOS-Linux/agentos-starter` is carrying runtime/interface drafts and starter alignment.
- `SociOS-Linux/workstation-contracts` is carrying the contract + example + validator + CI pattern for disciplined contract publication.
- Service/domain repositories such as `sherlock-search`, `cloudshell-fog`, and `contractforge` own their own contract families.
- `socioprophet-standards-storage` already exists as a broader cross-organizational standards lane.

If this repository were treated as another generic `spec` root, schema ownership would become ambiguous and duplicated.

## Decision

This repository will own the **SocioProphet agent-plane standards/profile layer**.

That means it owns:

- SocioProphet-specific normative profile definitions
- conformance levels and acceptance expectations
- compatibility statements across imported upstream repositories
- evidence obligations for profile-conformant systems
- profile overlays and constraints that are specific to SocioProphet
- ADRs that explain ownership, imports, versioning, and deprecation

This repository will **not** own:

- base SourceOS or core agent-plane schemas
- runtime starter implementations or service code
- service-specific API/event contracts that already belong elsewhere
- generic organization-wide standards outside the agent-plane profile scope

## Consequences

### Positive

- Ownership is explicit rather than inferred.
- The repository can move quickly on profile and compatibility work without forking lower-level schemas.
- Upstream schema families remain canonical in their own repositories.
- SocioProphet gets one place to state what combinations of upstream artifacts are accepted together.

### Negative

- Some changes that users may want to make here will actually belong upstream and must be routed there first.
- The repository must maintain discipline around imports, pins, and compatibility claims.

## Rules flowing from this decision

1. **Upstream-first rule**
   - If a change is fundamentally a base schema change, it belongs upstream first.

2. **No-shadowing rule**
   - This repository must not silently duplicate or fork lower-level machine contracts already owned elsewhere.

3. **Profile publication rule**
   - A profile change is not complete until it states the imported upstream(s), compatibility impact, and evidence/conformance consequences.

4. **Explicit divergence rule**
   - Any unavoidable divergence from upstream must be explained in a follow-on ADR with a reconciliation path.

## Follow-on work

The next artifacts expected after this ADR are:

- a first core profile definition
- a compatibility matrix across `sourceos-spec`, `agentos-starter`, `tritrpc`, and key SocioProphet service repos
- conformance criteria for capability descriptors, execution decisions, session receipts, and evidence bundles
