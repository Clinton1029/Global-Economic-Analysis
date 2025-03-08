import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def perform_eda(df):
    """Performs exploratory data analysis on the dataset."""
    
    # Display basic info about the dataset
    logging.info("\n🔹 Dataset Information:")
    logging.info(df.info())

    # Check the first few rows
    logging.info("\n🔹 First Few Rows:")
    logging.info(df.head())

    # Check the number of rows and columns
    logging.info("\n🔹 Dataset Shape: %s", df.shape)

    # Count missing values per column
    logging.info("\n🔹 Missing Values:\n%s", df.isnull().sum())

    # Check for duplicate rows
    logging.info("\n🔹 Duplicate Rows: %d", df.duplicated().sum())

    # Summary statistics of numerical columns
    logging.info("\n🔹 Summary Statistics (Numerical Columns):")
    logging.info(df.describe())

    # Summary statistics of categorical columns
    logging.info("\n🔹 Summary Statistics (Categorical Columns):")
    logging.info(df.describe(include="object"))

    # Unique country names
    logging.info("\n🔹 Unique Countries: %d", df["Country Name"].nunique())

    # Unique country codes
    logging.info("\n🔹 Unique Country Codes: %d", df["Country Code"].nunique())

    # List all unique country names
    logging.info("\n🔹 Unique Country Names:")
    logging.info(df["Country Name"].unique())

    # Find outliers using the interquartile range (IQR)
    Q1 = df["GDP (current US$)_x"].quantile(0.25)
    Q3 = df["GDP (current US$)_x"].quantile(0.75)
    IQR = Q3 - Q1

    # Define lower and upper bounds
    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    # Count potential outliers
    outliers = df[(df["GDP (current US$)_x"] < lower_bound) | (df["GDP (current US$)_x"] > upper_bound)]
    logging.info(f"\n🔹 Potential Outliers in GDP: {outliers.shape[0]}")

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=["number"])

    # Compute correlation matrix
    correlation_matrix = numeric_df.corr()

    # Display correlation matrix
    logging.info("\n🔹 Correlation Matrix:\n%s", correlation_matrix)

    # Top 10 countries with the most records
    logging.info("\n🔹 Top 10 Countries with Most Records:")
    logging.info(df["Country Name"].value_counts().head(10))

    # Top 10 years with the most data
    logging.info("\n🔹 Top 10 Years with Most Data:")
    logging.info(df["Year"].value_counts().head(10))


def run():
    """Runs EDA when script is executed directly."""
    file_path = r"C:\Users\Hp\Documents\Global-Economic-Analysis\data\cleaned_data.csv"
    
    try:
        df = pd.read_csv(file_path)
        logging.info("\n✅ Successfully loaded cleaned data.")
        perform_eda(df)
        logging.info("\n✅ EDA Completed Successfully!")
    except FileNotFoundError:
        logging.error(f"\n❌ Error: File not found at {file_path}. Please check the path.")
    except Exception as e:
        logging.error(f"\n❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    run()