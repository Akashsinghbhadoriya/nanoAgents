from tools.calculator import CalculatorTool

def test_calculator():
    tool = CalculatorTool()

    result = tool.run("2+2")

    assert result == "4"