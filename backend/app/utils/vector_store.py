import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.config import (
    OPENAI_API_KEY,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    VECTOR_STORE_PATH,
    EMBEDDING_MODEL,
)


class VectorStore:
    """Utility class to manage the vector store for semantic search."""

    def __init__(self):
        """Initialize the vector store with OpenAI embeddings."""
        self.embeddings = OpenAIEmbeddings(
            model=EMBEDDING_MODEL, openai_api_key=OPENAI_API_KEY
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
        )
        self.vector_store = None

    def create_or_load(self, texts, collection_name):
        """Create a new vector store or load an existing one."""
        os.makedirs(VECTOR_STORE_PATH, exist_ok=True)

        # Collection path for this specific data
        collection_path = os.path.join(VECTOR_STORE_PATH, collection_name)

        # Check if vector store already exists
        if os.path.exists(collection_path) and os.path.isdir(collection_path):
            try:
                print(f"Loading existing vector store from {collection_path}")
                self.vector_store = FAISS.load_local(
                    collection_path,
                    self.embeddings,
                    allow_dangerous_deserialization=True,
                )
                return self.vector_store
            except Exception as e:
                print(f"Error loading vector store: {e}")
                print("Creating a new vector store...")

        # Create new vector store if it doesn't exist or loading failed
        docs = self._prepare_documents(texts)

        if not docs:
            print("No documents to index.")
            return None

        print(f"Creating new vector store with {len(docs)} documents")
        self.vector_store = FAISS.from_documents(docs, self.embeddings)

        # Save the vector store locally
        try:
            self.vector_store.save_local(collection_path)
            print(f"Vector store saved to {collection_path}")
        except Exception as e:
            print(f"Error saving vector store: {e}")

        return self.vector_store

    def _prepare_documents(self, texts):
        """Split the text into documents for indexing."""
        if isinstance(texts, str):
            # Single text, split it into chunks
            docs = self.text_splitter.create_documents([texts])
        elif isinstance(texts, list) and all(isinstance(item, str) for item in texts):
            # List of texts, split each one
            docs = self.text_splitter.create_documents(texts)
        elif isinstance(texts, list) and all(
            hasattr(item, "page_content") for item in texts
        ):
            # Already documents
            docs = texts
        else:
            print(f"Unsupported text format: {type(texts)}")
            return []

        return docs

    def search(self, query, k=5):
        """Search the vector store for relevant documents."""
        if not self.vector_store:
            print("Vector store not initialized.")
            return []

        try:
            results = self.vector_store.similarity_search(query, k=k)
            return results
        except Exception as e:
            print(f"Error searching vector store: {e}")
            return []
