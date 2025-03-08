import pandas as pd
import numpy as np
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
    logging.info("\n🔹 Statistical Summary:\n%s", summary)

    # --- 2. Correlation Analysis ---
    correlation_matrix = numerical_df.corr()
    logging.info("\n🔹 Correlation Matrix:\n%s", correlation_matrix)

    # --- 3. Outlier Detection using IQR ---
    if "GDP (current US$)_x" in numerical_df.columns:
        outliers_gdp = detect_outliers(numerical_df, "GDP (current US$)_x")
        logging.info(f"\n🔹 Number of Outliers in GDP: {len(outliers_gdp)}")

    # --- 4. Feature Engineering (if needed) ---
    if "GDP (current US$)_x" in df.columns and "Population" in df.columns:
        df["GDP per Capita"] = df["GDP (current US$)_x"] / df["Population"]
        logging.info("\n🔹 GDP per Capita Feature Created.")

    return df

def run():
    """Runs data analysis when script is executed directly."""
    file_path = os.path.abspath("data/cleaned_data.csv")
    output_csv = os.path.abspath("data/processed_data.csv")
    output_excel = os.path.abspath("data/processed_data.xlsx")

    try:
        df = pd.read_csv(file_path)
        logging.info("\n✅ Successfully loaded cleaned data.")
        df_processed = perform_data_analysis(df)

        # Save processed data
        df_processed.to_csv(output_csv, index=False)
        df_processed.to_excel(output_excel, index=False)
        
        logging.info(f"\n✅ Processed data saved as CSV: {output_csv}")
        logging.info(f"✅ Processed data saved as Excel: {output_excel}")

    except FileNotFoundError:
        logging.error(f"\n❌ Error: File not found at {file_path}. Please check the path.")
    except Exception as e:
        logging.error(f"\n❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    run()