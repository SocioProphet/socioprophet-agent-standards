# Logical Statistical Profile 0001

Status: draft normative profile for logical-statistical reasoning components in SocioProphet agents and evaluation systems.

## Purpose

This profile defines how SocioProphet systems describe components that combine:
- logical structure
- uncertainty handling
- relational domains
- weighted soft constraints

This profile is intended to support systems that unify symbolic and statistical reasoning rather than treating them as disjoint stacks.

## Core model family

The initial reference family for this profile is the class of weighted relational graphical models exemplified by Markov Logic style systems.

The profile does not require one specific implementation, but it expects systems to be able to express:
- first-order or relational structure
- weighted formulas or weighted constraints
- probabilistic or score-based uncertainty
- soft satisfaction rather than only hard satisfiability

## Required declaration fields

Any component claiming conformance SHOULD declare:
- `logical_representation`
- `statistical_representation`
- `weight_semantics`
- `inference_mode`
- `learning_mode`
- `relation_scope`
- `evidence_mode`

## Recommended values

Suggested values include:
- `logical_representation`: first_order_logic, typed_relational_logic, rule_graph
- `statistical_representation`: markov_network, factor_graph, probabilistic_graphical_model, hybrid_graphical_model
- `weight_semantics`: hard_constraint, soft_constraint, weighted_formula, utility_weight
- `inference_mode`: weighted_model_counting, lifted_inference, approximate_sampling, variational, theorem_proving_hybrid
- `learning_mode`: weight_learning, structure_learning, discriminative, generative, hybrid
- `evidence_mode`: open_world, closed_world_fixture, bounded_candidate_universe

## Normative rules

1. A conforming logical-statistical component MUST distinguish hard constraints from soft weighted constraints.
2. A conforming component SHOULD distinguish relational structure from grounded instances.
3. A conforming component SHOULD expose both model semantics and inference semantics in the spec.
4. A conforming component used in production SHOULD specify whether it supports lifted or grouped reasoning over repeated relational structure.
5. A conforming component used for agent control or testing SHOULD declare how evidence affects weights, satisfiability, and decision outputs.

## Downstream intent

This profile is intended to support:
- semantic route selection
- logical route selection
- evidence-aware gating
- benchmark specification
- policy and provenance tests
- hybrid symbolic/statistical agent behaviors
