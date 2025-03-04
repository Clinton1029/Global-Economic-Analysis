import pandas as pd

# Load the dataset
file_path = "../data/world_economic_indicators.csv"  # Change this to the correct file path
df = pd.read_csv(file_path)

# Display the first 5 rows
print("🔹 First 5 rows of the dataset:")
print(df.head())

# Display basic information
print("\n🔹 Dataset Info:")
print(df.info())

# Check for missing values
print("\n🔹 Missing Values:")
print(df.isnull().sum())


# fill with median remittance for each country
df["Personal remittances, received (% of GDP)"] = df.groupby("Country Name")["Personal remittances, received (% of GDP)"].transform(lambda x: x.fillna(x.median()))

# Fill any remaining missing values with the global median remittance
global_median_remittance = df["Personal remittances, received (% of GDP)"].median()
df["Personal remittances, received (% of GDP)"].fillna(global_median_remittance, inplace=True)


# Check if all missing values are now filled
print(df["Personal remittances, received (% of GDP)"].isnull().sum())  # Should be 0


# Fill missing unemployment values
df["Unemployment, total (% of total labor force)"] = df.groupby("Country Name")["Unemployment, total (% of total labor force)"].transform(lambda x: x.fillna(x.mean()))

# Fill remaining missing values with global average
global_unemployment_avg = df["Unemployment, total (% of total labor force)"].mean()
df["Unemployment, total (% of total labor force)"].fillna(global_unemployment_avg, inplace=True)

# Check if all missing values are handled
print(df["Unemployment, total (% of total labor force)"].isnull().sum())  # Should be 0

# Check if GDP_x and GDP_y are the same
identical_gdp = (df["GDP (current US$)_x"] == df["GDP (current US$)_y"]).all()
identical_growth = (df["GDP growth (annual %)_x"] == df["GDP growth (annual %)_y"]).all()

print("Are GDP_x and GDP_y identical? ", identical_gdp)
print("Are GDP growth_x and GDP growth_y identical? ", identical_growth)


# Interpolate missing GDP values within each country group
df["GDP (current US$)_x"] = df.groupby("Country Name")["GDP (current US$)_x"].transform(lambda x: x.interpolate())

# Fill remaining GDP missing values with the country’s median GDP
df["GDP (current US$)_x"].fillna(df.groupby("Country Name")["GDP (current US$)_x"].transform("median"), inplace=True)

# Fill any remaining missing GDP values with the global median GDP
global_gdp_median = df["GDP (current US$)_x"].median()
df["GDP (current US$)_x"].fillna(global_gdp_median, inplace=True)

# Display missing values after handling GDP data
print("Missing values after handling GDP data:")
print(df[["GDP (current US$)_x"]].isnull().sum())


# Interpolate within each country
df["GDP growth (annual %)_x"] = df.groupby("Country Name")["GDP growth (annual %)_x"].transform(lambda x: x.interpolate())

# Fill remaining missing values with the global mean
global_gdp_growth_mean_x = df["GDP growth (annual %)_x"].mean()
df["GDP growth (annual %)_x"].fillna(global_gdp_growth_mean_x, inplace=True)


# Interpolate within each country
df["GDP (current US$)_y"] = df.groupby("Country Name")["GDP (current US$)_y"].transform(lambda x: x.interpolate())

# Fill remaining missing values with the country’s median GDP
df["GDP (current US$)_y"].fillna(df.groupby("Country Name")["GDP (current US$)_y"].transform("median"), inplace=True)

# If any missing values remain, fill them with the global median GDP
global_gdp_median_y = df["GDP (current US$)_y"].median()
df["GDP (current US$)_y"].fillna(global_gdp_median_y, inplace=True)


# Interpolate within each country
df["GDP growth (annual %)_y"] = df.groupby("Country Name")["GDP growth (annual %)_y"].transform(lambda x: x.interpolate())

# Fill remaining missing values with the global mean
global_gdp_growth_mean_y = df["GDP growth (annual %)_y"].mean()
df["GDP growth (annual %)_y"].fillna(global_gdp_growth_mean_y, inplace=True)


print("Missing values after handling GDP and Growth columns:")
print(df[["GDP growth (annual %)_x", "GDP (current US$)_y", "GDP growth (annual %)_y"]].isnull().sum())

# check duplicated rows
print("Duplicate Rows:", df.duplicated().sum())

# check the data type
print(df.dtypes)


print(df.info())  # Check overall structure
print(df.describe())  # Get statistical summary

# saving the clean data

# Save the cleaned data to CSV
df.to_csv("cleaned_data.csv", index=False)

# Save the cleaned data to Excel
df.to_excel("cleaned_data.xlsx", index=False, engine="openpyxl")

print("Cleaned data saved successfully in CSV and Excel formats!")


