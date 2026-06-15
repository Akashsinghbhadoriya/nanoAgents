from evaluation.benchmark import Benchmark
from evaluation.evaluator import Evaluator
from tools.calculator import CalculatorTool
from tools.filereader import FileReaderTool
from tools.search import SearchTool
from agents.tool_registry import ToolRegistry
from agents.agent import Agent
from llm.ollama_llm import OllamaLLM
from memory.conversation_memory import ConversationMemory
from memory.in_memory_fact_memory import InMemoryFactMemory
from tools.memory import MemoryTool
from agent_system.agent_system import AgentSystem
from planning.planner import Planner
from planning.executor import PlanExecutor
from evaluation.result_writer import ResultWriter

factmemory = InMemoryFactMemory()
registry = ToolRegistry()
registry.register(CalculatorTool())
registry.register(FileReaderTool())
registry.register(SearchTool())
registry.register(MemoryTool(factmemory))
llm = OllamaLLM()
memory = ConversationMemory()
agent = Agent(registry, llm, memory, factmemory)
planner = Planner(llm)
executor = PlanExecutor(agent)
agent_system = AgentSystem(planner, executor)

benchmark = Benchmark(data_set="evaluation/datasets/basic_tasks.json")
evaluator = Evaluator(agent_system = agent_system)

result = evaluator.evaluate(benchmark)

path = ResultWriter.save(
    result
)

print(
    f"Accuracy: {result.accuracy}%"
)

print(
    f"Results saved to: {path}"
)