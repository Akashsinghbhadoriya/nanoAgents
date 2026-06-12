from llm.base import LLM
import requests

class OllamaLLM(LLM):

    def __init__(self, model = "llama3.2:3b"):
        super().__init__()
        self.model = model

    def generate(self, prompt):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model" : self.model,
                "prompt": prompt,
                "stream": False,
                "format": "json"
            }
        )

        return response.json()["response"]
