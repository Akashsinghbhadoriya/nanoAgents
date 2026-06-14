# tests/test_tool_registry.py

from agents.tool_registry import ToolRegistry
from agents.tool_call import ToolCall

from tools.calculator import CalculatorTool


def test_calculator_execution():

    registry = ToolRegistry()

    registry.register(
        CalculatorTool()
    )

    tool_call = ToolCall(
        tool="calculator",
        args={
            "expression": "5*5"
        }
    )

    result = registry.execute(
        tool_call
    )

    assert result == '25'