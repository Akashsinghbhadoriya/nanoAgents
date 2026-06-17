from llm.base import LLM
import requests

class OllamaLLM(LLM):

    def __init__(self, model = "qwen3:8b"):
        super().__init__()
        self.model = model
        self.base_url = "http://localhost:11434"

        self.verify_server_status()

    def generate(self, prompt):

        try:
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
        
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                return f"Error: The model '{self.model}' was not found. Run 'ollama pull {self.model}'."
            return f"HTTP Error: {e}"
        
        except requests.exceptions.ConnectionError:
            return "Connection Error: Ollama server disconnected unexpectedly."
    
    def verify_server_status(self):
        """Checks if the Ollama server is running and accessible."""
        try:
            response = requests.get(self.base_url, timeout=2)
            if response.status_code == 200 and "Ollama is running" in response.text:
                return True
            raise RuntimeError("Ollama server responded but is not behaving correctly.")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                "❌ Ollama is NOT running. Please start the Ollama application before running this script."
            )
