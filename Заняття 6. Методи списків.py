# pip install faker

# import random
# from faker import Faker

# fake = Faker("uk_UA")

# students = []

# for _ in range(50):
#     first_name = fake.first_name()
#     middle_name = fake.middle_name()
#     last_name = fake.last_name()

#     students.append([first_name, middle_name, last_name])

# print(students)

# for student in students:
#     if student[2].startswith("А"):
#         print(student)

# random.randint(15, 60)

prods = [
    "Гречка",
    "Макарони",
    "Спагеті",
    "Картопля",
    "Буряк",
    "Морква",
    "Капуста",
    "Цибуля",
    "Часник",
    "Борошно",
    "Яйця",
    "Соняшникова олія",
    "Вершкове масло",
    "Сіль",
    "Перець",
    "Цукор",
    "Оцет",
    "Сода",
    "Чай",
    "Кава"
]

products = []
print(["№", "Назва товару"])
for i, product in enumerate(prods):
    print([i+1, product])
    products.append([i+1, product])

commands = [
    "Показати список наявних товарів",
    "Додати новий товар до списку",
    "Додати список товарів",
    "Видалити товар за ім'ям",
    "Видалити товар за номер",
    "Відсортувати список товарів за ім'ям товарів",
    "Відсортувати список товарів за номером"
]

while True:
    break

stop_worlds = ["stop", "exit"]
while True:
    print(f"Введіть назву товару для додавання у список товарів або введіть одне зі слів {stop_worlds} для припинення")
    product = input()

    if product in stop_worlds:
        break

    prods = [prod[1] for prod in products]
    if product not in prods:
        products.append([len(products) + 1, product])
    else:
        print(f"Товар '{product}' вже наявний у списку")

products.sort(key=lambda product: product[1])
for product in products:
    print(product)

