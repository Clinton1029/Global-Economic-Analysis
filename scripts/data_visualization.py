import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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



# Select the top 3 countries by average GDP
top_countries = df.groupby("Country Name")["GDP (current US$)_x"].mean().nlargest(3).index.tolist()

# Filter data for these countries
df_top = df[df["Country Name"].isin(top_countries)]

def plot_trend_matplotlib_dynamic(metric, ylabel):
    """Plots an enhanced trend visualization using only Matplotlib with a dynamic title."""
    plt.figure(figsize=(12, 6))
    colors = ["b", "g", "r"]  # Assign different colors for clarity
    
    for i, country in enumerate(top_countries):
        country_data = df_top[df_top["Country Name"] == country]
        plt.plot(country_data["Year"], country_data[metric], marker='o', linestyle='-', color=colors[i], label=country)

        # Annotate the last data point
        last_year = country_data["Year"].max()
        last_value = country_data[country_data["Year"] == last_year][metric].values[0]
        plt.text(last_year, last_value, f"{last_value:,.2f}", fontsize=10, verticalalignment='bottom', color=colors[i])

    plt.xlabel("Year", fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    # Generate dynamic title based on the metric
    title = f"Trends in {ylabel} Over Time (Top 3 Countries)"
    plt.title(title, fontsize=14, fontweight="bold")
    
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

# Plot GDP Trends
plot_trend_matplotlib_dynamic("GDP (current US$)_x", "GDP (current US$)")

# Plot Unemployment Trends
plot_trend_matplotlib_dynamic("Unemployment, total (% of total labor force)", "Unemployment Rate (%)")

# Plot Remittances Trends
plot_trend_matplotlib_dynamic("Personal remittances, received (% of GDP)", "Remittances (% of GDP)")




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the processed data
df = pd.read_csv("data/processed_data.csv")


# Select the most recent year (2022) for comparison
year_selected = 2022
df_year = df[df["Year"] == year_selected]

# Identify the highest and lowest unemployment rates
top_unemployment = df_year.nlargest(5, "Unemployment, total (% of total labor force)")
low_unemployment = df_year.nsmallest(5, "Unemployment, total (% of total labor force)")

# Combine data
df_unemployment = pd.concat([top_unemployment, low_unemployment])

# Plot bar chart
plt.figure(figsize=(12, 6))
plt.barh(df_unemployment["Country Name"], df_unemployment["Unemployment, total (% of total labor force)"], color=["red"]*5 + ["green"]*5)

plt.xlabel("Unemployment Rate (%)", fontsize=12)
plt.ylabel("Country", fontsize=12)
plt.title(f"Highest & Lowest Unemployment Rates by Country ({year_selected})", fontsize=14, fontweight="bold")

# Annotate bars with exact values
for index, value in enumerate(df_unemployment["Unemployment, total (% of total labor force)"]):
    plt.text(value + 0.2, index, f"{value:.2f}%", fontsize=10, verticalalignment="center")

plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.show()
