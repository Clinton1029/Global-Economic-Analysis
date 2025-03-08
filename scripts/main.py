import sys
import os
import logging

# Ensure the scripts directory is in the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

# Import modules
import data_cleaning
import data_analysis
import data_visualization
import eda

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run():
    """Runs the full workflow of the Global Economic Analysis project."""
    logging.info("Starting Global Economic Analysis workflow...")

    try:
        # Step 1: Data Cleaning
        logging.info("Cleaning data...")
        cleaned_data = data_cleaning.clean_data()
        logging.info("Data cleaning completed.\n")

        # Step 2: Exploratory Data Analysis (EDA)
        logging.info("Performing Exploratory Data Analysis (EDA)...")
        eda.perform_eda(cleaned_data)
        logging.info("EDA completed.\n")

        # Step 3: Statistical Analysis
        logging.info("Performing Statistical Analysis...")
        analysis_results = data_analysis.analyze_data(cleaned_data)
        logging.info("Statistical Analysis completed.\n")

        # Step 4: Data Visualization
        logging.info("Generating Visualizations...")
        data_visualization.visualize_data(cleaned_data)
        logging.info("Data visualization completed.\n")

        logging.info("Global Economic Analysis workflow completed successfully!")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    run()
