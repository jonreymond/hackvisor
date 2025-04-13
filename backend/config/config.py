import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Data paths
CLIENT_STATE_PATH = os.path.abspath("data/client_state.csv")
PRODUCT_PORTFOLIO_PATH = os.path.abspath("data/raiffeisenprodukte_final_EN.docx")
TRANSCRIPT_PATH = os.path.abspath("data/transcript.m4a")
BIASES_PATH = os.path.abspath("data/biases.csv")
OUTPUT_DIR = os.path.abspath("output")

# Vector store path
VECTOR_STORE_PATH = os.path.abspath("data/vector_store")

# Model configuration
LLM_MODEL = "gpt-4o"  # Azure OpenAI deployment name
EMBEDDING_MODEL = "text-embedding-ada-002"

# Agent configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
