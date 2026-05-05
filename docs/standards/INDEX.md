# Standards Catalog

This file catalogs the standards currently landed or proposed under `docs/standards/`.

## Domains

- `agent-plane/` — runtime-facing agent action, trace, lifecycle, evidence, and conformance profiles
- `authentication/` — identity proof, sessioning, federation, recovery, and machine identity
- `conformance/` — profile-layer conformance criteria and release posture
- `networking/` — mesh identity advertisement, path-template vocabulary, and network-facing capability contracts

## Agent-plane standards

- `agent-plane/001-agent-action-trace-conformance-profile.md`
  - runtime-facing Action Ontology consumption profile for agent capability declarations, action records, trace records, receipts, policy refs, and conformance evidence

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
