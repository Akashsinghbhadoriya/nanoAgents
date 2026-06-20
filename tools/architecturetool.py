from tools.base import Tool
from tools.tool_result import ToolResult

class SystemDesignTool(Tool):

    name = "ArchitectureTool"
    description = """
        This is a system design tool used for
        generating a complete software architecture when a user
        gives the details about the application
        Input:
            query (str)
    """

    def __init__(self, llm):
        super().__init__()
        self.llm = llm

    def run(self, query):

        prompt = f"""
        You are a Staff software architect.

        Design a high-level architecture for:
        {query}

        take all these pointers into consideration:
        Requirements
        Architecture
        Database
        APIs
        Capacity Planning
        Caching
        Messaging
        Tradeoffs
        Failure Scenarios

        {{
            "requirements": [],
            "components": [],
            "database": [],
            "apis": [],
            "scaling": [],
            "tradeoffs": []
        }}
    """
        
        response = self.llm.generate(prompt)

        return ToolResult(
            success=True,
            content=response
        )
        
