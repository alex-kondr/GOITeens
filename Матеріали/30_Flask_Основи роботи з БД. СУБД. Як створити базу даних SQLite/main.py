import sqlite3

try:
    sqlite_connection = sqlite3.connect("my_first_test.db")
    cursor = sqlite_connection.cursor()
    # query = "select sqlite_version();"
    # cursor.execute(query)
    # record = cursor.fetchall()
    # print(f"Версія бази даних: {record}")
    # with open("create")
    # create_query = 
    cursor.close()

except sqlite3.Error as error:
    print("Виникла помилка", error)

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Підключення до бази даних успішно закрите")
