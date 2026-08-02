# 030 — Agent Catalog Connectivity Standard

Status: Draft v0.1
Authority: `SocioProphet/socioprophet-agent-standards`
Related: `SocioProphet/prophet-core-catalog` (`ds.agents-manifests`, `docs/ASSET-CATALOG-PROGRAM.md`), `SocioProphet/agentplane`, `SocioProphet/agent-registry`

## Purpose

The agent catalog (`ds.agents-manifests`) MUST be a **connected graph**, not a flat list. An
agent is only governable when the assets it depends on and the systems that admit it are traceable
from its catalog record. This standard makes that connectivity a normative requirement and closes
the "invisible authority" gap for agents.

## Normative connectivity requirements

Every agent record in `ds.agents-manifests` MUST carry a `connections` object linking the agent to
the agent-substrate assets it uses:

- **skills** — the skills it can invoke (`.claude/skills/**`, `SKILL.md`, plugin skills).
- **tools** — the tools/MCP servers it may call (tool schemas, function/tool declarations).
- **prompts** — the system prompts / prompt templates / blueprint prompt fields it runs under.
- **preferences** — the settings and directives that shape it (`settings.json`, `CLAUDE.md`, keybindings, behavior prefs).
- **personas** — the persona(s) it adopts (persona definitions, ProCybernetica `AgentCoordinateVector` / sefirot persona vectors, persona-chooser configs).

Where a connected asset is itself cataloged (e.g. a tool contract in `ds.schemas-contracts`), the
connection MUST reference that catalog id rather than duplicating it.

## Substrate binding requirements

Every agent record MUST bind to the three agent-substrate systems:

- **agent-plane** (`SocioProphet/agentplane`): `agent_plane_ref` — the plane/adapter the agent runs on.
- **agent-registry** (`SocioProphet/agent-registry`): `registry_ref` — the agent's manifest-admission entry.
- **agent-standards** (`SocioProphet/socioprophet-agent-standards`): `standard_ref` — the standard/profile the agent conforms to.

## Invariants (fail-closed)

- **INV-ACC-1 (no invisible agent authority):** an agent with declared capabilities but no
  resolvable `registry_ref` MUST be surfaced as a gap; capabilities without a registry entry are not
  authorized. Mirrors the estate's `no-invisible-authority` invariant.
- **INV-ACC-2 (declared before connected):** a `connections` reference that does not resolve to a
  real asset MUST fail catalog validation rather than pass silently.
- **INV-ACC-3 (freshness):** the connectivity graph MUST be maintained by the catalog contribution
  loop (`loop.catalog-contribution` in `ds.feedback-loops`) — updated on each merge to main, not
  hand-curated once.
- **INV-ACC-4 (no orphan standard):** an agent claiming conformance MUST reference a `standard_ref`
  that exists in this repo; an unresolvable `standard_ref` is a gap.

## Enforcement

`ds.agents-manifests` records the graph; the catalog's fail-closed validator enforces INV-ACC-2.
INV-ACC-1 / INV-ACC-4 gap sets are surfaced in the dataset README (`unregistered / unstandardized
agents`). This standard is itself cataloged by `ds.rules-policies` and its lifecycle is governed per
`ds.feedback-loops` (`life.pattern-policy-vocab`).
