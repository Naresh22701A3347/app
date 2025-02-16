# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/digitize', methods=['POST'])
def digitize():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['image']
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    # Read the image file
    in_memory_file = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(in_memory_file, cv2.IMREAD_COLOR)

    # Preprocess the image (convert to grayscale)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Use Tesseract to do OCR on the processed image
    text = pytesseract.image_to_string(thresh)

    return jsonify({'digitizedText': text})

if __name__ == '__main__':
    app.run(debug=True)