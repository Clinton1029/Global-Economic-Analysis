 # Performs statistical analysis & calculations

import pandas as pd
import numpy as np

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_data.csv")

# Ensure only numeric columns are used for analysis
numerical_df = df.select_dtypes(include=[np.number])

# --- 1. Basic Statistical Summary ---
summary = numerical_df.describe()
print("Statistical Summary:\n", summary)

# --- 2. Correlation Analysis ---
correlation_matrix = numerical_df.corr()
print("Correlation Matrix:\n", correlation_matrix)
