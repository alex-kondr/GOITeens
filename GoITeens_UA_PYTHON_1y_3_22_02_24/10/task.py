# Зрізи

# Відокремлення ім’я та прізвища
# Заданий рядок, який містить ім’я та прізвище користувача, що розділені пробілом
# Написати програму з використанням зрізів, яка виокремить ім’я та прізвище

# full_name = "Ivan,Ivanov,Ivanovich,hello"
# delimiter = ","
# names = []

# idx = 0
# count_space = full_name.count(delimiter)

# for _ in range(count_space):
#     idx_start = idx
#     idx = full_name.find(delimiter, idx_start) + 1
#     word = full_name[idx_start:idx-1]
#     names.append(word)
# else:
#     names.append(full_name[idx:])

# print(names)










# Дано рядок, який містить довільне речення, слова в якому розділені пробілами.
# З використанням зрізів знайти і вивести слово, яке має найменшу довжину.

# string = "Дано рядок, якиймістить довільне речення, слова в. якому розділені пробілами. З використанням зрізів знайти і вивести слово, яке має найбільшу довжину."
# string = string.replace(",", "").replace(".", "")
# delimiter = " "

# idx = 0
# smallest_word = ""
# len_smallest_word = 3333789922244

# count_space = string.count(delimiter)
# for _ in range(count_space+1):
#     idx_start = idx
#     idx = string.find(delimiter, idx_start) + 1
#     word = string[idx_start:idx-1]

#     len_word = len(word)
#     if len_word < len_smallest_word and len(word) > 1:
#         smallest_word = word
#         len_smallest_word = len_word

# print(smallest_word)

# my_set = set("hello")
# for i in my_set:
#     print(i)
# print(my_set)



# my_string = "hello"
# my_set = set(my_string)
# print(my_set)







# Задано список номерів мобільних телефонів:
# Вважаючи, що всі номери записані у форматі +38 (код) 111-11-11,
# порахувати кількість абонентів оператора, що має коди «067», «097», «068»

# vodafone = {"066", "095", "099", "050", "065"}
# kyivstar = {"067", "068", "064", "096", "098", "097"}
# life = {"063", "093"}

# phone = input("Введіть номер телефону у форматі '+38 (050) 123-45-55': ")
# op_code = phone[5:8]

# if op_code in vodafone:
#     print("Ваш оператор 'Vodafone'")
# elif op_code in kyivstar:
#     print("Ваш оператор 'Kyivstar'")
# elif op_code in life:
#     print("Ваш оператор 'LifeCell'")
# else:
#     print("Невідомий оператор")






# Множини

### Створити множину




### Додати до неї новий елемент



### Видалити елемент з виключенням



### Видалити елемент з множини не викликаючи виключення









# Дано список клієнтів, які купили товар А та список клієнтів, які купили товар В.
# Знайти:
# - клієнтів, які купили обидва товари А і B
# - створити один список клієнтів, шляхом операції об’єднання

# pencil = {"Андрій", "Дмитро", "Іван", "Вадим", "Максима"}
# pen = {"Леонід", "Дмитро", "Нікіта", "Вадим"}

# print(pencil & pen)
# print(pencil.intersection(pen))
# print(pencil ^ pen)
# print(pen.difference(pencil))
# print(pencil | pen)
# print(pencil.union(pen))





# Створіть список з чисел від 1 до 10 та використайте зрізи для виводу елементів від другого до п'ятого включно.








# Створіть рядок та використайте зрізи для виводу перших трьох та останніх трьох символів.







# Визначи, чи порядок значень у запропонованому списку є строго зростаючим
# my_list = [4, 5, 6, 7, 3, 7, 9]







# Створіть список зі стрічок та використайте зрізи для виводу останніх трьох символів з кожної стрічки.








# Створіть програму, яка приймає від користувача рядок і перевіряє чи є він паліндромом
# (слово, яке читається однаково зліва направо та справа наліво).
# Виведіть результат у вигляді логічного значення (True або False).









# Створіть програму, яка приймає від користувача дві строки та перевіряє,
# чи є вони анаграмами (слова, у яких ті самі літери, але в різному порядку).
# Виведіть результат у вигляді логічного значення (True або False).





# Створіть список зі стрічок та використайте зрізи для виводу символів з кожної стрічки у зворотньому порядку.









# Створіть програму, яка перевіряє чи рядок включає в собі лише цифри.







# Створіть програму, яка приймає рядок, та повертає рядок, з якого було видалено всі пробіли.






# Створіть множину та перевірте, чи є вона підмножиною іншої множини.
# a = set(range(10))
# b = set(range(5, 10))

# c = a | b
# print(a == c)