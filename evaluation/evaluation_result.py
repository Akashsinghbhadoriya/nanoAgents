from dataclasses import dataclass

@dataclass
class EvaluationResult:

    total: int
    passed: int
    failed: int
    accuracy: float
    details: list