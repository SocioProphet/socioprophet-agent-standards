# asa-triune Architecture — Conformance Reference

Status: normative reference pointer.

The `asa-triune` agent architecture claim is specified and conformance-checked in
`SocioProphet/superconscious`. This standards repo **references** that checklist
as the normative pass/fail point for any agent declaring
`architecture: asa-triune`; it is not re-specified here.

- Architecture spec: `SocioProphet/superconscious:docs/asa-triune-architecture.v0.1.md`
- Conformance checklist (normative pass/fail): `SocioProphet/superconscious:docs/asa-triune-conformance-checklist.v0.1.md`
- Tracking issue: `SocioProphet/superconscious#79`

Level markers in that checklist (C1/C2/C3) align with
`conformance/CONFORMANCE-CRITERIA-0001.md`. A profile that admits the
`asa-triune` claim MUST enforce all MUST items in the referenced checklist,
including its falsification obligation (one passing fixture and one deliberately
non-conformant fixture that fails).
