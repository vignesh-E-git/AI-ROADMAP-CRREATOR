from flask import Flask, request, jsonify, send_from_directory
import os
import main

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/roadmap', methods=['POST'])
def generate_roadmap():
    data = request.json
    topic = data.get('topic')
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    try:
        # Calls the existing logic from main.py
        result = main.roadmap(topic)
        return jsonify({'roadmap': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("==================================================")
    print("🚀 Blueprint Web Server is starting...")
    print("👉 To view the UI, open your browser to: http://127.0.0.1:5000")
    print("⚠️ Make sure you have flask installed: pip install flask")
    print("==================================================")
    app.run(debug=True, port=5000)
