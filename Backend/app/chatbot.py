from typing import List, Dict, Any
from pathlib import Path
import os
from dotenv import load_dotenv

# Importaciones de nuestros módulos internos (todos dentro de app)
from app.loader import load_documents
from app.splitter import split_documents
from app.vector_store import create_vector_store
from app.retriever import create_retriever
from app.llm import get_llm
from app.prompts import create_prompt
from app.config import EMBEDDING_MODEL, GOOGLE_API_KEY, PDF_PATH
from app.embeddings import get_embeddings

# Importaciones de LangChain (necesarias para anotaciones opcionales)
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

class CorporateAIAgent:
    """
    Agente RAG que responde preguntas basándose en un documento PDF.
    """

    def __init__(self):
        self.retriever = None
        self.llm = get_llm()
        self.prompt = create_prompt()

    def initialize(self):
        """Carga el PDF, lo fragmenta, construye la base vectorial y el retriever."""
        documents = load_documents()
        chunks = split_documents(documents)
        vector_store = create_vector_store(chunks)
        self.retriever = create_retriever(vector_store)

    def ask(self, question: str) -> str:
        """
        Busca contexto relevante, lo combina con la pregunta y consulta a Gemini.
        """
        # 1. Obtener documentos relevantes
        docs = self.retriever.invoke(question)

        # 2. Construir el contexto a partir de los fragmentos
        context = "\n\n".join(doc.page_content for doc in docs)

        # 3. Generar los mensajes con el prompt
        messages = self.prompt.invoke({
            "context": context,
            "question": question
        })

        # 4. Llamar a Gemini
        response = self.llm.invoke(messages)

        # 5. Extraer el contenido de la respuesta (puede ser str o lista)
        if isinstance(response.content, list):
            for item in response.content:
                if isinstance(item, dict) and item.get("type") == "text":
                    return item.get("text", "")
            return ""
        return response.content