def build_react_prompt(query, actions, observations, tools, memory, facts, context):
    # 1. Format the execution history cleanly
    history = ""
    for a, o in zip(actions, observations):
        history += f"""
Action Taken: {a.tool}
Arguments Used: {a.args}
Observation: {o.content}
---
"""

    # 2. Build the structured prompt
    return f"""You are a ReAct agent.

You must follow this process:
1. Decide an action based on the User Query, History, and Memory.
2. Receive an observation.
3. Use the observation to decide the next action.
4. When enough information exists, return with type="finish".
5. If a tool has success = False in the Observation then we need to retry again the same tool do not hallucinate.

[CRITICAL RULES]
- Never repeat an action if the history or observations already contain the required information.
- Recent or the last user query is at the last in the Conversational Memory.
- If the task is a fact which is stored in factmemory, use the memory tool to check or retrieve it. If found, pass type="finish" with the suitable answer.
- Your response must be raw, valid JSON matching one of the schemas below. Do not output anything else.

[AVAILABLE TOOLS]
{tools}

[KNOWN FACT MEMORY KEYS]
{facts}

[CONTEXT]
{context}

[CONVERSATIONAL MEMORY]
{memory}

[EXECUTION HISTORY]
{history}

[CURRENT TASK TO EXECUTE]
User Query: {query}

[RESPONSE FORMAT]
You must respond strictly with one of the following two JSON formats depending on the state of the task:

If you need to use a tool:
{{
    "type": "action",
    "tool": "name_of_the_tool",
    "args": {{"argument_name": "value"}}
}}

If you do not have sufficient information to answer the user query return proper answer always it should not be empty
{{
    "type": "failure",
    "success": False,
    "answer": "Your final detailed message here."
}}
If a required tool fails and the task cannot continue and their is repeated failure return this:
{{
    "type": "finish",
    "success": False,
    "answer": "Your final detailed message here."
}}
If you have sufficient information to answer the user query:
{{
    "type": "finish",
    "success": True,
    "answer": "Your final detailed message here."
}}

Response:"""
