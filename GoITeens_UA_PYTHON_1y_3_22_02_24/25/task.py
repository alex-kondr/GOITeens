# class MyClass:
#     pass


# class Animal:
#     color = "Black"
#     weight = 5
#     eat = False

#     def eating(self):
#         self.eat = True
#         print("Eating...")

#     def run(self):
#         if self.eat:
#             print("Run->")
#         else:
#             print("No yet :(")

class Animal:
    eat = False

    def __new__(cls, *args, **kwarf):
        print("New method")
        return super().__new__(cls)

    def __init__(self, color: str, weight: float):
        self.color = color
        self.weight = weight

    def eating(self):
        self.eat = True
        print("Eating...")

    def run(self):
        if self.eat:
            print("Run->")
        else:
            print("No yet :(")

    def change_weight(self, weight: float):
        self.weight = weight


class Pulse:
    live = True

    def is_live(self):
        print("It`s a LIVE!!!!!!!" if self.live else "Ups.... You die")


animal = Animal("Black", 8)
animal.eating()


class Dog(Animal, Pulse):
    speed = 50

    def run_by_cat(self):
        print("Runing chase the cat")


# animal.run_by_cat()

dog = Dog("Black", 3)
dog.run()
dog.eating()
dog.run()
dog.run_by_cat()
dog.live = False
dog.is_live()





# Створити два різних класи.

# Створити клас, який наслідується з одного з попередніх класів та додає новий атрибут.

# Створити екземпляри всіх трьох класів, та роздрукувати всі атрибути даних екземплярів,
# а також продемонструвати роботу методу одного з екземплярів












# Реалізуйте програму, яка зчитує вміст файла "data.txt" і виводить кількість слів у цьому файлі.








# Напишіть функцію, яка отримує шлях до файла і слово як аргументи.
# Функція повинна перевіряти, скільки разів слово зустрічається у файлі.








# Реалізуйте програму, яка зчитує вміст кількох файлів і об'єднує їх у новий файл "combined.txt".







# Напишіть функцію, яка перевіряє, чи є файл "data.txt" порожнім.







# Напишіть функцію, яка отримує шлях до файла і перевіряє, чи містить файл лише числа.
# Поверніть True, якщо так, і False — у протилежному випадку.







# Реалізуйте програму, яка знаходить найдовший рядок у файлі "data.txt" і виводить його разом із його довжиною.









# Реалізуйте програму, яка видаляє всі порожні рядки з файла "data.txt".