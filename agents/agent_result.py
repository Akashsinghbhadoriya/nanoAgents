from dataclasses import dataclass

@dataclass
class AgentResult:

    answer: str
    traces: list
    success: bool