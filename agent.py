"""
Root ADK entrypoint.

The merged agent implementation lives in onboarding_companion.agent so the
project has one source of truth for tools, skills, and guardrails.
"""

try:
    from .onboarding_companion.agent import root_agent
except ImportError:
    from onboarding_companion.agent import root_agent
