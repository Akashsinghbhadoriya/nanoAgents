from dataclasses import dataclass

@dataclass
class ToolResult:

    success: bool
    content: str