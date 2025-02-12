from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend to access API

# Load the trained model & vectorizer
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route("/")
def home():
    return "Fake News Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.json
        news_text = data.get("text", "")

        if not news_text:
            return jsonify({"error": "No text provided"}), 400

        # Convert text to TF-IDF vector
        text_vector = vectorizer.transform([news_text]).toarray()

        # Predict using the model
        prediction = model.predict(text_vector)[0]
        result = "Fake News" if prediction == 1 else "Real News"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
