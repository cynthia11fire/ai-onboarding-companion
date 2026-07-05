# AI Onboarding Companion

### Making the first 90 days clearer, calmer, and more human.

## Project Overview

AI Onboarding Companion is an enterprise onboarding agent built with Google Agent Development Kit (ADK). It supports new hires during their first 90 days by giving clear next-step guidance, answering everyday onboarding questions, coordinating across HR / manager / IT needs, and escalating sensitive or human-centered moments to the right person.

The project belongs to the Business Agent track because onboarding is a real operational challenge: it affects productivity, HR workload, manager visibility, employee confidence, and early retention.

Most onboarding systems manage tasks. AI Onboarding Companion guides people through organizational socialization.

## Problem

Employee onboarding is not handled by one person or one system.

A new hire needs to complete documents, pick up equipment, understand tools, learn team norms, ask small questions, and build confidence. HR needs to track progress. Managers need to know when support is needed. IT needs to coordinate accounts and devices.

In many organizations, these activities are fragmented across people, documents, chat messages, and disconnected systems. As a result, new hires often ask:

- What should I do next?
- Who should I ask?
- Is this question too small to ask?
- Am I adapting well?
- Do I belong here?

The goal of this project is not only to finish onboarding tasks faster. The goal is to help new hires become productive, connected, and confident during their first 90 days.

## Why an AI Agent?

A traditional chatbot can answer isolated questions.

An AI Agent can coordinate a journey.

AI Onboarding Companion uses onboarding state, tools, memory, skills, and guardrails to decide what support is useful next. It does not simply answer questions. It checks the employee's current onboarding status, recommends the highest-priority next step, routes questions to the right contact, records completed progress, and triggers human approval when needed.

This makes the Agent useful for real onboarding workflows where context, safety, and timing matter.

## Core Product Idea

The product is built around one principle:

**AI supports people. It does not replace them.**

For the new hire, the Agent reduces uncertainty and provides one clear step at a time.

For HR and managers, the Agent highlights support moments: situations where a new hire may benefit from human help, such as repeated confusion, missing key steps, no connection made yet, or a sensitive access request.

The system avoids framing employees as performance scores. It focuses on support, clarity, and timely human connection.

## Agent Capabilities

The Agent combines four modular skills.

### 1. Administrative Support

Guides onboarding administration such as HR documents, laptop pickup, NDA, Slack setup, system access, training tasks, and process questions.

It reduces friction by giving one small next action instead of overwhelming the new hire with a long checklist.

### 2. Role Clarity

Helps the new hire understand what matters most right now.

The Agent uses task priority, day number, and onboarding state to recommend the top priorities for today. It explains why each task matters, not just what the task is.

### 3. Connection and Socialization

Helps new hires navigate people, processes, and everyday workplace norms.

This includes questions such as who to contact, how to ask for help, what tools the team uses, how to reach IT, or where to confirm policies such as dress code. The Agent does not invent company policy. If the exact information is unavailable, it gives a safe general suggestion and routes the user to HR, manager, IT, or buddy.

### 4. Meaning

Transforms completed onboarding activities into evidence-based reflection using:

**Behavior -> Motivation -> Value -> Meaning**

Instead of giving generic praise, the Agent grounds feedback in observed completed tasks. Meaning Score only increases after the Agent actually delivers grounded meaning feedback and calls `confirm_meaning_delivered()`.

## Technical Architecture

The implementation uses Google ADK with a SkillToolset-based architecture.

Key components:

- `agent.py`: root ADK re-export
- `onboarding_companion/agent.py`: ADK root agent, instructions, guardrails, SkillToolset, model configuration, and tool registration
- `onboarding_companion/tools.py`: onboarding tools, shared memory, task updates, HITL approval, connection logging, and adaptation scoring
- `skills/*/SKILL.md`: four modular skill definitions
- `ONBOARDING_DB`: in-memory onboarding state for the prototype
- `eval/test_cases.json`: evaluation scenarios
- `eval/priority_and_privacy.feature`: Gherkin behavior specification
- `demo_ui/`: local product demo UI for storytelling
- `AGENTS.md`: system blueprint

The current prototype simulates enterprise systems through Python tools. In a production deployment, the same tool boundaries could connect to HRIS, Google Workspace, Slack, Microsoft 365, IT service desk systems, or e-signature workflows.

## Course Concepts Demonstrated

| Course Concept | Implementation |
| --- | --- |
| Agent with ADK | Google ADK root agent with model, instructions, tools, and guardrails |
| Tool Use | Six custom Python tools for status retrieval, task completion, HITL, connection logging, scoring, and meaning confirmation |
| Skills | Four modular skills loaded through SkillToolset |
| Memory | `ONBOARDING_DB` stores profile, tasks, contacts, behaviors, achievements, connections, and adaptation state |
| Human-in-the-Loop | Sensitive actions call `request_hitl_approval()` before proceeding |
| Evaluation | JSON test cases and Gherkin scenarios define expected behavior |
| Spec-driven Development | `AGENTS.md`, `SKILL.md`, and `.feature` files describe the intended behavior before implementation |

## Safety and Privacy

Onboarding involves personal data, access requests, HR decisions, and workplace policy. The Agent includes safety boundaries:

- It does not grant sensitive access directly.
- It does not invent contacts, policies, or completed work.
- It uses Human-in-the-Loop approval for finance, legal, payroll, contracts, personal data, and system access.
- It avoids employee-facing language such as "risk" or "monitoring" and uses supportive framing instead.
- It routes uncertain policy questions to the right human contact instead of guessing.

Example: if a user asks for finance dashboard access, the Agent does not approve the request itself. It creates a pending approval request for the manager.

## Evaluation

The project includes structured evaluation artifacts.

The Gherkin specification defines expected behavior for priority guidance and privacy protection. For example:

```gherkin
Feature: Priority and Privacy Safe Onboarding

Scenario: New hire asks what to do next
  Given the agent has retrieved onboarding status
  When the user asks what to focus on today
  Then the agent should recommend incomplete tasks by priority
  And explain why each task matters
```

The evaluation checks whether the Agent:

- retrieves onboarding state before giving personalized guidance
- recommends incomplete tasks using priority metadata
- explains why each task matters
- avoids exposing unnecessary private information
- requests human approval before sensitive actions
- updates Meaning Score only after meaning feedback is delivered

## Demo Flow

The demo is designed to show both the new hire experience and the HR support perspective.

1. A new hire opens **Your First Day**.
2. The Agent welcomes Safi and recommends one clear first step.
3. Safi asks what to focus on today.
4. The Agent uses onboarding memory to recommend top priorities.
5. Safi asks everyday workplace questions such as NDA, IT contact, dress code, and communication tools.
6. The Agent answers safely: it gives general guidance where appropriate and routes company-specific questions to the right person.
7. The demo shows how the same onboarding journey can create support moments for HR and managers.

The product UI is intentionally calm and practical. It is closer to a guided journey than a chatbot. The new hire should feel: "I know what to do next."

## What Makes This Different

Success is not measured by completed tasks alone.

It is measured by whether new hires become productive, connected, and confident during their first 90 days.

Every onboarding activity becomes an opportunity to provide the right support for the right person at the right time.

## Current Limitations and Roadmap

The current project is a working capstone prototype. It uses an in-memory database and simulated enterprise tools.

Future enterprise capabilities include:

- authentication
- role-based access control
- audit logging
- secure document handling
- HRIS integration
- Google Calendar / Gmail / Slack / Microsoft 365 integration
- digital signature workflows
- production deployment on Cloud Run or similar infrastructure

These are intentionally treated as roadmap items so the capstone can focus on the agent behavior, tool boundaries, memory, safety, and evaluation design.

## Final Reflection

AI Onboarding Companion demonstrates how an AI Agent can support organizational socialization, not just task completion.

It coordinates onboarding steps, remembers progress, uses tools, respects safety boundaries, and helps human support arrive when it matters most.

The long-term vision is simple:

**Make the first 90 days clearer, calmer, and more human.**

The goal is not to replace HR. It is to make every human conversation happen at the right moment.

