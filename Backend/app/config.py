from pathlib import Path
import os
from dotenv import load_dotenv

# Directorio raíz del proyecto (sube un nivel desde app/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env
load_dotenv(BASE_DIR / ".env")

# Carpeta donde está el PDF
DATA_DIR = BASE_DIR / "data"

# Ruta completa al PDF (ajusta el nombre si es diferente)
PDF_PATH = DATA_DIR / "POLÍTICA DE ATENCIÓN AL CLIENTE, CAMBIOS Y DEVOLUCIONES.pdf"

# Clave de API de Google
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Modelo de embeddings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"