from tools.base import Tool
from tools.tool_result import ToolResult

class CalculatorTool(Tool):
    name = "calculator"
    description = """
    Performs arithmetic calculations.
    Input:
        expression (str)
    """

    def run(self, expression):
        return ToolResult(
            success=True,
            content=str(eval(expression))
        )