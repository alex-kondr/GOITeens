import sqlite3


connection = sqlite3.connect("test.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY)")
connection.commit()
cursor.close()
connection.close()
