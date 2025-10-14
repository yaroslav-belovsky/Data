import pandas as pd

df = pd.read_csv("ds_salaries.csv")

print(df.columns)
print("\n\n\n")
print(df["salary_in_usd"].mean())
print("\n\n\n")
print(df["salary_in_usd"].describe())
print("\n\n\n")
print(df["salary_in_usd"].mode()[0])