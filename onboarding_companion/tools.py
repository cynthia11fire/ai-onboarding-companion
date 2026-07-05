"""
Onboarding Companion tools.

These functions simulate the MCP-connected systems a production onboarding
agent would call: HRIS, IT service desk, access approval workflow, and employee
experience analytics.
"""

from datetime import datetime


ONBOARDING_DB = {
    "safi": {
        "name": "Safi",
        "role": "Product Designer",
        "department": "Design Team",
        "start_date": "2026-06-24",
        "day_in_role": 1,
        "day_number": 1,
        "buddy": {
            "name": "Maya Chen",
            "slack": "@maya.chen",
            "role": "Design Team Buddy",
        },
        "manager": {
            "name": "David Lee",
            "slack": "@david.lee",
            "role": "Design Director",
        },
        "it_contact": {
            "name": "Kevin Wu",
            "slack": "@kevin.wu",
            "role": "IT Support",
        },
        "hr_contact": {
            "name": "Mina Lee",
            "slack": "@mina.lee",
            "role": "People Operations",
        },
        "tasks": {
            "hr_documents": {
                "done": False,
                "label": "Submit HR documents",
                "day": 1,
                "priority": 1,
                "category": "administrative",
            },
            "laptop_pickup": {
                "done": False,
                "label": "Pick up laptop from IT",
                "day": 1,
                "priority": 2,
                "category": "administrative",
            },
            "nda_signed": {
                "done": False,
                "label": "Sign NDA on 3F",
                "day": 1,
                "priority": 3,
                "category": "administrative",
            },
            "buddy_meeting": {
                "done": False,
                "label": "Schedule a 15-minute buddy check-in",
                "day": 1,
                "priority": 4,
                "category": "connection",
            },
            "slack_setup": {
                "done": False,
                "label": "Set up Slack and join team channels",
                "day": 1,
                "priority": 5,
                "category": "administrative",
            },
            "system_access": {
                "done": False,
                "label": "Confirm required system access",
                "day": 2,
                "priority": 6,
                "category": "administrative",
            },
            "manager_1on1": {
                "done": False,
                "label": "Schedule first manager 1-on-1",
                "day": 3,
                "priority": 7,
                "category": "role_clarity",
            },
            "team_intro": {
                "done": False,
                "label": "Introduce yourself in the Design Team channel",
                "day": 3,
                "priority": 8,
                "category": "connection",
            },
            "first_week_training": {
                "done": False,
                "label": "Complete first-week product onboarding training",
                "day": 7,
                "priority": 9,
                "category": "role_clarity",
            },
        },
        "connections_logged": [],
        "behaviors": [],
        "achievements": [],
        "hitl_requests": [],
        "adaptation_score": {
            "clarity": 0,
            "connection": 0,
            "meaning": 0,
        },
    }
}


def _clarity_score(emp: dict) -> float:
    total = len(emp["tasks"])
    done = sum(1 for task in emp["tasks"].values() if task["done"])
    return round((done / total) * 100, 1) if total else 0


def _connection_score(emp: dict) -> float:
    return min(len(emp["connections_logged"]) * 20, 100)


def _meaning_score(emp: dict) -> float:
    return emp["adaptation_score"]["meaning"]


def _sync_adaptation_score(emp: dict) -> dict:
    emp["adaptation_score"]["clarity"] = _clarity_score(emp)
    emp["adaptation_score"]["connection"] = _connection_score(emp)
    emp["adaptation_score"]["meaning"] = _meaning_score(emp)
    return emp["adaptation_score"]


def _risk_signals(emp: dict) -> list[str]:
    risks = []

    if emp["day_in_role"] >= 2:
        day1_keys = ["hr_documents", "laptop_pickup", "nda_signed"]
        if not all(emp["tasks"][key]["done"] for key in day1_keys):
            risks.append(
                "Day 1 administrative tasks are still incomplete; reduce friction before it becomes anxiety."
            )

    if emp["day_in_role"] >= 3 and not emp["tasks"]["manager_1on1"]["done"]:
        risks.append(
            "No manager 1-on-1 is logged yet; role clarity may be at risk."
        )

    if emp["day_in_role"] >= 7 and len(emp["connections_logged"]) == 0:
        risks.append(
            "No colleague connections are logged after the first week; belonging may be at risk."
        )

    if _clarity_score(emp) < 30 and emp["day_in_role"] >= 3:
        risks.append(
            "Task progress is low for this stage; the new hire may need a clearer priority path."
        )

    return risks


def get_onboarding_status(employee_id: str) -> dict:
    """
    Retrieve the current onboarding status for an employee.

    Args:
        employee_id: Employee ID, for example "safi".

    Returns:
        Current employee state, contacts, tasks, recent behaviors, and risk signals.
    """
    emp_id = employee_id.lower().strip()
    if emp_id not in ONBOARDING_DB:
        return {"error": f"Employee '{employee_id}' was not found."}

    emp = ONBOARDING_DB[emp_id]
    _sync_adaptation_score(emp)
    pending = [
        {
            "task_id": task_id,
            **{k: v for k, v in task.items() if k != "done"},
            "is_due_now": task["day"] <= emp["day_number"],
        }
        for task_id, task in emp["tasks"].items()
        if not task["done"]
    ]
    completed = [
        {"task_id": task_id, "label": task["label"]}
        for task_id, task in emp["tasks"].items()
        if task["done"]
    ]
    pending.sort(
        key=lambda task: (
            not task["is_due_now"],
            task["day"],
            task["priority"],
        )
    )

    return {
        "name": emp["name"],
        "role": emp["role"],
        "department": emp["department"],
        "day_in_role": emp["day_in_role"],
        "day_number": emp["day_number"],
        "buddy": emp["buddy"],
        "manager": emp["manager"],
        "it_contact": emp["it_contact"],
        "hr_contact": emp["hr_contact"],
        "pending_tasks": pending[:5],
        "completed_tasks": completed,
        "achievements": emp["achievements"][-5:],
        "adaptation_score": emp["adaptation_score"],
        "recent_behaviors": emp["behaviors"][-3:],
        "connections_logged": emp["connections_logged"][-3:],
        "risk_signals": _risk_signals(emp),
    }


def mark_task_complete(employee_id: str, task_id: str) -> dict:
    """
    Mark a tracked onboarding task complete and log an observable behavior.

    Args:
        employee_id: Employee ID.
        task_id: Task ID, for example "laptop_pickup" or "nda_signed".

    Returns:
        Updated progress and a signal that Meaning Skill should respond.
    """
    emp_id = employee_id.lower().strip()
    if emp_id not in ONBOARDING_DB:
        return {"error": f"Employee '{employee_id}' was not found."}

    emp = ONBOARDING_DB[emp_id]
    if task_id not in emp["tasks"]:
        return {
            "error": f"Task '{task_id}' was not found.",
            "valid_task_ids": list(emp["tasks"].keys()),
        }

    task = emp["tasks"][task_id]
    if task["done"]:
        return {
            "already_complete": True,
            "task_id": task_id,
            "task": task["label"],
        }

    task["done"] = True
    behavior = {
        "task_id": task_id,
        "label": task["label"],
        "completed_at": datetime.now().isoformat(),
        "day_in_role": emp["day_in_role"],
        "meaning_delivered": False,
    }
    emp["behaviors"].append(behavior)
    achievement = {
        "task_id": task_id,
        "task": task["label"],
        "category": task["category"],
        "completed_at": behavior["completed_at"],
        "day_in_role": emp["day_in_role"],
        "day_number": emp["day_number"],
        "meaning_delivered": False,
    }
    emp["achievements"].append(achievement)
    _sync_adaptation_score(emp)

    done_count = sum(1 for item in emp["tasks"].values() if item["done"])
    total = len(emp["tasks"])

    return {
        "success": True,
        "task_completed": task["label"],
        "employee_name": emp["name"],
        "progress": f"{done_count}/{total}",
        "achievement_logged": achievement,
        "adaptation_score": emp["adaptation_score"],
        "trigger_meaning_for": task_id,
        "trigger_meaning_feedback": True,
        "meaning_status": "pending_delivery",
    }


def confirm_meaning_delivered(employee_id: str, task_id: str) -> dict:
    """
    Confirm that Meaning Skill feedback was actually delivered for a task.

    This is the Meaning Score write path. Completing a task only creates a
    pending behavior; the meaning score increases only after the agent delivers
    grounded Behavior -> Motivation -> Value -> Meaning feedback.

    Args:
        employee_id: Employee ID.
        task_id: Task ID that received meaning feedback.

    Returns:
        Updated meaning score and confirmation details.
    """
    emp_id = employee_id.lower().strip()
    if emp_id not in ONBOARDING_DB:
        return {"error": f"Employee '{employee_id}' was not found."}

    emp = ONBOARDING_DB[emp_id]
    for behavior in reversed(emp["behaviors"]):
        if behavior["task_id"] == task_id:
            if behavior["meaning_delivered"]:
                return {
                    "already_confirmed": True,
                    "task_id": task_id,
                    "meaning_score": _meaning_score(emp),
                }

            behavior["meaning_delivered"] = True
            behavior["meaning_delivered_at"] = datetime.now().isoformat()
            for achievement in reversed(emp["achievements"]):
                if achievement["task_id"] == task_id:
                    achievement["meaning_delivered"] = True
                    achievement["meaning_delivered_at"] = behavior["meaning_delivered_at"]
                    break
            emp["adaptation_score"]["meaning"] = min(
                emp["adaptation_score"]["meaning"] + 20,
                100,
            )
            _sync_adaptation_score(emp)

            return {
                "success": True,
                "meaning_delivered_for": task_id,
                "meaning_score": _meaning_score(emp),
                "meaning_score_delta": 20,
                "adaptation_score": emp["adaptation_score"],
            }

    return {
        "error": f"No completed behavior found for task '{task_id}'.",
        "hint": "Call mark_task_complete() before confirming meaning delivery.",
    }


def request_hitl_approval(employee_id: str, action: str, reason: str) -> dict:
    """
    Create a human-in-the-loop approval request for a sensitive action.

    Args:
        employee_id: Employee ID.
        action: The sensitive action being requested.
        reason: Why the new hire needs it.

    Returns:
        Pending approval request details.
    """
    emp_id = employee_id.lower().strip()
    if emp_id not in ONBOARDING_DB:
        return {"error": f"Employee '{employee_id}' was not found."}

    emp = ONBOARDING_DB[emp_id]
    request = {
        "request_id": f"HITL-{len(emp['hitl_requests']) + 1:03d}",
        "action": action,
        "reason": reason,
        "status": "pending_approval",
        "notify": emp["manager"]["slack"],
        "created_at": datetime.now().isoformat(),
    }
    emp["hitl_requests"].append(request)
    _sync_adaptation_score(emp)

    return {
        "hitl_triggered": True,
        "request_id": request["request_id"],
        "message": (
            f"Approval is required before I can help with '{action}'. "
            f"I've routed this to {emp['manager']['name']} ({emp['manager']['slack']}) "
            "and will not proceed until a human approves it."
        ),
        "action_requested": action,
        "status": "pending_approval",
        "approved": False,
    }


def log_connection_made(employee_id: str, connected_with: str, context: str) -> dict:
    """
    Record that the new hire connected with a colleague.

    Args:
        employee_id: Employee ID.
        connected_with: Name or Slack handle of the colleague.
        context: Why the connection happened.

    Returns:
        Updated connection score.
    """
    emp_id = employee_id.lower().strip()
    if emp_id not in ONBOARDING_DB:
        return {"error": f"Employee '{employee_id}' was not found."}

    emp = ONBOARDING_DB[emp_id]
    entry = {
        "connected_with": connected_with,
        "context": context,
        "logged_at": datetime.now().isoformat(),
        "day_in_role": emp["day_in_role"],
    }
    emp["connections_logged"].append(entry)
    _sync_adaptation_score(emp)

    return {
        "success": True,
        "connection_logged": entry,
        "total_connections": len(emp["connections_logged"]),
        "connection_score": _connection_score(emp),
        "adaptation_score": emp["adaptation_score"],
    }


def get_adaptation_score(employee_id: str) -> dict:
    """
    Return the employee's adaptation score.

    Clarity, connection, and meaning are weighted to show whether onboarding is
    producing progress, relationships, and value recognition.
    """
    emp_id = employee_id.lower().strip()
    if emp_id not in ONBOARDING_DB:
        return {"error": f"Employee '{employee_id}' was not found."}

    emp = ONBOARDING_DB[emp_id]
    _sync_adaptation_score(emp)
    clarity = emp["adaptation_score"]["clarity"]
    connection = emp["adaptation_score"]["connection"]
    meaning = _meaning_score(emp)
    total = round(clarity * 0.3 + connection * 0.3 + meaning * 0.4, 1)

    return {
        "employee_name": emp["name"],
        "day_in_role": emp["day_in_role"],
        "scores": {
            "clarity": {"score": clarity, "weight": "30%", "label": "Role clarity"},
            "connection": {"score": connection, "weight": "30%", "label": "Social connection"},
            "meaning": {"score": meaning, "weight": "40%", "label": "Meaning recognition"},
        },
        "total_score": total,
        "risk_signals": _risk_signals(emp) or ["No active risk signals."],
        "interpretation": (
            "Needs immediate support"
            if total < 30
            else "Building momentum"
            if total < 60
            else "Strong onboarding trajectory"
        ),
    }


