import pandas as pd
import numpy as np
import os

def detect_outliers(df, column):
    """Detects outliers in a given numerical column using the IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

def perform_data_analysis(df):
    """Performs statistical analysis & feature engineering on the dataset."""

    # Ensure only numeric columns are used for analysis
    numerical_df = df.select_dtypes(include=[np.number])

    # --- 1. Basic Statistical Summary ---
    summary = numerical_df.describe()
    print("\n🔹 Statistical Summary:\n", summary)

    # --- 2. Correlation Analysis ---
    correlation_matrix = numerical_df.corr()
    print("\n🔹 Correlation Matrix:\n", correlation_matrix)

    # --- 3. Outlier Detection using IQR ---
    if "GDP (current US$)_x" in numerical_df.columns:
        outliers_gdp = detect_outliers(numerical_df, "GDP (current US$)_x")
        print(f"\n🔹 Number of Outliers in GDP: {len(outliers_gdp)}")

    # --- 4. Feature Engineering (if needed) ---
    if "GDP (current US$)_x" in df.columns and "Population" in df.columns:
        df["GDP per Capita"] = df["GDP (current US$)_x"] / df["Population"]
        print("\n🔹 GDP per Capita Feature Created.")

    return df

def run():
    """Runs data analysis when script is executed directly."""
    file_path = os.path.abspath("data/cleaned_data.csv")
    output_csv = os.path.abspath("data/processed_data.csv")
    output_excel = os.path.abspath("data/processed_data.xlsx")

    try:
        df = pd.read_csv(file_path)
        print("\n✅ Successfully loaded cleaned data.")
        df_processed = perform_data_analysis(df)

        # Save processed data
        df_processed.to_csv(output_csv, index=False)
        df_processed.to_excel(output_excel, index=False)
        
        print(f"\n✅ Processed data saved as CSV: {output_csv}")
        print(f"✅ Processed data saved as Excel: {output_excel}")

    except FileNotFoundError:
        print(f"\n❌ Error: File not found at {file_path}. Please check the path.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    run()
