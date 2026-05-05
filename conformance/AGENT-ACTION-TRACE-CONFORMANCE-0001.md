# Agent Action / Trace Conformance Criteria 0001

## Purpose

This conformance note defines the first acceptance criteria for implementations claiming compatibility with the Agent Action / Trace Conformance Profile.

## Required evidence

A conforming implementation SHOULD provide:

1. an `AgentActionTraceProfile` document
2. at least one valid action record example
3. at least one valid trace record example
4. a negative example or validation report proving malformed traces are rejected
5. a policy/evidence/receipt linkage statement

## Runtime expectations

A conforming runtime MUST NOT treat traces as authorization.

A conforming runtime MUST distinguish:

- semantic ontology terms
- runtime action records
- coordination traces
- policy decisions
- evidence receipts

## Initial downstream consumers

Expected consumers include:

- `SocioProphet/agentplane`
- `SourceOS-Linux/agent-machine`
- `SourceOS-Linux/agent-term`
- `SocioProphet/prophet-platform`

## Status

Bootstrap criteria only. This should be hardened with executable validators in a later PR.
