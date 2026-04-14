# Graduation Profile 0001

Status: draft normative profile for parallel agent graduation.

## Purpose

This profile defines how SocioProphet agents describe **what maturity level they have reached** across multiple parallel lanes.

## Core principle

Agents MUST NOT graduate on capability alone.

Graduation SHOULD be measured as a vector across multiple lanes. Promotion SHOULD be limited by the lowest critical lane, not the highest-performing lane.

## Required graduation lanes

Every production-facing agent SHOULD be graded across at least:
- `capability`
- `safety_policy`
- `reliability_recovery`
- `observability_auditability`
- `provenance_reproducibility`
- `efficiency_budget`
- `human_oversight_acceptability`

## Suggested stage ladder

Recommended maturity stages:
- `L0_research_only`
- `L1_simulation_only`
- `L2_shadow_mode`
- `L3_assist_mode`
- `L4_supervised_actuation`
- `L5_bounded_autonomy`
- `L6_federated_or_delegated_autonomy`

## Promotion rule

A promotion rule SHOULD take the form:
- all required lanes meet or exceed the target stage threshold
- no blocking incident exists in the evaluation window
- required graduation gates are satisfied

## Normative rules

1. Promotion to any stage with side-effecting actuation MUST require successful safety and rollback evaluation.
2. Promotion to bounded autonomy SHOULD require incident-free operation over a declared observation window.
3. Promotion records SHOULD emit evidence references to the supporting evaluation artifacts.
4. Any downgrade or freeze decision SHOULD be recorded with blocking-lane justification.

## Graduation artifact

A graduation artifact SHOULD contain:
- `agent_ref`
- `current_stage`
- `lane_scores`
- `blocking_lanes`
- `promotion_window`
- `evidence_refs`
- `gate_refs`
- `decision_ref`
