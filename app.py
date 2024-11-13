# This is not ready for production

from flask import Flask, request, jsonify
import os
import subprocess
import shutil

app = Flask(__name__)

# Set the base root directory for GraphRAG
GRAPH_RAG_ROOT = './ragtest'
INPUT_FOLDER = os.path.join(GRAPH_RAG_ROOT, 'input')

# Ensure input folder exists
os.makedirs(INPUT_FOLDER, exist_ok=True)

@app.route('/initialize', methods=['GET'])
def initialize_workspace():
    """Initialize GraphRAG workspace. Clears existing workspace if it exists."""

    def clear_directory(directory_path):
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):  
                shutil.rmtree(item_path)

    # Clear the contents of the GRAPH_RAG_ROOT directory if it exists
    if os.path.exists(GRAPH_RAG_ROOT):
        clear_directory(GRAPH_RAG_ROOT)

    # Recreate the input folder and initialize the workspace
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    subprocess.run(['graphrag', 'init', '--root', GRAPH_RAG_ROOT], check=True)
    
    return jsonify({"message": "Workspace initialized successfully."}), 200

@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload a text file to the input folder for indexing."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    if file and file.filename.endswith('.txt'):
        file_path = os.path.join(INPUT_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({"message": f"File '{file.filename}' uploaded successfully."}), 200
    else:
        return jsonify({"error": "Only .txt files are allowed"}), 400

@app.route('/index', methods=['GET'])
def index_documents():
    """Index documents in GraphRAG workspace."""
    if not os.path.exists(GRAPH_RAG_ROOT):
        return jsonify({"error": "Workspace not initialized."}), 400

    subprocess.run(['graphrag', 'index', '--root', GRAPH_RAG_ROOT], check=True)
    return jsonify({"message": "Indexing completed successfully."}), 200

@app.route('/query', methods=['POST'])
def query():
    """Query the indexed content with specified method and question."""
    data = request.get_json()
    query_method = data.get('method')
    query_text = data.get('query')

    if query_method not in ['global', 'local']:
        return jsonify({"error": "Invalid query method. Choose 'global' or 'local'."}), 400

    if not query_text:
        return jsonify({"error": "Query text is required."}), 400

    result = subprocess.run(
        ['graphrag', 'query', '--root', GRAPH_RAG_ROOT, '--method', query_method, '--query', query_text],
        capture_output=True, text=True, check=True
    )

    return jsonify({"result": result.stdout.strip()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
