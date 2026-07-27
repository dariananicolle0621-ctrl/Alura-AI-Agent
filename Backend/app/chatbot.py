# Imports necesarios (algunos ya estaban en tu código)
from typing import List, Dict, Any
from pathlib import Path
import os
from dotenv import load_dotenv

# Imports de tus módulos internos
from Backend.app.loader import load_documents
from Backend.app.splitter import split_documents
from Backend.app.vector_store import create_vector_store
from app.retriever import create_retriever
from Backend.app.llm import get_llm
from Backend.app.prompts import create_prompt
from Backend.app.config import EMBEDDING_MODEL, GOOGLE_API_KEY, PDF_PATH
from Backend.app.embeddings import get_embeddings

# Imports de LangChain (los que usas en los imports)
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# Si quieres anotaciones de tipo más precisas, importa estas (opcional)
# from langchain_core.documents import Document
# from langchain_core.retrievers import Retriever
# from langchain_core.language_models import LLM
# from langchain_core.prompts import PromptTemplate

class CorporateAIAgent:
    """
    Agente RAG que responde preguntas basándose en un documento PDF.
    """

    def __init__(self):
        # Sin anotaciones de tipo para evitar errores si no están importadas
        self.retriever = None
        self.llm = get_llm()
        self.prompt = create_prompt()

    def initialize(self):
        """
        Carga el PDF y prepara el sistema RAG.
        """
        documents = load_documents()
        chunks = split_documents(documents)

        vector_store = create_vector_store(chunks)

        self.retriever = create_retriever(vector_store)

    def ask(self, question: str) -> str:
        """
        Busca contexto relevante y consulta Gemini.
        """
        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        messages = self.prompt.invoke({
            "context": context,
            "question": question
        })

        response = self.llm.invoke(messages)

        # Manejo robusto del contenido (tomado del código 1)
        if isinstance(response["content"], list):
            for item in response["content"]:
                if isinstance(item, dict) and item.get("type") == "text":
                    return item.get("text", "")
            return ""

        return response["content"]