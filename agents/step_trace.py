from dataclasses import dataclass

@dataclass
class StepTrace:
    step: list
    query: str
    prompt: str
    llm_response: str
    action: str
    observation: str