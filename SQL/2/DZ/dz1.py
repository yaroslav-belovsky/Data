import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('GAMES.db')

# Створення курсора
cursor = conn.cursor()

# Створення таблиці (якщо її ще немає)
cursor.execute("""
CREATE TABLE IF NOT EXISTS games (

id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
rating INTEGER,
level TEXT

)
""")

# Вставка одного запису

name = input("назва: ")

rating = int(input("рейтинг: "))

level = input("рівень складності: ")

print("id     name    rating    level")

cursor.execute(f"INSERT INTO games (name, rating, level) VALUES ('{name}', {rating}, '{level}')")

# Підтвердження змін
conn.commit()

# Перевірка результату (вибірка всіх записів)
cursor.execute("SELECT * FROM games")
data = cursor.fetchall()
for date in data:
    print(date)  # Вивести всі записи з таблиці


# Закриття з'єднання
conn.close()