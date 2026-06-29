import pandas as pd
import matplotlib.pyplot as plt


# Load cleaned data

df = pd.read_csv("data/cleaned_data.csv")


print("Cleaned Data:")
print(df)


# Create summary report

summary = df.describe()


# Save Excel report

summary.to_excel(
    "reports/report.xlsx"
)


# Create department chart

department_count = df["Department"].value_counts()


department_count.plot(
    kind="bar",
    title="Employees by Department"
)


plt.xlabel("Department")
plt.ylabel("Number of Employees")


plt.savefig(
    "reports/department_chart.png"
)


print("Report Generated Successfully!")