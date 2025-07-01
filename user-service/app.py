from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
users = []

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

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
