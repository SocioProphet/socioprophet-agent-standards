#!/usr/bin/env python3
"""Validate WorkspaceContextFabricProfile fixtures."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas/workspace-context-fabric-profile.schema.json"
EXAMPLE = ROOT / "examples/workspace-context-fabric-profile.example.json"
INVALID = ROOT / "examples/workspace-context-fabric-profile.missing-surface.invalid.json"

REQUIRED_SURFACES = {
    "Workroom",
    "ProfessionalWorkroom",
    "ContextFabricContracts",
    "WorkspaceContextRecord",
    "WorkroomContextEvidence",
    "WorkspaceRecallPromotionPacket",
    "WorkspaceContextRegistryBinding",
    "EstateRegistration",
}

REQUIRED_REPOS = {
    "SocioProphet/prophet-workspace",
    "SocioProphet/prophet-platform",
    "SocioProphet/agentplane",
    "SocioProphet/memory-mesh",
    "SocioProphet/agent-registry",
    "SocioProphet/sociosphere",
}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_profile(path):
    data = load(path)
    assert data["apiVersion"] == "agent-standards.socioprophet.org/workspace-context-fabric/v0.1"
    assert data["kind"] == "WorkspaceContextFabricProfile"
    assert data["metadata"]["name"]
    assert data["metadata"]["profileVersion"]
    surfaces = {item["surface"] for item in data["requiredSurfaces"]}
    repos = set(data["owningRepositories"])
    missing_surfaces = REQUIRED_SURFACES - surfaces
    missing_repos = REQUIRED_REPOS - repos
    if missing_surfaces:
        raise AssertionError("missing surfaces: " + ", ".join(sorted(missing_surfaces)))
    if missing_repos:
        raise AssertionError("missing repos: " + ", ".join(sorted(missing_repos)))
    for item in data["requiredSurfaces"]:
        assert item["ownerRepo"]
        assert item["contractRef"]
        assert item.get("validationRef")
    assert data["validationRefs"]


def main():
    try:
        schema = load(SCHEMA)
        assert schema["title"] == "WorkspaceContextFabricProfile"
        validate_profile(EXAMPLE)
        try:
            validate_profile(INVALID)
        except AssertionError:
            pass
        else:
            raise AssertionError("negative fixture unexpectedly passed")
    except Exception as exc:
        print(f"ERR: {exc}", file=sys.stderr)
        return 2
    print("OK: WorkspaceContextFabricProfile validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
