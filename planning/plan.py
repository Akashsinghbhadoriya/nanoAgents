from dataclasses import dataclass
from planning.task import Task

@dataclass
class Plan:
    goal: str
    tasks: list[Task]