"""Module contains code to practice keyboard shortcut and basic data handling and syntax."""

import pandas as pd
import numpy as np

# Data handling practice shee

EXAMPLE = "Hello World"

if EXAMPLE == "Hello World":
    EXAMPLE = EXAMPLE + " what now?"
    print(EXAMPLE)
else:
    print(EXAMPLE + ' is not equal to "Hello World"')

# handling sample data to practice keyboard shortcut and basic commands

sample_data = {
    "Name": ["Alice", "Robert", "Harry", "Snape", None],
    "Age": [33, 56, 15, None, 76],
    "City": ["Paris", "Madird", "Berlin", "Paris", "Berlin"],
    "Salary": [45000, 89000, None, 52000, 23000],
}
df = pd.DataFrame(sample_data)
print(df)

# Handle missing values

df = df.dropna(subset=["Name"])
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

print(df)

# Add new computed column using a lambda function
df["Seniority"] = df["Age"].apply(lambda x: "Senior" if x >= 40 else "Junior")

Berlin_df = df[df["City"] == "Berlin"]
Paris_df = df[df["City"] == "Paris"]

Paris_mean_salary = Paris_df["Salary"].mean()
Berlin_mean_salary = Berlin_df["Salary"].mean()
# determining which city has the higher mean salary
if Berlin_mean_salary < Paris_mean_salary:
    print(
        f"The highest mean Salary per city is in Paris with {Paris_mean_salary:,.2f} €."
    )
elif Berlin_mean_salary == Paris_mean_salary:
    print(f"The mean salary in the City is both {Berlin_mean_salary:,.2f} €.")
else:
    print(
        f"The highest mean Salary per city is in Berlin with {Berlin_mean_salary:,.0f} €."
    )

# doing the same but inside the if-condition
if (Berlin_mean := df.loc[df["City"] == "Berlin", "Salary"].mean()) <= (
    Paris_mean := df.loc[df["City"] == "Paris", "Salary"].mean()
):
    print(f"The highest mean Salary per city is in Paris with {Paris_mean:,.2f} €.")
else:
    print(f"The highest mean Salary per city is in Berlin with {Berlin_mean:,.2f} €.")

# group by city nd compute stats
city_stats = df.groupby("City")["Salary"].mean().reset_index(name="AvgSalary")

print(city_stats)

# add another column on taxes
df["Taxes"] = np.where(
    df["Seniority"] == "Senior", 0.6 * df["Salary"], 0.2 * df["Salary"]
)

print(df)
