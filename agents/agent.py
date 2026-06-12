from agents.trace import AgentTrace
import json

class Agent:

    def __init__(self, registry, selector):
        self.registry = registry
        self.selector = selector

    def run(self, query):

        tool_call, prompt, response = self.selector.select(query)

        if tool_call is None:
            return "No tool found"
        
        result = self.registry.execute(tool_call)

        trace = AgentTrace(
            query=query,
            prompt=prompt,
            llm_output=response,
            selected_tool=tool_call.tool,
            arguments=tool_call.args,
            result=result
        )
        print(json.dumps(trace.__dict__, indent=4, default=str))

        return result