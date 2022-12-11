import sqlite3

connection = sqlite3.connect('Accountsys.db')

cur =connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS AccountDB ( UserName TEXT,"
            "EMAIL TEXT, Password TEXT)")

cur.execute("INSERT INTO AccountDB VALUES('Minnie','Minnie23@gmail.com','minie7894')")

connection.commit()
connection.close()

