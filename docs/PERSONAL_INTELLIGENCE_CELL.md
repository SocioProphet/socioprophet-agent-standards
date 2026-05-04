# Personal Intelligence Cell Standard

Status: draft normative standard
Owner: SocioProphet agent standards
Scope: AgentPlane-compatible personal, project, community, and organization intelligence cells

## Purpose

A Personal Intelligence Cell is the smallest governed unit of durable agency in the SocioProphet estate. It binds identity, memory, source watching, social awareness, reputation, policy, action permissions, and exportable feeds into one auditable runtime object.

This standard captures the useful conceptual lessons from Aigents without adopting Aigents as a runtime dependency. Aigents' valuable prior art is the notion of an individual trainable software agent that searches the web for a user, shares results privately or in communities, evaluates relevance with collective intelligence, and runs as a cell connected to humans and peer agents over multiple communication channels.

SocioProphet generalizes that into a governed, local-first, policy-aware intelligence cell.

## Decision

We will not integrate Aigents Java, Aigents Language, telnet access, or legacy social-network adapters as core dependencies.

We will reuse the conceptual model:

- one cell per human, project, community, organization, or bounded mission;
- watch patterns over sources;
- private precise feeds;
- social and peer-aware relevance;
- collective-intelligence feedback;
- reputation for people, agents, sources, claims, models, and workflows;
- readable action logs;
- multi-channel access;
- resource-bounded cognition.

## Primitive

A Personal Intelligence Cell MUST include these state domains:

1. Identity binding
   - human, project, community, organization, or mission owner;
   - delegated agent identities;
   - authority scope and revocation state.

2. Watch graph
   - watched sources;
   - watched topics;
   - semantic patterns;
   - structured claim templates;
   - graph patterns;
   - policy-conditioned triggers.

3. Source graph
   - source identity;
   - source type;
   - crawl or subscription mode;
   - trust score;
   - provenance requirements;
   - rate limits and resource budgets.

4. Signal ledger
   - observed item;
   - extracted entities;
   - extracted claims;
   - supporting evidence;
   - confidence;
   - novelty;
   - relevance;
   - policy status;
   - downstream actions.

5. Social graph
   - peers;
   - communities;
   - followers;
   - opinion leaders;
   - trust edges;
   - similarity edges;
   - influence paths;
   - collaboration context.

6. Reputation graph
   - reputation subject: human, agent, source, model, workflow, community, or claim;
   - context;
   - evidence;
   - time decay;
   - dispute state;
   - policy effect.

7. Memory surface
   - user preferences;
   - accepted/rejected signals;
   - durable interests;
   - temporary campaigns;
   - prior actions;
   - learned relevance profiles;
   - retention policy.

8. Policy envelope
   - observation permissions;
   - memory permissions;
   - sharing permissions;
   - publication permissions;
   - action permissions;
   - enterprise overlays;
   - audit requirements.

9. Action log
   - user intent;
   - agent interpretation;
   - policy checks;
   - tool calls;
   - emitted events;
   - generated feeds;
   - notifications;
   - reversibility markers.

10. Feed exports
    - private feed;
    - project feed;
    - community feed;
    - RSS-compatible feed;
    - ActivityPub-compatible feed;
    - webhook stream;
    - email digest;
    - Matrix/room stream;
    - GitHub issue/PR stream where appropriate.

## Contract shape

A conforming cell SHOULD expose these logical resources, independent of transport:

```text
Cell
  id
  owner_ref
  kind: personal | project | community | organization | mission
  policy_ref
  memory_ref
  created_at
  updated_at

Watch
  id
  cell_id
  expression
  expression_type: natural_language | boolean | semantic | regex | claim_template | graph_pattern | policy_trigger
  source_scope
  relevance_policy
  notification_policy
  resource_budget
  state

Source
  id
  kind: web | rss | repo | document | social | mail | chat | local_fs | api | sensor | manual
  uri
  trust_profile
  crawl_profile
  provenance_profile
  policy_ref

Signal
  id
  cell_id
  source_id
  watch_id
  observed_at
  title
  summary
  entities
  claims
  evidence_refs
  novelty_score
  relevance_score
  confidence_score
  reputation_effects
  policy_status

Peer
  id
  cell_id
  peer_ref
  kind: human | agent | community | organization
  trust_scope
  memory_scope
  delegation_scope
  revocation_state

ReputationEvent
  id
  subject_ref
  subject_kind: human | agent | source | model | workflow | community | claim
  context
  evidence_refs
  delta
  decay_policy
  dispute_state
  policy_effect

IntentEvent
  id
  cell_id
  actor_ref
  intent_text
  structured_intent
  policy_decision
  tool_calls
  emitted_events
  reversibility
```

## Control loops

Every cell MUST support explicit cybernetic loops:

1. Observe
   - ingest source changes;
   - normalize evidence;
   - preserve provenance.

2. Orient
   - classify entities, claims, risks, and opportunities;
   - compare against watch patterns;
   - compute novelty, relevance, confidence, and trust.

3. Decide
   - evaluate policy;
   - select notification, feed, memory, sharing, or action path;
   - honor resource and interruption budgets.

4. Act
   - emit feed item;
   - notify user or peer;
   - update memory;
   - open issue or task;
   - request review;
   - execute delegated action only when policy permits.

5. Learn
   - consume feedback;
   - adjust watch patterns;
   - update source trust;
   - update reputation;
   - prune stale memory;
   - reduce noise.

## Resource-bounded cognition

A conforming cell MUST budget:

- compute;
- storage;
- network calls;
- model calls;
- crawl frequency;
- notification frequency;
- memory retention;
- action risk;
- enterprise policy exposure.

A cell that cannot explain its resource budget is not conforming.

## Product surface

The default user-facing abstraction SHOULD avoid technical internals. The clean product objects are:

- My Cells
- My Watches
- My Sources
- My Signals
- My People
- My Communities
- My Trust
- My Feeds
- My Actions
- My Policies

This replaces leaky user-facing terminology such as embeddings, vector stores, model routers, execution services, or crawl daemons.

## SocioProphet estate mapping

- AgentPlane: cell runtime, lifecycle, peer-agent orchestration, transport adapters.
- Memory Mesh: memory state, watch history, learned relevance, embeddings, graph state, retention.
- PolicyFabric / Guardrail Fabric: permission envelopes, action constraints, enterprise overlays, audit gates.
- SocioSphere: people graph, communities, influence maps, collaboration context, relationship hygiene.
- HolographMe: human identity, digital twin, consent, delegation, representation, reputation surface.
- Lampstand: local search/indexing, evidence extraction, retrieval, provenance, source monitoring.
- Prophet Platform: runtime deployment, contracts, API surface, evaluation fabric, observability.
- SourceOS: local-first daemon, encrypted local state, offline queue, OS integration.
- TurtleTerm / Neovim / cloudfog-shell: operator surface for power users and developers.

## Implementation lanes

Lane 1: normative schema
- add cell, watch, source, signal, peer, reputation, and intent contracts;
- define JSON Schema and OpenAPI/TriTRPC bindings;
- define conformance tests.

Lane 2: runtime skeleton
- add a minimal `cell-service` to prophet-platform;
- expose health, create cell, list watches, create watch, ingest signal, emit feed item;
- persist control-plane state in Postgres;
- emit analytical facts to ClickHouse where evaluation fabric already expects profile-score-like outputs.

Lane 3: Lampstand integration
- use Lampstand as the first bounded source/index adapter;
- map indexed documents and search results into Source and Signal records;
- preserve evidence and provenance.

Lane 4: policy integration
- gate every observe, remember, share, publish, and act event through policy;
- log every policy decision into IntentEvent.

Lane 5: social and reputation layer
- add peer graph and reputation events;
- support trusted-peer feedback into relevance scoring;
- expose relationship/source hygiene recommendations.

Lane 6: feed exports
- private feed first;
- RSS-compatible export second;
- webhook and GitHub issue streams third;
- Matrix/ActivityPub later.

Lane 7: product surface
- SocioSphere portal pages for Watches, Sources, Signals, People Graph, Trust Graph, Feeds, and Actions;
- operator commands for TurtleTerm/Neovim/cloudfog-shell.

## Acceptance criteria

A first useful implementation is complete when:

- a user can create a cell;
- a user can add at least one source and one watch pattern;
- the system can ingest an item from the source;
- the system can produce a Signal with evidence and provenance;
- the system can score novelty, relevance, confidence, and source trust;
- the system can pass the Signal through policy;
- the system can export the Signal to a private feed;
- the system records an IntentEvent and policy decision;
- the system can receive user feedback and update the watch/relevance profile;
- all runtime behavior is covered by validation and smoke tests.

## Non-goals

- Do not preserve Aigents Language as a user-facing or internal protocol.
- Do not expose telnet-style administration.
- Do not depend on legacy social-network connectors.
- Do not build a generic crawler before proving the cell/watch/signal/feed loop.
- Do not allow agents to share memory or signals without explicit policy.

## References

- Aigents mission and project overview: https://aigents.com/
- Aigents help: https://aigents.com/en/help.html
- Aigents welcome/product framing: https://aigents.com/en/welcome.html
- Aigents architecture paper: https://aigents.com/papers/2017/ArchitectureOfAgentWithSocialAwarenessBICA2017.pdf
- Aigents executive summary: https://aigents.com/papers/aigents-summary.pdf
