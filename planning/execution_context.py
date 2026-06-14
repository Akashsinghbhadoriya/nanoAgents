from dataclasses import dataclass, field

@dataclass
class ExecutionContext:

    completed_tasks: list = field(default_factory=list)

    def add_result(
        self,
        task_id,
        task_description,
        result
    ):

        self.completed_tasks.append(
            {
                "task_id": task_id,
                "task": task_description,
                "result": result
            }
        )

    @property
    def final_result(self):

        if not self.completed_tasks:
            return None
        
        return self.completed_tasks[-1]["result"]