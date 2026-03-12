from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)
# Load trained model and encoders
model = joblib.load("random_forest_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
symptom_index = joblib.load("symptom_index.pkl")

description_df = pd.read_csv("description.csv")
precaution_df = pd.read_csv("precaution.csv")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        symptoms = data.get("symptoms", [])
        
        if not symptoms:
            return jsonify({"error": "Please provide at least one symptom."}), 400

        # Convert symptoms to lowercase and map them to index
        symptom_vector = np.zeros(len(symptom_index), dtype=int)
        for symptom in symptoms:
            symptom = symptom.lower().strip()
            if symptom in symptom_index:
                symptom_vector[symptom_index[symptom]] = 1
            else:
                print(f"⚠️ Warning: '{symptom}' not found in training features. Check spelling!")

        # Predict disease
        symptom_vector = symptom_vector.reshape(1, -1)
        predicted_disease_index = model.predict(symptom_vector)[0]
        predicted_disease = label_encoder.inverse_transform([predicted_disease_index])[0]

        # Get disease description
        description = description_df.loc[description_df["Disease"] == predicted_disease, "Description"]
        description = description.values[0] if not description.empty else "No description available."

        # Get precautions
        precautions = precaution_df.loc[precaution_df["Disease"] == predicted_disease].iloc[:, 1:].values.flatten().tolist()

        return jsonify({
            "disease": predicted_disease,
            "description": description,
            "precautions": precautions
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
