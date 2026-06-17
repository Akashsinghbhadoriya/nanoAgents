from dataclasses import dataclass

@dataclass
class ReflectionResult:

    passed: bool
    reason: str
    action: str
    retry_instruction: str