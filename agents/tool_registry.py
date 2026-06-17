
class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool
    
    def get(self, name):
        return self.tools[name]
    
    def tool_descriptions(self):
        descriptions = []

        for tool in self.tools.values():
            descriptions.append(
                f"""
                Tool Name: {tool.name}
                Description: {tool.description}
                """
            )

        return "\n".join(descriptions)
    
    def execute(self, tool_call):

        if not tool_call.tool or not tool_call.args:
            return "no tool found or no tool args found"
        
        tool = self.tools[tool_call.tool]

        return tool.run(**tool_call.args)