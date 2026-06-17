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
from reflection.reflector import Reflector
from logger.run_logger import RunLogger
from logger.progress_report import ProgressReporter
from routing.router import Router

def create_app():
    factmemory = FactMemory()
    logger = RunLogger()
    progress = ProgressReporter()
    registry = ToolRegistry()
    registry.register(CalculatorTool())
    registry.register(FileReaderTool())
    registry.register(SearchTool())
    registry.register(MemoryTool(factmemory))
    llm = OllamaLLM()
    reflector = Reflector(llm)
    router = Router(llm)
    memory = PersistentMemory()
    agent = Agent(registry, llm, memory, factmemory)
    planner = Planner(llm)
    executor = PlanExecutor(agent, reflector, MAX_RETRIES=3)
    system = AgentSystem(planner, executor, memory, logger, progress, router, llm)

    return system