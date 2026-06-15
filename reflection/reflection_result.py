from dataclasses import dataclass

@dataclass
class ReflectionResult:

    passed: bool
    reason: str