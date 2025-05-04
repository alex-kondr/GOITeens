# Інкапсуляція (Encapsulation)

# class MyClass:
#     def __init__(self):
#         self.public_attribute = "Public attribute"
#         self._protected_attribute = "Protected attribute"
#         self.__private_attribute = "Private attribute"

#     def public_method(self):
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
# obj.__private_method()



# Наслідування (Inheritance)

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def drive(self):
        print("The vehicle is in motion.")

    def stop(self):
        print("The vehicle has stopped.")


class Car(Vehicle):
    def __init__(self, brand, year, fuel_type):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def drive(self):
        print("The car is driving on the road.")


class NewClass:
    new_attr = "Новий атрибут"


class Liftback(Car, NewClass):
    def __init__(self, brand, year, fuel_type, color):
        super().__init__(brand, year, fuel_type)
        self.color = color


# car = Car("Nissan", 1992, "Бензин")
# # print(car.brand)
# car.drive()
# car.stop()

class Bicycle(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def drive(self):
        print("The bicycle is being pedaled.")


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

class Author:
    def __init__(self, name):
        self.name = name
        self.books = ["Book_1", "Book_2"]

    def write(self):
        print(f"{self.name} is writing a book.")


class Book:
    def __init__(self, title, author: Author):
        self.title = title
        author.books.append(title)
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")
        print(f"Author books: {self.author.books}")


# book = Book("Зелена книга", "Автор")


# author = Author("John Smith")
# book = Book("Python Programming", author)
# book.display_info()

# book_2 = Book("Book_3", author)
# book_2.display_info()

# author.write()
# print(f"{author.books = }")




# Поліморфізм (Polymorphism)

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# shapes = [Rectangle(5, 3), Circle(2), Rectangle(4, 6)]

# for shape in shapes:
#     print(shape.area())



# Метакласи

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
    # Додавання атрибуту до класу
        attrs['extra_attr'] = 100
    # Створення нового класу з метакласом
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=MyMeta):
    pass


obj = MyClass()
print(obj.extra_attr) # Виведе: 100