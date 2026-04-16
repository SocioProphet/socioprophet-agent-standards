# Spine Integration Guardrails (v0.1)

This pack captures **guardrails** implied by the current “spine” repositories so we can integrate tools
without violating our standards or accidentally creating irreversible coupling.

## 1) Spine repos and their roles (canonical)

| Repo | Role | What must stay stable | What is allowed to change fast |
|---|---|---|---|
| SourceOS | **L0 OS substrate** | doctor/surfaces/volumes/profile invariants | tooling containers, opt-in UX, packaging mechanics |
| sociosphere | **L1 workspace controller** | manifest+lock composition and directionality rules | UI workbench + adapter inventory |
| TriTRPC | **L1 wire protocol** | fixtures + byte-equality invariants | helper tools, docs, ports |
| socioprophet-standards-storage | **L1 standards** | normative RFC2119 constraints | benchmarks/workloads, examples |
| socioprophet-standards-knowledge | **L1 standards** | normative bindings + schema/context IDs | examples, workloads, non-normative commentary |
| agentplane | **L2 control plane** | bundle schema + evidence lifecycle | executor backends, fleet inventory |
| tritfabric | **L2 training/runtime** | opt-in model + contract-first surfaces | backends (Ray, etc.), internal modules |
| global-devsecops-intelligence | **L1 contract skeleton** | event envelope + mapping DSL schemas | modules and adapters |

### Directionality (do-not-violate)
- **sociosphere → TriTRPC** allowed; **TriTRPC → sociosphere** forbidden.
- Standards repos can *reference* TriTRPC by commit/tag, but **TriTRPC must not import standards**.
- SourceOS should not depend on heavy runtimes by default. Runtimes are opt-in and preferably per-user.

## 2) Core invariants we keep repeating (because history is cruel)

### 2.1 Deterministic transport (TriTRPC)
- Byte equality against fixtures is the main gate.
- AEAD AAD definition must match fixtures.
- Canonical JSON hashing uses **RFC 8785 (JCS)** and BLAKE3 when required by receipts.

### 2.2 Contract-first capability packaging (SourceOS caps/)
- “Contract-only” packages define:
  - triRPC method surface
  - schemas
  - topic taxonomy
  - policy guard vocabulary
- Implementations live elsewhere and must:
  - default deny
  - emit evidence/audit events
  - never leak forbidden content in explain/debug surfaces

### 2.3 Opt-in by default (SourceOS + TritFabric)
- No background services or listeners on first install.
- Prefer UDS (unix domain sockets) over TCP.
- Explicit UX acknowledgement for enabling anything that touches user data or the network.

### 2.4 Local-first + rootless user-space
- Immutable base OS (Silverblue/Atomic Desktop pattern).
- Tooling and dependencies in containers/toolboxes.
- Keep host clean: no system-wide pip installs (doctor rule).

## 3) What “safe to integrate” means in practice

A component is “safe to integrate” into the spine when:

1) **It has a task contract** (`make validate` at minimum).
2) **Its license is compatible with our lane**:
   - Lane **core**: MIT/Apache-2.0/BSD-2/3 (permissive) only.
   - Lane **optional**: can include copyleft or missing-license components, but must be isolated and removable.
3) **It’s behind an adapter boundary**:
   - We never call a tool directly from everywhere.
   - We call an interface (Executor, BrowserOps, MemoryAPI, etc.).
4) **It cannot silently run**:
   - opt-in token or explicit enablement
   - telemetry and evidence emission
5) **It does not violate SourceOS volume policy**:
   - No executing out of Downloads (noexec).
   - Secrets stay in Secrets volume, encrypted.

## 4) Known drift risk we must resolve early

### 4.1 semantic-search-bi contract drift
Archive shows **two different declarations** of semantic-search capability:
- SourceOS has a complete contract package (rpc/schemas/topics/tools).
- sociosphere has only a capd YAML with a different, expanded surface.

**Policy:** pick one canonical contract package and make the other a generated mirror, not a second source of truth.

### 4.2 Missing licenses
- sociosphere-main: LICENSE missing in archive.
- global-devsecops-intelligence: LICENSE missing in archive.

**Policy:** treat as internal-only until a LICENSE is added and affirmed.

### 4.3 socios repo license conflict
socios-main contains both MIT and GPL-3.0 license texts.

**Policy:** resolve to a single declared license (or an explicit dual-license statement) before we ship or link it into permissive code.

## 5) 90-day integration order (no distribution required)

### Phase A (Days 1–14): hygiene + gates
- Add validate targets to repos missing task contracts.
- Add a workspace “spine validate” command (runner wrapper).
- Add license + hygiene gates to CI (fail on .DS_Store, missing LICENSE in core lane, etc.).
- Decide canonical semantic-search contract package.

### Phase B (Days 15–45): bring up the control plane
- Materialize spine repos in sociosphere workspace.
- Ensure TriTRPC fixtures pass on Linux toolboxes.
- Wire agentplane to use TriTRPC envelopes for all internal RPC surfaces.
- Establish evidence artifact directory under SourceOS Projects volume.

### Phase C (Days 46–90): integrate third-party tools *as replaceable adapters*
- CompletionService (Tabby), BrowserOps (Stagehand), Memory (Mem0), Executor (OpenCode), ProcessSpine (AIWG).
- Each adapter gets:
  - a minimal triRPC surface
  - policy guard + evidence events
  - a local integration test in the workspace harness
- For any non-permissive or missing-license tool: run it as a separate service with a strict RPC boundary and a replacement plan.
