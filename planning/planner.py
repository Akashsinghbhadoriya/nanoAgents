import json
from planning.plan import Plan
from planning.task import Task
from planning.prompts import PLANNER_PROMPT, replanner_prompt

class Planner:

    def __init__(self, llm):
        self.llm = llm

    def create_plan(self, goal):

        prompt = f"""
            {PLANNER_PROMPT}

        Goal:
            {goal}
        """

        response = self.llm.generate(prompt)

        data = json.loads(response)

        tasks = []

        for idx , description in enumerate(data["tasks"]):

            tasks.append(
                Task(
                    id=idx + 1,
                    description=description
                )
            )
        
        return Plan(
            goal=goal,
            tasks=tasks
        )
    
    def create_replan(self, goal, step_traces, failure_reason, context):
        prompt = replanner_prompt(
            goal,
            step_traces, 
            failure_reason, 
            context
        )

        response = self.llm.generate(prompt)

        data = json.loads(response)

        tasks = []

        for idx , description in enumerate(data["tasks"]):

            tasks.append(
                Task(
                    id=idx + 1,
                    description=description
                )
            )
        
        return Plan(
            goal=goal,
            tasks=tasks
        )