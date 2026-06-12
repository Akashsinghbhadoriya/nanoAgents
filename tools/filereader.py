from tools.base import Tool

class FileReaderTool(Tool):
    name = "file_reader"
    description = """
    Reads text files.
    Input:
        filepath (str)
    """
    def run(self, filepath):
        with open(filepath, "r") as f:
            return f.read()