# Archive-to-upstream mapping

## Spine mapping
- `SourceOS-main` (archive) -> **`sourceos-a2a-mcp-bootstrap`** for current bootstrap/bridge work; SourceOS capability/spec material remains conceptually canonical but the visible upstream repo in the org is currently `sourceos-a2a-mcp-bootstrap`.
- `sociosphere-main` (archive) -> **`sociosphere`** (current canonical workspace controller).
- `TriTRPC-main` (archive) -> **`TriTRPC`**.
- `socioprophet-standards-storage` + `socioprophet-standards-knowledge` (archive) -> retain as standards sources, but **`socioprophet-agent-standards`** now appears to be the consolidated normative profile for the current platform and AgentOS-facing rules.
- `tritfabric_repo_fresh` (archive) -> runtime/deployment intent likely lands in **`prophet-platform`** (plus any surviving dedicated runtime repo if retained later).
- `agentplane` (archive) -> **`agentplane`** (still canonical execution control plane).
- `global-devsecops-intelligence` (archive) -> either keep as an internal contract incubator or fold curated contracts into `prophet-platform` / `socioprophet-agent-standards` once license is explicit.
- `socios-main` (archive) -> keep optional until license ambiguity is resolved.

## Canonical-source decisions
- Capability packages: SourceOS-derived contract packages remain canonical; sociosphere mirrors/locks/validates them.
- Workspace composition + trust/policy validation: sociosphere.
- Platform runtime/service graph: prophet-platform.
- Normative profile, conformance, evidence, compatibility: socioprophet-agent-standards.
- Deterministic wire and fixtures: TriTRPC.
