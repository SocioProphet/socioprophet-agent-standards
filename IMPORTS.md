# Imports

This repository is a profile layer. It imports, constrains, and version-aligns upstream contract families rather than duplicating them.

## Canonical imports

### `SourceOS-Linux/sourceos-spec`

Role:
- base SourceOS and core agent-plane schema families
- lower-level machine-readable contract primitives

Imported here for:
- compatibility mapping
- profile constraints
- accepted version pinning

### `SociOS-Linux/agentos-starter`

Role:
- runtime interface drafts
- starter alignment and adoption exemplars
- implementation-side interface shape

Imported here for:
- conformance expectations
- runtime/profile alignment
- example compatibility mapping

### `SociOS-Linux/workstation-contracts`

Role:
- contract + example + validator + CI reference pattern
- local execution contract discipline

Imported here for:
- validation expectations
- contract publication discipline
- local execution conformance patterns

### `SocioProphet/tritrpc`

Role:
- wire/control-plane protocol semantics
- transport-aligned contract surfaces

Imported here for:
- protocol compatibility assertions
- capability/control-plane alignment
- profile-side interoperability requirements

### `SocioProphet/socioprophet-standards-storage`

Role:
- broader organization-wide standards and shared schema families

Imported here for:
- cross-cutting standards alignment
- references to shared schema families that remain outside this repository’s ownership boundary

### `SocioProphet/sherlock-search`

Role:
- semantic search service contracts

Imported here for:
- domain compatibility matrixing
- service-specific alignment against the SocioProphet agent-plane profile

### `SocioProphet/cloudshell-fog`

Role:
- cloud-shell and fog interface contracts
- policy and runtime interaction boundaries

Imported here for:
- profile conformance against shell/fog execution surfaces
- evidence and policy compatibility requirements

### `SocioProphet/contractforge`

Role:
- economic and artifact-oriented contract families

Imported here for:
- artifact and contract lifecycle compatibility
- evidence and publication alignment

### `SocioProphet/prophet-platform`

Role:
- runtime integration and deployment-side composition

Imported here for:
- deployment/profile compatibility expectations
- platform-facing conformance mapping

## Import discipline

1. This repository should pin imported upstreams by version, tag, or commit when compatibility claims are made.
2. Upstream contract evolution should be reflected here through explicit compatibility updates, not silent drift.
3. If an upstream contract is incompatible with the current profile, the incompatibility should be recorded explicitly.
4. This repository may add profile overlays, but it should not silently fork upstream machine contracts.

## Expected future sections

As the repository matures, this file should grow to include:

- explicit version pins
- compatibility matrix by profile release
- deprecation notes for retired imports
- rationale for profile-side overlays
