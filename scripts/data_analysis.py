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

# --- 3. Outlier Detection using IQR ---
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]
 
# Identify outliers in GDP (current US$)_x
outliers_gdp = detect_outliers(numerical_df, "GDP (current US$)_x")
print(f"Number of Outliers in GDP: {len(outliers_gdp)}")
