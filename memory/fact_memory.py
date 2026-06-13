import json
from pathlib import Path

class FactMemory:

    def __init__(self, filepath="memory/facts.json"):
        
        self.filepath = Path(filepath)
        self.facts = {}

        self.load()

    def load(self):

        if self.filepath.exists():

            with open(self.filepath, "r") as f:
                self.facts = json.load(f)

        else:
            self.facts = {}

    def save(self):

        self.filepath.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(self.filepath, "w") as f:
            json.dump(self.facts, f, indent=2)

    def set_fact(self, key, value):
        
        self.facts[key] = value

        self.save()

    def get_fact(self, key):

        return self.facts.get(key)
    
    def get_all_facts(self):
        return self.facts.keys()