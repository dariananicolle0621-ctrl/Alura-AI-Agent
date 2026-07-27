from pathlib import Path
import os
from dotenv import load_dotenv

# Directorio raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar el archivo .env desde la raíz del proyecto
load_dotenv(BASE_DIR / ".env")

# Carpeta de datos
DATA_DIR = BASE_DIR / "data"

# Ruta del PDF
PDF_PATH = DATA_DIR / "POLÍTICA DE ATENCIÓN AL CLIENTE, CAMBIOS Y DEVOLUCIONES (1).pdf"

# API Key de Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Modelo de embeddings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
