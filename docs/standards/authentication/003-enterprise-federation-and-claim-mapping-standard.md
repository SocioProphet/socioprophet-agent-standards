# 003 - Enterprise Federation and Claim Mapping Standard

| Metadata | Value |
| --- | --- |
| Standard ID | 003 |
| Status | Draft normative profile |
| Depends on | `001-agent-authentication-session-and-recovery-standard.md` |
| Applies to | OIDC federation, SAML compatibility lanes, tenant routing, subject mapping, role/group claim normalization, logout propagation |
| Last updated | 2026-04-14 |

## 1. Purpose

This standard defines how SocioProphet systems accept enterprise identity proof from external identity providers and transform that proof into an internal subject, tenant, session, and authorization context.

Federation is a proof ingress layer, not a substitute for first-party policy. The purpose of this standard is to ensure that enterprise SSO does not become an uncontrolled bypass around session issuance, role assignment, tenant boundaries, recovery policy, or auditability.

## 2. Normative posture

1. **OIDC-first.**
   - OpenID Connect SHOULD be the default federation profile.
   - SAML MAY be supported as a compatibility lane where required by tenant demand.

2. **External proof, internal session.**
   - Upstream proof from the enterprise IdP MAY establish identity.
   - SocioProphet MUST still issue its own first-party session and policy context.

3. **Routing before issuance.**
   - Tenant and IdP routing MUST be determined before internal session issuance.

4. **Claims are not blindly trusted.**
   - Upstream claims MUST be normalized and validated against tenant configuration.
   - Broad authorization MUST NOT be granted solely because a group or role claim is present upstream.

5. **Federation is not recovery bypass.**
   - Enterprise federation MUST NOT bypass recovery, support, or privileged-access controls defined elsewhere.

## 3. Federation subject model

An enterprise-federated user MUST be represented internally by at least:

- internal `subject_id`
- `tenant_id`
- `federation_binding_id`
- upstream issuer / IdP identifier
- upstream stable subject handle
- normalized email / identifier where policy allows
- assurance context summary
- role and group claim material after normalization

The internal subject MUST remain the canonical local reference even when authentication is performed externally.

## 4. Tenant routing

Implementations MUST define deterministic tenant-routing behavior.

Routing inputs MAY include:

- email domain
- explicit tenant selector
- organization slug
- IdP hint parameter
- invitation or bootstrap context

Routing rules MUST define what happens when:

- the domain matches one tenant
- the domain matches multiple tenants
- the domain matches no configured enterprise tenant
- a user attempts first-party login to a federated-only tenant
- a user attempts enterprise login to a first-party-only tenant

Implicit fallback behavior MUST be documented. Silent tenant confusion is not acceptable.

## 5. Supported federation profiles

### 5.1 OIDC profile

For OIDC tenants, implementations SHOULD support a modern authorization-code-based flow and MUST capture enough metadata to validate:

- issuer
- audience / client binding
- subject
- token lifetime / freshness
- tenant binding
- session posture

### 5.2 SAML compatibility profile

Where SAML is required, implementations MUST define a compatibility lane with explicit mapping and validation rules.

SAML support MUST NOT reduce the strength of:

- tenant isolation
- claim validation
- privileged access controls
- auditability

## 6. Claim normalization

Upstream claims MUST be transformed into an internal canonical form before they are consumed by authorization or product logic.

The normalized federation context SHOULD include:

- `tenant_id`
- `subject_id`
- `issuer_id`
- `upstream_subject`
- `normalized_login_identifier`
- `display_name`
- `group_bindings`
- `role_bindings`
- `assurance_context`
- `session_constraints`

Implementations MUST explicitly document which upstream attributes are authoritative and which are advisory.

## 7. Account linking rules

Federation introduces account-linking risk.

Requirements:

1. The system MUST define whether linking is:
   - pre-provisioned only
   - just-in-time (JIT) allowed
   - invitation-driven
2. Email equality alone SHOULD NOT be treated as universally sufficient proof for sensitive account linking.
3. Linking behavior for privileged accounts MUST be stricter than for standard accounts.
4. A subject MUST NOT be silently rebound from one tenant or issuer to another without explicit policy and evidence.

## 8. Just-in-time provisioning

JIT provisioning MAY be supported if tenant policy allows it.

Requirements:

1. JIT provisioning MUST still create an internal subject and session context.
2. JIT provisioning MUST apply tenant-specific role defaults conservatively.
3. Elevated roles MUST NOT be assigned solely by optimistic default during JIT creation.
4. JIT provisioning events MUST be auditable.

## 9. Role and group claim mapping

Upstream role and group claims are inputs, not final authorization truth.

Requirements:

1. Group/role claim mapping MUST be defined per tenant.
2. Mappings MUST be explicit, reviewable, and auditable.
3. Unknown upstream groups SHOULD default to no privilege.
4. Privileged roles SHOULD require explicit mapping approval.
5. Authorization MUST still be enforced by the internal authorization service after claim normalization.

## 10. Session issuance after federation

After successful federation proof and claim normalization:

1. SocioProphet MUST issue an internal first-party session.
2. The session MUST record:
   - tenant ID
   - internal subject ID
   - issuer / federation binding
   - assurance context
   - mapped roles / attributes
   - policy constraints
3. Browser clients SHOULD receive cookie-based first-party sessions rather than long-lived front-end refresh capability.

## 11. Logout and revocation

Federated logout behavior MUST be documented.

Implementations SHOULD distinguish:

- local application logout
- first-party session revocation
- upstream IdP logout propagation
- account suspension / disablement

Where enterprise deployment requires logout propagation, the mechanism SHOULD be supported and tested. Local logout alone may be insufficient in tightly governed enterprise deployments.

## 12. Support, recovery, and tenant administration

Federation does not remove the need for strong support and recovery controls.

Requirements:

1. Tenant admins MAY control allowed federation bindings only through authenticated, auditable management paths.
2. Support staff MUST NOT silently rebind users to a different issuer without strong controls.
3. Recovery for federated accounts MUST define what happens when:
   - the enterprise IdP is unavailable
   - the user loses corporate access
   - the user is transferred between tenants
   - the user departs the organization

## 13. Evidence and audit events

Implementations MUST emit events for at least:

- `federation.route.started`
- `federation.route.selected`
- `federation.proof.accepted`
- `federation.proof.rejected`
- `federation.subject.linked`
- `federation.subject.provisioned`
- `federation.claims.normalized`
- `federation.role_mapping.applied`
- `federation.binding.revoked`
- `federation.logout.propagated`

Each event SHOULD include:

- tenant ID
- internal subject ID
- issuer ID
- upstream subject handle or surrogate
- routing basis
- provisioning mode
- mapped role/group summary
- operator ID where applicable
- correlation / trace ID

## 14. Data model primitives

### 14.1 Federation binding
- `federation_binding_id`
- `subject_id`
- `tenant_id`
- `issuer_id`
- `upstream_subject`
- `binding_state`
- `created_at`
- `last_success_at`
- `revoked_at`

### 14.2 Claim mapping rule
- `mapping_rule_id`
- `tenant_id`
- `issuer_id`
- `upstream_claim_name`
- `upstream_claim_value`
- `mapped_role_or_attribute`
- `approved_by`
- `state`

### 14.3 Federation event context
- `event_id`
- `tenant_id`
- `subject_id`
- `issuer_id`
- `routing_basis`
- `provisioning_mode`
- `assurance_context`

## 15. Conformance requirements

An implementation MAY claim conformance only if:

- tenant routing is explicit
- OIDC or a justified enterprise profile is documented
- internal subject and session issuance occur after successful external proof
- account linking rules are documented
- claim normalization exists before authorization consumption
- role/group mappings are explicit and auditable
- logout and revocation behavior are documented

## 16. Anti-patterns

The following are prohibited or strongly discouraged.

- treating upstream group claims as direct final authorization without mapping
- silently auto-linking privileged accounts on weak signals
- allowing issuer changes without durable evidence
- using federation as a bypass around first-party session controls
- assuming SSO removes the need for support and recovery policy
- collapsing all tenants into one undifferentiated federation policy

## 17. Summary

Enterprise federation is an ingress mechanism for identity proof. It is not a replacement for first-party sessioning, policy, authorization, or audit. SocioProphet systems MUST route tenants deterministically, normalize claims explicitly, map external proof into internal subject context, and preserve tenant boundaries throughout.
