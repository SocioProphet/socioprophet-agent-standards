# AgentOS Spec 0001

Status: draft normative profile.

## Purpose

This profile harmonizes the existing SocioProphet control, gating, graduation, orchestration, and evidence work into one canonical AgentOS declaration surface.

It does not replace the existing profiles. It binds them together and defines the minimum object that any AgentOS-conformant agent should expose.

## Upstream profile set

This profile composes these existing normative profiles:
- `EVIDENCE_PROFILE_0001`
- `CONTROL_PROFILE_0001`
- `GATING_PROFILE_0001`
- `GRADUATION_PROFILE_0001`
- `ORCHESTRATION_PROFILE_0001`
- `CONTROL_GATING_GRADUATION_PROFILE_0001`
- `ORCHESTRATION_RAY_PROFILE_0001`

It also introduces two adjacent required contract families:
- `M2_ADAPTER_IPC_PROFILE_0001`
- `LIBERTY_STACK_PROFILE_0001`

## Required AgentOS declaration surfaces

Every AgentOS-conformant agent SHOULD declare:
- identity and authority surface
- control surface
- gating surface
- graduation surface
- orchestration surface
- evidence surface
- runtime substrate surface
- workstation or runner adapter surface
- migration or restore safety surface when the agent performs destructive or sovereignty-affecting operations

## Canonical agent object

An AgentOS spec SHOULD include at minimum:
- `agent_ref`
- `profiles`
- `control`
- `gating`
- `graduation`
- `orchestration`
- `evidence`
- `runtime_substrate`
- `adapter_contracts`
- `risk_posture`

## Harmonization rules

1. AgentOS MUST treat existing profile docs as the normative meaning source for control, gating, graduation, orchestration, and evidence.
2. AgentOS MUST NOT duplicate those semantics under new incompatible field names.
3. AgentOS SHOULD reference M2 when local runner, workstation, or adapter mediation is required.
4. AgentOS SHOULD reference Liberty Stack when the agent participates in export, import, verification, cutover, replay, or deletion workflows.
5. Production-facing AgentOS specs SHOULD preserve replayability and evidence linkage across all side-effecting actions.

## Minimal compatibility contract

A downstream runtime or platform SHOULD be able to answer, for any agent:
- how it chooses actions
- what gates must pass
- what maturity level it has reached
- how work is orchestrated
- which evidence objects it emits
- which runtime substrate executes it
- which adapter contract mediates local execution
- which rollback, replay, or deletion safeguards apply
