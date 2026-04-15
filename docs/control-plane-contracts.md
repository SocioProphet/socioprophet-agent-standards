# Control-plane contracts

This repository carries the shared control-plane contract vocabulary used across AgentPlane and SourceOS Linux realization repos.

## Initial contract set

### Channel

A channel is a promoted environment pointer for an accepted artifact set.

Initial shared values:

- `dev`
- `candidate`
- `stable`

The canonical schema is `schemas/channel.schema.json`.

### Capability

A capability is a tested and versioned unit of behavior with explicit owners, inputs, outputs, and proving tests.

The canonical schema is `schemas/capability.schema.json`.

## Intended use

- `agentplane` should reference these shared terms when describing promotion and execution flow.
- `source-os` should reference these shared terms when realizing Linux hosts, images, and builder surfaces.
- future ops repos should reuse these schemas rather than redefining channel or capability meaning locally.
