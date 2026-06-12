from agents.tool_call import ToolCall
import json

def build_prompt(query, tools):

    return f"""
        You are a tool selection engine.

        Available tools:

        {tools}

        choose the best tool

        Return only Valid JSON.
        Example:

        {{
            "tool":"calculator",
            "args": {{
                "expression":"55*123"
            }}
        }}

        User Query:
        {query}
        """

def parse_tool_call(response):

    data = json.loads(response)

    return ToolCall(
        tool=data["tool"],
        args=data["args"]
    )

class LLMSelector:

    def __init__(self, llm, registry):
        
        self.llm = llm
        self.registry = registry

    def select(self, query):

        prompt = build_prompt(
            query, 
            self.registry.tool_descriptions()
        )

        response = self.llm.generate(prompt)

        return parse_tool_call(response), prompt, response