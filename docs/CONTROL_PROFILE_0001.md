# Control Profile 0001

Status: draft normative profile for agent control-family classification.

## Purpose

This profile defines how SocioProphet agents describe **how they choose** actions.

It is not limited to reinforcement learning labels. It standardizes durable control-family categories that can map to learned, symbolic, hybrid, or planner-based systems.

## Required control-family declaration

Every agent spec should declare one or more primary control families:
- `value_based`
- `policy_based`
- `actor_critic`
- `imitation_bootstrapped`
- `goal_conditioned`
- `model_based_planner`
- `constrained_safe`
- `offline_replay_driven`
- `hierarchical_options`
- `multi_agent_delegated`
- `formal_policy_constrained`

## Required fields

Each agent should declare:
- `control_family`
- `proposal_mode` — how candidate actions are generated
- `selection_mode` — how candidate actions are chosen
- `state_representation`
- `goal_vector`
- `uncertainty_mode`
- `update_mode` — fixed, periodically adapted, continuously adapted, or externally trained

## Normative rules

1. Production agents MUST NOT expose only paper-family labels such as `PPO` or `DQN` as their normative control description.
2. Agent specs SHOULD express paper-family lineage only as an informative subfield.
3. Production agents SHOULD prefer platform-stable descriptions such as `policy_based + actor_critic + constrained_safe`.
4. Any agent with non-trivial side effects MUST declare whether its control logic is planner-dominant, policy-dominant, or gate-dominant.

## Recommended subfields

Recommended informative subfields:
- `algorithm_lineage`
- `planner_backend`
- `critic_type`
- `memory_mode`
- `retrieval_mode`
- `self_discover_reasoning_structure` — true/false

## Reasoning-structure alignment

If an agent uses task-level structure discovery and instance-level execution, it SHOULD declare:
- `reasoning_structure_discovery_mode`
- `instance_execution_mode`
- `structure_fill_strategy`

This supports the pattern where the system first discovers a reusable reasoning structure and then fills that structure during execution.
