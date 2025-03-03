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



