"""Document loaders for various file formats."""

from pathlib import Path
from typing import Protocol
from localresearcher.core.schemas import Document


class DocumentLoader(Protocol):
    """Protocol for document loaders."""
    
    def load(self, path: Path) -> Document:
        """Load a document from a file."""
        ...


class TextLoader:
    """Load plain text files."""
    
    def load(self, path: Path) -> Document:
        """Load a text file."""
        content = path.read_text(encoding="utf-8")
        return Document(
            path=str(path),
            content=content,
            file_type="text",
            metadata={"size": len(content)},
        )


class MarkdownLoader:
    """Load Markdown files."""
    
    def load(self, path: Path) -> Document:
        """Load a Markdown file."""
        content = path.read_text(encoding="utf-8")
        return Document(
            path=str(path),
            content=content,
            file_type="markdown",
            metadata={"size": len(content)},
        )


class PDFLoader:
    """Load PDF files."""
    
    def load(self, path: Path) -> Document:
        """Load a PDF file."""
        try:
            from pypdf import PdfReader
            
            reader = PdfReader(path)
            content = ""
            for page in reader.pages:
                content += page.extract_text() + "\n"
            
            return Document(
                path=str(path),
                content=content.strip(),
                file_type="pdf",
                metadata={
                    "pages": len(reader.pages),
                    "size": len(content),
                },
            )
        except Exception as e:
            raise ValueError(f"Failed to load PDF: {e}")


def get_loader(path: Path) -> DocumentLoader:
    """Get appropriate loader for file type."""
    suffix = path.suffix.lower()
    
    if suffix == ".pdf":
        return PDFLoader()
    elif suffix == ".md":
        return MarkdownLoader()
    elif suffix in {".txt", ".text"}:
        return TextLoader()
    else:
        # Default to text loader
        return TextLoader()


def load_document(path: Path) -> Document:
    """Load a document using the appropriate loader."""
    loader = get_loader(path)
    return loader.load(path)