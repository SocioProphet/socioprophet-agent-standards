# M2 Adapter IPC Error Code Registry 0001

Status: draft normative companion note.

## Purpose

This note makes the first M2 adapter error-code family explicit so downstream runtime repos preserve structured failure semantics.

## Registry

- `E_PROTOCOL_INCOMPATIBLE` — adapter and caller disagree on protocol version or required semantics
- `E_CAPABILITY_MISSING` — requested operation is not supported by the adapter
- `E_LOCK_MISSING` — referenced lock artifact is absent
- `E_LOCK_INVALID` — lock artifact exists but fails validation
- `E_LOCK_HASH_FAILED` — lock hashing or digest comparison failed
- `E_TASK_FAILED` — invoked task completed unsuccessfully
- `E_PATH_ESCAPE` — adapter rejected an unsafe path resolution
- `E_WRITE_DENIED` — adapter denied a write or mutation request
- `E_INTERNAL` — adapter encountered an unexpected internal failure

## Normative rules

1. Adapters SHOULD emit structured error objects, not only free-form text.
2. Runtime consumers SHOULD preserve the exact error code for receipts and evidence.
3. Platform-local wrappers SHOULD map internal exceptions into this registry rather than inventing repo-local ad hoc categories.
4. Additional future codes MAY be added, but existing codes SHOULD remain stable once emitted into evidence-bearing records.
