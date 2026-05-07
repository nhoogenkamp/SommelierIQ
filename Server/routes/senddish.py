from flask import request, jsonify

# Function handles POST request from frontend
def send_dish():

    # Reading the JSON sent
    data = request.get_json()
    # Print received data in Flask terminal
    print(data)
    
    # Return same data back to frontend
    return jsonify(data), 200