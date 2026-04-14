# Orchestration Profile 0001

Status: draft normative profile for agent orchestration, skills, routes, and recipe execution.

## Purpose

This profile defines how SocioProphet agents describe **how work is composed and routed** across skills, prompts, tools, data planes, and execution recipes.

## Core orchestration surfaces

An orchestrated agent SHOULD declare these surfaces:
- `identity_surface`
- `context_memory_surface`
- `skill_catalog_surface`
- `route_selection_surface`
- `recipe_execution_surface`
- `evidence_surface`

## Skill model

A skill SHOULD be treated as a reusable and sequenceable unit of work.

Skill families MAY include:
- `productivity_skill`
- `analytics_skill`
- `business_system_skill`
- `automation_skill`
- `rpa_skill`
- `custom_skill`

## Route model

Agents SHOULD support at least:
- `semantic_route`
- `logical_route`
- `retrieval_route`
- `execution_route`

The orchestration layer SHOULD be able to choose between routes using policy and gate state, not only model preference.

## Recipe execution model

A recipe SHOULD describe:
- the service or task type
- version
- required data references
- arguments
- execution controller
- worker topology
- status/report outputs

## Reasoning-structure model

Agents that perform task-level structure discovery SHOULD distinguish:
- task-level structure discovery
- instance-level structure filling and execution

This profile treats that distinction as a first-class orchestration concern, not only a prompting trick.

## Normative rules

1. Skill composition SHOULD remain explicit and inspectable.
2. Route selection SHOULD remain policy- and gate-aware.
3. Execution recipes SHOULD emit evidence and status artifacts.
4. Identity, context, and memory SHOULD be treated as orchestration primitives, not optional add-ons.
