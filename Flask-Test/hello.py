from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ruta para la página principal (frontend)
@app.route('/')
def home():
    return render_template('index.html')  # Archivo HTML que crearemos después

# Ruta para interactuar con el backend
@app.route('/process', methods=['POST'])
def process():
    data = request.json  # Datos enviados desde el frontend
    # Aquí puedes conectar tu lógica de Python
    result = {"response": f"Recibido: {data}"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)