# 020 — Multi-Domain Geospatial Agent Runtime Standard

Status: Draft v0.2
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

## Normative schemas

The following JSON Schemas are normative for this standard:

- `schemas/jsonschema/multidomain/geospatial_agent_runtime_profile.v1.schema.json`
- `schemas/jsonschema/multidomain/geospatial_runtime_evidence_bundle.v1.schema.json`

The profile schema defines runtime admission metadata. The evidence bundle schema defines per-run evidence emitted by executable runtimes.

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

## Runtime evidence bundle requirements

Every executable multi-domain geospatial runtime SHOULD emit a `geospatial_runtime_evidence_bundle.v1` object.

The evidence bundle MUST include:

- `evidence_version`
- `evidence_id`
- `runtime_id`
- `runtime_class`
- standards references
- input manifest with SHA-256 hash
- output manifest with SHA-256 hash
- policy posture, including approval, sensitive-geospatial handling, network posture, and secret posture
- replay metadata

A runtime that cannot emit a replayable evidence bundle MUST mark replay mode as `not_replayable` and explain that limitation in its runtime-boundary document.

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

## Lattice Forge admission rule

A geospatial runtime may be admitted to Lattice Forge only after it has:

1. an executable entrypoint,
2. schema-bound inputs and outputs,
3. a validation command,
4. a sample fixture,
5. policy bundle reference,
6. evidence bundle definition,
7. replay semantics,
8. standards cross-reference to this file plus storage/knowledge/platform standards,
9. runtime candidate validation,
10. packaging, SBOM, signing, and rollback tests.

## Validation

This repository validates runtime profile and evidence bundle fixtures through:

```bash
make multidomain-geospatial-agent-validate
```
