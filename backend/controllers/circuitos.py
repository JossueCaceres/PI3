# Lógica de endpoints relacionados con circuitos

from flask import Blueprint, request, jsonify
from services.generador import generar_proyectos
from services.cv_model import predecir_componentes

circuitos_bp = Blueprint('circuitos', __name__)

@circuitos_bp.route('/api/componentes', methods=['POST'])
def recibir_componentes():
    # Endpoint para recibir una lista de componentes(Del Frontend utilizando cv_model.py) y generar proyectos
    data = request.json
    componentes = data.get('componentes', [])
    proyectos = generar_proyectos(componentes)
    # Si algún proyecto tiene error de rate limit, responde 429
    if any('error' in p for p in proyectos):
        return jsonify({"error": "Límite diario de generación alcanzado. Intenta de nuevo mañana.", "proyectos": proyectos}), 429
    return jsonify({"proyectos": proyectos})


@circuitos_bp.route('/api/imagenes', methods=['POST'])
def recibir_imagenes():
    # Endpoint para recibir una lista de imágenes y generar proyectos
    imagenes = request.files.getlist('imagenes')
    if not imagenes:
        return jsonify({"error": "No se recibieron imágenes"}), 400
    
    # Aquí deberías llamar a tu función de predicción de componentes
    componentes, ids = predecir_componentes(imagenes)
    
    return jsonify({
        "componentes": componentes,
        "ids": list(ids)
    })

    #componentes = {"resistor": 2, "capacitor": 1}
    #ids = [1, 1, 3]