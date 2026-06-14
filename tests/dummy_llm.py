# tests/dummy_llm.py

class DummyLLM:

    def __init__(self):

        self.step = 0

    def generate(self, prompt):

        self.step += 1

        if self.step == 1:

            return """
            {
                "type":"action",
                "tool":"calculator",
                "args":{
                    "expression":"10+20+30"
                }
            }
            """

        return """
        {
            "type":"finish",
            "answer":"60"
        }
        """