import os
import sys
import uuid
import re
import json as pyjson
from concurrent.futures import ThreadPoolExecutor
#Si estas corriendo solo "generador.py"
#from open_services import chatgpt_test_token 

#Si estas corriendo App.py desde el directorio del proyecto
from services.openai_service import chatgpt_test_token 

from openai import RateLimitError

def generar_proyectos(componentes):
    # componentes: lista de dicts, ej: [{"nombre": "LED", "cantidad": 3}, ...]
    niveles = [
        {
            "nivel": "fácil",
            "prompt": (
                "Eres un experto en electrónica educativa. "
                "Genera un circuito sencillo y pedagógico usando los componentes listados y sus cantidades. "
                "La descripción debe ser puntual y explicar el objetivo didáctico. "
                "El código Arduino (sketch.ino) debe estar muy comentado, explicando cada línea para principiantes. "
                "El diagrama (diagram.json) debe diferenciar claramente las piezas, ubicarlas separadas y evitar superposición o paralelismo de cables. "
                "Asegúrate de que el circuito sea fácil de armar y entender. "
                "El README debe ser breve, incluir instrucciones paso a paso y al menos un tip práctico para evitar errores comunes. "
                "No uses todos los componentes si no es necesario, prioriza la claridad. "
                "Incluye en la respuesta un enumerado SQL de los componentes usados y su cantidad, por ejemplo: INSERT INTO componentes (nombre, cantidad) VALUES ... "
            )
        },
        {
            "nivel": "medio",
            "prompt": (
                "Eres un experto en electrónica educativa. "
                "Genera un circuito de dificultad media usando más componentes y lógica intermedia, considerando las cantidades disponibles. "
                "La descripción debe ser puntual y resaltar el aprendizaje esperado. "
                "El código Arduino (sketch.ino) debe estar muy comentado, explicando bloques de lógica y conexiones. "
                "El diagrama (diagram.json) debe diferenciar claramente las piezas, ubicarlas de forma ordenada y evitar superposición o paralelismo de cables. "
                "El circuito debe ser un reto razonable para estudiantes con conocimientos básicos. "
                "El README debe ser breve, incluir instrucciones claras y al menos un tip para organizar los cables. "
                "No uses todos los componentes si no es necesario, prioriza la pedagogía. "
                "Incluye en la respuesta un enumerado SQL de los componentes usados y su cantidad, por ejemplo: INSERT INTO componentes (nombre, cantidad) VALUES ... "
            )
        },
        {
            "nivel": "difícil",
            "prompt": (
                "Eres un experto en electrónica educativa. "
                "Genera un circuito avanzado y pedagógico usando todos los componentes posibles, lógica compleja y conexiones bien organizadas, considerando las cantidades disponibles. "
                "La descripción debe ser puntual y resaltar el desafío y los conceptos avanzados involucrados. "
                "El código Arduino (sketch.ino) debe estar muy comentado, explicando cada bloque funcional y las decisiones de diseño. "
                "El diagrama (diagram.json) debe diferenciar claramente las piezas, ubicarlas de forma óptima y evitar superposición o paralelismo de cables. "
                "El circuito debe ser un reto para estudiantes avanzados. "
                "El README debe ser breve, incluir instrucciones resumidas y al menos un tip para depurar errores complejos. "
                "No uses todos los componentes si no es necesario, prioriza la pedagogía. "
                "Incluye en la respuesta un enumerado SQL de los componentes usados y su cantidad, por ejemplo: INSERT INTO componentes (nombre, cantidad) VALUES ... "
            )
        }
    ]
    proyectos = []
    # Corrige el path para que siempre apunte a /Users/jossuec/Desktop/PROYECTO/PI3/backend/storage
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../storage'))
    os.makedirs(output_dir, exist_ok=True)

    # Calcula la ruta del directorio raiz
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(root_dir)
    # Selección de tokens para paralelismo
    from config import GITHUB_TOKEN, GITHUB_TOKEN2, GITHUB_TOKEN3
    tokens = [
        GITHUB_TOKEN,
        GITHUB_TOKEN2,
        GITHUB_TOKEN3
    ]

    # Almacena el SQL de cada proyecto en un archivo indexado por id
    sql_index_path = os.path.join(output_dir, "proyectos_componentes.sql.json")
    try:
        if os.path.exists(sql_index_path):
            with open(sql_index_path, "r") as f:
                sql_index = pyjson.load(f)
        else:
            sql_index = {}
    except Exception:
        sql_index = {}

    def extraer_sql(texto):
        # Busca la primera línea tipo INSERT INTO ... VALUES ...;
        match = re.search(r'(INSERT INTO componentes \(nombre, cantidad\) VALUES [^;]+;)', texto)
        return match.group(1) if match else None

    def limpiar_backticks(texto):
        return re.sub(r'```[a-zA-Z]*\n?|```', '', texto).strip()

    def generar_para_nivel(nivel, idx):
        proyecto_id = str(uuid.uuid4())
        prompt_base = nivel["prompt"] + f" Lista de componentes y cantidades: {componentes}. "
        prompt_desc = prompt_base + "Dame solo una descripción puntual del circuito y el enumerado SQL."
        prompt_sketch = prompt_base + "Dame solo el código Arduino (sketch.ino) muy comentado, sin explicación adicional."
        prompt_diagram = prompt_base + "Dame solo el JSON de diagrama tipo Wokwi (diagram.json), sin explicación adicional."
        prompt_readme = prompt_base + "Dame solo un README breve con instrucciones y tips para armar el circuito."
        token = tokens[idx % len(tokens)]
        try:
            descripcion = limpiar_backticks(chatgpt_test_token(prompt_desc, token))
            sketch = limpiar_backticks(chatgpt_test_token(prompt_sketch, token))
            diagram = limpiar_backticks(chatgpt_test_token(prompt_diagram, token))
            readme = limpiar_backticks(chatgpt_test_token(prompt_readme, token))
        except RateLimitError as e:
            return {
                "id": None,
                "nivel": nivel["nivel"],
                "error": "Límite diario de generación alcanzado. Intenta de nuevo mañana.",
                "detalle": str(e)
            }
        # Extrae el SQL de la descripción
        sql = extraer_sql(descripcion)
        if sql:
            sql_index[proyecto_id] = sql
            with open(sql_index_path, "w", encoding="utf-8") as f:
                pyjson.dump(sql_index, f, indent=2, ensure_ascii=False)
        sketch_path = os.path.join(output_dir, f"{proyecto_id}_sketch.ino")
        diagram_path = os.path.join(output_dir, f"{proyecto_id}_diagram.json")
        readme_path = os.path.join(output_dir, f"{proyecto_id}_README.md")
        with open(sketch_path, "w", encoding="utf-8") as f: f.write(sketch)
        with open(diagram_path, "w", encoding="utf-8") as f: f.write(diagram)
        with open(readme_path, "w", encoding="utf-8") as f: f.write(readme)
        return {
            "id": proyecto_id,
            "nivel": nivel["nivel"],
            "descripcion": descripcion,
            "archivos": {
                "sketch": f"/descargar/{proyecto_id}_sketch.ino",
                "diagrama": f"/descargar/{proyecto_id}_diagram.json",
                "readme": f"/descargar/{proyecto_id}_README.md"
            },
            "sql": sql
        }

    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [executor.submit(generar_para_nivel, nivel, idx) for idx, nivel in enumerate(niveles)]
        for futuro in futuros:
            proyectos.append(futuro.result())
    return proyectos

# Test manual
if __name__ == "__main__":
    # Aqui debe de ir la lista de componentes detectados por el modelo de CV 
    componentes = [{"nombre": "Arduino UNO", "cantidad": 1}, {"nombre": "Protoboard", "cantidad": 1}, {"nombre": "LED", "cantidad": 3}, {"nombre": "Resistencia", "cantidad": 3}, {"nombre": "Jumpers", "cantidad": 10}]
    proyectos = generar_proyectos(componentes)
    for p in proyectos:
        print(f"\nNivel: {p['nivel']}")
        print(f"Descripción: {p['descripcion']}")
        print(f"Archivos: {p['archivos']}")
