from tools.base import Tool
from pathlib import Path
from tools.tool_result import ToolResult

class FileReaderTool(Tool):
    name = "file_reader"
    description = """
    Reads text files.
    Input:
        filepath (str)
    """
    def run(self, filepath):
        path = Path(filepath)
        if path.exists():
            with open(filepath, "r") as f:
                return ToolResult(
                    content=f.read(),
                    success=True
                    )
        
        return ToolResult(
            success=False,
            content=f"FilePath does not exist {filepath}"
        )