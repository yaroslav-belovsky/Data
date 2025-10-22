import pandas as pd
import matplotlib.pyplot as plt

# Завантажуємо дані
df = pd.read_csv("billionaires.csv")

# Підраховуємо кількість мільярдерів у кожній індустрії
industry_counts = df["Industry"].value_counts()
print(industry_counts)
# Беремо ТОП-5 індустрій, решту об'єднуємо в "Інші"
top_industries = industry_counts[:10]
print("1",top_industries)
top_industries["Інші"] = industry_counts[10:].sum()
print("2",top_industries)

# Будуємо кругову діаграму
plt.figure(figsize=(8, 8)) # Задаємо розмір
plt.pie(
top_industries,
labels=top_industries.index,
autopct="%1.1f%%", # Додаємо відсотки
colors=plt.cm.Paired.colors, # Встановлюємо кольори
startangle=140 # Повертаємо діаграму
)
plt.title("Розподіл мільярдерів за індустріями")
plt.show()