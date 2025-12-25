import os
import pandas as pd

print("Python script started")

# Get the directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to the data file
file_path = os.path.join(current_dir, "..", "data", "full_medical_mapping.xlsx")

print("Looking for file at:", file_path)

# Load the dataset
data = pd.read_excel(file_path)

# Display basic information
print("Dataset loaded successfully")
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])
print("\nColumn names:")
print(data.columns)
