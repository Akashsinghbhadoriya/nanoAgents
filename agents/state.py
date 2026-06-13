from dataclasses import dataclass, field

@dataclass
class AgentState:

    user_query: str

    actions: list = field(default_factory=list)
    observations: list = field(default_factory=list)