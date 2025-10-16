import pandas as pd

df = pd.read_csv("education.csv").dropna()


info = df[df["Year"] == 1950]

info = info.sort_values("Education").head(10)

print(info)
