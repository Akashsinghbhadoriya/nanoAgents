class InMemoryFactMemory:

    def __init__(self):

        self.facts = {}

    def set_fact(
        self,
        key,
        value
    ):

        self.facts[key] = value

    def get_fact(
        self,
        key
    ):

        return self.facts.get(key)

    def get_all_facts(self):

        return self.facts.keys()