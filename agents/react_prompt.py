def build_react_prompt(query, actions, observations, tools, memory, facts, context):

    history = ""

    for a, o in zip(actions, observations):

        history += f"""
                Action:
                {a.tool}
                Args:
                {a.args}

                Observation:
                {o.content}
                """
        
    
    return f"""
You are a ReAct agent.

You must follow this process:

1. Decide an action.
2. Receive an observation.
3. Use the observation to decide the next action.
4. When enough information exists, return type="finish".
5. Utilize the conversational memory as well for answering the user queries
6. Recent or the last user query is at the last in the memory and not at the start

Never repeat an action if the observation already contains the required information.

User Query:

{query}

Known fact Memory Keys:
{facts}
Use the memory tool to retrieve fact values when needed.

Context:

{context}

History:

{history}

Conversational Memory:

{memory}

Available tools:

{tools}

Use the Observation from History to determine the next step
Respond only in JSON.

Tool Action:

{{
    "type":"action",
    "tool":"calculator",
    "args":{{}}
}}

Final Answer:

{{
    "type": "finish",
    "answer": "..."
}}
"""
