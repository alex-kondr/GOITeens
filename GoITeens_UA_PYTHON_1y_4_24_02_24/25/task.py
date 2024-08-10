class Animal:
    type = "Animal"

    def __init__(self, weight: float):
        print("Call __init__ method")
        self.weight = weight

    def eating(self):
        print(f"{self.type}: Я їм їжу...")
        self.weight += 0.5

    def run(self):
        print(f"{self.type}: Я біжу ->")
        self.weight -= 0.3


class Dog(Animal):
    type = "Dog"

    def bark(self):
        print(f"{self.type} say: Bark, bark!")

    def run(self):
        print(f"{self.type}: Я біжу ->")
        self.weight -= 0.4

class Cat(Animal):
    type = "Cat"

    def meow(self):
        print(f"{self.type} say: Meow...mrrrrrrr")


class Paw:
    def eating(self):
        print("Я лапою їм їжу...")

    def up(self):
        print("Я підняв ляпу...")

    def down(self):
        print("Я опускаю лапу...")


class BlackDog(Dog):
    paw = Paw()


dog = Dog(7)
cat = Cat(2.6)

black_dog = BlackDog(12)

print(f"{black_dog.type}: Моя вага: '{black_dog.weight = }' кг")
black_dog.eating()
print(f"{black_dog.type}: Моя вага: '{black_dog.weight = }' кг")

input()
black_dog.run()
print(f"{black_dog.type}: Моя вага: '{black_dog.weight = }' кг")

black_dog.paw.up()
black_dog.paw.down()


# Створити два різних класи.

# Створити клас, який наслідується з одного з попередніх класів та додає новий атрибут.

# Створити екземпляри всіх трьох класів, та роздрукувати всі атрибути даних екземплярів, а також продемонструвати роботу методу одного з екземплярів
