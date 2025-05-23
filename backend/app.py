from flask import Flask, jsonify
from controllers.circuitos import circuitos_bp

app = Flask(__name__)
app.register_blueprint(circuitos_bp)

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"error": "Límite diario de generación alcanzado. Intenta de nuevo mañana."}), 429

if __name__ == "__main__":
    app.run(debug=True)
