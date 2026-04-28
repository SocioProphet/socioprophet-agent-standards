#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_PROFILE_TOP = ["runtime_id", "runtime_class", "version", "inputs", "outputs", "policy", "evidence", "replay", "lattice_admission"]
RUNTIME_CLASSES = {"ingest", "transformation", "analytics", "report", "advisory_tasking"}
REQUIRED_POLICY = ["policy_bundle_ref", "approval_required", "denied_data_classes", "sensitive_geo_handling"]
REQUIRED_EVIDENCE = ["input_manifest", "output_manifest", "environment_fingerprint", "audit_log"]
REQUIRED_REPLAY = ["mode", "procedure_ref"]
REQUIRED_LATTICE = ["entrypoint", "validation_command", "fixture_ref", "admission_state"]

REQUIRED_BUNDLE_TOP = ["evidence_version", "evidence_id", "runtime_id", "runtime_class", "standards_refs", "input_manifest", "output_manifest", "policy", "replay"]
REQUIRED_BUNDLE_INPUT = ["input_ref", "input_sha256", "input_schema_hint"]
REQUIRED_BUNDLE_OUTPUT = ["output_ref", "output_sha256", "output_schema_ref"]
REQUIRED_BUNDLE_POLICY = ["approval_required", "sensitive_geo_handling", "network_posture", "secret_posture"]
REQUIRED_BUNDLE_REPLAY = ["mode", "command"]
SHA256_RE = re.compile(r"^sha256:[0-9a-fA-F]{64}$")
REQUIRED_STANDARD_REFS = {
    "SocioProphet/socioprophet-standards-storage/docs/standards/096-multidomain-geospatial-storage-contracts.md",
    "SocioProphet/socioprophet-standards-knowledge/docs/standards/080-multidomain-geospatial-knowledge-context.md",
    "SocioProphet/socioprophet-agent-standards/docs/standards/020-multidomain-geospatial-agent-runtime.md",
}


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


def validate_profile(path: Path) -> None:
    data = load_json(path)
    require_keys(data, REQUIRED_PROFILE_TOP, str(path))
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


def validate_evidence_bundle(path: Path) -> None:
    data = load_json(path)
    require_keys(data, REQUIRED_BUNDLE_TOP, str(path))
    if data.get("evidence_version") != "v1":
        fail(f"{path}: evidence_version must be v1")
    if data["runtime_class"] not in RUNTIME_CLASSES:
        fail(f"{path}: unsupported runtime_class {data['runtime_class']!r}")
    refs = set(data.get("standards_refs", []))
    missing = sorted(REQUIRED_STANDARD_REFS - refs)
    if missing:
        fail(f"{path}: missing standards refs: {', '.join(missing)}")
    input_manifest = data.get("input_manifest")
    if not isinstance(input_manifest, dict):
        fail(f"{path}: input_manifest must be object")
    require_keys(input_manifest, REQUIRED_BUNDLE_INPUT, f"{path}:input_manifest")
    if not SHA256_RE.match(input_manifest["input_sha256"]):
        fail(f"{path}: input_manifest.input_sha256 must be sha256:<64 hex>")
    output_manifest = data.get("output_manifest")
    if not isinstance(output_manifest, dict):
        fail(f"{path}: output_manifest must be object")
    require_keys(output_manifest, REQUIRED_BUNDLE_OUTPUT, f"{path}:output_manifest")
    if not SHA256_RE.match(output_manifest["output_sha256"]):
        fail(f"{path}: output_manifest.output_sha256 must be sha256:<64 hex>")
    policy = data.get("policy")
    if not isinstance(policy, dict):
        fail(f"{path}: policy must be object")
    require_keys(policy, REQUIRED_BUNDLE_POLICY, f"{path}:policy")
    if not isinstance(policy["approval_required"], bool):
        fail(f"{path}: policy.approval_required must be boolean")
    replay = data.get("replay")
    if not isinstance(replay, dict):
        fail(f"{path}: replay must be object")
    require_keys(replay, REQUIRED_BUNDLE_REPLAY, f"{path}:replay")
    if replay["mode"] not in {"deterministic_fixture", "bounded_replay", "not_replayable"}:
        fail(f"{path}: invalid replay.mode {replay['mode']!r}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    profile_schema = root / "schemas/jsonschema/multidomain/geospatial_agent_runtime_profile.v1.schema.json"
    bundle_schema = root / "schemas/jsonschema/multidomain/geospatial_runtime_evidence_bundle.v1.schema.json"
    if not profile_schema.exists():
        fail(f"missing schema: {profile_schema.relative_to(root)}")
    if not bundle_schema.exists():
        fail(f"missing schema: {bundle_schema.relative_to(root)}")
    load_json(profile_schema)
    load_json(bundle_schema)

    fixture_dir = root / "fixtures/multidomain"
    profiles = sorted(path for path in fixture_dir.glob("*.json") if path.is_file()) if fixture_dir.exists() else []
    if not profiles:
        fail("no multidomain agent runtime profile fixtures found")
    for fixture in profiles:
        validate_profile(fixture)

    evidence_dir = fixture_dir / "evidence"
    bundles = sorted(evidence_dir.glob("*.json")) if evidence_dir.exists() else []
    if not bundles:
        fail("no multidomain runtime evidence bundle fixtures found")
    for bundle in bundles:
        validate_evidence_bundle(bundle)

    print(f"OK: validated {len(profiles)} runtime profile fixture(s) and {len(bundles)} evidence bundle fixture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
