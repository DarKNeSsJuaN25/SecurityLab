from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)

# Clave de autorización API KEY
API_KEY = "000000111111"

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'  # Cambia esto por una clave secreta segura
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    # Verifica las credenciales (puedes personalizar esto)
    if request.json.get('api_key') == API_KEY:
        access_token = create_access_token(identity='usuario')
        return jsonify({'access_token': access_token})
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401

@app.route('/group01', methods=['GET'])
@jwt_required()  # Requiere un token JWT válido
def group01():
    return jsonify({'result': 'Este es el grupo 01'})

@app.route('/group02', methods=['GET'])
@jwt_required()  # Requiere un token JWT válido
def group02():
    return jsonify({'error': 'Acceso no autorizado'}), 401

@app.route('/group03', methods=['GET'])
@jwt_required()  # Requiere un token JWT válido
def group03():
    return jsonify({'error': 'Acceso no autorizado'}), 401

@app.route('/group04', methods=['GET'])
@jwt_required()  # Requiere un token JWT válido
def group04():
    return jsonify({'error': 'Acceso no autorizado'}), 401

if __name__ == "__main__":
    app.run(debug=True, port=5000)

