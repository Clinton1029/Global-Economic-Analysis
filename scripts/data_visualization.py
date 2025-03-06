import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Load the processed data
df = pd.read_csv("data/processed_data.csv")

# Print available columns
print("Available columns:", df.columns)

# Define required columns based on your dataset
required_columns = [
    "Country Name",
    "Country Code",
    "Year",
    "Personal remittances, received (% of GDP)",
    "Unemployment, total (% of total labor force)",
    "GDP (current US$)_x",
    "GDP growth (annual %)_x",
    "GDP (current US$)_y",
    "GDP growth (annual %)_y"
]

# Check if any required columns are missing
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    raise ValueError(f"Missing columns in dataset: {missing_columns}")

print("Dataset is ready for visualization!")
