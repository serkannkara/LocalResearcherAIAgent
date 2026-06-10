"""File reading tool."""

from pathlib import Path
from localresearcher.rag.loader import load_document


class FileReaderTool:
    """Tool for reading various file formats."""
    
    async def read(self, path: Path) -> str:
        """Read a file and return its content."""
        document = load_document(path)
        return document.content