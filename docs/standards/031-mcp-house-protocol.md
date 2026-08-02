# 031 — MCP House-Protocol Transport Standard

Status: Draft v0.1
Authority: `SocioProphet/socioprophet-agent-standards`
Related:
- `SocioProphet/TriTRPC` (`docs/AGENT_SANDBOX_TRANSPORT_PROFILE.md`, `spec/README-full-spec.md`, `tools/verify_agent_sandbox_transport.py`) — the house protocol
- `SocioProphet/socioprophet-standards-knowledge` (`docs/standards/044-agent-sandbox-lifecycle.md`) — canonical lifecycle semantics the transport profile carries
- `SocioProphet/prophet-core-catalog` (`tools/catalog_mcp_server.py`, `tools/verify_catalog_mcp_transport.py`, `docs/CATALOG-MCP.md`) — first conforming MCP surface
- `docs/standards/030-agent-catalog-connectivity.md` — the tool/MCP `connections` these surfaces are cataloged under

## Purpose

MCP (Model Context Protocol) surfaces are how agents in the estate call tools. A vanilla
MCP server speaks JSON-RPC 2.0 over stdio with untyped, un-digested, un-attested message
bodies. That is an **invisible-authority** gap: a tool request or result crossing an
agent boundary carries no bound media type, no content digest, no producer identity, and
no canonical form — so it cannot be verified, replayed, or governed.

This standard closes that gap. **Every MCP surface in the estate MUST ride the TriTRPC
transport profile.** The MCP tool contract (its named tools) is preserved; what changes
is that every request and response is carried as a **house-protocol typed blob**, not a
bare JSON-RPC body.

## The house protocol (normative carriage)

Per TriTRPC `docs/AGENT_SANDBOX_TRANSPORT_PROFILE.md`, an MCP surface's carried artifacts
MUST use:

- **Canonical JSON** — UTF-8, sorted object keys, no insignificant whitespace, exact
  enum strings. Any bytes that participate in a digest MUST be this canonical form.
- **Digest binding** — a `payload_digest` of the form `sha256:<lowercase-hex>` computed
  over the canonical payload byte string, bound in the envelope.
- **Typed media type** — `application/vnd.socioprophet.<type>+json;v=0`, distinct for
  request and result (e.g. `...catalog-query+json;v=0` / `...catalog-result+json;v=0`).
- **Typed blob envelope** binding: media type + payload digest + semantic schema ref +
  producer identity/attestation + parent ref.
- **Method naming** — request/response frames are method-named `<surface>.<tool>.REQ` /
  `<surface>.<tool>.RES` (the TriTRPC CLI `--method X.REQ` style).

Frame-codec note: reimplementing the ternary TriTRPC wire frame (TritPack243 / TLEB3 /
XChaCha20-Poly1305 AEAD) is NOT required of an MCP surface. Conformance is to the
canonical-JSON + digest + media-type + typed-envelope + method-naming **transport
profile**. Where a surface does not bind the ternary frame codec, it MUST document the
frame-binding seam (which envelope field maps to which frame slot) so the binding can be
added without redesign.

## Invariants (fail-closed)

- **INV-MCP-1 (no vanilla MCP):** an MCP surface MUST NOT expose tools over vanilla
  JSON-RPC 2.0 / stdio without a house-protocol carriage. A tool request or result that
  is not a house-protocol typed blob MUST be rejected, not served.
- **INV-MCP-2 (unbound payload rejected):** a request or response whose payload is not
  canonical JSON, or whose `sha256:` `payload_digest` does not match the canonical
  payload bytes, or which is missing a required envelope field (media type, digest,
  semantic schema ref, producer, method), MUST be rejected. An undigested or unbound
  payload is never a valid MCP message.
- **INV-MCP-3 (conformance verifier required):** every MCP surface MUST ship a
  conformance verifier that mirrors TriTRPC's `verify_*` tools and has **teeth both
  ways** — it MUST accept a known-good frame AND reject a tampered frame (digest
  mismatch, wrong media type, non-canonical payload, missing envelope field). The
  verifier MUST be wired into that surface's `validate` / CI gate, so a non-conforming
  frame fails the build rather than reaching an agent.

## Conformance criteria

An MCP surface conforms to this standard when:

1. Its request/response frames carry the typed envelope and method naming above.
2. Its payload digests are `sha256` over canonical JSON, and mismatches are rejected.
3. It declares its media types (`application/vnd.socioprophet.<type>+json;v=0`).
4. It documents the frame-binding seam to the TriTRPC wire frame.
5. It ships a teeth-both-ways conformance verifier wired into `validate`/CI, with
   committed good AND tampered fixtures.
6. It references this standard (`standard_ref`) per `030-agent-catalog-connectivity.md`,
   so the MCP tool is a cataloged, governable asset.

## Reference implementation

`SocioProphet/prophet-core-catalog` is the first conforming surface:

- server: `tools/catalog_mcp_server.py` — media types
  `application/vnd.socioprophet.catalog-query+json;v=0` /
  `application/vnd.socioprophet.catalog-result+json;v=0`, methods
  `catalog.<tool>.REQ` / `catalog.<tool>.RES` for
  `define · who_uses · blast_radius · search · stats · dataset`;
- verifier: `tools/verify_catalog_mcp_transport.py` (teeth both ways), wired into
  `make validate`;
- binding doc + frame seam: `docs/CATALOG-MCP.md`.

## Enforcement

This standard is cataloged by `prophet-core-catalog` `ds.rules-policies`. New MCP
surfaces are surfaced as governance gaps until they declare a `standard_ref` to `031`
and ship a wired conformance verifier (INV-MCP-3). All MCP must use the house protocol.
