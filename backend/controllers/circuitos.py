# Lógica de endpoints relacionados con circuitos

from flask import Blueprint, request, jsonify
from services.generador import generar_proyectos

circuitos_bp = Blueprint('circuitos', __name__)

@circuitos_bp.route('/api/componentes', methods=['POST'])
def recibir_componentes():
    data = request.json
    componentes = data.get('componentes', [])
    proyectos = generar_proyectos(componentes)
    # Si algún proyecto tiene error de rate limit, responde 429
    if any('error' in p for p in proyectos):
        return jsonify({"error": "Límite diario de generación alcanzado. Intenta de nuevo mañana.", "proyectos": proyectos}), 429
    return jsonify({"proyectos": proyectos})
