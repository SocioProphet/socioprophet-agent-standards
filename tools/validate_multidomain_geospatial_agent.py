#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_TOP = ["runtime_id", "runtime_class", "version", "inputs", "outputs", "policy", "evidence", "replay", "lattice_admission"]
RUNTIME_CLASSES = {"ingest", "transformation", "analytics", "report", "advisory_tasking"}
REQUIRED_POLICY = ["policy_bundle_ref", "approval_required", "denied_data_classes", "sensitive_geo_handling"]
REQUIRED_EVIDENCE = ["input_manifest", "output_manifest", "environment_fingerprint", "audit_log"]
REQUIRED_REPLAY = ["mode", "procedure_ref"]
REQUIRED_LATTICE = ["entrypoint", "validation_command", "fixture_ref", "admission_state"]


def fail(msg: str) -> None:
    print(f"ERR: {msg}", file=sys.stderr)
    raise SystemExit(2)


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path}: invalid JSON: {exc}")
    if not isinstance(data, dict):
        fail(f"{path}: expected top-level object")
    return data


def require_keys(obj: dict, keys: list[str], where: str) -> None:
    missing = [key for key in keys if key not in obj]
    if missing:
        fail(f"{where}: missing required keys: {', '.join(missing)}")


def validate_fixture(path: Path) -> None:
    data = load_json(path)
    require_keys(data, REQUIRED_TOP, str(path))
    if data["runtime_class"] not in RUNTIME_CLASSES:
        fail(f"{path}: unsupported runtime_class {data['runtime_class']!r}")
    if not isinstance(data["inputs"], list) or not data["inputs"]:
        fail(f"{path}: inputs must be a non-empty array")
    for idx, item in enumerate(data["inputs"]):
        if not isinstance(item, dict):
            fail(f"{path}: inputs[{idx}] must be object")
        require_keys(item, ["schema_ref", "data_class"], f"{path}:inputs[{idx}]")
    if not isinstance(data["outputs"], list) or not data["outputs"]:
        fail(f"{path}: outputs must be a non-empty array")
    for idx, item in enumerate(data["outputs"]):
        if not isinstance(item, dict):
            fail(f"{path}: outputs[{idx}] must be object")
        require_keys(item, ["schema_ref", "artifact_type"], f"{path}:outputs[{idx}]")
    if not isinstance(data["policy"], dict):
        fail(f"{path}: policy must be object")
    require_keys(data["policy"], REQUIRED_POLICY, f"{path}:policy")
    if not isinstance(data["policy"].get("approval_required"), bool):
        fail(f"{path}: policy.approval_required must be boolean")
    if not isinstance(data["evidence"], dict):
        fail(f"{path}: evidence must be object")
    require_keys(data["evidence"], REQUIRED_EVIDENCE, f"{path}:evidence")
    if not isinstance(data["replay"], dict):
        fail(f"{path}: replay must be object")
    require_keys(data["replay"], REQUIRED_REPLAY, f"{path}:replay")
    if not isinstance(data["lattice_admission"], dict):
        fail(f"{path}: lattice_admission must be object")
    require_keys(data["lattice_admission"], REQUIRED_LATTICE, f"{path}:lattice_admission")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    schema = root / "schemas/jsonschema/multidomain/geospatial_agent_runtime_profile.v1.schema.json"
    if not schema.exists():
        fail(f"missing schema: {schema.relative_to(root)}")
    load_json(schema)
    fixture_dir = root / "fixtures/multidomain"
    fixtures = sorted(fixture_dir.glob("*.json")) if fixture_dir.exists() else []
    if not fixtures:
        fail("no multidomain agent runtime fixtures found")
    for fixture in fixtures:
        validate_fixture(fixture)
    print(f"OK: validated {len(fixtures)} multidomain geospatial agent runtime fixture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
