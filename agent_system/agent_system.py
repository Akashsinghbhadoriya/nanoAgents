from agent_system.agent_context import AgentContext
import json

class AgentSystem:

    def __init__(self, planner, executor, memory, logger, progress, router, llm):
        
        self.planner = planner
        self.executor = executor
        self.memory = memory
        self.logger = logger
        self.progress = progress
        self.router = router
        self.llm = llm

    def run(self, goal):

        self.memory.add("user", goal)
        response = self.router.route(goal)

        self.progress.routing_started(response.get("route"))
        if response.get("route") == "direct":
            result = json.loads(self.llm.generate(goal))
            return AgentContext(
                final_result=result["response"]
            )
        
        self.progress.planning_started()
        plan = self.planner.create_plan(goal)

        context, step_traces = self.executor.execute(plan, self.progress)
        self.memory.add("assistant", context.final_result)

        data = {
            "query":goal,
            "plan":plan,
            "response":context.final_result,
            "context":context,
            "step_traces": step_traces
        }
        
        filepath = self.logger.save(data)
        print(f"logs are saved at {filepath}")
        return context