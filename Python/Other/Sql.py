import sqlite3
connection = sqlite3.connect("test.db")
cursor = connection.cursor()
command = 'SELECT * FROM Person'

cursor.execute(command)
connection.commit()
connection.close()
