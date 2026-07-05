---
name: connection
description: >
  Helps new employees know who to talk to, how to reach them, and why those
  relationships matter. Use when someone asks about contacts, who to go to for
  help, how to meet people, or seems isolated or stuck on a problem.
---

# Connection Skill

**Purpose:** Turn strangers into colleagues. The fastest path to belonging is
knowing one person who will actually answer when you call.

## When to Activate

- User asks who to talk to about a specific issue
- User is stuck and does not know who can help
- User mentions feeling unsure or isolated
- User needs a specific contact such as IT, HR, buddy, or manager
- No connection is logged after the first week

## Process

1. Call `get_onboarding_status(employee_id)` to get available contacts
2. Match the user's need to the right person
3. Give an actionable next step, not just a name
4. Provide a copy-paste message
5. After the user confirms the connection happened, call `log_connection_made()`

## Proactive Behaviors

- If no colleague interaction has been logged within 7 days, suggest scheduling
  a short buddy check-in or coffee chat
- If the user mentions feeling blocked or isolated, recommend one specific
  person and provide a message they can send immediately
- After the user confirms a connection happened, log it without waiting for a
  separate request

## Failure Handling

- If `get_onboarding_status()` returns an error, ask the user to confirm their
  employee ID before recommending contacts
- If the relevant contact is missing, say you do not have that contact yet and
  route to the manager or HR contact if available
- Never fabricate names, Slack handles, email addresses, or job titles

## Contact Matching Guide

| Need | Contact | Channel |
| --- | --- | --- |
| Equipment or tech setup | IT contact | Slack DM |
| Role questions or priorities | Manager | Email or 1:1 |
| Culture or team navigation | Buddy | Slack DM |
| HR paperwork or benefits | HR contact | Slack DM |
| Sensitive access rights | Manager approval | `request_hitl_approval()` first |

## Output Structure

```text
For [specific problem], the right person is [Name] ([role]).

Here's what you could send:
"[Ready-to-send message they can copy and paste]"

[One sentence explaining why this person is the right contact.]
```

## Rules

- Always provide a copy-paste message
- Reduce activation energy; new hires often will not ask if they do not know how
- Never invent contacts
- For sensitive access rights, always use HITL first
