from tools.base import Tool
from tools.tool_result import ToolResult

class ScaleTool(Tool):

    name = "ScaleTool"

    description = """
    Generate scaling recommendations and
    identify bottlenecks.
    Input: 
        system_name (str)
    """

    def __init__(self, llm):
        self.llm = llm

    def run(self, system_name):

        prompt = f"""
You are a Principal Distributed Systems Engineer.

Estimate scaling requirements for:

{system_name}

Return:

1. Expected bottlenecks
2. Caching strategy
3. Database scaling
4. Message queues
5. High availability strategy
6. Traffic handling recommendations

Focus on practical engineering decisions.
"""

        return ToolResult(
            success= True,
            content= self.llm.generate(prompt)
        )