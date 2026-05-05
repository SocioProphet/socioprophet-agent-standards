#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_TOP = ["apiVersion", "kind", "metadata", "spec"]
REQUIRED_METADATA = ["name", "profileVersion"]
REQUIRED_SPEC = ["ontologyRef", "standardsRef", "agent", "capabilities", "tracePatterns", "evidence"]
REQUIRED_AGENT = ["subjectRef", "runtimeRole"]
REQUIRED_EVIDENCE = ["requiresPolicyRef", "requiresReceiptRef"]
EXPECTED_API_VERSION = "agent-standards.socioprophet.org/v0.1"
EXPECTED_KIND = "AgentActionTraceProfile"
REQUIRED_TRACE_PATTERNS = {"ContractNet", "PubSub"}


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


def require_non_empty_string(value: object, where: str) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(f"{where}: expected non-empty string")


def require_non_empty_string_array(value: object, where: str) -> list[str]:
    if not isinstance(value, list) or not value:
        fail(f"{where}: expected non-empty array")
    out: list[str] = []
    for idx, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(f"{where}[{idx}]: expected non-empty string")
        out.append(item)
    return out


def validate_schema(path: Path) -> None:
    data = load_json(path)
    if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        fail(f"{path}: expected JSON Schema draft 2020-12")
    if data.get("title") != EXPECTED_KIND:
        fail(f"{path}: expected title {EXPECTED_KIND}")
    props = data.get("properties")
    if not isinstance(props, dict):
        fail(f"{path}: properties must be object")
    if props.get("apiVersion", {}).get("const") != EXPECTED_API_VERSION:
        fail(f"{path}: apiVersion const must be {EXPECTED_API_VERSION}")
    if props.get("kind", {}).get("const") != EXPECTED_KIND:
        fail(f"{path}: kind const must be {EXPECTED_KIND}")


def validate_profile(path: Path) -> None:
    data = load_json(path)
    require_keys(data, REQUIRED_TOP, str(path))
    if data.get("apiVersion") != EXPECTED_API_VERSION:
        fail(f"{path}: apiVersion must be {EXPECTED_API_VERSION}")
    if data.get("kind") != EXPECTED_KIND:
        fail(f"{path}: kind must be {EXPECTED_KIND}")

    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        fail(f"{path}: metadata must be object")
    require_keys(metadata, REQUIRED_METADATA, f"{path}:metadata")
    require_non_empty_string(metadata.get("name"), f"{path}:metadata.name")
    require_non_empty_string(metadata.get("profileVersion"), f"{path}:metadata.profileVersion")

    spec = data.get("spec")
    if not isinstance(spec, dict):
        fail(f"{path}: spec must be object")
    require_keys(spec, REQUIRED_SPEC, f"{path}:spec")

    ontology_ref = spec.get("ontologyRef")
    standards_ref = spec.get("standardsRef")
    require_non_empty_string(ontology_ref, f"{path}:spec.ontologyRef")
    require_non_empty_string(standards_ref, f"{path}:spec.standardsRef")
    if "SocioProphet/ontogenesis" not in ontology_ref:
        fail(f"{path}: ontologyRef must point to SocioProphet/ontogenesis")
    if "SocioProphet/socioprophet-standards-storage" not in standards_ref:
        fail(f"{path}: standardsRef must point to SocioProphet/socioprophet-standards-storage")

    agent = spec.get("agent")
    if not isinstance(agent, dict):
        fail(f"{path}: spec.agent must be object")
    require_keys(agent, REQUIRED_AGENT, f"{path}:spec.agent")
    require_non_empty_string(agent.get("subjectRef"), f"{path}:spec.agent.subjectRef")
    require_non_empty_string(agent.get("runtimeRole"), f"{path}:spec.agent.runtimeRole")

    capabilities = require_non_empty_string_array(spec.get("capabilities"), f"{path}:spec.capabilities")
    trace_patterns = set(require_non_empty_string_array(spec.get("tracePatterns"), f"{path}:spec.tracePatterns"))
    missing_patterns = sorted(REQUIRED_TRACE_PATTERNS - trace_patterns)
    if missing_patterns:
        fail(f"{path}: spec.tracePatterns missing required bootstrap pattern(s): {', '.join(missing_patterns)}")
    if not any(cap in capabilities for cap in ("writeTrace", "executeTask", "consume")):
        fail(f"{path}: capabilities must include at least one runtime action capability")

    evidence = spec.get("evidence")
    if not isinstance(evidence, dict):
        fail(f"{path}: spec.evidence must be object")
    require_keys(evidence, REQUIRED_EVIDENCE, f"{path}:spec.evidence")
    if evidence.get("requiresPolicyRef") is not True:
        fail(f"{path}: spec.evidence.requiresPolicyRef must be true")
    if evidence.get("requiresReceiptRef") is not True:
        fail(f"{path}: spec.evidence.requiresReceiptRef must be true")


def expect_profile_failure(path: Path) -> None:
    try:
        validate_profile(path)
    except SystemExit as exc:
        if exc.code == 2:
            print(f"OK: {path.name} failed as expected")
            return
        raise
    fail(f"{path}: invalid profile unexpectedly passed")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    schema = root / "schemas" / "agent-plane" / "agent-action-trace-profile.schema.json"
    example = root / "examples" / "agent-action-trace-profile.example.json"
    invalid_wrong_ontology = root / "examples" / "agent-action-trace-profile.invalid-wrong-ontology-ref.json"
    invalid_no_policy = root / "examples" / "agent-action-trace-profile.invalid-no-policy-ref.json"

    for required_path in (schema, example, invalid_wrong_ontology, invalid_no_policy):
        if not required_path.exists():
            fail(f"missing file: {required_path.relative_to(root)}")

    validate_schema(schema)
    validate_profile(example)
    expect_profile_failure(invalid_wrong_ontology)
    expect_profile_failure(invalid_no_policy)

    print("OK: validated AgentActionTraceProfile schema, example, and negative fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
