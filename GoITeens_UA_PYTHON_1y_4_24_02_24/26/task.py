# Інкапсуляція (Encapsulation)

# class MyClass:
#     def __init__(self):
#         self.public_attribute = "Public attribute"
#         self._protected_attribute = "Protected attribute"
#         self.__private_attribute = "Private attribute"

#     def public_method(self):
#         # print(f"Print private attr: {self.__private_attribute}")
#         print("This is a public method")

#     def _protected_method(self):
#         print("This is a protected method")

#     def __private_method(self):
#         print("This is a private method")


# obj = MyClass()

# print(obj.public_attribute)
# obj.public_method()

# print(obj._protected_attribute)
# obj._protected_method()

# print(obj._MyClass__private_attribute)
# input()
# obj."__private_attribute" = "Hello"
# input()
# print(obj.__private_attribute)
# input()
# print(obj._MyClass__private_attribute)

# obj.__private_method()



# Наслідування (Inheritance)

# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

#     def drive(self):
#         print("The vehicle is in motion.")

#     def stop(self):
#         print("The vehicle has stopped.")


# class Car(Vehicle):
#     def __init__(self, brand, year, fuel_type):
#         super().__init__(brand, year)
#         self.fuel_type = fuel_type

#     def drive(self):
#         super().drive()
#         print("The car is driving on the road.")


# class Bicycle(Vehicle):
#     def __init__(self, brand, year, color):
#         super().__init__(brand, year)
#         self.color = color

#     def drive(self):
#         print("The bicycle is being pedaled.")


# car = Car("Toyota", 2021, "Petrol")
# car.drive()
# car.stop()
# print(car.brand)
# print(car.year)
# print(car.fuel_type)

# bicycle = Bicycle("Giant", 2022, "Red")
# bicycle.drive()
# bicycle.stop()
# print(bicycle.brand)
# print(bicycle.year)
# print(bicycle.color)




# Асоціація

# class Author:
#     def __init__(self, name):
#         self.name = name
#         self.books = ["Name book"]

#     def write(self, name: str):
#         print(f"{self.name} is writing {name}")


# class Title:
#     def __init__(self, title: str):
#         self.title = title


# class Book:
#     def __init__(self, title: Title, author: Author):
#         self.title = title
#         self.author = author

#     def display_info(self):
#         print(f"Title: {self.title.title}")
#         print(f"Author: {self.author.name}")


# author = Author("John Smith")
# title = Title("Python Programming")
# book = Book(title, author)
# # book.display_info()
# print(book.title.title)
# print(book.author.name)
# book.author.write(book.title)

# author.write()




# Поліморфізм (Polymorphism)
# from abc import ABC, abstractmethod


# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2


# shapes = [Rectangle(5, 3), Circle(2), Rectangle(4, 6)]

# for shape in shapes:
#     print(shape.area())



# Метакласи

# class MyMeta(type):
#     def __new__(cls, name, bases, attrs):
#     # Додавання атрибуту до класу
#         attrs['extra_attr'] = 100
#     # Створення нового класу з метакласом
#         return super().__new__(cls, name, bases, attrs)

#     # def __init__(self)
#     # def __call__(self)

# class MyClass(metaclass=MyMeta):
#     pass


# obj = MyClass()
# print(obj.extra_attr) # Виведе: 100




# products
# reviews
# employees
# logs


class Product:
    count = 0
    color = "white"
    employee = None

    def __init__(self, name: str) -> None:
        self.name = name

    def sold(self) -> str:
        if self.count > 0:
            self.count -= 1
            return "Товар успішно продано"
        else:
            return "Товар відсутній"

    def show_count(self) -> int:
        return self.count


class Review:
    def __init__(self, text: str, grade: float, author) -> None:
        self.text = text
        self.grade = grade
        self.author = author

    def change_review(self, author, text: str) -> str:
        if author != self.author:
            return "Не можливо змінити чужий відгук"

        self.text = text
        return "Відгук успішно змінено"


class Employee:
    start_date: str|None = None
    is_work: bool = False

    def __init__(self, name: str, posititon: str, salary: float) -> None:
        self.name = name
        self.position = posititon
        self.salary = salary

    def change_salary(self, new_salary) -> str:
        self.salary = new_salary
        return "ЗП успішно змінено"


products = [Product("Кава"), Product("Хліб")]
employees = [Employee("Алекс", "Менеджер", 12000)]