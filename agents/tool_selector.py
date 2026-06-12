from agents.tool_call import ToolCall

class ToolSelector:

    def select(self, query):

        query = query.lower()

        if "*" in query:
            return ToolCall(
                tool="calculator",
                args={
                    "expression": query
                }
            )
        
        if ".txt" in query:
            return ToolCall(
                tool="file_reader",
                args={
                    "filepath": query
                }
            )
        
        return None