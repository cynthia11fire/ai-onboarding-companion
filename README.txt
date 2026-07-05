# AI Onboarding Companion

> From outsider to insider in 90 days, one conversation at a time.

**Google Vibe AI Agents Intensive 2026 | Enterprise Agents Track**

Most onboarding tools ask, "Did you sign the form?"

This agent asks, "Do you know why any of this matters?"

Traditional onboarding measures completion. This project measures integration:
whether a new hire understands their role, builds real relationships, and
develops a sense of belonging.

Designed to reduce onboarding friction, accelerate employee integration, and
surface early attrition risks before they become HR problems.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env: GOOGLE_GENAI_API_KEY=your_key_here
adk web .
```

Open http://localhost:8000 and select `onboarding_companion`.

## Try It

Start with:

```text
Hi, I'm Safi. It's my first day!
```

Then try:

- `What should I focus on today?`
- `I just picked up my laptop from Kevin.`
- `I need help setting up Slack. Who should I ask?`
- `Can you give me access to the finance dashboard?`
- `How am I doing so far?`

## Project Structure

```text
onboarding_agent/
  agent.py                         Root ADK agent with SkillToolset demo
  onboarding_companion/            Package entrypoint for adk web/adk run
    agent.py                       Agent + SkillToolset configuration
    tools.py                       Onboarding tools and in-memory state
  skills/
    administrative-support/SKILL.md
    role-clarity/SKILL.md
    connection/SKILL.md
    meaning/SKILL.md
  eval/test_cases.json             Evaluation scenarios
  eval/priority_and_privacy.feature Gherkin spec for priority + privacy
  AGENTS.md                        System blueprint
  run_demo.py                      Scripted 6-step demo
```

## Course Concepts

| Concept | Implementation |
| --- | --- |
| Agent = Model + Harness | `root_agent` instruction and guardrails |
| Tool Use | 6 custom Python tools |
| Skills | 4 SKILL.md files |
| Memory | `ONBOARDING_DB` procedural and episodic state |
| HITL Safety | `request_hitl_approval()` blocks sensitive actions |
| Eval Suite | `eval/test_cases.json` |
| Spec-driven Development | `AGENTS.md`, `SKILL.md`, and Gherkin feature specs |
