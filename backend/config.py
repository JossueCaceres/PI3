# Configuración general del backend

import os
from dotenv import load_dotenv
load_dotenv()

# El token debe venir de variable de entorno
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_TOKEN2 = os.getenv("GITHUB_TOKEN2")
GITHUB_TOKEN3 = os.getenv("GITHUB_TOKEN3")
GITHUB_AI_ENDPOINT = "https://models.github.ai/inference"
GITHUB_AI_MODEL = "openai/gpt-4.1"
