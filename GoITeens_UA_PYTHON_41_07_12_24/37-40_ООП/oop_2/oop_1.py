# Наслідування (Inheritance)

class Car:
    count = 4

    def move_left(self):
        print("Автомобіль рухається вліво")

    def move_rigth(self):
        print("Автомобіль рухається вправо")


# car = Car()
# print(car.count)


class BMW(Car):
    def fuel_down(self):
        print("Паливо зменшується")


# bmw = BMW()
# print(f"{bmw.count = }")
# bmw.move_left()
# bmw.fuel_down()












# Інкапсуляція (Encapsulation)

class Bank:
    def __init__(self, balance: float, username: str, permision: str = "user"):
        self.__balance = balance
        self.username = username
        self._permision = permision

    def get_balance(self, username: str, permision: str = "user"):
        if self.username == username or permision == "admin":
            return self.__balance
        raise ValueError("У Вас відсутні права для перегляду")

    def add_balace(self, balance: float):
        if balance <= 0:
            raise ValueError("Поповнення рахунку можливе тільки з додатнім числом")
        self.__balance += balance


# my_bank = Bank(balance=100, username="mega_user")
# # print(my_bank.get_balance("mega_user"))
# my_bank.__balance






class Bank:
    def __init__(self, balance: float, username: str, permision: str = "user"):
        self.__balance = balance
        self.username = username
        self._permision = permision

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balace(self, new_balance: float):
        if new_balance <= 0:
            raise ValueError("Поповнення рахунку можливе тільки з додатнім числом")
        self.__balance += new_balance


# my_bank = Bank(balance=100, username="mega_user")
# print(f"{my_bank.balance = }")
# my_bank.balace = -200
# print(f"{my_bank.balance = }")



# Завдання
# 1. Створити клас BankAccount, який матиме публічний
# атрибут account_holder, захищений атрибут _balance
# та приватний атрибут __pin_code.
# 2. Забезпечити можливість взаємодії з балансом через публічні методи,
# не дозволяючи змінювати баланс напряму.
# 3. Використати захищений метод для перевірки балансу.
# 4. Забезпечити приватний метод для оновлення PIN-коду.


class BankAccount:
    def __init__(self, account_holder: str, balance: float, pin_code: str):
        self.account_holder = account_holder
        self._balance = balance
        self.__pin_code = pin_code

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance: float):
        self._balance += new_balance


my_bank = BankAccount("user", 100, "1234")
# my_bank._balance = 200
my_bank.balance = 200
print(f"{my_bank.balance = }")








# Завдання 2
# Створити клас Student, який матиме публічний атрибут name,
# захищений атрибут _marks і приватний атрибут __grade.
# Реалізувати метод для додавання оцінок з перевіркою допустимих значень.
# Додати гетери та сетери для доступу до оцінок і зміни їх.
# Реалізувати метод для визначення успішності студента на основі середньої оцінки.







# Використання гетерів та сетерів


# клас Employee, що матиме приватний атрибут __salary.
# Реалізувати гетер та сетер для зміни зарплати, де
# сетер перевірятиме, чи нове значення зарплати більше за 0.
# Створити метод для збільшення зарплати на певний відсоток із використанням сетера.
