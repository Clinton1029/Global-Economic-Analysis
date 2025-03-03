import pandas as pd

# Load the dataset
file_path = "../data/world_economic_indicators.csv"  # Change this to the correct file path
df = pd.read_csv(file_path)

# Display the first 5 rows
print("🔹 First 5 rows of the dataset:")
print(df.head())

# Display basic information
print("\n🔹 Dataset Info:")
print(df.info())

# Check for missing values
print("\n🔹 Missing Values:")
print(df.isnull().sum())