# Personal Intelligence Cell: Second-Pass Aigents Audit

Status: draft addendum
Related standard: `docs/PERSONAL_INTELLIGENCE_CELL.md`
Related runtime lane: `SocioProphet/prophet-platform#384`

## Purpose

This addendum captures second-pass concepts from Aigents that were not fully represented in the initial Personal Intelligence Cell standard. These are not reasons to adopt Aigents as a dependency. They are product and standards lessons to absorb into the SocioProphet stack.

## Material omissions to fold into the standard

### 1. WatchPattern grammar deserves its own substandard

The initial standard listed `natural_language`, `boolean`, `semantic`, `regex`, `claim_template`, `graph_pattern`, and `policy_trigger` expression types. That is not precise enough.

Aigents' pattern system has a more extraction-oriented model:

- implicit phrase templates;
- multiple alternative templates per watched thing;
- slot variables prefixed with `$`;
- typed variables such as word, time, number, and money;
- lemma/alternative groups;
- ordered frames;
- nested hierarchical templates.

SocioProphet should define `WatchPattern` as a first-class object, not just a string field.

Required contract sketch:

```text
WatchPattern
  id
  watch_id
  source_scope
  pattern_kind: phrase | boolean | regex | semantic | typed_template | claim_template | graph_pattern | policy_trigger
  raw_expression
  normalized_expression
  alternatives[]
  variables[]
  frames[]
  extraction_schema_ref
  examples[]
  validation_fixtures[]
  version
```

```text
PatternVariable
  name
  type: word | text | time | date | number | money | entity | url | email | location | custom
  required
  constraints
  normalization
```

```text
PatternFrame
  order
  alternatives[]
  nested_frames[]
  variable_refs[]
```

This gives us deterministic extraction before escalating to LLM or embedding-based interpretation.

### 2. Relevance feedback needs explicit user actions

The first standard says the cell can receive feedback. Aigents has clearer user feedback primitives: follow relevant news, check/mark relevant items, and delete irrelevant items.

SocioProphet should standardize feedback as explicit events:

```text
FeedbackEvent
  id
  cell_id
  signal_id
  actor_ref
  action: follow | mark_relevant | mark_irrelevant | delete | mute_source | promote_source | refine_watch | share | save | dismiss
  reason
  policy_context
  learning_effect
  created_at
```

These events should train relevance, trust, source hygiene, watch tuning, and notification suppression.

### 3. Portable cell archive and migration are required

Aigents warns users to back up Sites, Things, News, Peer, and Self properties during public testing. The deeper lesson is that a personal intelligence cell must be portable, exportable, migratable, and recoverable.

SocioProphet should define:

- `CellArchive` export format;
- signed manifest;
- encrypted payload option;
- schema version;
- migration path;
- restore dry-run;
- redaction/export policy;
- user-readable inventory.

This belongs in SourceOS local-first work and Memory Mesh retention/migration policy.

### 4. ChannelAdapter lifecycle was under-specified

The initial standard mentioned feeds and channels, but not channel lifecycle. Aigents treats cells as reachable over HTTP, telnet, email, SMS, messengers, and peer-cell channels. We reject telnet and legacy unsecured control, but the concept of channel adapters is important.

Required object:

```text
ChannelAdapter
  id
  cell_id
  kind: local_ui | http_gateway | email | matrix | activitypub | rss | webhook | slack | discord | telegram | github | cli | neovim | turtleterm
  direction: inbound | outbound | bidirectional
  auth_profile_ref
  policy_ref
  rate_limit
  delivery_guarantee
  cleanup_policy
  failure_policy
  enabled
```

Every channel must be policy-gated and audit-logged.

### 5. Controlled language should become conformance machinery, not a product dependency

The first standard correctly rejected Aigents Language as our protocol, but it did not fully harvest the useful idea: every GUI action can compile into a declarative or interrogative statement.

SocioProphet should use this as a conformance property:

- every UI action compiles into `StructuredIntent`;
- every `StructuredIntent` can be rendered as readable text;
- every intent can be replayed against a cell test harness;
- every policy decision can cite the intent and evidence.

This gives us auditability, explainability, replay, and cross-surface parity across web, CLI, TurtleTerm, Neovim, and agents.

### 6. Social environment assessment is broader than people graph display

The first standard included peers, trust edges, followers, opinion leaders, and influence paths. It did not explicitly include social environment assessment over time.

SocioSphere should support:

- social environment snapshots;
- temporal drift of relationships;
- emerging communities;
- stale ties;
- attention sinks;
- source/person coupling;
- coordinated amplification detection;
- relationship hygiene recommendations;
- trust changes with provenance.

### 7. Reputation must be temporal and anti-manipulation aware

The first standard included reputation events, time decay, disputes, and policy effects. The Aigents reference corpus emphasizes reputation systems for human-computer environments, artificial societies, marketplaces, social engineering resistance, and temporal graph architecture.

We should add explicit anti-gaming controls:

- Sybil resistance hooks;
- collusion indicators;
- provenance weighting;
- context-bounded reputation;
- temporal decay models;
- review/dispute flows;
- reputation confidence intervals;
- separation of trust, authority, popularity, and expertise.

### 8. Business intelligence use cases should become fixtures

Aigents' use cases are concrete: weather/solar-flare alerts, real estate listings, low-cost local offers, competitor monitoring, legal/public-hearing monitoring, and political/journalistic monitoring.

SocioProphet should convert these into test fixtures for WatchPattern and Signal extraction:

- weather alert fixture;
- real estate listing fixture;
- market offer fixture;
- competitor release fixture;
- legal hearing fixture;
- public figure/political event fixture;
- GitHub/repo change fixture;
- standards/regulatory change fixture.

This prevents the cell service from becoming abstract architecture with no extraction proof.

### 9. Heterogeneous sources should include blockchain/payment rails as optional adapters

Aigents' current business framing mentions heterogeneous social and online media sources, blockchains, and payment systems. We should not make tokenized/blockchain behavior core, but the source/action model should leave clean extension points for ledger and payment events.

Optional adapter classes:

- blockchain event source;
- wallet or account activity source;
- payment rail event source;
- marketplace/reputation source;
- governance vote source.

These must be policy gated and disabled by default for personal cells.

### 10. Cell configuration should be explicit state

Aigents exposes cell self-configuration: name, internal data location, save frequency, network/email parameters, and self/peer properties.

SocioProphet should define `CellConfig`:

```text
CellConfig
  cell_id
  display_name
  data_location_policy
  save_frequency
  sync_policy
  backup_policy
  channel_defaults
  notification_defaults
  resource_budget_defaults
  local_first_mode
  enterprise_overlay_refs
```

This maps directly to SourceOS daemon behavior.

## Required follow-up changes

1. Add `WatchPattern`, `PatternVariable`, and `PatternFrame` to the normative schema lane.
2. Add `FeedbackEvent`, `CellArchive`, `ChannelAdapter`, and `CellConfig` to contract backlog.
3. Add temporal social environment assessment to SocioSphere mapping.
4. Add anti-manipulation reputation controls to reputation lane.
5. Add business/use-case fixtures to conformance tests.
6. Add optional ledger/payment source hooks, disabled by default and policy-gated.

## Revised minimum viable loop

The minimum useful loop should now be:

create cell -> configure cell -> add source -> add typed watch pattern -> ingest source item -> extract typed variables -> create signal -> score novelty/relevance/confidence/trust -> policy check -> emit feed item -> append intent event -> receive feedback event -> update watch/source/reputation state -> export archive.

## Non-goals reaffirmed

- No Aigents Java dependency.
- No Aigents Language as platform protocol.
- No telnet administration.
- No unsecured peer-cell communication.
- No legacy social adapters as first-class requirements.
- No blockchain/payment adapter enabled by default.
- No reputation score without provenance and context.
