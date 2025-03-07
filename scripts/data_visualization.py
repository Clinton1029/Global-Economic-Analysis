# (1) line chart  of GDP, Unemployment, or Remittances over time

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




#(2) Bar graph of countries with the highest and lowest unemployment rates

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


#(3) Scatter Plot: Show the relationship between GDP and Unemployment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the processed data
df = pd.read_csv("data/processed_data.csv")


# Define correct column names
gdp_column = "GDP (current US$)_x"  
unemployment_column = "Unemployment, total (% of total labor force)"

# Select relevant columns for GDP and Unemployment
df_scatter = df[["GDP (current US$)_x", "Unemployment, total (% of total labor force)", "Country Name"]].dropna()

# Rename columns for clarity
df_scatter.rename(columns={"GDP (current US$)_x": "GDP", 
                           "Unemployment, total (% of total labor force)": "Unemployment"}, inplace=True)

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_scatter["GDP"], df_scatter["Unemployment"], alpha=0.6, edgecolors="k")

# Add labels and title
plt.xlabel("GDP (Current US$)")
plt.ylabel("Unemployment Rate (%)")
plt.title("Relationship Between GDP and Unemployment")

# Set log scale for better visualization (optional, since GDP values vary widely)
plt.xscale("log")

# Show plot
plt.show()

#(4) Histogram Showing the distribution of GDP Growth rates

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the processed data
df = pd.read_csv("data/processed_data.csv")


# Use the correct GDP Growth Rate column
gdp_growth_column = "GDP growth (annual %)_x"

# Drop NaN values in GDP Growth Rate
df = df.dropna(subset=[gdp_growth_column])

# Plot Histogram
plt.figure(figsize=(10, 6))
plt.hist(df[gdp_growth_column], bins=20, color="royalblue", edgecolor="black", alpha=0.7)

# Dynamic Title
plt.title(f"Distribution of {gdp_growth_column}", fontsize=14, fontweight="bold")
plt.xlabel("GDP Growth Rate (%)", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()


#(5) Box plot of GDP growth by region

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the processed data
df = pd.read_csv("data/processed_data.csv")


# Sample mapping of countries to regions (This should ideally come from external data or user input)
# For demonstration, a few mappings are added; in practice, this should be more comprehensive.
country_to_region = {
    "United States": "North America",
    "Canada": "North America",
    "Mexico": "North America",
    "Germany": "Europe",
    "France": "Europe",
    "United Kingdom": "Europe",
    "China": "Asia",
    "India": "Asia",
    "Japan": "Asia",
    "Brazil": "South America",
    "Argentina": "South America",
    "South Africa": "Africa",
    "Nigeria": "Africa",
    "Australia": "Oceania"
}

# Create a new column "Region" based on the mapping
df["Region"] = df["Country Name"].map(country_to_region)

# Filter only necessary columns and drop NaN values
df_boxplot = df[["Region", "GDP growth (annual %)_x"]].dropna()

# Rename column for consistency
df_boxplot = df_boxplot.rename(columns={"GDP growth (annual %)_x": "GDP Growth (%)"})

# Get unique regions
regions = df_boxplot["Region"].dropna().unique()

# Create the box plot
plt.figure(figsize=(12, 6))
plt.boxplot(
    [df_boxplot[df_boxplot["Region"] == region]["GDP Growth (%)"] for region in regions],
    labels=regions
)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Titles and labels
plt.title("GDP Growth Distribution by Region")
plt.xlabel("Region")
plt.ylabel("GDP Growth (%)")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.show()
