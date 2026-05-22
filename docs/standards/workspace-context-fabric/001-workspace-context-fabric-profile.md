# 001. Workspace Context Fabric Profile v0.1

## Status

Draft profile.

## Purpose

This standard defines the compatibility profile for Workspace Context Fabric v0.1 across the SocioProphet estate.

It is a profile and conformance layer. It does not move ownership of service contracts or runtime records into this repository.

## Authority chain

- Workspace/domain contracts: `SocioProphet/prophet-workspace`
- Runtime platform record binding: `SocioProphet/prophet-platform`
- Execution evidence bridge: `SocioProphet/agentplane`
- Recall promotion packet: `SocioProphet/memory-mesh`
- Agent authority binding: `SocioProphet/agent-registry`
- Estate registration: `SocioProphet/sociosphere`

## Required surfaces

A v0.1 compatible implementation must identify these surfaces:

- base Workroom contract
- ProfessionalWorkroom profile contract
- ContextGraph contract
- ProviderCapture contract
- ProviderProjection contract
- ShareGrant contract
- RecallCandidate contract
- WorkspaceContextRuntimeBinding contract
- platform workspace-context record
- WorkroomContextEvidence record
- WorkspaceRecallPromotionPacket record
- WorkspaceContextAuthorityBinding record

## Boundary rules

- Workroom and Context Fabric semantics stay in `prophet-workspace`.
- Platform runtime records stay in `prophet-platform`.
- Execution evidence stays in `agentplane`.
- Recall promotion stays in `memory-mesh`.
- Agent/session/grant authority stays in `agent-registry`.
- Sociosphere remains the estate registration and boundary governance surface.

## Initial conformance statement

An implementation is v0.1-compatible when it can provide a valid `WorkspaceContextFabricProfile` document listing the required upstream refs and can show evidence that the referenced contract family has local validation coverage in each owning repository.
