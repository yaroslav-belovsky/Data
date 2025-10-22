import pandas as pd
import matplotlib.pyplot as plt

# Завантажуємо дані
df = pd.read_csv('education.csv')

# Фільтруємо дані для Бразилії
brazil_data = df[df['Entity'] == 'Brazil']

# Створюємо лінійний графік
plt.figure(figsize=(10,6))
plt.plot(brazil_data['Year'], brazil_data['Education'], marker='*', color='r')

# Додаємо заголовок та підписи до осей
plt.title('Зміни частки населення з базовою освітою в Бразилії', fontsize=14)
plt.xlabel('Рік', fontsize=12)
plt.ylabel('Частка населення з базовою освітою (%)', fontsize=12)

# Показуємо графік
plt.grid(True)
plt.show()