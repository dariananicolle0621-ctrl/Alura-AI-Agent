from langchain_huggingface import HuggingFaceEmbeddings
from app.config import EMBEDDING_MODEL

def get_embeddings():
    """Inicializa y devuelve el modelo de embeddings."""
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)