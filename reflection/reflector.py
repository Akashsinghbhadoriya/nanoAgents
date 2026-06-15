import json
from reflection.reflection_prompt import reflection_prompt
from reflection.reflection_result import ReflectionResult

class Reflector:

    def __init__(self, llm):
        
        self.llm = llm

    def reflect(self, goal, trace, result):

        prompt = reflection_prompt(goal, trace, result)

        response = self.llm.generate(prompt)
        data = json.loads(response)

        return ReflectionResult(
            passed=data["passed"],
            reason=data["reason"]
        )