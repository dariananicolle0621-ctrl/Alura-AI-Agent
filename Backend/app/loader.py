from langchain_community.document_loaders import PyPDFLoader
from app.config import PDF_PATH

def load_documents():
    """Carga el PDF y devuelve una lista de documentos (páginas)."""
    loader = PyPDFLoader(str(PDF_PATH))
    return loader.load()