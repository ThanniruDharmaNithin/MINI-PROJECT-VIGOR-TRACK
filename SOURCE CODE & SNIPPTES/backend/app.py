from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from sklearn.utils import shuffle

app = Flask(__name__)

# Load models and data
tree = joblib.load("decision_tree_model.pkl")
rnd_forest = joblib.load("random_forest_model.pkl")
nb = joblib.load("naive_bayes_model.pkl")
knn = joblib.load("knn_model.pkl")

df = pd.read_csv('training_og.csv')
df = shuffle(df, random_state=42)

# Load severity data
df1 = pd.read_csv('severity.csv')
discrp = pd.read_csv("description.csv")
ektra7at = pd.read_csv("precaution.csv")

# List of features (symptoms) that were used to train the model
features = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 'prognosis'
]  # Ensure this matches your training data

def predd(x, S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17):
    psymptoms = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17]
    
    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    
    for j in range(len(psymptoms)):
        for k in range(len(a)):
            if psymptoms[j] == a[k]:
                psymptoms[j] = b[k]
    
    psy = [psymptoms]
    pred2 = x.predict(psy)
    
    disp = discrp[discrp['Disease'] == pred2[0]].values[0][1]
    recomnd = ektra7at[ektra7at['Disease'] == pred2[0]]
    c = np.where(ektra7at['Disease'] == pred2[0])[0][0]
    
    precuation_list = []
    for i in range(1, len(ektra7at.iloc[c])):
        precuation_list.append(ektra7at.iloc[c, i])
    
    return pred2[0], disp, precuation_list

# API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if 'symptoms' not in data or len(data['symptoms']) != 17:
            raise ValueError("Please provide exactly 17 symptoms.")

        # Unpack symptoms
        symptoms = data['symptoms']
        
        # Call the predd function with the Random Forest model and symptoms
        disease_name, description, precautions = predd(
            rnd_forest, *symptoms  # Unpack the symptoms list into arguments
        )

        return jsonify({
            "disease": disease_name,
            "description": description,
            "precautions": precautions
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)