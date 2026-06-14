
class AgentSystem:

    def __init__(self, planner, executor):
        
        self.planner = planner
        self.executor = executor


    def run(self, goal):

        plan = self.planner.create_plan(goal)

        context = self.executor.execute(plan)

        return context