from flask import Flask, request, jsonify
from flask_cors import CORS  # Optional: if frontend calls API
import uuid


app = Flask(__name__)
CORS(app)  # Optional: allows cross-origin requests

users = []


# ✅ Health check route for CI testing & monitoring
@app.route('/')
def home():
    return 'User service is running', 200


@app.route('/health')
def health():
    return 'OK', 200


# ✅ GET all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)


# ✅ POST create new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {
        'id': str(uuid.uuid4()),
        'name': data.get('name'),
        'email': data.get('email')
    }
    users.append(user)
    return jsonify(user), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
