# (1) line chart of GDP, Unemployment, or Remittances over time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Load the processed data
    df = pd.read_csv("data/processed_data.csv")

    # Log available columns
    logging.info(f"Available columns: {df.columns}")

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

    logging.info("Dataset is ready for visualization!")

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

    def run():
        """Executes all the visualization functions sequentially."""
        # Plot GDP Trends
        plot_trend_matplotlib_dynamic("GDP (current US$)_x", "GDP (current US$)")

        # Plot Unemployment Trends
        plot_trend_matplotlib_dynamic("Unemployment, total (% of total labor force)", "Unemployment Rate (%)")

        # Plot Remittances Trends
        plot_trend_matplotlib_dynamic("Personal remittances, received (% of GDP)", "Remittances (% of GDP)")

        # (2) Bar graph of countries with the highest and lowest unemployment rates
        year_selected = 2022
        df_year = df[df["Year"] == year_selected]
        
        top_unemployment = df_year.nlargest(5, "Unemployment, total (% of total labor force)")
        low_unemployment = df_year.nsmallest(5, "Unemployment, total (% of total labor force)")
        
        df_unemployment = pd.concat([top_unemployment, low_unemployment])
        
        plt.figure(figsize=(12, 6))
        plt.barh(df_unemployment["Country Name"], df_unemployment["Unemployment, total (% of total labor force)"], color=["red"]*5 + ["green"]*5)
        
        plt.xlabel("Unemployment Rate (%)", fontsize=12)
        plt.ylabel("Country", fontsize=12)
        plt.title(f"Highest & Lowest Unemployment Rates by Country ({year_selected})", fontsize=14, fontweight="bold")
        
        for index, value in enumerate(df_unemployment["Unemployment, total (% of total labor force)"]):
            plt.text(value + 0.2, index, f"{value:.2f}%", fontsize=10, verticalalignment="center")
        
        plt.gca().invert_yaxis()
        plt.grid(axis="x", linestyle="--", alpha=0.6)
        plt.show()

        # (3) Scatter Plot: Show the relationship between GDP and Unemployment
        df_scatter = df[["GDP (current US$)_x", "Unemployment, total (% of total labor force)", "Country Name"]].dropna()
        df_scatter.rename(columns={"GDP (current US$)_x": "GDP", "Unemployment, total (% of total labor force)": "Unemployment"}, inplace=True)
        
        plt.figure(figsize=(10, 6))
        plt.scatter(df_scatter["GDP"], df_scatter["Unemployment"], alpha=0.6, edgecolors="k")
        
        plt.xlabel("GDP (Current US$)")
        plt.ylabel("Unemployment Rate (%)")
        plt.title("Relationship Between GDP and Unemployment")
        plt.xscale("log")
        plt.show()

        # (4) Histogram Showing the distribution of GDP Growth rates
        df.dropna(subset=["GDP growth (annual %)_x"], inplace=True)
        plt.figure(figsize=(10, 6))
        plt.hist(df["GDP growth (annual %)_x"], bins=20, color="royalblue", edgecolor="black", alpha=0.7)
        plt.title("Distribution of GDP Growth Rates", fontsize=14, fontweight="bold")
        plt.xlabel("GDP Growth Rate (%)", fontsize=12)
        plt.ylabel("Number of Countries", fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

        # (5) Box plot of GDP growth by region
        df["Region"] = df["Country Name"].map({
            "United States": "North America", "Canada": "North America", "Mexico": "North America",
            "Germany": "Europe", "France": "Europe", "United Kingdom": "Europe",
            "China": "Asia", "India": "Asia", "Japan": "Asia",
            "Brazil": "South America", "Argentina": "South America",
            "South Africa": "Africa", "Nigeria": "Africa",
            "Australia": "Oceania"
        })
        df_boxplot = df[["Region", "GDP growth (annual %)_x"]].dropna()
        plt.figure(figsize=(12, 6))
        plt.boxplot([df_boxplot[df_boxplot["Region"] == region]["GDP growth (annual %)_x"] for region in df_boxplot["Region"].dropna().unique()], labels=df_boxplot["Region"].dropna().unique())
        plt.xticks(rotation=45, ha="right")
        plt.title("GDP Growth Distribution by Region")
        plt.xlabel("Region")
        plt.ylabel("GDP Growth (%)")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

    # Call run function to execute all visualizations
    run()

except Exception as e:
    logging.error(f"An error occurred: {e}")