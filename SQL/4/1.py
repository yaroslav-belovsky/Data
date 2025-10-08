import  sqlite3
import  tkinter as tk
from cProfile import label

# Підключення до бази даних

conn = sqlite3.connect('my_database.db')

# Створення курсора
cursor = conn.cursor()

def dod_click():
    new_user_name = entry_name.get()
    new_user_age = entry_age.get()
    cursor.execute(f"INSERT INTO users (name, age) VALUES ('{new_user_name}', {new_user_age})")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    text_label = "id   name   age"
    data = cursor.fetchall()
    for date in data:
        text_label += f"\n{date}"  # Вивести всі записи з таблиці
    label.config(text = f"{text_label}")

def on_click():
    old_user_name = entry_name.get()
    old_user_age = entry_age.get()
    new_user_name = entry_zminu_name.get()
    new_user_age = entry_zminu_age.get()
    cursor.execute(f"UPDATE users SET name = '{new_user_name}', age = {new_user_age} WHERE name = '{old_user_name}' and age = {old_user_age}")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    text_label = "id   name   age"
    data = cursor.fetchall()
    for date in data:
        text_label += f"\n{date}"  # Вивести всі записи з таблиці
    label.config(text=f"{text_label}")

def delate_click():
    new_user_name = entry_name.get()
    new_user_age = entry_age.get()
    cursor.execute(f"DELETE FROM users WHERE name like '%{new_user_name}%' and age = {int(new_user_age)}")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    text_label = "id   name   age"
    data = cursor.fetchall()
    for date in data:
        text_label += f"\n{date}"  # Вивести всі записи з таблиці
    label.config(text=f"{text_label}")

# Створення таблиці (якщо її ще немає)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER

)
""")

root = tk.Tk()
root.geometry("500x500")

frame_name_age = tk.Frame(root)
frame_name_age.pack()

entry_name = tk.Entry(frame_name_age, font=("Arial", 12))
entry_name.grid(row=0, column=0)

entry_age = tk.Entry(frame_name_age, font=("Arial", 12))
entry_age.grid(row=0, column=1)

frame_zminu_name_age = tk.Frame(root)
frame_zminu_name_age.pack()

entry_zminu_name = tk.Entry(frame_zminu_name_age, font=("Arial", 12))
entry_zminu_name.grid(row=0, column=0)

entry_zminu_age = tk.Entry(frame_zminu_name_age, font=("Arial", 12))
entry_zminu_age.grid(row=0, column=1)

button_dod = tk.Button(root, text="додати юзера", command=dod_click, bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
button_dod.pack() # Add horizontal padding

button_on = tk.Button(root, text="онвити юзера", command=on_click, bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
button_on.pack() # Add horizontal padding

button_delate = tk.Button(root, text="видалити юзера", command=delate_click, bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
button_delate.pack() # Add horizontal padding

cursor.execute("SELECT * FROM users")
text_label = "id   name   age"
data = cursor.fetchall()
for date in data:
    text_label += f"\n{date}"  # Вивести всі записи з таблиці

label = tk.Label(root, text=f"{text_label}", bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
label.pack()

root.mainloop()
conn.close()