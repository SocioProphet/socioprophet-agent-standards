#!/usr/bin/env python3
"""Validate the consent-plane catalogs (001-purpose-bound-tool-use-and-agent-roles).

Checks each catalog is well-formed and that the four are referentially
consistent: roles/surfaces/tools reference only defined purposes, surfaces
reference defined spaces, role tolerations reference real space taints, and
taint effects are valid. Without this the catalogs are an unvalidated blob;
this is the schema + integrity gate.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required for validate_consent_plane.py") from exc

ROOT = Path(__file__).resolve().parents[1]
CP = ROOT / "standards" / "consent-plane"
VALID_EFFECTS = {"NoEntry", "NoExecute", "PreferNoEntry"}


def load(name: str, kind: str, errors: list[str]) -> dict:
    p = CP / name
    if not p.exists():
        errors.append(f"missing catalog {name}")
        return {}
    d = yaml.safe_load(p.read_text())
    if not isinstance(d, dict):
        errors.append(f"{name}: top-level must be a mapping, got {type(d).__name__}")
        return {}
    if d.get("kind") != kind:
        errors.append(f"{name}: kind must be {kind}, got {d.get('kind')!r}")
    if not isinstance(d.get("spec"), dict):
        errors.append(f"{name}: missing spec")
    return d


def main() -> int:
    errors: list[str] = []
    tpb = load("tool-purpose-bindings_v1.yaml", "ToolPurposeBindings", errors)
    roles = load("agent-roles_v1.yaml", "AgentRoleCatalog", errors)
    surfaces = load("surfaces_v1.yaml", "SurfaceCatalog", errors)
    spaces = load("spaces_v1.yaml", "SpaceCatalog", errors)
    if errors:  # can't cross-check if a catalog failed to load
        return _report(errors)

    purposes = set((tpb["spec"].get("purposes") or {}).keys())
    if not purposes:
        errors.append("tool-purpose-bindings: no purposes defined")

    # tools reference defined purposes
    for b in tpb["spec"].get("bindings", []):
        for pur in b.get("purposes", []):
            if pur not in purposes:
                errors.append(f"tool {b.get('tool')!r}: undefined purpose {pur!r}")

    # spaces: valid taints + collect the set of (key=value) taints that exist
    space_ids: set[str] = set()
    taint_kv: set[str] = set()
    for s in spaces["spec"].get("spaces", []):
        sid = s.get("id")
        if not sid:
            errors.append("space entry missing 'id'")
            continue
        space_ids.add(sid)
        for t in s.get("taints", []):
            if t.get("effect") not in VALID_EFFECTS:
                errors.append(f"space {sid!r}: bad taint effect {t.get('effect')!r}")
            if t.get("key") is None or t.get("value") is None:
                errors.append(f"space {sid!r}: taint missing key/value")
                continue
            taint_kv.add(f"{t.get('key')}={t.get('value')}")

    # roles reference defined purposes; EVERY toleration must match a real
    # space taint (catches typos like `tenant=` or `foo=bar`, not just ring=*).
    for r in roles["spec"].get("roles", []):
        for pur in r.get("admissible", []):
            if pur not in purposes:
                errors.append(f"role {r.get('id')!r}: undefined purpose {pur!r}")
        for tol in r.get("tolerations", []):
            if tol not in taint_kv:
                errors.append(f"role {r.get('id')!r}: toleration {tol!r} matches no space taint")

    # surfaces reference defined purposes + defined spaces
    for sf in surfaces["spec"].get("surfaces", []):
        for pur in sf.get("purposes", []) + sf.get("deny_purposes", []):
            if pur not in purposes:
                errors.append(f"surface {sf.get('id')!r}: undefined purpose {pur!r}")
        for sp in sf.get("space_deny", []):
            if sp not in space_ids:
                errors.append(f"surface {sf.get('id')!r}: space_deny references unknown space {sp!r}")

    return _report(errors, ok=f"consent-plane: {len(purposes)} purposes, "
                   f"{len(roles['spec'].get('roles', []))} roles, "
                   f"{len(surfaces['spec'].get('surfaces', []))} surfaces, "
                   f"{len(space_ids)} spaces — all referentially consistent.")


def _report(errors: list[str], ok: str = "") -> int:
    if errors:
        print(f"FAIL: {len(errors)} problem(s) in consent-plane catalogs:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"OK: {ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
