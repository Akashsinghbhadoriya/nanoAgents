from tools.calculator import CalculatorTool
from tools.filereader import FileReaderTool
from tools.search import SearchTool
from agents.tool_registry import ToolRegistry
from agents.agent import Agent
from llm.ollama_llm import OllamaLLM
from memory.persistent_memory import PersistentMemory
from memory.fact_memory import FactMemory
from tools.memory import MemoryTool
from agent_system.agent_system import AgentSystem
from planning.planner import Planner
from planning.executor import PlanExecutor

factmemory = FactMemory()
registry = ToolRegistry()
registry.register(CalculatorTool())
registry.register(FileReaderTool())
registry.register(SearchTool())
registry.register(MemoryTool(factmemory))
llm = OllamaLLM()
memory = PersistentMemory()
agent = Agent(registry, llm, memory, factmemory)
planner = Planner(llm)
executor = PlanExecutor(agent)
system = AgentSystem(planner, executor)

context = system.run("add all the numbers in test.txt file")
print(context)
print("final result:", context.final_result)

# print(agent.run("add all the numbers in sample.txt file"))

# print(agent.run("What was the answer of the last user query"))

# print(agent.run("my favourite city is pune"))

# print(agent.run("What is my favourite city"))
