# Control Gating Graduation Profile 0001

Status: draft normative profile.

This profile defines three required layers for SocioProphet agents:

1. Control layer — how an agent chooses actions.
2. Gating layer — what must be satisfied before an action executes.
3. Graduation layer — how an agent is promoted across maturity stages.

## Control families

Every agent should declare one or more control families:
- value based
- policy based
- actor critic
- imitation bootstrapped
- goal conditioned
- model based planner
- constrained safe
- hierarchical options
- formal policy constrained

## Gate classes

Every action should classify gates as:
- hard gate
- soft advisory
- graduation gate

Core gate families should include authorization, scope, policy, risk, evidence, uncertainty, budget, safety, approval, and rollback.

## Graduation lanes

Every production-facing agent should be graded across at least:
- capability
- safety policy
- reliability recovery
- observability auditability
- provenance reproducibility
- efficiency budget
- human oversight acceptability

## Ray lifecycle note

When an agent participates in Ray-based training, tuning, benchmarking, or serving, the same control, gate, and graduation vocabulary should apply across the full lifecycle.
