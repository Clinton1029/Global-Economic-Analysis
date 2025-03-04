import pandas as pd

# Load the dataset
file_path = "../data/world_economic_indicators.csv"  # Change this to the correct file path
df = pd.read_csv(file_path)

# Exploratory Data analysis

# 1. Basic Information
print("Dataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
