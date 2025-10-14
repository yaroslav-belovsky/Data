import pandas as pd
from numpy.ma.extras import median

# Завантаження даних з файлу
df = pd.read_csv("movies_dataset.csv")

# Відобразимо перші 5 рядків
print(df)
print(df.columns) #Виведе список колонок

print("\n\n\n\n")
print(df.shape) #Виведе (кількість рядків, кількість колонок)

print("\n\n\n\n")
print(df.info()) #Загальна інформація (які є типи даних, чи є пропущені значення)

print("\n\n\n\n")
print(df.describe()) #Основні статистичні показники для числових колонок

print("\n\n\n\n")
mean = df["Rating"]
print(mean)


print("\n\n\n\n")
print("mean()")
mean = df["Rating"].mean()
print(mean)

print("\n\n\n\n")
print("median()")
mean = df["Rating"].median()
print(mean)

print("\n\n\n\n")
print("mode()")
mean = df["Rating"].mode()
print(mean)

print("\n\n\n\n")
print("dropna()")
mean = df["Rating"].dropna()
print(mean)

print("\n\n\n\n")
print("columns")
print(df.columns)