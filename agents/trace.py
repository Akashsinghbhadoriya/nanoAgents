from dataclasses import dataclass

@dataclass
class AgentTrace:
    query: str
    prompt: str
    llm_output: str
    selected_tool: str
    arguments: dict
    result: str