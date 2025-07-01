from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
flights = []

@app.route('/api/flights', methods=['GET'])
def get_flights():
    return jsonify(flights)

@app.route('/api/flights', methods=['POST'])
def add_flight():
    data = request.get_json()
    flight = {
        'id': str(uuid.uuid4()),
        'origin': data.get('origin'),
        'destination': data.get('destination')
    }
    flights.append(flight)
    return jsonify(flight), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
