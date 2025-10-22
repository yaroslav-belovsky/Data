# стовпчастий графік, який показує середній бюджет фільмів по країнах виробництва

import pandas as pd
import matplotlib.pylab as plt
from numpy.ma.core import count

countries_origin = []
df = pd.read_csv("movies_dataset.csv")
budget = df["budget"].value_counts()
for i in budget:
    countries_origin = df[df["countries_origin"] == i]
print(budget)
top1 = countries_origin[:10]
top2 = budget[:10]

plt.bar(top2["budget"], top1["countries_origin"])

plt.xlabel("бюджет")
plt.ylabel("країни")

plt.show()



