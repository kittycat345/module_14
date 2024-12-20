import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL


)
''')
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                   (f"User{str(i)}", f"example{str(i)}@gmail.com", i * 10, 1000))
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE age = ?", (500, i * 10))
for i in range(1,11,3):
    cursor.execute("DELETE from Users WHERE age = ?", (i*10,))
cursor.execute("SELECT username, email, age, balance from Users WHERE age != 60 ")
for row in cursor.fetchall():
    print("Имя пользователя: {} | Почта: {} | Возраст: {} | Баланс: {}".format(row[0],row[1],row[2],row[3]))

cursor.execute("DELETE FROM Users WHERE id=6")
cursor.execute("SELECT COUNT(*) FROM Users")
cursor.execute("SELECT SUM(balance) FROM Users")
cursor.execute("SELECT AVG(balance) FROM Users")
avg = cursor.fetchall()
print(avg)

