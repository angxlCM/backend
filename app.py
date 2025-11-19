from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde cualquier origen (GitHub Pages, etc.)

# Diccionario para guardar la última ubicación recibida
ultima_ubicacion = {}

# Recibe la ubicación desde el frontend (POST)
@app.route('/ubicacion', methods=['POST'])
def recibir_ubicacion():
    global ultima_ubicacion
    data = request.get_json()
    lat = data.get('latitud')
    lng = data.get('longitud')
    timestamp = data.get('timestamp')
    ultima_ubicacion = {"latitud": lat, "longitud": lng, "timestamp": timestamp}
    print(f"Ubicación guardada: {ultima_ubicacion}")
    return 'Ubicación recibida', 200

# Devuelve la última ubicación en formato JSON
@app.route('/ultima', methods=['GET'])
def enviar_ultima():
    return jsonify(ultima_ubicacion)

# Ruta principal de prueba
@app.route('/')
def home():
    return "API Flask activa y funcionando."

# Solo para desarrollo local, Railway ignora esto
if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
