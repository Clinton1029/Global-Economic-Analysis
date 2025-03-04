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


# Unique country names
print("Unique Countries:", df["Country Name"].nunique())

# Unique country codes
print("Unique Country Codes:", df["Country Code"].nunique())

# List all unique country names
print(df["Country Name"].unique())


# Find outliers using the interquartile range (IQR)
Q1 = df["GDP (current US$)_x"].quantile(0.25)
Q3 = df["GDP (current US$)_x"].quantile(0.75)
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

# Count potential outliers
outliers = df[(df["GDP (current US$)_x"] < lower_bound) | (df["GDP (current US$)_x"] > upper_bound)]
print(f"Potential Outliers in GDP: {outliers.shape[0]}")

# Select only numeric columns
numeric_df = df.select_dtypes(include=["number"])

# Compute correlation matrix
correlation_matrix = numeric_df.corr()

# Display correlation matrix
print("Correlation Matrix:\n", correlation_matrix)


