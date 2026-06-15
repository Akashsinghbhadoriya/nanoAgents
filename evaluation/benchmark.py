import json

class Benchmark:

    def __init__(self, data_set):
        
        with open(data_set, "r") as f:
            self.samples = json.load(f)
