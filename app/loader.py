from langchain_community.document_loaders import PyPDFLoader

from app.config import PDF_PATH


def load_documents():
    """
    Carga el documento PDF y devuelve una lista de páginas.
    """

    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()

    return documents