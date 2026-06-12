from dataclasses import dataclass

@dataclass
class ToolCall:
    tool: str
    args: dict