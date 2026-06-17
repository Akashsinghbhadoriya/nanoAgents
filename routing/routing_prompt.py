def build_routing_prompt(query):

    return f"""
Decide whether this query needs:

1. direct
   - Answer can be given immediately.

2. agent
   - Requires tools
   - Multiple steps
   - Planning

Query:
{query}

Return JSON:

{{
    "route":"direct"
}}

or

{{
    "route":"agent"
}}
"""