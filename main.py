from tools.calculator import CalculatorTool
from tools.filereader import FileReaderTool
from tools.search import SearchTool
from agents.tool_registry import ToolRegistry
from agents.agent import Agent
from llm.ollama_llm import OllamaLLM
from memory.persistent_memory import PersistentMemory
from tools.memory import MemoryTool

registry = ToolRegistry()
registry.register(CalculatorTool())
registry.register(FileReaderTool())
registry.register(SearchTool())
registry.register(MemoryTool())
llm = OllamaLLM()
memory = PersistentMemory()
agent = Agent(registry, llm, memory)

# print(agent.run("add all the numbers in sample.txt file"))

# print(agent.run("What was the answer of the last user query"))

# print(agent.run("my favourite city is pune"))

# print(agent.run("What is my favourite city"))
