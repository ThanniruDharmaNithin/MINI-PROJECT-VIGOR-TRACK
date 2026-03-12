import pandas as pd
import numpy as np
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score, accuracy_score
from sklearn.utils import shuffle

# Load and preprocess the dataset
df = pd.read_csv('training_og.csv')
df = shuffle(df, random_state=42)

# Replace underscores with spaces in columns
for col in df.columns:
    df[col] = df[col].str.replace('_', ' ')
    
# Checking for missing values
null_checker = df.apply(lambda x: sum(x.isnull())).to_frame(name='count')
print("Null values in each column:\n", null_checker)

# Removing extra spaces
cols = df.columns
data = df[cols].values.flatten()
s = pd.Series(data)
s = s.str.strip()
s = s.values.reshape(df.shape)
df = pd.DataFrame(s, columns=df.columns).fillna(0)

# Load severity data and replace symptoms with weights
df1 = pd.read_csv('severity.csv')
df1['Symptom'] = df1['Symptom'].str.replace('_', ' ')

# Map symptoms to weights
vals = df.values
symptoms = df1['Symptom'].unique()
for i in range(len(symptoms)):
    vals[vals == symptoms[i]] = df1[df1['Symptom'] == symptoms[i]]['weight'].values[0]
    
# Replace uncommon symptoms with zero
df = pd.DataFrame(vals, columns=df.columns).replace(['dischromic  patches', 'spotting  urination', 'foul smell of urine'], 0)

# Check for duplicates in the dataset
duplicates = df[df.duplicated()]
print(f"Number of duplicate rows: {duplicates.shape[0]}")
if not duplicates.empty:
    print("Duplicate rows:")
    print(duplicates)

# Separate features and labels
data = df.iloc[:, 1:].astype(float).values
labels = df['Disease'].values

# Train-test split with hold-out validation (10% reserved for final testing)
x_train, x_holdout, y_train, y_holdout = train_test_split(data, labels, test_size=0.1, random_state=42)

# Initialize models
models = {
    'Decision Tree': DecisionTreeClassifier(criterion='gini', random_state=42, max_depth=13),
    'Random Forest': RandomForestClassifier(random_state=42, max_features='sqrt', n_estimators=500, max_depth=13),
    'Naive Bayes': GaussianNB(),
    'KNN': KNeighborsClassifier()
}

# Perform regular train-test split evaluation
print("Training with regular train-test split:")
for name, model in models.items():
    model.fit(x_train, y_train)
    preds = model.predict(x_holdout)
    print(f'{name} - F1-score% = {f1_score(y_holdout, preds, average="macro") * 100:.2f} | Accuracy% = {accuracy_score(y_holdout, preds) * 100:.2f}')
    dump(model, f'{name.lower().replace(" ", "_")}_model.pkl')

print("\nModels have been trained and saved successfully with train-test split.")
