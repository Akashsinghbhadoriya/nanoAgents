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

    def run(self, goal, MAX_REPLANS = 2):

        self.memory.add("user", goal)
        response = self.router.route(goal)

        self.progress.routing_started(response.get("route"))
        if response.get("route") == "direct":
            result = json.loads(self.llm.generate(goal))
            return AgentContext(
                final_result=result
            )
        
        self.progress.planning_started()
        plans, contexts, final_step_traces, final_reflections = [], [], [], []
        plan = self.planner.create_plan(goal)
        plans.append(plan)
        context, step_traces, reflections = self.executor.execute(plan, self.progress)
        contexts.append(context)
        final_step_traces.extend(step_traces)
        final_reflections.extend(reflections)
        reflection = reflections[-1]
        retry = 0
        while reflection.action == "replan" and retry < MAX_REPLANS:
            plan = self.planner.create_replan(goal, step_traces, reflection.reason, context)
            plans.append(plan)
            context, step_traces, reflections = self.executor.execute(plan, self.progress)
            final_step_traces.extend(step_traces)
            final_reflections.extend(reflections)
            reflection = reflections[-1]
            contexts.append(context)
            retry += 1

        self.memory.add("assistant", context.final_result)

        data = {
            "query":goal,
            "plan":to_dict(plans),
            "response":context.final_result,
            "context":to_dict(contexts),
            "step_traces": to_dict(final_step_traces),
            "reflection": to_dict(final_reflections)
        }
        
        filepath = self.logger.save(data)
        print(f"logs are saved at {filepath}")
        return context