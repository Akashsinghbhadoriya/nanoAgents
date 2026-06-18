from tools.base import Tool
from tools.tool_result import ToolResult
from pathlib import Path


class FileSearchTool(Tool):
    name = "file_search"
    description = """
    Searches for files by name or by keyword inside file contents.

    Use this tool to locate a file before reading it with file_reader.

    Use when:
    - User asks to find a file by name (e.g. "find config.json")
    - User asks which file contains a class, function, or keyword
    - You need a file path before calling file_reader

    Modes:
        "name"    - searches filenames matching the query (substring match)
        "content" - searches inside files for lines containing the query

    Input:
        query (str)       - filename or keyword to search for
        directory (str)   - root directory to search in (default: ".")
        mode (str)        - "name" or "content" (default: "name")

    Examples:

    Find a file named "config":
    {
        "query": "config",
        "directory": ".",
        "mode": "name"
    }

    Find which file contains "FactMemory":
    {
        "query": "FactMemory",
        "directory": ".",
        "mode": "content"
    }

    Returns a list of matching file paths.
    """

    def run(self, query, directory=".", mode="name"):
        root = Path(directory)
        matches = []

        for path in root.rglob("*"):
            if not path.is_file():
                continue

            if mode == "name":
                if query.lower() in path.name.lower():
                    matches.append(str(path))

            elif mode == "content":
                try:
                    text = path.read_text(errors="ignore")
                    if query in text:
                        matches.append(str(path))
                except Exception:
                    continue

        if not matches:
            return ToolResult(
                success=False,
                content=f"No files found for query '{query}' in '{directory}' using mode '{mode}'"
            )

        return ToolResult(
            success=True,
            content="\n".join(matches)
        )
