import json
from pathlib import Path
from memory.conversation_memory import ConversationMemory

class PersistentMemory(ConversationMemory):

    def __init__(self, max_messages=10, filepath="memory/memory.json"):
        super().__init__(max_messages)
        self.filepath = Path(filepath)
        self.load()

    def load(self):

        if self.filepath.exists():

            with open(self.filepath, "r") as f:
                self.messages = json.load(f)
        else:
            self.messages = []
    
    def save(self):

        self.filepath.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(self.filepath, "w") as f:
            json.dump(self.messages,f, indent=2)

    def add(self, role, content):
        super().add(role, content)

        self.save()
    
