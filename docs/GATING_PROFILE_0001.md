# Gating Profile 0001

Status: draft normative profile for policy gates and gate activations.

## Purpose

This profile defines how SocioProphet agents describe **what they are allowed to do** and which gates must activate before an action is executed.

## Gate classes

Every action profile SHOULD classify gates into three classes:
- `hard_gate` — blocks execution when unsatisfied
- `soft_gate` — influences ranking, clarification, or escalation
- `graduation_gate` — controls whether an agent class may be promoted to a higher maturity level

## Core gate families

Agents SHOULD support these gate families where applicable:
- `authorization_gate`
- `scope_gate`
- `policy_gate`
- `risk_gate`
- `evidence_gate`
- `uncertainty_gate`
- `budget_gate`
- `safety_gate`
- `approval_gate`
- `rollback_gate`

## Normative execution rule

Production execution SHOULD follow:
`propose -> score -> gate -> execute -> emit_evidence -> evaluate`

For any action with side effects, gate evaluation MUST dominate learned utility ranking.

## Action profiles

Every agent action SHOULD declare an action profile such as:
- `read_only`
- `draft_write`
- `tool_read`
- `tool_write`
- `external_communication`
- `cross_tenant_sensitive`
- `policy_sensitive`
- `delegation_creating`
- `self_modifying`

Each action profile MUST map to a required gate set.

## Gate activation record

An execution SHOULD emit a gate activation record containing:
- `action_ref`
- `required_gates`
- `activated_gates`
- `failed_gates`
- `policy_decision_ref`
- `approval_ref` if applicable
- `rollback_requirement`

## Normative rules

1. Any cross-tenant or external side-effecting action MUST require authorization, scope, policy, risk, and approval gates.
2. Any low-risk read action SHOULD require at minimum authorization, scope, and policy gates.
3. Any non-trivial write action SHOULD declare rollback expectations before execution.
4. Any action executed under high uncertainty SHOULD either escalate, clarify, or abort.
