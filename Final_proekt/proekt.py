import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("archivef1/drivers.csv")
df2 = pd.read_csv("archivef1/results.csv")
df3 = pd.read_csv("archivef1/races.csv")

print(df1["driverRef"])



driverId = list(df1[df1["driverRef"] == "leclerc"]["driverId"])[0]

driver_info = df2[df2["driverId"] == driverId][["points", "raceId"]]

empty_driver_info = driver_info[driver_info["points"] != "\\N"][["points", "raceId"]]

points = empty_driver_info["points"]

dates = df3[df3["raceId"].isin(list(empty_driver_info["raceId"]))]["date"]

plt.figure(figsize=(10,6))
plt.plot(list(dates), list(points))#, marker="*", color="r"
plt.xticks(list(dates), rotation='vertical')
plt.title("зміна балів в Леклера")
plt.xlabel("дати")#, frontsize=12
plt.ylabel("бали")#, frontsize=12

plt.grid(True)
plt.tight_layout()
plt.show()