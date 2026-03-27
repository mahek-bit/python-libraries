import pandas as pd

# Load employee performance dataset
df = pd.read_csv("employee_performance.csv")

print("Original Employee Dataset:")
print(df)

# 1. Fill missing Salary with mean
if 'Salary' in df.columns:
    df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# 2. Fill missing Performance_Score with mean (optional)
if 'Performance_Score' in df.columns:
    df['Performance_Score'].fillna(df['Performance_Score'].mean(), inplace=True)

# 3. Remove duplicate employee records
df_cleaned = df.drop_duplicates()

print("\nCleaned Employee Dataset:")
print(df_cleaned)

# 4. Show summary statistics
print("\nSummary Statistics:")
print(df_cleaned.describe())

# Optional: Save cleaned data
df_cleaned.to_csv("cleaned_employee_performance.csv", index=False)