import pandas as pd
df = pd.read_csv("movies_dataset.csv").dropna()
info = (df[df['genres'].str.contains("Comedy")][["Title", "Year"]])
print(info)

info = df.groupby('Languages')['Rating'].count()
print(info)

print("\n\n\n")
info = df[df["Year"] == 2014][["Title", "Year", "Rating"]]
info = info.sort_values("Rating").head(10)
print(info)