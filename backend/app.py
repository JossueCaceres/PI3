from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from controllers.circuitos import circuitos_bp
import os

#Inicia o crea tu backend server de Flask
app = Flask(__name__)
CORS(app)
app.register_blueprint(circuitos_bp)

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Límite diario de generación alcanzado. Intenta de nuevo mañana."}), 429

@app.route('/descargar/<filename>')
def descargar_archivo(filename):
    storage_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'storage'))
    return send_from_directory(storage_dir, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
