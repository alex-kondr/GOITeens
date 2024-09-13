import sqlite3

def first_sql_query():
    try:
        sqlite_connection = sqlite3.connect("my_first_test.db")
        cursor = sqlite_connection.cursor()
        # query = "select sqlite_version();"
        # cursor.execute(query)
        # record = cursor.fetchall()
        # print(f"Версія бази даних: {record}")
        # with open("create_table_query.txt") as fh:
        with open("insert_data_query.txt") as fh:
        # with open("select_row.txt") as fh:
            query = fh.read()

        rows = cursor.execute(query)
        rows1 = cursor.fetchall()
        print(f"{rows1 = }")
        # for row in rows:
        #     print(f"{row = }")
        # sqlite_connection.commit()
        print(f"{cursor.rowcount = }")
        cursor.close()

    except sqlite3.Error as error:
        print("Виникла помилка", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Підключення до бази даних успішно закрите")


def insert_data_query(first_name: str, last_name: str, age: int, grade: int):
    query_with_param = """INSERT INTO Students (first_name, last_name, age, grade) VALUES (?, ?, ?, ?)"""
    data_tuple = (first_name, last_name, age, grade)

    try:
        sql_con = sqlite3.connect("my_first_test.db")
        cursor = sql_con.cursor()
        cursor.execute(query_with_param, data_tuple)
        sql_con.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка: ", error)

    finally:
        if sql_con:
            sql_con.close()
            print("Підключення до бази даних закрите")


insert_data_query("DD", "KK", 35, 99)