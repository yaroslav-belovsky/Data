import sqlite3

def znaitu(kategoria):
    znaitu = input("що знайти? ")
    cursor.execute(f"SELECT * FROM pleiList WHERE {kategoria} LIKE '{znaitu}%'")
    znaidene = cursor.fetchall()
    print(f"\nось те що знайдено:")
    print("id     name    rating    rik     autor")
    for znaidena in znaidene:
        print(znaidena)

# Підключення до бази даних
conn = sqlite3.connect('pleiList.db')

# Створення курсора
cursor = conn.cursor()

# Створення таблиці (якщо її ще немає)
cursor.execute("""
CREATE TABLE IF NOT EXISTS pleiList (

id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
rating INTEGER,
rik TEXT,
autor TEXT

)
""")
while True:
    # Вставка одного запису
    menu = int(input("що зробити?\n1: додати пісню\n2: знайти пісню \n3: зупинити програму\n4: подивитись всі пісні\n"))
    if menu == 1:
        name = input("назва: ")

        rating = int(input("рейтинг: "))

        rik = input("рік випуску: ")

        autor = input("автор")

        print("теперішній плей ліст:")

        print("id     name    rating    rik     autor")

        cursor.execute(f"INSERT INTO pleiList (name, rating, rik, autor) VALUES ('{name}', {rating}, '{rik}', {autor})")

        # Підтвердження змін
        conn.commit()

        # Перевірка результату (вибірка всіх записів)
        cursor.execute("SELECT * FROM pleiList")
        data = cursor.fetchall()
        for date in data:
            print(date)  # Вивести всі записи з таблиці


        # Закриття з'єднання

        input()
    elif menu == 2:
        kategoria = input('''по якій категорії?
        1: id
        2: назва
        3: рейтинг
        4: рік випуску
        5: автор 
        '''
                          )
        if int(kategoria) == 1:
            znaitu("id")
        elif int(kategoria) == 2:
            znaitu("name")
        elif int(kategoria) == 3:
            znaitu("rating")
        elif int(kategoria) == 4:
            znaitu("rik")
        elif int(kategoria) == 5:
            znaitu("autor")
        input()
    elif menu == 3:
        break
    elif menu == 4:
        # Перевірка результату (вибірка всіх записів)
        cursor.execute("SELECT * FROM pleiList")
        data = cursor.fetchall()
        print("id     name    rating    rik     autor")
        for date in data:
            print(date)  # Вивести всі записи з таблиці

        # Закриття з'єднання
        input()

conn.close()