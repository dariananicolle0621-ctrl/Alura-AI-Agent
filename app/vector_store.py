from langchain_community.vectorstores import FAISS

from app.embeddings import get_embeddings


def create_vector_store(chunks):
    """
    Crea una base vectorial FAISS a partir de los fragmentos.
    """

    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store