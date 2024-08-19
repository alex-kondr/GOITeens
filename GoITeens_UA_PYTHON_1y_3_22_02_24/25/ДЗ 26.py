class Field:
    name = ""


class Product(Field):
    def __init__(self, name: str, start_date: str, expire_date: str, count: int):
        self.name = name
        self.start_date = start_date
        self.expire_date = expire_date
        self.count = count

    def sold(self, count) -> str:
        if count <= self.count:
            self.count -= count
            return "Товар успішно продано"
        else:
            return "Недостатня кількість товару"

    def show_count_product(self) -> int:
        return self.count


class Employee(Field):
    salary: float = .0

    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position

    def change_salary(self, salary: float) -> str:
        self.salary = salary
        return "ЗП успішно створено"

    def change_posititon(self, pisition: str) -> str:
        pass


class Author(Field):
    def __init__(self, name: str, city: str) -> None:
        self.name = name
        self.city = city


class Review:
    def __init__(self, text: str, grade: float, author: Author) -> None:
        self.text = text
        self.grade = grade
        self.__author = author

    def change_review(self, text: str, author: Author) -> str:
        if author == self.__author:
            self.text = text
            return "Відгук успішно змнінено"
        else:
            return "Недоступна дія"


class Shop:
    def __init__(self) -> None:
        self.products: list[Product] = []
        self.reviews: list[Review] = []
        self.employees: list[Employee] = []

    def add_product(self, product: Product):
        self.products.append(product)


product_1 = Product("Хліб", "01.01.2024", "10.01.2024", 10)
product_2 = Product("Хліб", "01.01.2024", "10.01.2024", 10)
# product_2 = Product("Кава", "01.01.2024", "10.01.2024", 5)
# product_3 = Product("Масло", "01.01.2024", "10.01.2024", 50)

shop = Shop()
shop.add_product(product_1)
shop.add_product(product_2)
# shop.add_product(product_3)

print(shop.products)