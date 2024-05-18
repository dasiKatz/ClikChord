
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/audio_file', methods=['POST'])
def audio_file():
    # Check if the post request has the file part
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['audioFile']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file
    file_path = os.path.join("C:/Users/User/Desktop/Project", "song.mp3")
    file.save(file_path)
#####כאן מבצעים את כל הפונקציות




    return jsonify({'message': 'File received and saved as uploaded_file.mp3'}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
