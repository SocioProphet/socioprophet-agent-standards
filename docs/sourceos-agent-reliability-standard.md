# SourceOS Agent Reliability Standard

## Status

Draft v0.1. This standard defines the clean-room SocioProphet/SourceOS profile for reliable agentic work across code, runtime, models, memory, infrastructure, browser automation, external communications, and human governance.

This is not a fork or derivative of any external standard. It is the normative standard that our repos should implement through AgentPlane, guardrail-fabric, PolicyFabric, MemoryMesh, SocioSphere, SourceOS developer tooling, TurtleTerm, and Neovim integration.

## Core principle

An AI agent is not reliable because it produces plausible text. An AI agent is reliable when its actions are bounded by policy, its work is evidenced, its failures are recoverable, its authority is explicit, its memory is governed, and its completion claims are independently verifiable.

## Non-negotiables

1. Local-first control: policy, session logs, and evidence must function without a required cloud service.
2. Deterministic guardrails: high-risk enforcement must not depend on a model call.
3. Evidence-forward execution: every meaningful action must be reconstructable from receipts, logs, or artifacts.
4. Completion gates: agents may not claim done without satisfying explicit repo/runtime gates.
5. Human authority: external publication, production mutation, privilege escalation, and policy weakening require human authority.
6. Anti-tamper: agents may not disable, weaken, hide, or delete their own controls.
7. Memory governance: durable learnings must become reviewable repo/project/org knowledge, not untraceable chat residue.
8. Fail-informatively: failures must preserve context, support remediation, and improve future controls.
9. Open trust posture: the platform must be understandable, inspectable, and auditable.
10. Clean-room implementation: do not vendor or depend on restricted-license control-plane code for the core standard.

## Reliability maturity levels

### L0: Manual assistance

The agent produces advice or code snippets but does not operate inside a controlled execution environment.

Required controls:

- Human manually executes changes.
- No autonomous tool mutation.
- No reliability claim beyond advisory support.

### L1: Local policy hooks

The agent uses tools, but tool calls are intercepted by deterministic local policy.

Required controls:

- Shared policy decision ABI.
- Local decision log.
- Baseline command, file, Git, secret, environment, and package policies.
- Human-readable remediation for denials.

### L2: Repo completion gates

The agent operates inside a repo and must satisfy completion gates.

Required controls:

- Non-protected branch or explicit signed override.
- Committed work.
- Pushed branch.
- PR or documented no-PR exception.
- Tests/CI status evidence.
- Task summary and changed-file summary.
- No unresolved critical guardrail denials.

### L3: Observed sessions

The agent session is inspectable and replayable enough for review.

Required controls:

- Session transcript or event stream.
- Tool event log.
- Policy decision log.
- Redaction evidence.
- Artifact export.
- Local session monitor.

### L4: Durable runtime

Agent work runs through a durable state machine rather than ad hoc sessions.

Required controls:

- State lifecycle with queued, leased, running, succeeded, failed, retry scheduled, requeued, pruned, quarantined, waiting for human, waiting for resource, superseded, and reconciled states.
- Durable control signals.
- Idempotent retries.
- Node/tool/provider/risk-class retry policy.
- Fanout/join semantics.
- Scheduling and cancellation.

### L5: Governed memory and model routing

The agent uses governed memory and governed model access.

Required controls:

- Repo-local playbooks.
- Memory provenance.
- Human-reviewable durable learnings.
- Provider routing policy.
- Prompt/output redaction.
- Cost, latency, region, provider, and model evidence.
- Local model fallback where appropriate.

### L6: Enterprise cybernetic control

The system operates as a full control plane across users, repos, devices, agents, models, memory, and runtime.

Required controls:

- Enterprise/org/repo/user/local policy inheritance.
- Signed break-glass overrides.
- Audit export.
- SIEM/OpenTelemetry/event-stream integration.
- Human approval queues.
- Reliability scorecards.
- Incident mode.
- Continuous evaluation and control-loop improvement.

## Control surfaces

### Agent workspaces

A reliable agent must operate inside a bounded workcell with explicit repo, branch, task, executor, policy, and runtime identity.

Required evidence:

- workspace ID
- repo
- base ref
- working branch
- task prompt digest
- executor profile
- environment profile
- policy profile
- session ID
- artifact directory

### Tool calls

Every tool call should be normalized into a policy context before execution and an event after execution.

Minimum context:

- event type
- tool name
- action class
- input digest
- redacted input summary
- cwd or workspace ID
- repo/branch/commit where applicable
- session ID
- agent identity
- policy scope

### Policy decisions

The standard policy decision values are:

- `allow`
- `allow_with_context`
- `instruct`
- `deny`
- `redact`
- `escalate`
- `quarantine`
- `defer`

Every non-allow decision must include a reason and remediation. High-risk allow decisions should also be logged.

### Human approval

Human approval must be explicit, scoped, expiring, and evidenced.

Required approval fields:

- approver identity
- approval time
- expiration
- allowed action class
- allowed resource
- reason
- related policy decision
- related task/session
- resulting artifact or PR

### External action

Public posting, account-affecting browser automation, email sending, issue comments, PR comments, documentation publishing, package publishing, and infrastructure mutation are external actions.

Default rule: read and draft are separable from publish. Agents may draft; publication requires explicit authority unless a policy profile grants a narrow exception.

Recommended handoff pattern:

1. Agent writes draft artifact.
2. Agent commits draft on a fresh branch.
3. Agent opens PR or review artifact.
4. Human reviews and publishes.
5. Posted result is logged separately after human confirmation.

### Runtime state

AgentPlane-compatible systems should model more than pending/running/done.

Required terminal states:

- succeeded
- failed
- pruned
- quarantined
- superseded
- cancelled
- reconciled

Required waiting states:

- queued
- leased
- running
- retry_scheduled
- requeued
- waiting_for_human
- waiting_for_resource

### Memory updates

Agents may identify durable operational learnings. They may not silently mutate governance memory.

Memory update controls:

- Proposed learning must be written as a diff or artifact.
- The destination scope must be explicit: repo, project, user, org, enterprise.
- Conflicting playbook entries must be reconciled, not duplicated.
- High-impact playbook updates require human review.
- Memory update evidence must include source session and reason.

## Metrics catalog

Required platform metrics:

- task completion rate
- false-done rate
- time to PR
- time to green CI
- rework rate
- policy denial rate
- policy false-positive rate
- human override rate
- unresolved critical denial count
- secret exposure near-miss rate
- dangerous command attempt rate
- package/infrastructure mutation rate
- model cost per completed task
- model route failure rate
- redaction event rate
- memory update acceptance rate
- replay success rate
- control-loop latency
- audit completeness

## Scorecard

A repo is agent-ready when:

- It has a repo-local operating contract.
- It declares policy profile and runtime profile.
- It has test/check commands discoverable by agents.
- It has completion gates.
- It emits evidence artifacts.
- It blocks protected branch mutation.
- It blocks secret leakage.
- It supports local session review.
- It can export an audit bundle.

## Role model

Recommended operating roles:

- Agent Operator: initiates or supervises agent tasks.
- Policy Steward: owns policy packs and inheritance.
- Runtime Steward: owns execution environments and state-machine reliability.
- Memory Steward: reviews durable learnings and playbook updates.
- Model Gateway Steward: owns provider routing, budgets, and egress controls.
- Human Approver: grants scoped exceptions and publication authority.
- Incident Commander: coordinates agent-related incidents and postmortems.

## Conformance profiles

### Developer local profile

- Local policy hooks.
- Local logs.
- Repo stop gates.
- Manual PR review.

### Team repo profile

- Shared repo policies.
- CI-required stop gates.
- PR-required external action drafts.
- Local session export.

### Enterprise profile

- Org/enterprise inheritance.
- Signed policy packs.
- Break-glass approvals.
- SIEM/export hooks.
- Provider egress controls.
- Incident mode.

### Air-gapped profile

- No required telemetry.
- No external provider calls unless explicitly configured.
- Local model fallback.
- Offline audit export.
- Local package/cache controls.

## Implementation ownership

- guardrail-fabric: policy decision ABI, policy packs, simulation, redaction, hooks, fail-closed enforcement.
- AgentPlane: workcells, state machine, runtime events, stop gates, evidence artifacts, replay.
- PolicyFabric: inheritance, signed policies, enterprise profiles, break-glass governance.
- MemoryMesh: durable learnings, provenance, memory scopes, playbook reconciliation.
- SocioSphere: governance console, approval queues, scorecards, audit review.
- SourceOS/TurtleTerm/Neovim: local developer UX, terminal-native review, policy explanations, session monitor.

## Initial compliance checklist

- [ ] Policy Decision ABI exists and has schema tests.
- [ ] Local JSONL decision log exists.
- [ ] Baseline policy pack blocks high-risk shell/Git/secret/package actions.
- [ ] Agent hook adapter exists for at least one agent client.
- [ ] AgentPlane can ingest policy decisions as evidence.
- [ ] Stop gates block false-done completion.
- [ ] Repo-local operating contract template exists.
- [ ] External action draft-through-review pattern exists.
- [ ] Model route decision artifact exists.
- [ ] Local session monitor can inspect tool calls and policy decisions.

## Definition of world-class

A world-class agent reliability platform does not merely prevent bad commands. It closes the loop: it observes, decides, acts, records, evaluates, learns, updates its operating contract, and proves completion. SourceOS must make this loop visible, local-first, policy-bound, and governable at human and enterprise scale.
