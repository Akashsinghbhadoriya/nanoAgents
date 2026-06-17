
def reflection_prompt(goal, trace, result):

    return f"""
    Goal:
    {goal}

    Execution Trace:
    {trace}

    Final Result:
    {result}

    Review the execution.

    Was the task completed successfully?
    Determine:
        1. pass
        - Task completed successfully

        2. retry
        - Task can succeed with another attempt

        3. stop
        - Task cannot succeed without user input
        - Required resource missing
        - Tool unavailable

        4. replan
        - Current plan is invalid
        - Different strategy needed

    Return JSON:

    {{
        "passed": true/false,
        "reason": "...",
        "action": "pass/retry/stop/replan"
        "retry_instruction": "if action is retry add the retry instruction here"
    }}
    """