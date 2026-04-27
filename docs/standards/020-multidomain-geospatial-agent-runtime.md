# 020 — Multi-Domain Geospatial Agent Runtime Standard

Status: Draft v0.1
Authority: `SocioProphet/socioprophet-agent-standards`
Related: `SocioProphet/prophet-platform-standards/docs/standards/070-multidomain-geospatial-standards-alignment.md`

## Purpose

This standard defines how agents may interact with multi-domain geospatial data, runtime boundaries, evidence bundles, approval gates, and replay artifacts across SourceOS, AgentOS, Agentplane, Lattice Forge, and Prophet Platform services.

## Runtime classes

The following runtime classes are in scope:

- ingest runtimes: OSM, STAC, AIS, LRIT-authorized, ADS-B, SensorThings, CCSDS-like telemetry, field observations
- transformation runtimes: conflation, tiling, indexing, catalog projection, redaction, geometry validation
- analytics runtimes: anomaly scoring, route risk, coverage/revisit windows, vessel/air/asset track quality, soil/environment prediction
- report runtimes: decision cards, evidence bundles, map layer manifests, runtime boundary reports
- advisory tasking runtimes: authorized task proposals, never ungoverned action

## Agent execution requirements

Every multi-domain geospatial agent runtime MUST define:

- runtime ID and version
- input schema references
- output schema references
- policy bundle references
- allowed data classes
- denied data classes
- sensitive-location handling
- source license constraints
- expected evidence bundle
- replay command or replay procedure
- approval requirements
- failure and rollback semantics

## Approval gates

Agents MUST NOT execute privileged geospatial operations without policy approval. The following require explicit approval gates:

- any runtime that writes to canonical stores
- any runtime that unmasks sensitive geospatial data
- any runtime that exports restricted datasets
- any runtime that interacts with defense/public-safety data
- any runtime that performs live tasking or operational recommendations
- any runtime that promotes derived observations to canonical truth

## Safety boundary

This standard allows authorized analysis, public-safety, humanitarian, logistics, infrastructure, environmental, compliance, and customer-owned operational workflows. It does not define or authorize ungoverned targeting, evasion, sensitive-site exploitation, or unauthorized tracking workflows.

## Runtime evidence bundle

Each run SHOULD emit:

- input manifest
- output manifest
- source provenance refs
- runtime boundary ID
- policy bundle hash
- environment fingerprint
- decision/audit log
- replay metadata
- redaction/masking report when applicable

## Lattice Forge admission rule

A geospatial runtime may be admitted to Lattice Forge only after it has:

1. an executable entrypoint,
2. schema-bound inputs and outputs,
3. a validation command,
4. a sample fixture,
5. policy bundle reference,
6. evidence bundle definition,
7. replay semantics,
8. and a standards cross-reference to this file plus storage/knowledge/platform standards.
