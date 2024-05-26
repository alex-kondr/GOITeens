# Зробити перевірку того, чи є число 3 в множині перших дев'яти простих чисел prime_numbers:
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
# print(4 in prime_numbers)








# Створити словник із наступними ключами (дивись нижче).
# Зробити перевірку чи є елемент 'age' серед ключів словника та вивести інформацію, яка подана в Результаті.

user = {
    "name": "Bill",
    "surname": "Bosh",
    "age": 22
}

# if "age" in user:
#     print(True)
# print("age" in user)




# Задано словник, що містить відстані від Києва до обласних центрів. Знайти обласний центр, найбільш віддалений від Києва.
cities = {
    'Київ'    : 0,
    'Вінниця' : 240,
    'Харків'  : 470,
    'Ужгород' : 808,
    'Львів'   : 540,
    'Житомир' : 120,
    'Одеса'   : 430
}

# city = ""
# lenght = 0
# for city_temp, distance in cities.items():
#     if distance > lenght:
#         city = city_temp
#         lenght = distance

# print(f"Місто {city} найбільш віддалено від Києва, а саме на відстань {lenght}")

# city = max(cities, key=cities.get)
# print(f"Місто {city} найбільш віддалено від Києва, а саме на відстань {cities[city]}")




# Дано список міст, в яких працює Укрпошта та Нова Пошта.
# Користувач вводить місто з клавіатури.
# Запропонувати користувачеві доставку поштовим оператором або вивести повідомлення про неможливість доставки.
# post_ukr = {'Київ', 'Фастів', 'Ірпінь', 'Боярка'}
# post_new = {'Київ', 'Фастів', 'Кагарлик', 'Узин', 'Ірпінь', 'Гатне', 'Боярка', 'Гостомель'}
# user_city_min_lenth = 3

# city = input("Введіть назву міста (мінімум три символа): ")
# if city in post_new or city in post_ukr:
#     print("Доставка можлива")

# if city in post_ukr:
#     print("Доставка можлива Укрпоштою")

# if city in post_new:
#     print("Доставка можлива Новою поштою")

# if len(city) >= user_city_min_lenth:
#     for city_post in post_ukr:
#         if city in city_post:
#             print("Доставка можлива Укрпоштою")
#             break
#     else:
#         print("Доставка не можлива Укрпоштою")

#     for city_post in post_new:
#         if city in city_post:
#             print("Доставка можлива Новою поштою")
#             break
#     else:
#         print("Доставка не можлива Новою поштою")
# else:
#     print("Необхідно ввести не менше 3-х символів")






# Задано список туристичних ваучерів, в яких зазначено готель,
# прізвище власника, кількість подорожуючих.
# Підрахувати, скільки туристів їдуть в кожен з готелів.
clients = [
    ['White House', 'Іванов', 3],
    ['Shelter', 'Іванова', 5],
    ['Верховина', 'Іванова', 5],
    ['Буковель', 'Іванова', 5],
    ['White House', 'Абабагаламага', 5]
]

# hotels = {}
# for vaucher in clients:
#     if vaucher[0] not in hotels:
#         hotels[vaucher[0]] = vaucher[2]
#     else:
#         hotels[vaucher[0]] += vaucher[2]

# print(hotels)



# Напишіть програму, яка приймає список чисел та повертає новий список,
# що містить лише унікальні елементи вхідного.
numbers = [1, 5, 5, 7, 1, 9, 5]
# numbers_unique = []
# for number in numbers:
#     if number not in numbers_unique:
#         numbers_unique.append(number)


# numbers_unique = list(set(numbers))
# print(numbers_unique)



# Напишіть програму, яка приймає словник, та змінює всі значення на їх квадрати.
# my_dict = {
#     "a": 5,
#     "b": 1,
#     "c": 9
# }

# for key, value in my_dict.items():
#     my_dict[key] = value ** 2

# print(my_dict)




# Вивести на екран три найпоширеніші символи в рядку (пробіл за символ не вважаємо).
# my_string = "Вивести на екран три найпоширеніші символи в рядку".replace(" ", "")

# most_popule = {}
# for char in my_string:
#     if char not in most_popule:
#         most_popule[char] = my_string.count(char)

# sorted_most_popule = sorted(most_popule, key=most_popule.get, reverse=True)
# print(sorted_most_popule)
# print(sorted_most_popule[:3])







# Створіть програму, яка приймає список рядків та повертає список унікальних слів,
# які зустрічаються в цих рядках.
# strings = [
#     "створіть програму, яка приймає список рядків",
#     "повертає список унікальних слів",
#     "вивести на екран три найпоширеніші",
#     "яка приймає словник, та змінює всі значення"
# ]

# word_unique = set()
# for string in strings:
#     words = string.replace(",", "").split()
#     for word in words:
#         word_unique.add(word)

# word_unique = list(word_unique)
# print(word_unique)









# Напишіть програму, яка приймає список рядків та повертає список,
# в якому кожен елемент — це рядок, який містить першу літеру кожного слова в вхідному рядку.
# strings = [
#     "створіть програму, яка приймає список рядків",
#     "повертає список унікальних слів",
#     "вивести на екран три найпоширеніші",
#     "яка приймає словник, та змінює всі значення"
# ]

# chars = []
# # for string in strings:
# #     words = string.replace(",", "").split()
# #     for word in words:
# #         chars.append(word[0])

# for string in strings:
#     chars.extend([word[0] for word in string.replace(",", "").split()])

# print(chars)




# Створіть програму, яка приймає список та повертає рядок,
# який містить всі елементи вхідного списку, розділені комами.
# words = "в якому кожен елемент це рядок який містить першу літеру кожного слова в вхідному рядку".split()
# string = ",".join(words)
# print(string)






# Напишіть програму, яка приймає два словника та повертає словник,
# що містить ключі та значення обох вхідних словників.

cities = {
    'Київ'    : 0,
    'Вінниця' : 240,
    'Харків'  : 470,
    'Ужгород' : 808,
    'Львів'   : 540,
    'Житомир' : 120,
    'Одеса'   : 430
}

user = {
    "name": "Bill",
    "surname": "Bosh",
    "age": 22
}

# cities.update(user)

# print(cities)


# Створіть програму, яка приймає список та повертає список,
# який містить тільки непарні елементи вхідного списку.

# numbers = list(range(-20, 21))
# numbers = [number for number in numbers if number % 2 == 1]
# print(numbers)

# numbers = []
# for number in numbers:
#     if number % 2 == 1:
#         numbers.append(number)






# Напишіть програму, яка приймає два списки та повертає список,
# який містить елементи, які зустрічаються у обох вхідних списках.

# numbers_1 = list(range(-20, 21))
# numbers_2 = list(range(-10, 11))

# # numbers_2.extend(numbers_1)
# numbers_3 = numbers_1 + numbers_2
# print(numbers_1)
# print(numbers_2)
# print(numbers_3)




# Створіть програму, яка приймає список та повертає словник,
# де ключі — це елементи списку, а значення — це кількість входжень цих елементів в список.
# numbers_1 = list(range(-20, 21))
# numbers_2 = list(range(-10, 11))

# numbers_3 = numbers_1 + numbers_2

# import pprint

# my_dict = {number: numbers_3.count(number) for number in numbers_3}
# pprint.pprint(my_dict)





# Напишіть програму, яка приймає список чисел та повертає список,
# в якому кожен елемент — це кількість входжень цього числа в вхідному списку.
# numbers_1 = list(range(-20, 21))
# numbers_2 = list(range(-10, 11))
# numbers_3 = numbers_1 + numbers_2
# # my_set = set(numbers_3)

# # numbers_count = []
# # for number in my_set:
# #     numbers_count.append(numbers_3.count(number))

# numbers_count = [numbers_3.count(number) for number in set(numbers_3)]
# print(numbers_count)


# Створіть програму, яка приймає список та повертає новий список,
# в якому всі елементи вхідного списку випадковим чином перетасовані.









# Напишіть програму, яка приймає словник та повертає список ключів,
# значення яких є максимальними у словнику.








# Створіть програму, яка приймає список та повертає новий список,
# в якому всі елементи вхідного списку упорядковані в зворотному порядку.







# Напишіть функцію, яка приймає два списки та повертає True,
# якщо обидва списки містять однакові елементи, незалежно від їх порядку.










# Створіть програму, яка приймає список та повертає новий список,
# в якому кожен елемент — це сума попередніх елементів вхідного списку
# (тобто, перший елемент нового списку — це перший елемент вхідного списку,
# другий елемент нового списку — це сума першого та другого елементів вхідного списку і т.д.).