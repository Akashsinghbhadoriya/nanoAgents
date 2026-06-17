from tools.base import Tool
from tools.tool_result import ToolResult

class SearchTool(Tool):
    name = "search"

    def run(self, query):
        return ToolResult(
            success=True,
            content=f"Searching for {query}"
        )