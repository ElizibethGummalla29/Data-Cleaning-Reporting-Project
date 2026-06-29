import pandas as pd


# Load raw data
file_path = "data/raw_data.csv"

df = pd.read_csv(file_path)

print("Original Data:")
print(df)


# Remove duplicate rows
df = df.drop_duplicates()


# Handle missing values

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)


# Fix inconsistent department names

df["Department"] = df["Department"].str.upper()


# Remove extra spaces

df = df.apply(
    lambda x: x.str.strip()
    if x.dtype == "object"
    else x
)


# Save cleaned dataset

output_file = "data/cleaned_data.csv"

df.to_csv(
    output_file,
    index=False
)


print("\nCleaning Completed Successfully!")
print("Cleaned file created:", output_file)