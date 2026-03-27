import pandas as pd

# Load COVID-19 CSV file
covid_df = pd.read_csv("covid19_data.csv")

# Display first 5 records
print("First 5 Records of COVID-19 Dataset:")
print(covid_df.head())

# Display basic information
print("\nCOVID-19 Dataset Info:")
print(covid_df.info())

# Summary statistics
print("\nSummary Statistics of COVID-19 Dataset:")
print(covid_df.describe())

# District-wise summary
district_summary = covid_df.groupby("District")[["Confirmed", "Recovered", "Deaths", "Active"]].sum()

print("\nDistrict-wise COVID-19 Summary:")
print(district_summary)

# Top 5 districts with highest confirmed cases
top_confirmed = district_summary.sort_values(by="Confirmed", ascending=False).head(5)
print("\nTop 5 Districts with Highest Confirmed Cases:")
print(top_confirmed)

