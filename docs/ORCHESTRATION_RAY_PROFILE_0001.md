# Orchestration Ray Profile 0001

Status: draft normative profile.

This profile defines how SocioProphet agents describe skill orchestration, recipe execution, and Ray lifecycle integration.

## Orchestration surfaces

Every orchestrated agent should declare:
- identity surface
- context and memory surface
- skill catalog surface
- route selection surface
- recipe execution surface
- evidence surface

## Skill model

A skill is a reusable and sequenceable unit of work.

Skill families may include:
- productivity
- analytics
- business system
- automation
- custom

## Route model

Agents should distinguish at least:
- semantic route
- logical route
- retrieval route
- execution route

## Recipe execution

A recipe should declare:
- service or task type
- version
- data references
- arguments
- controller
- worker topology
- status outputs
- report outputs

## Ray lifecycle mapping

Recommended lifecycle mapping:
- Ray Data for ingestion and preparation
- Ray Train for distributed training
- Ray Tune for search and tuning
- Ray Serve for online serving
- KubeRay for cluster lifecycle

## Task-level and instance-level reasoning

Agents that discover reusable reasoning structure should distinguish:
- task-level structure discovery
- instance-level structure filling and execution

This distinction should be treated as a first-class orchestration concern.
