import os
import pandas as pd

# Get absolute path to data file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "..", "data", "full_medical_mapping.xlsx")

# Load dataset
data = pd.read_excel(file_path)

print("Original data shape:", data.shape)

# Separate disease and symptoms
disease_column = data["disease"]
symptom_columns = data.drop(columns=["disease"])

# Combine all symptom columns into a list per row
symptom_list = symptom_columns.values.tolist()

# Clean symptom text
cleaned_symptoms = [
    [str(symptom).strip().lower() for symptom in row if pd.notna(symptom)]
    for row in symptom_list
]

# Show example
print("\nSample disease:", disease_column.iloc[0])
print("Associated symptoms:", cleaned_symptoms[0])

print("\nPreprocessing complete.")
