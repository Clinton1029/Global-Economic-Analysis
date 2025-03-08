import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(file_path):
    """Loads and cleans the dataset by handling missing values and duplicates."""
    try:
        df = pd.read_csv(file_path)
        logging.info("\n✅ Successfully loaded dataset.")

        # Fill missing values for remittances
        df["Personal remittances, received (% of GDP)"] = df.groupby("Country Name")["Personal remittances, received (% of GDP)"].transform(lambda x: x.fillna(x.median()))
        global_median_remittance = df["Personal remittances, received (% of GDP)"].median()
        df["Personal remittances, received (% of GDP)"].fillna(global_median_remittance, inplace=True)

        # Fill missing values for unemployment
        df["Unemployment, total (% of total labor force)"] = df.groupby("Country Name")["Unemployment, total (% of total labor force)"].transform(lambda x: x.fillna(x.mean()))
        global_unemployment_avg = df["Unemployment, total (% of total labor force)"].mean()
        df["Unemployment, total (% of total labor force)"].fillna(global_unemployment_avg, inplace=True)

        # Handle GDP columns
        for col in ["GDP (current US$)_x", "GDP growth (annual %)_x", "GDP (current US$)_y", "GDP growth (annual %)_y"]:
            if col in df.columns:
                df[col] = df.groupby("Country Name")[col].transform(lambda x: x.interpolate())
                df[col].fillna(df.groupby("Country Name")[col].transform("median"), inplace=True)
                df[col].fillna(df[col].median(), inplace=True)

        # Remove duplicates
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            df.drop_duplicates(inplace=True)
            logging.info(f"\n✅ Removed {duplicates} duplicate rows.")

        # Save cleaned data
        output_csv = os.path.abspath("data/cleaned_data.csv")
        output_excel = os.path.abspath("data/cleaned_data.xlsx")

        df.to_csv(output_csv, index=False)
        df.to_excel(output_excel, index=False, engine="openpyxl")

        logging.info(f"\n✅ Cleaned data saved: {output_csv}")
        logging.info(f"✅ Cleaned data saved: {output_excel}")

        return df

    except FileNotFoundError:
        logging.error(f"\n❌ Error: File not found at {file_path}. Please check the path.")
    except Exception as e:
        logging.error(f"\n❌ An unexpected error occurred: {e}")

def run():
    """Runs data cleaning when script is executed directly."""
    file_path = os.path.abspath("data/world_economic_indicators.csv")
    df_cleaned = clean_data(file_path)
    if df_cleaned is not None:
        logging.info("\n✅ Data Cleaning Completed.")

if __name__ == "__main__":
    run()