import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('restoran.db')

# Створення курсора
cursor = conn.cursor()

# Створення таблиці (якщо її ще немає)
cursor.execute("""
CREATE TABLE IF NOT EXISTS restoran (

dish_name TEXT,
category TEXT,
price INTEGER,
available INTEGER
)
""")

# Вставка одного запису
cursor.execute("INSERT INTO restoran (dish_name, category, price, available) VALUES ('слоняча паста', 'основні страви', '52000000000000000', 1)")
cursor.execute("INSERT INTO restoran (dish_name, category, price, available) VALUES ('торт з серця галактики', 'дешеві', '52000000000000000000000000000000000000', 1)")
cursor.execute("INSERT INTO restoran (dish_name, category, price, available) VALUES ('сосиска з ядра сонця', 'гарячі страви', '5200000000000000000000000000000', 1)")
cursor.execute("INSERT INTO restoran (dish_name, category, price, available) VALUES ('кактус', 'най смчніші страви!(навпаки)', '52', 1)")
cursor.execute("INSERT INTO restoran (dish_name, category, price, available) VALUES ('картопля фрі паста', 'основні страви', '520000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 1)")

# Підтвердження змін
conn.commit()

# Перевірка результату (вибірка всіх записів)
cursor.execute("SELECT * FROM restoran")
data = cursor.fetchall()
for date in data:
    print(date)  # Вивести всі записи з таблиці

cursor.execute("SELECT * FROM restoran WHERE name LIKE 'паста%'")
pastu = cursor.fetchall()
print(f"\nа ось наша паста: \n{pastu}")

cursor.execute("SELECT * FROM restoran WHERE category LIKE ?", ("основні страви%"))
osnowni = cursor.fetchall()
print(f"\nа ось наші основні страви: \n{osnowni}")

cursor.execute("SELECT * FROM restoran WHERE price < 52000000000000001")
osnowni = cursor.fetchall()
print(f"\nа ось наші дешеві страви: \n{osnowni}")
conn.commit()
# Закриття з'єднання
conn.close()