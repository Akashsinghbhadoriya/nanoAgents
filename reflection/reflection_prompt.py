
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

    Return JSON:

    {{
        "passed": true/false,
        "reason": "..."
    }}
    """