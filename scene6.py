import pandas as pd

# Load Employee CSV file
employee_df = pd.read_csv("employee_data.csv")

# Display first 5 records
print("First 5 Records of Employee Dataset:")
print(employee_df.head())

# Display basic information
print("\nEmployee Dataset Info:")
print(employee_df.info())

# Summary statistics
print("\nSummary Statistics of Employee Dataset:")
print(employee_df.describe(include='all'))

# Average salary by department (if columns exist)
if "Department" in employee_df.columns and "Salary" in employee_df.columns:
    dept_salary = employee_df.groupby("Department")["Salary"].mean()
    print("\nAverage Salary by Department:")
    print(dept_salary)

# Maximum and minimum salary
if "Salary" in employee_df.columns:
    print("\nMaximum Salary:", employee_df["Salary"].max())
    print("Minimum Salary:", employee_df["Salary"].min())
    print("Average Salary:", employee_df["Salary"].mean())