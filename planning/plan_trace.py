from dataclasses import dataclass

@dataclass
class PlanTrace:
    goal: str
    tasks: list[str]