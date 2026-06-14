from planning.execution_context import ExecutionContext

class PlanExecutor:

    def __init__(self, react_agent):
        
        self.react_agent = react_agent

    def execute(self, plan):

        context = ExecutionContext()

        for task in plan.tasks:

            context_formatted = self.format_context(context)
            result = self.react_agent.run(task.description, context_formatted)

            context.add_result(
                task_id=task.id,
                task_description=task.description,
                result=result
            )
            task.completed = True

        return context
    
    def format_context(self, context):

        lines = []

        for item in context.completed_tasks:

            lines.append(
                f"""
            Task {item["task_id"]}

            Description:
            {item["task"]}

            Result:
            {item["result"]}
            """
            )

        return "\n".join(lines)