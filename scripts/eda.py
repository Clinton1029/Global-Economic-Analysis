import pandas as pd

# Load the cleaned data
df = pd.read_csv(r"C:\Users\Hp\Documents\Global-Economic-Analysis\data\cleaned_data.csv")

# Exploratory Data analysis


#Check the structure, shape, and basic details of the datase 
 

# Display basic info about the dataset
print(df.info())

# Check the first few rows
print(df.head())

# Check the number of rows and columns
print("Dataset shape:", df.shape)


# Count missing values per column
print("Missing Values:\n", df.isnull().sum())


# Check for duplicate rows
print("Duplicate Rows:", df.duplicated().sum())


# Summary statistics of numerical columns
print(df.describe())

# Summary statistics of categorical columns
print(df.describe(include="object"))
