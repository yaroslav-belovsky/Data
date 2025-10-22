import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("billionaires.csv")

plt.plot(df["Name"], df["Net Worth"])

plt.title("Зміни бюджету фільмів по роках")
plt.xlabel("фільми")
plt.ylabel("заробіток")

plt.show()