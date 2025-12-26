print("Starting model training script...")
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import accuracy_score

# Locate dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "..", "data", "full_medical_mapping.xlsx")

# Load data
data = pd.read_excel(file_path)

# Separate target and features
y = data["disease"]
X_raw = data.drop(columns=["disease"]).values.tolist()

# Clean symptom text
cleaned_symptoms = [
    [str(symptom).strip().lower() for symptom in row if pd.notna(symptom)]
    for row in X_raw
]

# Convert symptoms to binary features
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(cleaned_symptoms)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model trained successfully")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("Script finished execution")
