from tools.base import Tool

class CalculatorTool(Tool):
    name = "calculator"
    description = """
    Performs arithmetic calculations.
    Input:
        expression (str)
    """

    def run(self, expression):
        return str(eval(expression))