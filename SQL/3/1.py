cursor.execute("SELECT * FROM users WHERE age > ?", (age))

cursor.execute("SELECT * FROM users WHERE name LIKE ?", ("K%")) 