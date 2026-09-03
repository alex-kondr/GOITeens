# Regex — інструмент для пошуку, заміни та валідації
# текстових шаблонів, який дозволяє працювати з
# шаблонами для знаходження складних послідовностей символів.

# Основні функції:

# re.search(): шукає перше входження шаблону у рядок.
# re.match(): перевіряє відповідність початку рядка заданому шаблону.
# re.findall(): повертає список всіх входжень шаблону.
# re.sub(): замінює входження шаблону на інший рядок.
# re.split(): розбиває рядок за заданим шаблоном.

# import re
# match = re.search(r"abc", "123abc456")
# if match:
#     print("Знайдено:", match.group())


# import re
# results = re.findall(r"\d+", "My numbers are 123 and 4567")
# print("Найдені числа:", results)


# import re
# match = re.search(r"(\d{3})-(\d{2})-(\d{4})", "Contact: 123-45-6789")
# if match:
#     print("Цілий шаблон:", match.group(0))
#     print("Групи:", match.groups())


# . — будь-який символ (крім символу нового рядка).
# \d — цифра.
# \w — літера, цифра або підкреслення.
# \s — пробіл.
# , +, ? — квантифікатори (0 або більше, 1 або більше, 0 або 1 відповідно).
# {n}, {n,m} — точна кількість або діапазон повторень.
# ^ та $ — початок та кінець рядка.


# Методи rfind() та rindex()


# алгоритм Бойера–Мура
def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    bad_char_shift = {}
    for index, char in enumerate(pattern):
        bad_char_shift[char] = index

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            shift = max(1, j - bad_char_shift.get(text[s + j], -1))
            s += shift
    return -1


# text = "HERE IS A SIMPLE EXAMPLE"
# pattern = "EXAMPLE"
# index = boyer_moore_search(text, pattern)
# print(f"Підрядок '{pattern}' знайдено на позиції: {index}")


# Завдання 2
# Реалізуйте функцію bm_search_all(text, pattern),
# яка знаходить всі входження зразка в тексті за
# алгоритмом Бойера–Мура та повертає список індексів.
# Початковий код:

# def bm_search_all(text, pattern):
#     occurrences = []
#     # Побудуйте таблицю для "поганого символу" для pattern
#     # Виконайте пошук по тексту за алгоритмом Бойера–Мура, додаючи кожен знайдений індекс до occurrences
#     pass


# Завдання 3
# Реалізуйте функцію bm_vs_naive(text, pattern),
# яка порівнює час виконання пошуку зразка у тексті
# за допомогою наївного алгоритму та алгоритму
# Бойера–Мура. Функція повинна виводити отримані
# індекси та час пошуку для кожного методу.
# Початковий код:

# import time

# def naive_search(text, pattern):
#     # Реалізуйте наївний алгоритм пошуку підрядка
#     pass

# def bm_search(text, pattern):
#     # Використовуйте алгоритм Бойера–Мура (без додаткових функцій)
#     pass

# # Створіть великий текст для тестування
# text = "SAMPLE TEXT " * 1000
# pattern = "TEXT"
# # Виміряйте час для наївного пошуку та BM
# pass

# # Виведіть результати



# Завдання 4
# Реалізуйте функцію bm_search_with_log(text, pattern),
# яка виконує пошук зразка в тексті за алгоритмом Бойера–Мура
# та веде лог зсувів, що виконуються під час пошуку.
# Функція повинна повертати кортеж (index, log), де log — список значень зсувів, які застосовуються.
# Початковий код:

# def bm_search_with_log(text, pattern):
#     log = []
#     # Побудуйте таблицю для "поганого символу" для pattern
#     # Виконайте пошук за алгоритмом Бойера–Мура, записуючи кожен зсув у log
#     # Якщо зразок знайдено, поверніть (індекс, log)
#     pass



# Алгоритм Рабіна–Карпа є алгоритмом пошуку
# підрядків, який використовує хешування
# для ефективного порівняння зразка з підрядками тексту.

def rabin_karp_with_count(text, pattern):
    count = 0
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0, count

    d = 256
    q = 101
    h = pow(d, m - 1, q)
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
        count += 2

    for s in range(n - m + 1):
        count += 1
        if p == t:
            if text[s:s+m] == pattern:
                return s, count

        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
            count += 1
    return -1, count


# Завдання 2
# Реалізуйте функцію rabin_karp_search_all(text, pattern),
# яка знаходить усі входження зразка в тексті за алгоритмом
# Рабіна–Карпа і повертає список індексів.
# Початковий код:

# def rabin_karp_search_all(text, pattern):
#     occurrences = []
#     # Ініціалізуйте необхідні змінні та таблицю хешування
#     # Виконайте пошук за алгоритмом Рабіна–Карпа, додаючи кожен знайдений індекс до occurrences
#     pass


# Завдання 3
# Реалізуйте функцію rabin_karp_with_log(text, pattern),
# яка виконує пошук зразка за алгоритмом Рабіна–Карпа
# та записує лог обчислених хешів для кожного зсуву.
# Функція повинна повертати кортеж (index, log),
# де log — список хешів підрядків тексту на кожному кроці.
# Початковий код:

# def rabin_karp_with_log(text, pattern):
#     log = []
#     # Ініціалізуйте необхідні змінні, обчисліть хеш зразка та першого підрядка text
#     # Під час кожного зсуву додайте обчислений хеш до log
#     # Якщо зразок знайдено, поверніть (індекс, log)
#     pass


# Бібліотека NumPy

# import numpy as np

# text = "The quick brown fox jumps over the lazy dog"
# text_array = np.array(list(text))

# indices = np.where(text_array == 'o')[0]
# print("Індекси входження символу 'o':", indices)

# import numpy as np

# def vectorized_find(text, substring):
#     n = len(text)
#     m = len(substring)
#     if m == 0:
#         return 0
#     text_array = np.array(list(text))
#     pattern_array = np.array(list(substring))
#     candidates = np.array([text_array[i:i+m] for i in range(n - m + 1)])
#     match = np.all(candidates == pattern_array, axis=1)
#     indices = np.where(match)[0]
#     return indices[0] if indices.size > 0 else -1

# text = "Data science and machine learning often involve text processing."
# substring = "machine"
# result = vectorized_find(text, substring)
# print("Перший індекс входження 'machine':", result)


# За допомогою re.find() шукаємо
# шаблон HTML-тегів і замінюємо їх на порожній рядок:

# import re

# def clean_html(text):
#     clean_text = re.sub(r'<[^>]+>', '', text)
#     return clean_text

# sample_text = "<div>Hello, world!</div> This is a test."
# print(clean_html(sample_text))

# import re

# def extract_phone_numbers(text):
#     pattern = r'\\b\\d{3}[-.\\s]??\\d{3}[-.\\s]??\\d{4}\\b'
#     return re.findall(pattern, text)

# sample_text = "Call me at 415-555-1234 or 415.555.5678!"
# print("Телефонні номери:", extract_phone_numbers(sample_text))


# Перевіряємо наявність keyword у кожному рядку логів за допомогою str.find():

# def filter_logs(logs, keyword):
#     return [log for log in logs if log.find(keyword) != -1]

# sample_logs = [
#     "Process started successfully.",
#     "Warning: Memory usage high.",
#     "Error: Unable to open file.",
#     "Process failed due to timeout."
# ]
# filtered = filter_logs(sample_logs, "fail")
# print("Логи з 'fail':", filtered)



# def count_occurrences(text, substring):
#     count = 0
#     pos = text.find(substring)
#     while pos != -1:
#         count += 1
#         pos = text.find(substring, pos + 1)
#     return count

# review = "The product is good, very good, and extremely good!"
# frequency = count_occurrences(review.lower(), "good")
# print("Частота появи 'good':", frequency)


# Додаємо стовпець з інформацією про наявність слова 'learning':

# import pandas as pd

# data = {
#     'article': [
#         "Deep learning techniques are revolutionizing computer vision.",
#         "Financial markets rely on predictive analytics.",
#         "Advances in natural language processing are remarkable."
#     ]
# }
# df = pd.DataFrame(data)

# df['contains_learning'] = df['article'].str.find("learning") != -1
# print(df)