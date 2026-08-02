# Standards Catalog

This file catalogs the standards currently landed or proposed under `docs/standards/`.

## Domains

- `agent-plane/` — runtime-facing agent action, trace, lifecycle, evidence, and conformance profiles
- `authentication/` — identity proof, sessioning, federation, recovery, and machine identity
- `conformance/` — profile-layer conformance criteria and release posture
- `networking/` — mesh identity advertisement, path-template vocabulary, and network-facing capability contracts
- `workspace-context-fabric/` — compatibility profile for Workroom, Context Fabric, platform records, execution evidence, recall promotion, authority binding, and estate registration

## Estate-wide standards (top-level numbered)

- `020-multidomain-geospatial-agent-runtime.md`
  - multidomain geospatial agent runtime profile
- `030-agent-catalog-connectivity.md`
  - agents in `ds.agents-manifests` MUST be a connected graph (skills/tools/prompts/preferences/personas + agent-plane/registry/standards binding)
- `031-mcp-house-protocol.md`
  - every MCP surface MUST ride the TriTRPC transport profile (canonical JSON + `sha256` digest binding + typed media type + typed envelope + method naming); fail-closed INV-MCP-1..3; teeth-both-ways conformance verifier required per MCP surface

## Agent-plane standards

- `agent-plane/001-agent-action-trace-conformance-profile.md`
  - runtime-facing Action Ontology consumption profile for agent capability declarations, action records, trace records, receipts, policy refs, and conformance evidence

## Workspace Context Fabric standards

- `workspace-context-fabric/001-workspace-context-fabric-profile.md`
  - v0.1 profile binding workspace, platform, execution, recall, authority, and estate-registration surfaces without moving ownership out of the component repositories

## Authentication standards

- `authentication/001-agent-authentication-session-and-recovery-standard.md`
  - canonical browser, native, enterprise, admin, service, and recovery profile
- `authentication/002-credential-enrollment-and-authenticator-lifecycle-standard.md`
  - enrollment, additive vs replacement registration, lifecycle states, revocation, and recovery-factor handling
- `authentication/003-enterprise-federation-and-claim-mapping-standard.md`
  - OIDC-first federation, tenant routing, claim normalization, account linking, and internal session issuance after external proof
- `authentication/004-workload-and-service-identity-standard.md`
  - service/workload identity issuance, rotation, token exchange, audience scoping, and tenant-aware machine authorization

## Conformance standards

- `conformance/CONFORMANCE-CRITERIA-0001.md`
  - bootstrap conformance ladder for downstream compatibility and governed execution claims

## Networking standards

- `networking/001-mesh-capability-manifest-standard.md`
  - canonical mesh node capability-manifest shape for roles, transports, path templates, and signed constraints
- `networking/002-mesh-capability-manifest-canonicalization-and-conformance.md`
  - canonical serialization, hashing, signature-verification, and consumer verdict rules for mesh capability manifests

## Notes

- `001` is the umbrella authentication posture standard.
- `002`–`004` are companion standards that break out the major control surfaces needed to implement `001` cleanly.
- Implementation repositories SHOULD link directly to the standards they implement and declare any deviations.