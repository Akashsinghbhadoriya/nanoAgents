class ProgressReporter:

    def planning_started(self):
        print("Planning...")

    def routing_started(self, route):
        print(f"Routing to {route}")

    def task_started(
        self,
        task,
        current,
        total
    ):
        print(
            f"[{current}/{total}] "
            f"{task.description}"
        )

    def reflection(
        self,
        passed
    ):
        print(
            "PASS"
            if passed
            else
            "FAIL"
        )