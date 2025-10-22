import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("archivef1/drivers.csv")
df2 = pd.read_csv("archivef1/results.csv")
df3 = pd.read_csv("archivef1/races.csv")

print(df1["driverRef"])



id = df1[df1["driverRef"] == "leclerc"][["driverId"]].iloc[0]
print('id ', id["driverId"])

info1 = df2[df2["driverId"] == id["driverId"]][["points", "raceId"]]
print("info1", info1)

info2 = info1[info1["points"] != "\\N"][["points", "raceId"]]
print("info2",info2)
print('???', list(info1["raceId"]))
points = info2["points"]
print('fastestLapTime', points)

dates = df3[df3["raceId"].isin(list(info2["raceId"]))]["date"]
print('dates', dates)




plt.figure(figsize=(10,6))
plt.plot(list(dates), list(points))#, marker="*", color="r"
plt.xticks(list(dates), list(dates), rotation='vertical')
plt.title("зміна балів в Леклера на протязі років")
plt.xlabel("дати")#, frontsize=12
plt.ylabel("бали")#, frontsize=12

plt.grid(True)
plt.tight_layout()
plt.show()