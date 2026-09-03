# ЗАВДАННЯ 1
# Реалізуйте просту функцію find_substring(text, substring),
# яка використовує вбудований метод find() для пошуку першого входження підрядка у рядок.
# Початковий код:

# def find_substring(text, substring):
#     # тут
#     pass

# text = "Hello, welcome to Python programming!"
# result = find_substring(text, "Python")
# print("Перший індекс входження 'Python':", result)


# ЗАВДАННЯ 2
# Реалізуйте функцію find_substring_range(text, substring, start, end),
# яка знаходить позицію підрядка, обмежуючи область пошуку параметрами start та end.
# Початковий код:

# def find_substring_range(text, substring, start, end):
#     # тут
#     pass

# text = "banana"
# result = find_substring_range(text, "na", 2, 5)
# print("Позиція 'na' в тексті 'banana' у діапазоні 2-5:", result)


# ЗАВДАННЯ 3
# Реалізуйте функцію find_all_occurrences(text, substring),
# яка повертає список усіх позицій, де входить заданий підрядок у тексті, використовуючи метод find().
# Початковий код:

# def find_all_occurrences(text, substring):
#     indices = []
#     # ось тут
#     pass

# text = "abracadabra"
# result = find_all_occurrences(text, "abra")
# print("Усі позиції входження 'abra':", result)


# ЗАВДАННЯ 4
# Реалізуйте функцію custom_find(text, substring), яка імітує роботу методу find()
# за допомогою циклу (без використання вбудованого методу).
# Функція має повертати індекс першого входження або -1, якщо підрядок не знайдено.
# Початковий код:

# def custom_find(text, substring):
#     # ось тут
#     pass

# text = "Hello, world!"
# result = custom_find(text, "world")
# print("Перший індекс входження 'world':", result)

# def custom_find(text, substring):
#     n = len(text)
#     m = len(substring)
#     for i in range(n - m + 1):
#         if text[i:i+m] == substring:
#             return i
#     return -1


# Алгоритм Кнута–Морріса–Пратта (КМП)
# O(n + m): Де n – довжина тексту, m – довжина зразка. Обчислення
# префікс-функції займає O(m) часу, а сам пошук – O(n). Це значно
# ефективніше, ніж наївний підхід, який може мати часову
# складність O(n·m) у найгіршому випадку.


def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]

        if pattern[k] == pattern[q]:
            k += 1

        pi[q] = k

    return pi


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    pi = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]

        if pattern[q] == text[i]:
            q += 1

        if q == m:
            return i - m + 1
    return -1


# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# index = kmp_search(text, pattern)
# print(f"Підрядок '{pattern}' знайдено на позиції: {index}")


# ЗАВДАННЯ 5
# Реалізуйте функцію kmp_search_all(text, pattern),
# яка знаходить всі входження зразка в тексті за
# алгоритмом КМП та повертає список індексів цих входжень.
# Початковий код:

# def kmp_search_all(text, pattern):
#     occurrences = []
#     # Реалізуйте алгоритм КМП для знаходження всіх входжень зразка в тексті
#     # Додайте кожен знайдений індекс у список occurrences
#     pass

# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# result = kmp_search_all(text, pattern)
# print("Усі входження зразка:", result)


# Завдання 6
# Реалізуйте функцію kmp_search_with_log(text, pattern),
# яка виконує пошук зразка в тексті за алгоритмом КМП і
# зберігає лог (список проміжних значень q або позицій)
# кожного кроку. Функція повинна повертати кортеж
# (index, log), де index — індекс першого входження зразка, а log — список проміжних значень q.
# Початковий код:

# def kmp_search_with_log(text, pattern):
#     log = []  # Список для збереження проміжних значень
#     # Ініціалізуйте змінні n, m, q та обчисліть префікс-функцію pi для pattern
#     # Ітеруйтеся по тексту, оновлюючи q, і додавайте значення q до log
#     # Якщо q дорівнює m, поверніть (індекс, log)
#     pass

# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# index, log = kmp_search_with_log(text, pattern)
# print("Підрядок знайдено на позиції:", index)
# print("Лог проміжних значень:", log)


# Завдання 7
# Створіть скрипт для порівняння продуктивності
# наївного пошуку підрядка (через цикл ізпорівняннями)
# та алгоритму Кнута–Моррі–Пратта. Для цього
# використайте великий текст та повторіть пошук
# одного й того ж зразка за допомогою обох методів, вимірюючи час виконання.
# Початковий код:

# import time

# def naive_search(text, pattern):
#     n = len(text)
#     m = len(pattern)
#     for i in range(n - m + 1):
#         if text[i:i+m] == pattern:
#             return i
#     return -1

# # Використайте функцію kmp_search з Завдання 2

# # Завантажте великий текст (наприклад, повторіть короткий текст кілька тисяч разів)
# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 1000
# pattern = "consectetur"

# start_time = time.time()
# naive_result = naive_search(text, pattern)
# naive_time = time.time() - start_time

# start_time = time.time()
# kmp_result = kmp_search(text, pattern)
# kmp_time = time.time() - start_time

# print(f"Наївний пошук: індекс = {naive_result}, час = {naive_time:.6f} секунд")
# print(f"КМП: індекс = {kmp_result}, час = {kmp_time:.6f} секунд")



# Завдання 8
# Реалізуйте функцію kmp_search_with_prefix_table(text, pattern),
# яка виконує пошук підрядка за алгоритмом КМП і повертає кортеж
# (index, pi), де pi – таблиця префікс‑функції для зразка.
# Це допоможе проаналізувати, як обчислюється префікс‑функція
# та як вона використовується для прискорення пошуку.
# Початковий код:

# def kmp_search_with_prefix_table(text, pattern):
#     # Обчисліть довжини тексту та зразка
#     # Якщо зразок порожній, поверніть (0, [])
#     # Обчисліть таблицю префікс‑функції для pattern
#     # Виконайте пошук з використанням таблиці pi та поверніть (індекс, pi)
#     pass

# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# index, pi = kmp_search_with_prefix_table(text, pattern)
# print(f"Підрядок знайдено на позиції: {index}")
# print("Таблиця префікс-функції:", pi)