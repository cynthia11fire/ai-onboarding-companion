# AI Onboarding Companion - AGENTS.md

**Capstone Project | Google Vibe AI Agents Intensive 2026**  
Track: Enterprise Agents

## Mission

Help new employees go from feeling like outsiders to feeling like they belong
during their first 90 days, one conversation at a time.

The goal is not simply to complete onboarding, but to shorten
time-to-productivity while improving employee integration.

The gap this fills: most onboarding tools ask, "Did you sign the form?"  
This agent asks, "Do you know why any of this matters?"

## Architecture

```text
User
  -> onboarding_companion (root_agent)
      -> Skills
          -> administrative-support: paperwork, setup, access, blockers
          -> role-clarity: priorities, rationale, 30-day direction
          -> connection: who to talk to and how
          -> meaning: behavior-to-value reflection
      -> Tools
          -> get_onboarding_status()
          -> mark_task_complete()
          -> confirm_meaning_delivered()
          -> request_hitl_approval()
          -> log_connection_made()
          -> get_adaptation_score()
      -> Memory
          -> ONBOARDING_DB
              -> Procedural Memory: tasks, priorities, guardrails, tool flow
              -> Episodic Memory: achievements, behaviors, connections
              -> Adaptation State: clarity, connection, meaning, risk signals
```

## Course Concepts Demonstrated

| Day | Concept | Where |
| --- | --- | --- |
| Day 1 | Agent = Model + Harness | `root_agent` instruction + guardrails |
| Day 2 | Tool use | 6 custom tools |
| Day 3 | Agent Skills | 4 `SKILL.md` files |
| Day 3 | Memory / State | `ONBOARDING_DB` |
| Day 4 | HITL / Safety | `request_hitl_approval()` |
| Day 4 | Eval Suite | `eval/test_cases.json` |
| Day 5 | Spec-driven dev | `AGENTS.md` + `SKILL.md` + `eval/priority_and_privacy.feature` |

## Skills

### administrative-support

Loads when: user asks about paperwork, laptop, Slack setup, access, missing
steps, or process blockers.  
Output: one clean next step, correct contact if available, and HITL for
sensitive actions.

### role-clarity

Loads when: user asks about priorities, what to do, or feels lost.  
Output: top 3 actions with why-it-matters rationale connected to the 30-day
goal.

### connection

Loads when: user needs to reach someone or feels isolated.  
Output: right contact plus a copy-paste message.

### meaning

Loads when: task completed, user shares an achievement, or needs encouragement.  
Output: Behavior -> Motivation -> Value -> Meaning.

This is the differentiator. Other tools track tasks; this one helps people see
their own contribution. `confirm_meaning_delivered()` closes the loop by
marking meaning feedback as delivered before Meaning Score increases.

## Adaptation Score

| Dimension | Weight | Measures |
| --- | --- | --- |
| Clarity | 30% | Task completion and role understanding |
| Connection | 30% | Colleague interactions logged |
| Meaning | 40% | Value feedback delivered |

## Safety Guardrails

The agent must never:

- Grant system access without `request_hitl_approval()`
- Fabricate contact information
- Give praise without grounding it in observed behavior
- Mark tasks complete without calling `mark_task_complete()`

## Demo Flow

1. Safi introduces herself and the agent pulls onboarding status.
2. Safi asks what to do first and Role Clarity activates.
3. Safi completes laptop pickup and Meaning activates.
4. Safi asks who can help with Slack and Connection activates.
5. Safi requests finance dashboard access and HITL blocks the action.
6. Safi asks how onboarding is going and receives the adaptation score.
