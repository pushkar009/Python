from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

data_file_path = 'data.json'

# Load data from the file if it exists and is valid
def load_data():
    if os.path.exists(data_file_path):
        try:
            with open(data_file_path, 'r') as file:
                content = file.read().strip()  # Read and strip any spaces
                if content:  # Ensure the file is not empty
                    return json.loads(content)
                else:
                    return []  # Return an empty list if the file is empty
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file '{data_file_path}': {e}")
            return []  # Return an empty list if JSON is invalid
    else:
        return []  # Return an empty list if the file doesn't exist

# Save data to file
def save_data_to_file(data):
    with open(data_file_path, 'w') as file:
        json.dump(data, file, indent=4)  # Pretty print JSON with indentation

# Initialize `data` variable
data = load_data()

# Serve the index.html file
@app.route('/')
def index():
    html_path = os.path.join(os.path.dirname(__file__), 'index.html')
    if os.path.exists(html_path):
        with open(html_path, 'r') as f:
            return f.read()
    else:
        return "<h1>index.html not found!</h1>", 404

# API endpoint to store data
@app.route('/api/store', methods=['POST'])
def store_data():
    new_data = request.form.get('data')  # Fetch the 'data' from the POST request
    
    if not new_data:  # Validate that data is not empty
        return jsonify({'error': 'No data provided'}), 400

    data.append(new_data)  # Append new data to the list
    
    save_data_to_file(data)  # Save the updated data to the file
    
    return jsonify({'id': len(data)}), 201  # Return the new id (index) of the data

# API endpoint to retrieve data by ID
@app.route('/api/retrieve', methods=['GET'])
def retrieve_data():
    try:
        data_id = int(request.args.get('id'))  # Get the 'id' parameter from the URL
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid ID'}), 400  # Return error if 'id' is not a valid integer
    
    if data_id < 1 or data_id > len(data):
        return jsonify({'error': 'Data Not Found'}), 404  # Return error if 'id' is out of bounds
    
    data_value = data[data_id - 1]  # Retrieve the data by its 1-based index
    
    return jsonify({'id': data_id, 'data': data_value})

if __name__ == '__main__':
    app.run(debug=True)
