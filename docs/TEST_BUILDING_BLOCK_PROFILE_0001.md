# Test Building Block Profile 0001

Status: draft normative profile for using logical-statistical model families as primary test building blocks.

## Purpose

This profile defines how SocioProphet test suites describe reusable test building blocks derived from logical-statistical model families.

The goal is to make tests express not only expected answers, but also:
- structural reasoning expectations
- weighted evidence interactions
- route selection behavior
- gate activation behavior
- provenance requirements

## Test building block classes

A conforming test suite SHOULD support at least these classes:
- `structure_discovery_test`
- `instance_fill_test`
- `weighted_constraint_test`
- `relational_inference_test`
- `route_selection_test`
- `gate_activation_test`
- `graduation_readiness_test`
- `ray_lifecycle_promotion_test`

## Required fields for a test block

Each test block SHOULD declare:
- `test_block_id`
- `profile_refs`
- `input_context`
- `expected_structure`
- `expected_outputs`
- `expected_gates`
- `expected_evidence_refs`
- `evaluation_regime`

## Parallel graduation alignment

Test suites SHOULD distinguish:
- task-level reasoning structure discovery
- instance-level structure filling and execution

These should be tested separately and then jointly.

## Ray lifecycle alignment

When a model or agent participates in Ray-based pipelines, test blocks SHOULD be able to assert expectations over:
- training outputs
- tuning outputs
- benchmark reports
- serving readiness
- promotion and rollback records

## Normative rules

1. Production-facing test suites SHOULD include at least one route-selection test and one gate-activation test for each side-effecting action class.
2. Any bounded-autonomy promotion SHOULD require graduation-readiness tests across multiple lanes, not only capability tests.
3. Benchmarking tests SHOULD reuse the same evidence/provenance vocabulary as runtime surfaces.
4. Logical-statistical test blocks SHOULD specify whether they validate hard constraints, soft constraints, or both.
