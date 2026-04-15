# Repository boundaries

This note records the repository split for the SourceOS / SociOS / AgentPlane stack.

## Split

- `SocioProphet/agentplane` holds the execution control-plane contract, including placement, promotion, reversal, replay, evidence lifecycle, and operator topology.
- `SocioProphet/socioprophet-agent-standards` holds shared schemas, capability vocabulary, artifact vocabulary, policy vocabulary, conformance, and compatibility guidance.
- `SociOS-Linux/source-os` holds Linux host, image, and Nix realization.
- `SociOS-Linux/socios-scripts` holds installer and migration helpers.
- `SociOS-Linux/socios-alarm-builder` holds reference x86/ALARM image assembly.

## Practical rule

When a capability, artifact, or policy term is intended to be reused across repositories, its shared schema or vocabulary definition should be recorded in this repository even if the first implementation appears elsewhere.
