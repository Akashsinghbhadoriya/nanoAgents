from memory.memory import Memory

class ConversationMemory(Memory):

    def __init__(self, max_messages=10):
        self.messages = []
        self.max_messages = max_messages

    def add(self, role, content):
        self.messages.append({
            "role":role,
            "content":content
        })

    def get_context(self):
        return self.messages[-self.max_messages:]