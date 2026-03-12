import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

train_df = pd.read_csv("training_og.csv")
severity_df = pd.read_csv("severity.csv")

symptom_columns = [col for col in train_df.columns if col.startswith("Symptom")]
train_df.fillna("", inplace=True)

unique_symptoms = set()
for col in symptom_columns:
    unique_symptoms.update(train_df[col].unique())
unique_symptoms.discard("")  
unique_symptoms = sorted(list(unique_symptoms))  

symptom_index = {symptom.lower().strip(): i for i, symptom in enumerate(unique_symptoms)}

def encode_symptoms(row):
    vector = np.zeros(len(unique_symptoms), dtype=int)
    for col in symptom_columns:
        symptom = row[col].lower().strip()
        if symptom in symptom_index:
            vector[symptom_index[symptom]] = 1
    return vector

X = np.array(train_df.apply(encode_symptoms, axis=1).tolist())

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(train_df["Disease"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "random_forest_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
joblib.dump(symptom_index, "symptom_index.pkl")
print("✅ Model, label encoder, and symptom index saved successfully!")