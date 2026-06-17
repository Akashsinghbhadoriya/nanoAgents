def build_routing_prompt(query):

    return f"""
You are a routing system.

Classify the user query into one of the following routes.

1. direct
- General knowledge
- Explanation
- Simple reasoning
- No tools needed

Examples:
"What is FlashAttention?"
"Explain transformers."
"Why is the sky blue?"

2. tool
- A single tool can solve the task
- No planning required

Examples:
"What is 25 * 25?"
"What is my favorite city?"
"Search for OpenAI"

3. plan
- Multiple steps required
- Multiple tools required
- Task decomposition required

Examples:
"Read test.txt and add all numbers."
"Analyze this repository."
"Research Nvidia and summarize findings."

Query:
{query}

Return only JSON:

{{
    "route": "direct"
}}

or

{{
    "route": "tool"
}}

or

{{
    "route": "plan"
}}
"""