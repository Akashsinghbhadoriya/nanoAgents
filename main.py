from tools.calculator import CalculatorTool
from tools.filereader import FileReaderTool
from tools.search import SearchTool
from agents.tool_registry import ToolRegistry
from agents.llm_selector import LLMSelector
from agents.agent import Agent
from llm.ollama_llm import OllamaLLM

registry = ToolRegistry()
registry.register(CalculatorTool())
registry.register(FileReaderTool())
registry.register(SearchTool())
llm = OllamaLLM()
selector = LLMSelector(llm, registry)
agent = Agent(registry, selector)

print(agent.run("Open sample.txt file"))
