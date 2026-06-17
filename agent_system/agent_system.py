from agent_system.agent_context import AgentContext
import json

def to_dict(obj):
    if isinstance(obj, list):
        return [to_dict(item) for item in obj]
    if isinstance(obj, dict):
        return {k: to_dict(v) for k, v in obj.items()}
    if hasattr(obj, "__dict__"):
        return {k: to_dict(v) for k, v in obj.__dict__.items()}
    return obj

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
                final_result=result
            )
        
        self.progress.planning_started()
        plan = self.planner.create_plan(goal)

        context, step_traces, reflections = self.executor.execute(plan, self.progress)
        self.memory.add("assistant", context.final_result)

        data = {
            "query":goal,
            "plan":to_dict(plan),
            "response":context.final_result,
            "context":to_dict(context),
            "step_traces": to_dict(step_traces),
            "reflection": to_dict(reflections)
        }
        
        filepath = self.logger.save(data)
        print(f"logs are saved at {filepath}")
        return context