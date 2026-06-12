from tools.filereader import FileReaderTool

def test_calculator():
    tool = FileReaderTool()

    result = tool.run("sample.txt")

    assert result == "Hello Agent"