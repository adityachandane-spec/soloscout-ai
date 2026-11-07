"""Rule-based eligibility checks with explicit unknown handling."""
from dataclasses import dataclass
from typing import Any


@dataclass
class Check:
    requirement: str
    status: str  # pass, fail, unknown
    explanation: str


def check_eligibility(profile: dict[str, Any], opportunity: dict[str, Any]) -> dict[str, Any]:
    checks: list[Check] = []

    age = profile.get("age")
    min_age = opportunity.get("min_age")
    max_age = opportunity.get("max_age")
    if age is None or (min_age is None and max_age is None):
        checks.append(Check("Age", "unknown", "The participant age or event age limits are not fully specified."))
    elif min_age is not None and age < min_age:
        checks.append(Check("Age", "fail", f"Minimum age is {min_age}; profile age is {age}."))
    elif max_age is not None and age > max_age:
        checks.append(Check("Age", "fail", f"Maximum age is {max_age}; profile age is {age}."))
    else:
        checks.append(Check("Age", "pass", "The profile age fits the stated age range."))

    student_type = profile.get("student_type", "school")
    accepted = opportunity.get("accepted_student_types")
    if accepted is None:
        checks.append(Check("Education", "unknown", "The event's accepted education levels are not specified."))
    elif student_type in accepted:
        checks.append(Check("Education", "pass", f"The event accepts {student_type} students."))
    else:
        checks.append(Check("Education", "fail", f"The event does not list {student_type} students as eligible."))

    solo = profile.get("solo", True)
    solo_allowed = opportunity.get("solo_allowed")
    if solo_allowed is None:
        checks.append(Check("Team size", "unknown", "Solo participation rules are not specified."))
    elif not solo or solo_allowed:
        checks.append(Check("Team size", "pass", "The participation format matches the profile."))
    else:
        checks.append(Check("Team size", "fail", "This event does not allow individual participation."))

    fee = opportunity.get("fee_inr")
    budget = profile.get("budget_inr")
    if fee is None or budget is None:
        checks.append(Check("Fee", "unknown", "The fee or participant budget is not specified."))
    elif fee <= budget:
        checks.append(Check("Fee", "pass", f"Fee ₹{fee} is within the ₹{budget} budget."))
    else:
        checks.append(Check("Fee", "fail", f"Fee ₹{fee} exceeds the ₹{budget} budget."))

    statuses = [c.status for c in checks]
    if "fail" in statuses:
        overall = "Not eligible"
    elif "unknown" in statuses:
        overall = "Needs verification"
    else:
        overall = "Eligible based on listed rules"

    return {
        "status": overall,
        "checks": [c.__dict__ for c in checks],
        "passed": statuses.count("pass"),
        "failed": statuses.count("fail"),
        "unknown": statuses.count("unknown"),
    }
