---
name: role-clarity
description: >
  Helps new employees understand their priorities, success criteria, and what
  to focus on right now. Use when someone asks what they should do, what matters
  most, feels uncertain about their role, or needs a prioritized action list.
---

# Role Clarity Skill

**Purpose:** Eliminate the number one source of new hire anxiety: not knowing
what to do.

## When to Activate

- User asks what to do today or this week
- User asks what matters most right now
- User expresses confusion about priorities or role
- User just completed something and needs to know what comes next
- Day 1 starts and the agent should proactively generate a priority guide

## Process

1. Call `get_onboarding_status(employee_id)` to load current task state
2. Identify the top 3 pending tasks most relevant to the current day
3. For each task, explain why it matters
4. Connect today's work to the employee's 30-day goal

## Proactive Behaviors

- If Day 1 starts and the employee has not asked for help, proactively generate
  a priority guide from the top due-now tasks
- If the employee completes a task, suggest the next highest-priority task
- If low clarity risk is active, summarize the smallest next three actions

## Failure Handling

- If `get_onboarding_status()` returns an error, ask the user to confirm their
  employee ID instead of guessing
- If there are no pending tasks, shift to next-week success criteria
- If task priority metadata is missing, say the task order is uncertain and use
  day number plus available task labels rather than inventing priority

## Output Structure

```text
Day [X] Priority Guide for [Name]:

1. [Task Name] - [Why this matters right now]
2. [Task Name] - [Why this matters right now]
3. [Task Name] - [Why this matters right now]

These three things will set you up for [specific outcome by Day 30].
```

## Rules

- Never list tasks without rationale
- Always connect small daily actions to a larger purpose
- Use actual role and task names from the database
- If all tasks are done, shift to what makes the next week successful
