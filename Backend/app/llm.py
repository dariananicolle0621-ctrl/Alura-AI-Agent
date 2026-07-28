from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GOOGLE_API_KEY

def get_llm():
    """Inicializa el modelo Gemini (Flash)."""
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",  # o "gemini-2.0-flash" según disponibilidad
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2,
    )