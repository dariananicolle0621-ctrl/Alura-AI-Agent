from langchain_huggingface import HuggingFaceEmbeddings

from Backend.app.config import EMBEDDING_MODEL


def get_embeddings():
    """
    Inicializa y devuelve el modelo de embeddings.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embeddings