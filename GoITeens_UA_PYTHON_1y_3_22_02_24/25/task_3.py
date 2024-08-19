class Vehicle:
    def __init__(self, brand: str) -> None:
        self.brand = brand

    def start(self):
        print("Транспорт їде вперед")

    def stop(self):
        print("Транспорт зупиняється")


class Car(Vehicle):
    def __init__(self, brand: str, year: str) -> None:
        super().__init__(brand)
        self.year = year

    def start(self):
        print("Авто їде з великою швидкістю")


class Bicycle(Vehicle):
    def start(self):
        print("Їду за допомогою педалей")


vehicle = Vehicle("Україна")
car = Car("Toyota", "2012")
car.start()
car.stop()
print(car.brand)
print(car.year)