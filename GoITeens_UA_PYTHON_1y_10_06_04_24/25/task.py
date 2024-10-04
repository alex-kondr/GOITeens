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

# print(Animal.color)

# cat = Animal()
# dog = Animal()

# print(f"{cat.color = }")
# print(f"{dog.color = }")

# cat.color = "White"

# print(f"{cat.color = }")
# print(f"{dog.color = }")
# print("run")
# cat.run()

# # print("eating...")
# cat.eating()

# # print("run")
# cat.run()
# cat.run()
# cat.run()
# cat.run()
# cat.run()
# cat.run()
# print("dog")
# dog.run()





class Animal:
    eat = False

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


class Cat(Animal):
    def run(self):
        if self.eat:
            print("Run ->")
        else:
            print("Walking...")

    def sleep(self):
        print("..zzzz")


class BlackCat(Cat):
    def __init__(self, weigth):
        self.color = "Black"
        self.weight = weigth


class Dog(Animal):
    pass


cat = Cat("White", 3)
print(cat.color)
cat.run()
cat.eating()
cat.run()
cat.sleep()

dog = Dog("Black", 9)
# dog.sleep()

# print(Animal.color)

# cat = Animal("White", 3)
# dog = Animal("Black", 6)

# cat.eating()
# print(cat.weight)
# cat.change_weight(4)
# print(cat.weight)

# print(dog.weight)

class Pulse:
    live = True

    def is_live(self):
        print("It`s a LIVE!!!!!!!" if self.live else "Ups.... You die")

# obj = Pulse()
# obj.live = False
# obj.is_live()


# animal = Animal("Black", 8)
# animal.eating()


# class Dog(Animal, Pulse):
#     speed = 50

#     def run_by_cat(self):
#         print("Runing chase the cat")


# # animal.run_by_cat()

# dog = Dog("Black", 3)
# dog.run()
# dog.eating()
# dog.run()
# dog.run_by_cat()
# dog.live = False
# dog.is_live()



# class Animal:
#     type = "Animal"

#     def __init__(self, weight: float):
#         print("Call __init__ method")
#         self.weight = weight

#     def eating(self):
#         print(f"{self.type}: Я їм їжу...")
#         self.weight += 0.5

#     def run(self):
#         print(f"{self.type}: Я біжу ->")
#         self.weight -= 0.3


# class Dog(Animal):
#     type = "Dog"

#     def bark(self):
#         print(f"{self.type} say: Bark, bark!")

#     def run(self):
#         print(f"{self.type}: Я біжу ->")
#         self.weight -= 0.4


# class Cat(Animal):
#     type = "Cat"

#     def meow(self):
#         print(f"{self.type} say: Meow...mrrrrrrr")


# class Paw:
#     def eating(self):
#         print("Я лапою їм їжу...")

#     def up(self):
#         print("Я підняв ляпу...")

#     def down(self):
#         print("Я опускаю лапу...")


# class BlackDog(Dog):
#     paw = Paw()


# # dog = Dog(7)
# # cat = Cat(2.6)

# dog = BlackDog(7)
# dog.paw.down()

# dog.bark()








# Створити два різних класи.

# Створити клас, який наслідується з одного з попередніх класів та додає новий атрибут.

# Створити екземпляри всіх трьох класів, та роздрукувати всі атрибути даних екземплярів,
# а також продемонструвати роботу методу одного з екземплярів



# class Human:
#     name = ""

#     def voice(self):
#         print(f"Hello! My name is {self.name}")


# class Developer(Human):
#     field_description = "My Programming language"
#     value = ""

#     def make_some_code(self):
#         return f"{self.field_description} is {self.value}"


# class PythonDeveloper(Developer):
#     value = "Python"


# class JSDeveloper(Developer):
#     value = "JavaScript"


# p_dev = PythonDeveloper()
# p_dev.name = 'Bob'
# p_dev.voice()   # Hello! My name is Bob
# print(p_dev.make_some_code())  # My Programming language is Python


# js_dev = JSDeveloper()
# print(js_dev.make_some_code())  # My Programming language is JavaScript



# class MyClass:
#     attr_class = 5
#     my_list = [2]

#     def __new__(cls, *args, **kwargs):
#         print("Call __new__ method...")
#         return super().__new__(cls)

#     def __init__(self, value: str|float = "Hello"):
#         print(f"Class __init__ method... {value = }")
#         self.value = value

#     def __del__(self):
#         print("Call __del__ method")

#     def __call__(self, value):
#         return f"Call __call__ method.... {value = }"

#     def __len__(self):
#         print("Call __len__ method")
#         return len(self.my_list)

#     def __str__(self):
#         return "Call __str__ method. This is MyClass obj"

#     def __add__(self, other): # +
#         print("Call __add__ method...")
#         return self.value + " " + other.value

#     def __sub__(self, other): # -
#         pass

#     def __truediv__(self, other): # /
#         pass

#     def __floordiv__(self, other):  # //
#         pass

#     def __mod__(self, other): # %
#         pass

#     def __mul__(self, other): # *
#         pass

#     def __pow__(self, other): # **
#         pass

#     def __gt__(self, other): # >
#         pass

#     def __lt__(self, other): # <
#         pass

#     def __eq__(self, other): # ==
#         pass

#     @staticmethod
#     def my_func(value):
#         print(f"Value by my_func '{value}'")

#     @classmethod
#     def my_class_method(cls):
#         print(f"Attr class '{cls.attr_class}'")


# my_class = MyClass()
# my_class_2 = MyClass("Bye")
# print(my_class.attr_class)
# # my_class_2.my_func("Hello")
# my_class.attr_class = "Hi"
# print(my_class.attr_class)

# MyClass.my_func("Bye")
# MyClass.my_class_method()