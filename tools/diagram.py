from tools.base import Tool
from tools.tool_result import ToolResult

class Diagram(Tool):

    name = "DiagramTool"
    description = """
        Useful for generating text-based Mermaid.js diagram definitions
        from raw software architecture descriptions, text specs, or user flows.
        Use this tool whenever the user asks to visualize code, map system architectures, 
        draw database schemas, create API sequence flows, or generate structural diagrams-as-code.
        Input:
            architecture (str)
    """

    def __init__(self, llm):
        super().__init__()
        self.llm = llm

    def run(self, architecture):

        prompt = f"""
            Act as a Principal Software Architect. I need a Mermaid.js diagram for the following system: {architecture}.

            Based on my description, generate the code for a Mermaid diagram that best represents the system (e.g., a C4 model, sequence diagram, or flowchart). 

            Please ensure the Mermaid code:
            1. Is enclosed entirely in a single markdown code block (```mermaid ... ```).
            2. Uses modern, clean syntax compatible with the latest Mermaid.js renderer.
            3. Includes clear groupings (like subgraphs for AWS, GCP, Frontend, Backend) if applicable.
            4. Uses appropriate node shapes and distinct arrow styles for different types of traffic (e.g., synchronous, asynchronous, database queries).

            After the diagram code, provide a brief, bulleted explanation of why you chose this specific diagram type and the key components mapped.
            """
        
        response = self.llm.generate(prompt)

        return ToolResult(
            success=True,
            content=response
        )