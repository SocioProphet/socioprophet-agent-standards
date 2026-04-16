# M2 Adapter IPC Operation Matrix 0001

Status: draft normative companion note.

## Purpose

This note deepens `M2_ADAPTER_IPC_PROFILE_0001` by making the first operation family explicit.

It is a companion to the profile, not a replacement for it.

## Required operations

An M2-conformant adapter SHOULD support the following first-pass operations when applicable:

- `hello` — negotiate protocol presence and identify the adapter
- `info` — report protocol version and available capabilities
- `lock_validate` — check whether a referenced lock is present and valid
- `lock_hash` — produce or verify a deterministic lock hash
- `env_realize` — realize the execution environment from a declared reference
- `task_run` — invoke one declared task in a realized environment
- `deps_inventory` — emit dependency inventory for a subject or environment

## Operation intent

### hello
Purpose: bootstrap transport- and protocol-level confidence before any taskful operation.

### info
Purpose: report adapter identity, protocol version, and the capability surface actually available.

### lock_validate
Purpose: prevent execution against missing or stale dependency locks.

### lock_hash
Purpose: create a stable lock fingerprint for evidence, replay, and cache-key use.

### env_realize
Purpose: make the runtime environment concrete enough for execution and later replay.

### task_run
Purpose: execute one declared task with explicit arguments and receipt linkage.

### deps_inventory
Purpose: expose dependency structure for audit, replay, and troubleshooting.

## Normative sequencing guidance

A typical bounded flow SHOULD look like:
`hello -> info -> lock_validate -> lock_hash -> env_realize -> task_run -> deps_inventory`

Implementations MAY omit an operation only when the adapter capability declaration says so explicitly.

## Error alignment

Implementations SHOULD preserve the error registry defined by the M2 error schema and should not collapse adapter failures into generic string-only runtime errors.
