import pandas as pd

df = pd.read_csv("dz_fail_dla_pandas.csv")

print(df["Box Office ($M)"].median())
print("\n\n\n")
print(df["Box Office ($M)"].mode())
print("\n\n\n")
print(df["Box Office ($M)"].mean())
print("\n\n\n")
print(df["Box Office ($M)"].min())
print("\n\n\n")
print(df["Box Office ($M)"].max())