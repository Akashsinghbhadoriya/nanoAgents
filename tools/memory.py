from tools.base import Tool
from tools.tool_result import ToolResult

class MemoryTool(Tool):

    name = "memory"
    description = """
        Use memory tool whenever the user tells you
        a personal preference, fact, or long-term information
        that may be useful later. This is tool stores info in factmemory

        Use this tool whenever:

        - User states a preference
        - User states a favorite
        - User states a goal
        - User asks to remember something

        Examples:

        "My favorite city is Pune"

        {
        "operation":"set",
        "key":"favorite_city",
        "value":"Pune"
        }

        "What is my favorite city?"

        {
        "operation":"get",
        "key":"favorite_city"
        }
        Input:
            operation (str)
            key (str)
            value (str)
        """
    def __init__(self, factmemory):

        self.factmemory = factmemory

    def run(self, operation, key, value=None):

        if operation == "get":
            return ToolResult(
                success=True,
                content=self.factmemory.get_fact(key)
            )

        if operation == "set":
            self.factmemory.set_fact(key, value)

        return ToolResult(
            success=True,
            content=f"Stored {key}"
        )