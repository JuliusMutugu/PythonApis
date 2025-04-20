import random
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from DoubleLinkedList import DoublyLinkedList


app = Flask(__name__)
CORS(app)  

# Initialized the linked list
trip_list = DoublyLinkedList()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trips', methods=['GET'])
def get_trips():
    return jsonify(trip_list.to_array()), 200

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route('/add', methods=['POST'])
def add_trip():
    try:
        data = request.get_json()
        if 'pickup' not in data or 'destination' not in data or 'time' not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        trip_list.append(data)
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/trips/<int:id>', methods=['PUT'])
def update_trip(id):
    data = request.get_json()
    status = data.get('status')

    if not status:
        return jsonify({"error": "Status is required"}), 400

    updated = trip_list.update_trip_status(id, status)
    if updated:
        return jsonify({"id": id, "status": status}), 200
    else:
        return jsonify({"error": "Trip not found"}), 404

@app.route('/trips/<int:id>', methods=['DELETE'])
def delete_trip(id):
    deleted = trip_list.remove_by_id(id)
    if deleted:
        return jsonify({"message": "Trip deleted successfully"}), 200
    else:
        return jsonify({"error": "Trip not found"}), 404

@app.route('/trips/search/<search_term>', methods=['GET'])
def search_trip(search_term):
    result = trip_list.find(search_term)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "No trip found"}), 404
    
@app.route('/add', methods=['POST'])
def add():
    # Parse JSON from request
    trip_data = request.get_json()

    if not trip_data:
        return jsonify({'error': 'Invalid input'}), 400

    # Add trip data with random id
    trip = {
        'id': random.randint(1, 1000),
        'pickup': trip_data['pickup'],
        'destination': trip_data['destination'],
        'time': trip_data['time'],
        'capacity': 14,
        'booked': 10,
        'status': trip_data['status']
    }

    trip_list.append(trip)
    return jsonify({'message': 'Trip added successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
