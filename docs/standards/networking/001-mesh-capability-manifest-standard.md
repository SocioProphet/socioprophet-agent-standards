# Mesh Capability Manifest Standard

## Status

Draft.

## Purpose

Define a canonical manifest shape for nodes that participate in the mesh under the SourceOS / AgentPlane ecosystem.

The manifest describes:
- node identity binding
- advertised roles such as peer, relay, exit, bridge, or introducer
- supported transports
- supported path templates
- local constraints such as jurisdiction, operator, or full-tunnel permission
- issuance and revocation state
- attached signatures

## Canonical schema

The normative JSON Schema for this draft lives at:
- `schemas/capability-manifest.schema.json`

## Placement rule

This standard belongs in the shared standards repository because it defines reusable vocabulary and interchange shape.

Implementation repositories such as `SociOS-Linux/source-os` may realize Linux-facing behavior that consumes the manifest, but they should not become the canonical home for the schema itself.

## Relationship to Linux realization

Typical Linux consumers of this manifest will use it to gate:
- whether a node may advertise relay or exit roles
- which path templates may be selected
- whether anonymous ingress is allowed
- whether full-tunnel exit behavior is permitted

## Follow-on work

Future revisions should tighten:
- signature algorithm profile
- canonical serialization and hashing rules
- revocation propagation semantics
- conformance criteria for consumers
