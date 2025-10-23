import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("archivef1/drivers.csv")
df2 = pd.read_csv("archivef1/results.csv")
df3 = pd.read_csv("archivef1/races.csv")
def perewirka(menu):
    try:
        if int(menu) == 1:
            driverId = list(df1[df1["driverRef"] == "leclerc"]["driverId"])[0]

            driver_info = df2[df2["driverId"] == driverId][["points", "raceId"]]

            empty_driver_info = driver_info[driver_info["points"] != "\\N"][["points", "raceId"]]

            points = empty_driver_info["points"]

            dates = df3[df3["raceId"].isin(list(empty_driver_info["raceId"]))]["date"]

            plt.figure(figsize=(10, 6))
            plt.plot(list(dates), list(points))  # , marker="*", color="r"
            plt.xticks(list(dates), rotation='vertical')
            plt.title("зміна балів в Леклера")
            plt.xlabel("дати")  # , frontsize=12
            plt.ylabel("бали")  # , frontsize=12

            plt.grid(True)
            plt.tight_layout()
            plt.show()
        elif int(menu) == 2:
            driverId = list(df1[df1["driverRef"] == "leclerc"]["driverId"])[0]

            driver_info = df2[df2["driverId"] == driverId][["points", "raceId"]]

            empty_driver_info = driver_info[driver_info["points"] != "\\N"][["points", "raceId"]]

            join_race_and_results = empty_driver_info.join(df3, on="raceId",  lsuffix='_left', rsuffix='_right')
            mean_years = join_race_and_results.groupby("year")["points"].mean()

            plt.plot(mean_years.index.tolist(), list(mean_years))
            plt.xlabel("роки")
            plt.ylabel("бали")
            plt.title("зміна балів Леклера")

            plt.grid(True)
            plt.tight_layout()
            plt.show()
        elif int(menu) == 3:
            exit()
        else:
            print("щось не те...\nвведи ще раз!")
            home_menu = input(
                "натисніть 1 щоб подивитись середнє по датам, або 2 якщо хочете по рокам, а якщо хочите вийти натисніть 3\n")
            if home_menu != "3":
                perewirka(home_menu)
            elif home_menu == "3":
                exit()

    except ValueError:
        print("щось не те...\nвведи ще раз!")
        home_menu = input(
            "натисніть 1 щоб подивитись середнє по датам, або 2 якщо хочете по рокам, а якщо хочите вийти натисніть 3\n")
        if home_menu != "3":
            perewirka(home_menu)
        elif home_menu == "3":
            exit()

while True:
    home_menu = input("натисніть 1 щоб подивитись середнє по датам, або 2 якщо хочете по рокам, а якщо хочите вийти натисніть 3\n")
    if home_menu != "3":
        perewirka(home_menu)
    elif home_menu == "3":
        break
