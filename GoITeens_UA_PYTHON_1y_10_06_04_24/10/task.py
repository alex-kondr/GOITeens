# Зрізи
# start = 1
# end = 10
# numbers = list(range(start, end+1))
# print(numbers)
# print(numbers[2:])
# print(numbers[:5])
# print(numbers[::3])
# print(numbers[::-3])
# print(numbers[-5:-1])
# print(numbers[-2:-5:-1])

# print(numbers)
# # numbers.reverse()
# # print(numbers)

# numbers_new = numbers[::-1]
# print(numbers)
# print(numbers_new)


# string = "Заданий рядок, який містить ім’я та прізвище користувача"
# print(string[10:])
# print(string[:50])
# print(string[::-1])
# print(string[::100])








# Відокремлення ім’я та прізвища
# Заданий рядок, який містить ім’я та прізвище користувача, що розділені пробілом
# Написати програму з використанням зрізів, яка виокремить ім’я та прізвище

# my_string = "Ivan,Ivanov,Ivanovich,hello"
# delimiter = ","

# count = my_string.count(delimiter)
# # print(f"{count = }")
# # input()
# idx = 0

# for _ in range(count):
#     idx_start = idx
#     idx = my_string.find(delimiter, idx_start) + 1
#     world = my_string[idx_start:idx-1]
#     print(world)
#     print(len(world))
#     input()
# else:
#     world = my_string[idx:]
#     print(world)
#     print(len(world))










# Дано рядок, який містить довільне речення, слова в якому розділені пробілами.
# З використанням зрізів знайти і вивести слово, яке має найменшу довжину.

# string = "Дано рядок, який містить довільне речення, слова вв якому розділені пробілами. Зз використанням зрізів знайти іі вивести слово, яке має найбільшу довжину. 5"
# string = string.replace(",", "").replace(".", "")
# delimiter = " "

# smalest_world = ""
# smalest_len_world = 7894512

# idx = 0
# count = string.count(delimiter)
# for _ in range(count):
#     idx_start = idx
#     idx = string.find(delimiter, idx_start) + 1
#     world = string[idx_start:idx-1]

#     len_world = len(world)
#     if len_world < smalest_len_world:
#         smalest_world = world
#         smalest_len_world = len_world
# else:
#     world = string[idx:]

#     len_world = len(world)
#     if len_world < smalest_len_world:
#         smalest_world = world
#         smalest_len_world = len_world

# print(f"Слово '{smalest_world}' має наменшу довжину, яка дорівнює '{smalest_len_world}'")


# my_set = set()
# print(my_set)
# print(type(my_set))

# my_set = {1, 5, 8}


# numbers = [1, 5, 6, 1, 9, 6]
# print(f"{numbers = }")
# my_set = set(numbers)
# print(f"{my_set = }")
# new_numbers = list(my_set)
# print(f"{new_numbers = }")

# my_set.add(1)
# print(f"{my_set = }")


string = "Hello world"
my_list = list(string)
print(f"{my_list = }")
my_set = set(string)
print(f"{my_set = }")



# # print(len(my_set))
# my_set.discard(89)
# print(my_set)




# Задано список номерів мобільних телефонів:
# Вважаючи, що всі номери записані у форматі +38 (код) 111-11-11,
# порахувати кількість абонентів оператора, що має коди «067», «097», «068»









# Множини

### Створити множину
# numbers = set("Hello world!")
# print(numbers)



### Додати до неї новий елемент
# numbers.add("y")
# print(numbers)


### Видалити елемент з виключенням
# numbers.remove("o")
# print(numbers)




### Видалити елемент з множини не викликаючи виключення
# numbers.discard("d")
# print(numbers)

# number = numbers.pop()
# print(f"{numbers = }")
# print(f"{number = }")








# Дано список клієнтів, які купили товар А та список клієнтів, які купили товар В.
# Знайти:
# - клієнтів, які купили обидва товари А і B
# - створити один список клієнтів, шляхом операції об’єднання
# clients_a = {"Олександр", "Артем", "Дмитро", "Максим"}
# clients_b = {"Артем", "Матвій", "Єгор", "Дмитро"}

# print(f"Список клієнтів, які купили обидва товари: {clients_a & clients_b}")
# print(f"Список клієнтів, які щось купили: {clients_a | clients_b}")
# print(f"Список клієнтів, які один із товарів: {clients_a.symmetric_difference(clients_b)}")








# Створіть список з чисел від 1 до 10 та використайте зрізи для виводу елементів від другого до п'ятого включно.









# Створіть рядок та використайте зрізи для виводу перших трьох та останніх трьох символів.
# string = "Створіть рядок та використайте зрізи для виводу перших"
# new_string = string[:3] + string[-3:]
# print(new_string)






# Визначити, чи порядок значень у запропонованому списку є строго зростаючим
# numbers = [4, 5, 60, 80, 79, 95, 140]
# for i in range(1, len(numbers)):
#     if numbers[i] < numbers[i-1]:
#         print("Список не зростаючий")
#         break
# else:
#     print("Список строго зростаючий")







# Створіть список зі стрічок та використайте зрізи для виводу останніх трьох символів з кожної стрічки.
# strings = ["Створіть список", "стрічок та", "зрізи для виводу", "трьох!"]
# last_chars = [string[-3:] for string in strings if len(string) > 5]
# print(last_chars)

# for string in strings:
#     print(string[-3:])








# Створіть програму, яка приймає від користувача рядок і перевіряє чи є він паліндромом
# (слово, яке читається однаково зліва направо та справа наліво).
# Виведіть результат у вигляді логічного значення (True або False).
# user_string = input("Введіть слово: ")
# print(f"{user_string = }")
# is_polindrome = user_string == user_string[::-1]
# print(is_polindrome)









# Створіть програму, яка приймає від користувача дві строки та перевіряє,
# чи є вони анаграмами (слова, у яких ті самі літери, але в різному порядку).
# Виведіть результат у вигляді логічного значення (True або False).
# string_1 = "слово"
# string_2 = "влосоз"

# list_string_1 = set(string_1)
# # list_string_1.sort()
# print(list_string_1)

# list_string_2 = set(string_2)
# # list_string_2.sort()
# print(list_string_2)

# is_anagram = list_string_1 == list_string_2
# print(is_anagram)







# Створіть список зі стрічок та використайте зрізи для виводу символів з кожної стрічки у зворотньому порядку.









# Створіть програму, яка перевіряє чи рядок включає в собі лише цифри.







# Створіть програму, яка приймає рядок, та повертає рядок, з якого було видалено всі пробіли.






# Створіть множину та перевірте, чи є вона підмножиною іншої множини.