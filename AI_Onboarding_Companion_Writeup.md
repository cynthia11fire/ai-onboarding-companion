# AI Onboarding Companion

### Making the first 90 days clearer, calmer, and more human.

## Project Overview

AI Onboarding Companion is an AI Agent built with Google Agent Development Kit (ADK) to support employee onboarding.

The project focuses on a common enterprise problem: onboarding is not handled by one person or one system. New hires need guidance, HR needs progress visibility, managers need to know when to support, and IT or internal teams often need to help with access, tools, or workplace processes.

Traditional onboarding systems usually track task completion. This project explores how an AI Agent can guide a new hire through organizational socialization: understanding what to do next, who to ask, how the company works, and when human support is needed.

The goal is not only to complete onboarding tasks faster. The goal is to help new hires become productive, connected, and confident during their first 90 days.

---

## Why an AI Agent?

A traditional chatbot can answer isolated questions.

An AI Agent can coordinate a journey.

AI Onboarding Companion demonstrates agentic behavior by combining:

- structured onboarding skills
- tool-based workflow execution
- shared onboarding memory
- human-in-the-loop approval
- evaluation scenarios for priority and privacy behavior

The Agent does not simply respond to questions. It uses onboarding state to decide what guidance is useful next.

---

## Core Skills

### 1. Administrative Support

Helps new hires complete onboarding tasks such as required documents, equipment setup, system access, and training steps.

### 2. Role Clarity

Helps new hires understand what matters most right now, why a task is important, and how today's work connects to onboarding progress.

### 3. Connection and Socialization

Helps new hires navigate people, processes, and everyday workplace norms.

This includes questions such as who to contact, where to find resources, how to ask for help, where workplace routines live, and when a human should be involved.

### 4. Meaning

Transforms completed onboarding activities into evidence-based reflection using:

**Behavior -> Motivation -> Value -> Meaning**

Instead of giving empty praise or evaluating the employee, the Agent connects observed progress to confidence, connection, and integration.

---

## Technical Implementation

This project uses Google ADK with a modular SkillToolset architecture.

Key files include:

- `onboarding_companion/agent.py`  
  Defines the root ADK Agent, model configuration, tools, and SkillToolset.

- `onboarding_companion/tools.py`  
  Implements onboarding tools, memory updates, HITL approval, connection logging, and adaptation scoring.

- `skills/*/SKILL.md`  
  Defines four structured skills with activation conditions, reasoning process, output behavior, proactive behavior, and failure handling.

- `eval/test_cases.json`  
  Contains evaluation scenarios for the agent behavior.

- `eval/priority_and_privacy.feature`  
  Uses Gherkin scenarios to define expected behavior for priority guidance, privacy protection, and human approval.

---

## Course Concepts Demonstrated

| Course Concept | Implementation |
| --- | --- |
| Agent = Model + Harness | ADK root agent with instructions, tools, and guardrails |
| Tool Use | Custom onboarding tools for task completion, status retrieval, HITL, connection logging, and scoring |
| Skills | Four modular `SKILL.md` files loaded through SkillToolset |
| Memory | `ONBOARDING_DB` stores profile, tasks, achievements, connections, and adaptation state |
| Human-in-the-Loop | Sensitive actions require `request_hitl_approval()` |
| Evaluation | JSON test cases and Gherkin behavior specifications |
| Spec-driven Development | `AGENTS.md`, `SKILL.md`, and `.feature` files define expected behavior |

---

## Evaluation and Safety

The project includes structured evaluation using both JSON test cases and Gherkin specifications.

Example:

```gherkin
Feature: Priority and Privacy Safe Onboarding

Scenario: New hire asks what to do next
  Given the agent has retrieved onboarding status
  When the user asks what to focus on today
  Then the agent should recommend incomplete tasks by priority
  And explain why each task matters
```

The evaluation focuses on whether the Agent:

- retrieves onboarding state before giving guidance
- prioritizes incomplete tasks correctly
- explains the reason behind recommendations
- avoids exposing private employee data unnecessarily
- requests human approval before sensitive actions
- updates Meaning Score only after meaning feedback is delivered

This is important because enterprise onboarding involves personal data, access requests, and HR decisions. The Agent must be helpful without becoming unsafe or overly autonomous.

---

## Demo Flow

The demo shows two main views.

### 1. Your First Day

The new hire sees one clear next step instead of a crowded dashboard.

The Agent helps answer:

- What should I do next?
- Why does this matter?
- Who can help me?
- Can I ask this safely?

### 2. Support Center

HR sees where additional support may be useful.

The focus is not performance scoring. The focus is identifying support moments, such as:

- repeated confusion
- missed onboarding steps
- no connection made yet
- sensitive access request requiring approval

The Agent helps HR and managers support people at the right time.

---

## What Makes This Different?

Success is not measured by completed tasks alone.

It is measured by whether new hires become productive, connected, and confident during their first 90 days.

Every onboarding activity becomes an opportunity to provide the right support for the right person at the right time.

---

## Future Roadmap

Future enterprise capabilities include:

- authentication
- role-based access control
- audit logging
- secure document handling
- HRIS integration
- Slack / Microsoft 365 / Google Workspace integration
- digital signature workflows
- manager notification workflows

These are not required for the current prototype, but they define the path from capstone demo to enterprise-ready product.

---

## Final Reflection

AI Onboarding Companion shows how an AI Agent can support organizational socialization, not just task completion.

It coordinates onboarding steps, remembers progress, uses tools, respects safety boundaries, and helps human support arrive when it matters most.

The long-term vision is simple:

**AI supports people. It does not replace them.**
