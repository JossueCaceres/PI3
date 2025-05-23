# Integración con OpenAI para generación de código y descripciones

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from openai import OpenAI
from backend.config import GITHUB_TOKEN, GITHUB_AI_ENDPOINT, GITHUB_AI_MODEL
from dotenv import load_dotenv
load_dotenv()

def chatgpt_test(prompt):
    client = OpenAI(
        base_url=GITHUB_AI_ENDPOINT,
        api_key=GITHUB_TOKEN,
    )
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Eres un asistente útil para proyectos de electrónica educativa."},
            {"role": "user", "content": prompt}
        ],
        temperature=1.0,
        top_p=1.0,
        model=GITHUB_AI_MODEL
    )
    return response.choices[0].message.content

def chatgpt_test_token(prompt, token):
    client = OpenAI(
        base_url=GITHUB_AI_ENDPOINT,
        api_key=token,
    )
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Eres un asistente útil para proyectos de electrónica educativa."},
            {"role": "user", "content": prompt}
        ],
        temperature=1.0,
        top_p=1.0,
        model=GITHUB_AI_MODEL
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Prueba rápida
    prompt = "¿Cuál es la capital de Francia?"
    print(chatgpt_test(prompt))
