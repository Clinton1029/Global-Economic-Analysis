import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Select specific countries for visualization
selected_countries = ["United States", "China", "India", "Germany", "Brazil"]

# Filter data for selected countries
df_selected = df[df["Country Name"].isin(selected_countries)]

# Sort data by Year
df_selected = df_selected.sort_values(by=["Year"])

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Store line plots for animation
lines = {}
colors = ["b", "g", "r", "c", "m"]  # Different colors for each country

# Plot initial lines for each country
for i, country in enumerate(selected_countries):
    country_data = df_selected[df_selected["Country Name"] == country]
    line, = ax.plot(country_data["Year"], country_data["GDP growth (annual %)_x"], 
                    label=country, color=colors[i], linewidth=2)
    lines[country] = line

# Customize the plot
ax.set_title("Dynamic & Interactive Line Graph: GDP Growth Over Years", fontsize=14)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("GDP Growth (Annual %)", fontsize=12)
ax.legend()
ax.grid(True)

# Function to update the graph dynamically
def update(frame):
    for country in selected_countries:
        country_data = df_selected[df_selected["Country Name"] == country]
        y_values = country_data["GDP growth (annual %)_x"].values

        # Update y-data dynamically by shifting values
        lines[country].set_ydata(np.roll(y_values, -frame))
    
    return lines.values()

# Animate the graph
ani = animation.FuncAnimation(fig, update, frames=50, interval=200, blit=True)

# Show interactive plot
plt.show()