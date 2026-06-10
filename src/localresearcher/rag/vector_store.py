"""Vector store using ChromaDB."""

import chromadb
from pathlib import Path
from typing import Sequence
from localresearcher.core.config import settings
from localresearcher.core.schemas import Document
from localresearcher.rag.chunker import TextChunker
from localresearcher.rag.embeddings import EmbeddingProvider


class VectorStore:
    """ChromaDB-based vector store."""
    
    def __init__(
        self,
        persist_directory: Path | None = None,
        collection_name: str = "documents",
    ):
        self.persist_directory = persist_directory or settings.vector_store_path
        self.collection_name = collection_name
        
        self.client = chromadb.PersistentClient(path=str(self.persist_directory))
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"},
        )
        
        self.chunker = TextChunker(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
        )
        self.embedding_provider = EmbeddingProvider()
    
    async def add_document(self, document: Document) -> None:
        """Add a document to the vector store."""
        chunks = self.chunker.chunk(document.content)
        
        if not chunks:
            return
        
        embeddings = await self.embedding_provider.embed_batch(chunks)
        
        ids = [f"{document.id}_{i}" for i in range(len(chunks))]
        metadatas = [
            {
                "doc_id": str(document.id),
                "path": document.path,
                "file_type": document.file_type,
                "chunk_index": i,
            }
            for i in range(len(chunks))
        ]
        
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
        )
    
    async def search(self, query: str, top_k: int | None = None) -> list[str]:
        """Search for relevant document chunks."""
        top_k = top_k or settings.top_k_retrieval
        
        query_embedding = await self.embedding_provider.embed(query)
        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )
        
        if not results["documents"]:
            return []
        
        return results["documents"][0]
    
    def clear(self) -> None:
        """Clear all documents from the collection."""
        self.client.delete_collection(self.collection_name)
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"},
        )
    
    async def close(self) -> None:
        """Close the embedding provider."""
        await self.embedding_provider.close()