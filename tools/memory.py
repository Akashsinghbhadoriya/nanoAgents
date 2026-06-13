from tools.base import Tool
class MemoryTool(Tool):

    name = "memory"
    description = """
        Use memory tool whenever the user tells you
        a personal preference, fact, or long-term information
        that may be useful later

            Examples:
            - Favorite city
            - Favorite language
            - Personal preferences
            - Long-term goals
        Input:
            key (str)
            value (str)
        """
    
    def run(self, key, value):
        return {"key": key, "value": value}