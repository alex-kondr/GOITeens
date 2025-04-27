class Car:
    brand = "BMW"
    color = "Red"

    def move_left(self):
        print("Авто рухається вліво")

    def move_rigth(self):
        print("Авто рухається вправо")

    def change_color(self, new_color):
        self.color = new_color


# car = Car()
# car.move_left()
# car.move_rigth()
# print(car.brand)
# print(car.color)
# car.change_color("Green")
# car.color = "Green"
# print(car.color)


class Animal:
    calorie = 0

    def __init__(self, type_animal: str, color: str):
        self.type = type_animal
        self.color = color

    def sleep(self, time: int = 10):
        if self.calorie > 10:
            self.calorie -= 5 * time / 10
            print(f"{self.type} спить протягом {time} с")
        else:
            print("Нагодуй мене")

    def eating(self, calorie: int):
        self.calorie += calorie

    def move(self):
        if self.calorie > 50:
            self.calorie -= 20
            print(f"{self.type} рухається")
        else:
            print(f"{self.type} рухатись не може")


# cat_1 = Animal("Кішка", "Рудий")
# cat_2 = Animal("Кішка", "Чорний")
# dog = Animal("Собака", "Біла")

# print(dog.calorie)
# dog.eating(100)
# print(dog.calorie)
# dog.sleep()
# print(dog.calorie)
# dog.move()
# print(dog.calorie)
# dog.sleep(100)
# print(dog.calorie)


class Animal:
    def __init__(self, color: str, type_animal: str):
        self.color = color
        self._type = type_animal
        self.__calorie = 0

    def change_calorie(self, calorie):
        self.__calorie += calorie

    def get_calorie(self):
        return self.__calorie


cat = Animal("Білий", "Кішка")
# cat.color = "Чорний"
# print(cat.color)
# cat._type = "Собака"
# print(cat._type)
cat.__calorie = 50
cat.change_calorie(150)
print(cat.get_calorie())