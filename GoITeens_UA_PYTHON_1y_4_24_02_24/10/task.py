# Зрізи
# numbers = list(range(1, 11))
# print(numbers[::2])
# print(numbers[1::2])
# print(numbers[2::3])












# Виокремлення ім’я та прізвища
# Заданий рядок, який містить ім’я та прізвище користувача, що розділені пробілом
# Написати програму з використанням зрізів, яка виокремить ім’я та прізвище

# my_string = "Ivan,Ivanov,Ivanovich,hello"
# delimiter = ","

# names = []
# idx = 0
# count_delimiter = my_string.count(delimiter)
# for _ in range(count_delimiter):
#     idx_start = idx
#     idx = my_string.find(delimiter, idx_start) + 1
#     name = my_string[idx_start:idx-1]
#     names.append(name)
# else:
#     names.append(my_string[idx:])

# print(names)













# Дано рядок, який містить довільне речення, слова в якому розділені пробілами.
# З використанням зрізів знайти і вивести слово, яке має найменшу довжину.

# string = "Дано рядок, який містить довільне речення, слова в якому розділені пробілами. З використанням зрізів знайти і вивести слово, яке має найбільшу довжину."
# string = string.replace(",", "").replace(".", "")
# delimiter = " "

# smallest_word = ""
# len_smallest_word = 756454987690

# idx = 0
# count_delimiter = string.count(delimiter)
# for _ in range(count_delimiter+1):
#     idx_start = idx
#     idx = string.find(delimiter, idx_start) + 1
#     word = string[idx_start:idx-1]

#     len_word = len(word)
#     if len_word < len_smallest_word:
#         len_smallest_word = len_word
#         smallest_word = word

# print(f"Найменше слово '{smallest_word}', яке має довжину {len_smallest_word}")


# numbers = [1, 5, 6, 1, 9, 6]
# my_set = set(numbers)
# # print(len(my_set))
# my_set.discard(89)
# print(my_set)




# Задано список номерів мобільних телефонів:
# Вважаючи, що всі номери записані у форматі +38 (код) 111-11-11,
# порахувати кількість абонентів оператора, що має коди «067», «097», «068»
# vodafone = {"050", "066", "095", "099"}
# kyivstar = {"067", "068", "098", "097", "096"}
# life = {"063", "093"}

# phone_number = input("Введи свій номер телефону у форматі '+38 (050) 111-12-13': ")
# code_op = phone_number[5:8]

# if code_op in vodafone:
#     print("Оператор, який Вас обслуговує називається 'Vodafone'")
# elif code_op in kyivstar:
#     print("Оператор, який Вас обслуговує називається 'Kyivstar'")
# elif code_op in life:
#     print("Оператор, який Вас обслуговує називається 'Life'")
# else:
#     print("Невідомий оператор")








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
# numbers = list(range(1, 11))
# print(numbers[1:5:2])








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