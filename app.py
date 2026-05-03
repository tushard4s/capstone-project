from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Database Configuration
SUPABASE_URL = "https://nndermmeqarudyosmyfr.supabase.co/rest/v1/notes"
HEADERS = {
    "apikey": "sb_publishable_W2hM4twNuzWPpNliQVl4Hw_cuX-KaPF",
    "Authorization": "Bearer sb_publishable_W2hM4twNuzWPpNliQVl4Hw_cuX-KaPF",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

@app.route('/api/notes', methods=['GET'])
def get_notes():
    # Logic: SELECT all notes from Supabase
    response = requests.get(SUPABASE_URL, headers=HEADERS)
    return jsonify(response.json())

@app.route('/api/notes', methods=['POST'])
def add_note():
    # Logic: INSERT a new note from the frontend form
    data = request.json
    response = requests.post(SUPABASE_URL, headers=HEADERS, json=data)
    return jsonify(response.json()), 201

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    # Logic: DELETE a note from Supabase
    delete_url = f"{SUPABASE_URL}?id=eq.{note_id}"
    response = requests.delete(delete_url, headers=HEADERS)
    # Supabase typically returns 204 No Content for successful deletes
    if response.status_code == 204:
        return '', 204
    
    # If there's an error, it might return a JSON response
    try:
        return jsonify(response.json()), response.status_code
    except ValueError:
        return jsonify({"error": "Failed to delete"}), response.status_code

if __name__ == '__main__':
    app.run(port=5000, debug=True)