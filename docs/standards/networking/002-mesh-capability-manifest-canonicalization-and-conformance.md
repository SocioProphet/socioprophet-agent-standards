# Mesh Capability Manifest Canonicalization and Conformance

## Status

Draft.

## Purpose

Define how a mesh capability manifest is serialized, hashed, signed, and consumed so that producers and consumers evaluate the same bytes and arrive at the same verdict.

This document is a companion to:
- `networking/001-mesh-capability-manifest-standard.md`
- `schemas/capability-manifest.schema.json`

## Canonicalization profile

### 1. Input form

The producer starts from a JSON document that validates against `schemas/capability-manifest.schema.json`.

### 2. Detached signature model

The canonical byte sequence MUST be derived from the manifest with the `signatures` field removed.

Rationale:
- including signatures inside the signed payload creates recursive ambiguity
- detached signatures allow multiple signatures over the same canonical payload

### 3. Canonical JSON

The signature payload MUST be canonicalized as follows:
- UTF-8 encoding
- object keys sorted lexicographically by Unicode code point
- no insignificant whitespace
- arrays preserved in declared order
- numbers rendered in JSON canonical minimal form
- booleans and null rendered in standard lowercase JSON form

Consumers MUST reject manifests when they cannot reproduce the same canonical byte sequence deterministically.

### 4. Hashing

The canonical payload hash for this profile is:
- SHA-256 over the canonical UTF-8 byte sequence

The resulting digest is the `manifest digest` for audit, cache, and replay purposes.

### 5. Signature envelope

Each signature entry in `signatures[]` signs the canonical payload bytes, not the raw JSON source text.

Producers SHOULD include a stable `key_id` that lets consumers locate the corresponding public key without guessing.

### 6. Time validity

If `constraints.not_before` or `constraints.not_after` are present, consumers MUST evaluate them against their current trusted time source.

Consumers MUST reject manifests that are not yet valid or already expired unless their local policy explicitly supports grace handling.

## Consumer conformance rules

A consumer is conformant with this profile only if it performs all of the following checks.

### Required checks

1. schema validation succeeds
2. canonicalization succeeds deterministically
3. SHA-256 digest is computed over the canonical payload
4. at least one signature validates against an authorized key
5. any time validity constraints pass
6. revocation state is checked when revocation information is available
7. role, transport, and path-template values are interpreted strictly from the declared vocabulary

### Required failure posture

Consumers MUST fail closed for:
- schema-invalid manifests
- canonicalization failure
- signature failure
- expired or not-yet-valid manifests
- vocabulary values outside the declared schema

Consumers SHOULD return an explicit `INCONCLUSIVE` verdict instead of `VALID` when:
- revocation status cannot be checked
- trusted time is unavailable
- the signing key cannot be authorized conclusively

## Producer guidance

Producers SHOULD:
- emit stable field ordering before canonicalization even though consumers re-canonicalize
- avoid semantically duplicate entries in arrays such as `roles`, `transports`, and `path_templates`
- issue manifests with bounded validity windows when used for dynamic network roles such as exit or bridge
- rotate signatures without changing the canonical payload when only the signer set changes

## Relationship to Linux realization

Linux realization code such as `source-os` MAY materialize manifests into `/etc/sourceos/mesh/manifest.json`, but runtime consumers MUST still canonicalize and verify before trusting advertised roles or path-template permissions.

## Minimum conformance statement

An implementation claiming `mesh-capability-manifest-consumer/v0` conformance MUST:
- validate against the schema
- canonicalize using this profile
- compute the SHA-256 digest of the canonical payload
- verify at least one authorized signature
- fail closed or return `INCONCLUSIVE` according to the rules above

## Follow-on work

Future revisions should define:
- allowed signature algorithms and key formats
- revocation transport and freshness semantics
- transparency log or replay-ledger integration
- stronger multi-signature policy profiles for high-trust roles such as exits and introducers
