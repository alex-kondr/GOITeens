def add_employee(employees: dict) -> dict:
    login = input("Введіть логін для користувача: ")
    position = input("Введіть посаду працівника: ")
    salary = input("Введіть ЗП для користувача: ")
    start_date = input("Введіть дату старту роботи у форматі '01.01.2024': ")
    name = input("Введіть ім'я працівника: ")
    password = input("Введіть пароль для користувача: ")

    employees[login] = {
        "posititon": position,
        "salary": salary,
        "start_date": start_date,
        "name": name,
        "password": password
    }
    print("Користуча успішно додано.")
    return employees


def del_employee(employees: dict) -> dict:
    login = input("Введіть логін користувача для видалення співробітника: ")

    if login in employees:
        del employees[login]
        print(f"Користувача '{login}' успішно видалено")
    else:
        print("Такого користувача не знайдено")

    return employees


def show_employees(employees: dict) -> None:
    for employee in employees:
        print(f"Інформація про користувача з логіном {employee}\n")
        for key, value in employees[employee].items():
            print(f"{key}: {value}")
        print("\n")


def change_salary(employees: dict) -> dict:
    login = input("Введіть логін користувача: ")

    if login in employees:
        salary = input("Введіть нове значення ЗП: ")
        employees[login]["salary"] = salary
        print("Суму ЗП успішно змінено")
    else:
        print("Такого користувача не знайдено")

    return employees


def change_position(employees: dict) -> dict:
    login = input("Введіть логін працівника: ")

    if login in employees:
        position = input("Введіть нову посаду: ")
        employees[login]["position"] = position
        input("Посаду користувача успішно змінено\nНатисніть 'enter' для продовження ")
    else:
        input("Такого користувача не знайдено\nНатисніть 'enter' для продовження ")

    return employees
