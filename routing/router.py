import json
from routing.routing_prompt import build_routing_prompt

class Router:

    def __init__(self, llm):
        self.llm = llm

    def route(self, query):

        prompt = build_routing_prompt(
            query
        )

        response = self.llm.generate(
            prompt
        )

        return json.loads(response)