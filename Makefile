.PHONY: validate multidomain-geospatial-agent-validate

validate:
	./.venv/bin/python tools/validate_multidomain_geospatial_agent.py 2>/dev/null || python3 tools/validate_multidomain_geospatial_agent.py

multidomain-geospatial-agent-validate:
	./.venv/bin/python tools/validate_multidomain_geospatial_agent.py 2>/dev/null || python3 tools/validate_multidomain_geospatial_agent.py
