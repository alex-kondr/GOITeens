# stock = {"банан": 5, "яблуко": 7, "апельсин": 31, "лимон": 14}
# item = input("Вкажіть продукт: ")
# count = int(input("Введіть кількість: "))
# msg = False
# if item in stock:
#     if stock[item] >= count:
#         # print("True")
#         msg = True
#     # else:
#         # print("False")

# # else:
# #     print("False")

# print(msg)



# stock = {
#     "Яблуко": 20,
#     "Печиво": 50,
#     "Апельсин": 30,
#     "Слива": 25
# }

# product = input("Введіть товар який хочете купити > ")
# quantity = int(input("Введіть кількіст яку хочете купити > "))

# if product in stock and stock[product] >= quantity:
#     print(True)
# else:
#     print(False)



stock = {
    'Молоко': 60,
    'Вода': 20,
    'буряк': 5,
    'Пончик': 30 
}
a = int(input('Вкажіть кількість продуктів'))
b = input('Вкажіть продукт')

for product, number in stock.items():
    print(f"Товар: {product} - {number} шт.")
# print(f"Число продуктів: {sum(stock.values())}")

from pprint import pprint

users = {
     "Алекс": {
         "username": "alex",
         "age": 20,
         "city": "Київ",
         "sex": "male"
     },
     "Дмитро": {
         "username": "dima",
         "age": 15,
         "city": "Одеса",
         "e-mail": "dima@gmail.com"
    },
     "Владислав": {
         "username": "vlad",
         "age": 14,
    },
 }

user_searched = input("Введіть імена користувачів через пробіл: ").split()
for user in user_searched:
    if user in users:
        print(f"{user}: {users[user]}") # Ім’я, вік, стать, електронна пошта
        print(f"Ім’я: {user},\
              вік: {users[user].get("age"), "Інфо відсутнє"}, \
                стать: {users[user].get("sex", "Інфо відсутнє")}, \
                електронна пошта: {users[user].get("e-mail", "Інфо відсутнє")}")
    else:
        print(f"Користувача {user} не знайдено")

stock = {
    'Молоко': 60,
    'Вода': 20,
    'буряк': 5,
    'Пончик': 30 
}

a = int(input('Вкажіть кількість продуктів'))
b = input('Вкажіть продукт')

for product, number in stock.items():
    print(f"Товар: {product} - {number} шт.")



print(product, number )
if product in stock:
    if a <= stock[product]:
        ...
    print(True)
else:
    print(None)