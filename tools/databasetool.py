from tools.base import Tool
from tools.tool_result import ToolResult

class DatabaseTool(Tool):

    name = "DatabaseTool"

    description = """
    Generate database entities, schema design,
    relationships, primary keys and indexes.
    Input: 
        system_name (str)
    """

    def __init__(self, llm):
        self.llm = llm

    def run(self, system_name):

        prompt = f"""
You are a Staff Database Architect.

Design the database schema for:

{system_name}

Return:

1. Entities
2. Fields
3. Primary Keys
4. Relationships
5. Recommended Indexes

Be concise and practical.
"""

        return ToolResult(
            success= True,
            content= self.llm.generate(prompt)
        )