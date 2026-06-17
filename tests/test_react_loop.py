# tests/test_react_loop.py

from agents.agent import Agent

from tests.dummy_llm import DummyLLM

from agents.tool_registry import ToolRegistry

from tools.calculator import CalculatorTool

from memory.conversation_memory import ConversationMemory
from memory.fact_memory import FactMemory

def test_react_loop():

    registry = ToolRegistry()

    registry.register(
        CalculatorTool()
    )

    llm = DummyLLM()

    memory = ConversationMemory()
    factmemory = FactMemory()
    context = ""

    agent = Agent(
        llm=llm,
        registry=registry,
        memory=memory,
        factmemory=factmemory
    )

    result = agent.run(
        "Add 10 20 and 30",
        context
    )

    assert result.answer == "60"