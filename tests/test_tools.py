from tools.calculator import CalculatorTool
from tools.filereader import FileReaderTool
from tools.memory import MemoryTool
from memory.fact_memory import FactMemory

def test_calculator():
    tool = CalculatorTool()

    result = tool.run("2+2")

    assert result == "4"


def test_calculator():
    tool = FileReaderTool()

    result = tool.run("sample.txt")

    assert result == "Hello Agent"

def test_memory():
    factmemory = FactMemory()
    tool = MemoryTool(factmemory)

    tool.run("set", "favourite_city", "Pune")

    result = tool.run("get", "favourite_city")

    assert result == "Pune"