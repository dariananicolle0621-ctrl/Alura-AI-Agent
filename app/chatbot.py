from app.loader import load_documents
from app.splitter import split_documents
from app.vector_store import create_vector_store
from app.retriever import create_retriever
from app.llm import get_llm
from app.prompts import create_prompt


class CorporateAIAgent:
    """
    Agente RAG que responde preguntas basándose en un documento PDF.
    """

    def __init__(self):
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

    def ask(self, question):
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

        if isinstance(response.content, list):
            for item in response.content:
                if isinstance(item, dict) and item.get("type") == "text":
                    return item.get("text", "")

            return ""

        return response.content