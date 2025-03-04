import pandas as pd

# Load the cleaned data
df = pd.read_csv(r"C:\Users\Hp\Documents\Global-Economic-Analysis\data\cleaned_data.csv")

# Exploratory Data analysis

# Display basic info about the dataset
print(df.info())

# Check the first few rows
print(df.head())

# Check the number of rows and columns
print("Dataset shape:", df.shape)
