from tools.base import Tool

class SearchTool(Tool):
    name = "search"

    def run(self, query):
        return f"Searching for {query}"