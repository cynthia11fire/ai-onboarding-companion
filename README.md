# AI Onboarding Companion

### Making the first 90 days clearer, calmer, and more human.

AI Onboarding Companion is an AI Agent built with Google Agent Development Kit (ADK) to support employee onboarding.

It helps new hires understand what comes next, handles everyday onboarding questions, reduces administrative coordination for HR, and helps managers or HR step in when human judgment or support is needed.

The Agent helps coordinate the new hire's organizational socialization journey across people, workplace systems, and onboarding workflows.

---

## Why This Project?

Employee onboarding is one of the most collaborative processes inside an organization.

New hires complete paperwork, attend training, request system access, learn new tools, and try to understand how daily work actually happens. At the same time, HR tracks progress, managers coordinate onboarding activities, and IT prepares accounts and permissions.

Although these activities share the same goal, they are often distributed across different teams and systems. This makes onboarding time-consuming, fragmented, and inconsistent.

AI Onboarding Companion is designed to simplify coordination while improving the experience for everyone involved.

> **From paperwork to belonging.**
>
> Most onboarding systems manage tasks.
> AI Onboarding Companion guides people through organizational socialization.

---

## What Makes This Different?

Traditional onboarding systems primarily focus on process completion.

AI Onboarding Companion focuses on helping people successfully move through the onboarding journey.

Instead of simply tracking completed tasks, the Agent:

- provides contextual guidance for new hires
- answers everyday workplace questions before they become blockers
- reduces repetitive coordination for HR
- helps managers know when support matters most
- transforms onboarding activities into meaningful progress

Success is not measured by completed tasks alone.

It is measured by whether new hires become productive, connected, and confident during their first 90 days.

Every onboarding activity becomes an opportunity to provide the right support for the right person at the right time.

---

## One Event. Three Perspectives.

Every onboarding event creates value for multiple people.

| Perspective | Traditional Onboarding | AI Onboarding Companion |
|------------|------------------------|--------------------------|
| New Hire | Receives a confirmation message | Receives clear next-step guidance and meaningful support |
| HR | Tracks progress manually | Receives automatic milestone updates and support moments |
| Manager | Has limited visibility | Knows when the employee is ready for the next onboarding stage |

The same onboarding event produces different information for different stakeholders.

The Agent coordinates these perspectives through a single workflow.

---

## Core Skills

The Agent combines four complementary skills.

### 1. Administrative Support

Guides administrative onboarding tasks such as paperwork, equipment setup, system access, required training, and common process questions.

Examples include HR documents, laptop pickup, Slack setup, access requests, leave forms, repair requests, and onboarding checklists.

### 2. Role Clarity

Helps employees understand priorities, expectations, and what they should focus on next.

Rather than showing a long task list, the Agent recommends the most relevant next step and explains why it matters.

### 3. Connection and Socialization

Helps new hires navigate people, processes, and everyday workplace norms.

This includes questions that are often not documented clearly, such as who to ask, where common resources are, how internal processes work, where to go for lunch, how parking works, and what informal norms shape daily work.

The Agent handles everyday onboarding questions first, and escalates to HR, managers, IT, or other people only when human judgment or support is needed.

### 4. Meaning

Transforms completed onboarding activities into meaningful feedback using:

**Behavior -> Motivation -> Value -> Meaning**

Rather than simply confirming task completion, the Agent helps new hires understand how each step contributes to becoming part of the organization.

Meaning feedback is evidence-based. The Agent does not praise or judge employees without grounding feedback in observed behavior.

---

## Technical Highlights

This project demonstrates an enterprise-oriented AI Agent using Google ADK.

Key implementation includes:

- `onboarding_companion/agent.py`: Google ADK root agent with SkillToolset
- `onboarding_companion/tools.py`: six custom onboarding tools and shared memory
- `skills/*/SKILL.md`: four modular skill definitions
- `ONBOARDING_DB`: shared onboarding memory for tasks, contacts, behaviors, achievements, connections, and adaptation state
- `request_hitl_approval()`: Human-in-the-Loop approval for sensitive actions
- `confirm_meaning_delivered()`: closed-loop Meaning Score update
- `eval/test_cases.json`: evaluation scenarios
- `eval/priority_and_privacy.feature`: Gherkin scenarios for priority logic and privacy protection

The project demonstrates how AI Agents can coordinate people, tools, memory, and workflows, not simply answer questions.

---

## Demo Flow

1. A new hire opens **Your First Day**.
2. The Agent recommends the next onboarding step.
3. The user asks everyday onboarding questions in a safe-to-ask interface.
4. The user completes an onboarding task.
5. Role Clarity, Connection and Socialization, and Meaning Skills provide personalized guidance.
6. Sensitive access requests trigger Human-in-the-Loop approval.
7. HR reviews support moments through **Support Center**.

---

## Try It

Start the ADK web app:

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env: GOOGLE_GENAI_API_KEY=your_key_here
adk web .
```

Open http://localhost:8000 and select `onboarding_companion`.

Try these prompts:

```text
Hi, I'm Safi. It's my first day!
What should I focus on today?
I just picked up my laptop from Kevin.
I need help setting up Slack. Who should I ask?
Can you give me access to the finance dashboard?
How am I doing so far?
```

The project also includes a local demo UI for product storytelling:

```text
demo_ui/
```

---

## Project Structure

```text
onboarding_agent/
  agent.py                         Root ADK re-export
  onboarding_companion/
    agent.py                       Google ADK root agent with SkillToolset
    tools.py                       Onboarding tools and ONBOARDING_DB memory
  skills/
    administrative-support/SKILL.md
    role-clarity/SKILL.md
    connection/SKILL.md
    meaning/SKILL.md
  eval/
    test_cases.json                Evaluation scenarios
    priority_and_privacy.feature   Gherkin spec for priority + privacy
  demo_ui/                         Local product demo UI
  AGENTS.md                        System blueprint
  run_demo.py                      Scripted demo conversation
  requirements.txt
  .env.example
```

---

## Design Principles

- Human-centered AI
- One step at a time
- Safe-to-Ask interactions
- Evidence-based feedback
- Human-in-the-Loop for sensitive actions
- Privacy-aware design
- Support moments instead of performance judgment

---

## Future Roadmap

The current prototype focuses on onboarding experience.

Future enterprise capabilities include:

- Authentication
- Role-Based Access Control
- Audit Logging
- Secure Document Handling
- HRIS Integration
- Calendar, Slack, Microsoft 365, or Google Workspace integration
- Workflow Automation

---

## Vision

Every organization welcomes new employees.

Not every organization has the resources to provide a structured onboarding experience.

AI Onboarding Companion aims to help organizations of any size deliver onboarding that is more coordinated, more supportive, and more human.

AI supports people.

It does not replace them.

