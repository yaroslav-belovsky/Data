import pandas as pd
df = pd.read_csv("education.csv").dropna()

info = df[df["Entity"] == "India"][["Year", "Share of population with no education"]]
print(info)