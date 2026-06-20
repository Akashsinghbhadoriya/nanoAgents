from tools.base import Tool
from tools.tool_result import ToolResult

class APITool(Tool):

    name = "APITool"

    description = """
    Generate REST APIs and contracts.
    Input: 
        system_name (str)
    """

    def __init__(self, llm):
        self.llm = llm

    def run(self, system_name):

        prompt = f"""
You are a Senior Backend Engineer.

Generate APIs for:

{system_name}

Return:

1. Endpoint
2. Method
3. Request Body
4. Response Body
5. Purpose

Include the most important APIs only.
"""

        return ToolResult(
            success= True,
            content= self.llm.generate(prompt)
        )