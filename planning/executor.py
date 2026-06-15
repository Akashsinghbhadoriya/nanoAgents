from planning.execution_context import ExecutionContext

class PlanExecutor:

    def __init__(self, react_agent, reflector, MAX_RETRIES = 2):
        
        self.react_agent = react_agent
        self.max_retries = MAX_RETRIES
        self.reflector = reflector

    def execute(self, plan):

        context = ExecutionContext()

        for task in plan.tasks:
            
            retry = 0
            reflection = None
            while retry < self.max_retries:

                if reflection is not None:
                    context_formatted = self.format_context(context, reflection.reason)
                else:
                    context_formatted = self.format_context(context)

                result = self.react_agent.run(task.description, context_formatted)
                retry += 1

                context.add_result(
                    task_id=task.id,
                    task_description=task.description,
                    result=result
                )
                reflection = self.reflector.reflect(
                    goal=task.description,
                    trace=self.format_context(context),
                    result=result
                )
                if reflection.passed:
                    break

            task.completed = True

        return context
    
    def format_context(self, context, retry_reason=None):

        lines = []

        if retry_reason is not None:
            lines.append(
                f"""
                Previous attempt failed.

                Reason:

                {retry_reason}

                Try again.
                """
            )

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