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

if __name__ == '__main__':
    app.run(port=5000, debug=True)