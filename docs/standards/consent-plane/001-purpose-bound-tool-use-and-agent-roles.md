# 001 - Purpose-Bound Tool Use and Agent Roles

| Metadata | Value |
| --- | --- |
| Standard ID | 001 |
| Status | Draft normative profile |
| Depends on | `agent-plane/001-agent-action-trace-conformance-profile.md`, `authentication/004-workload-and-service-identity-standard.md` |
| Applies to | All agent tool invocations, agent role assignment, surface configuration, isolation-space admission, and the consent/receipt trail |
| Last updated | 2026-08-02 |

## 1. Purpose

This standard makes every agent tool invocation a **purpose-scoped, consent-checked, accountable act**. It binds five orthogonal isolation primitives — **role, surface, space, tool, purpose** — plus **consent**, so that an action is admissible only when all of them agree. The construction maps directly onto GDPR: purpose limitation (Art. 5(1)(b)), consent per purpose (Art. 6(1)(a)/7), data minimisation (Art. 5(1)(c)), accountability (Art. 5(2)), and consent withdrawal (Art. 7(3)). Adopted across the tool catalog, the agent-prompt catalog, the system-prompt catalog and the estate catalog on one purpose vocabulary, it yields a **consent-based regulatory setting** for the agent fabric.

This is not a new silo. It adds a `purpose` and `surface`/`space` dimension to the existing Action Ontology (`agent-plane/001`) records and reuses machine identity from `authentication/004`.

## 2. Normative posture

1. **Every agent binds to exactly one role.** A role (`agent-roles_v1.yaml`) is a machine identity's admissible-purpose set. It MUST hold the minimum purposes for its charter (data minimisation).
2. **Every tool declares the purposes it serves.** `tool-purpose-bindings_v1.yaml` is canonical; the purpose vocabulary is defined once there and referenced by name.
3. **Every invocation declares a purpose.** An undeclared purpose is refused, not defaulted.
4. **The surface caps the role.** A surface (`surfaces_v1.yaml`) is where the agent is embedded; its envelope is a hard cap on purposes/data-classes/spaces regardless of role. A browser-surface agent MUST NOT `implement` or `operate` even if injected — containment over trust.
5. **The space is admitted by taint/toleration.** A space (`spaces_v1.yaml`) is the isolation ring the operation targets. An operation MAY act in a space only if its `(role, surface)` context tolerates every blocking taint. `system-space`/`kernel-space` are tolerated only by the `operator` role.
6. **Data-namespace crossing requires per-tenant consent.** Tenant tolerations are granted per `(principal, tenant)` and are revocable; a `NoExecute` withdrawal aborts running operations touching that tenant (Art. 7(3)).
7. **Consent is per purpose, revocable, and recorded.** Where `consent_required: per-purpose`, an explicit grant for `(role, purpose, surface[, tenant])` MUST exist.
8. **Every decision emits a receipt.** `{role, surface, space, tool, purpose, context, decision}` — the Action-Ontology trace record, extended (accountability).

## 3. The admission gate (normative algorithm)

```
admit ⇔  purpose ∈ role.admissible
      ∧  purpose ∈ tool.purposes
      ∧  purpose ∈ surface.purposes ∧ purpose ∉ surface.deny_purposes
      ∧  tool.data_class ∈ surface.data_classes
      ∧  space ∉ surface.space_deny
      ∧  every blocking taint of space is tolerated by role (+ per-tenant consent for data-namespace)
      ∧  consent granted for (role, purpose, surface[, tenant]) if consent_required
```

Precedence, outer wins: **surface `space_deny` > space taint > role grant.** `DENY` is fail-closed.

## 4. GDPR mapping

| Primitive | GDPR |
| --- | --- |
| purpose | purpose limitation (Art. 5(1)(b)) |
| consent (per purpose) | lawful basis / consent (Art. 6(1)(a), 7) |
| role admissible-set | data minimisation (Art. 5(1)(c)) |
| data-namespace toleration | cross-context transfer basis; withdrawal (Art. 7(3)) |
| receipt | accountability (Art. 5(2)) |

## 5. Conformance

An implementation conforms when: roles/surfaces/spaces/tool-bindings validate against `tools/validate_consent_plane.py` (referential integrity across the four catalogs); the runtime enforces the §3 gate fail-closed; and each decision produces an Action-Ontology receipt carrying `purpose`, `surface`, and `space`.
