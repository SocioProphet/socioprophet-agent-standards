.PHONY: validate multidomain-geospatial-agent-validate agent-action-trace-profile-validate

validate:
	./.venv/bin/python tools/validate_multidomain_geospatial_agent.py 2>/dev/null || python3 tools/validate_multidomain_geospatial_agent.py
	./.venv/bin/python tools/validate_agent_action_trace_profile.py 2>/dev/null || python3 tools/validate_agent_action_trace_profile.py

multidomain-geospatial-agent-validate:
	./.venv/bin/python tools/validate_multidomain_geospatial_agent.py 2>/dev/null || python3 tools/validate_multidomain_geospatial_agent.py

agent-action-trace-profile-validate:
	./.venv/bin/python tools/validate_agent_action_trace_profile.py 2>/dev/null || python3 tools/validate_agent_action_trace_profile.py
