# На початку визначаються два індекси: left – початковий (зазвичай 0)
# та right – кінцевий (останній індекс масиву)
# Далі розраховують середній індекс за формулою mid = (left + right) // 2.
# Значення елемента за індексом mid порівнюють з шуканим значенням:
# Якщо елемент співпадає з шуканим, алгоритм завершується, повертаючи позицію mid.
# Якщо шуканий елемент менший за центральний, логічно, що потрібний
# елемент може бути лише у лівій половині масиву. Тоді змінюють right на mid - 1.
# Якщо шуканий елемент більший, то нова область пошуку – права половина: встановлюють left як mid + 1.
# [1, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1



# ЗАВДАННЯ 1
# Реалізуйте функцію iterative_binary_search(arr, target),
# яка здійснює ітеративний бінарний пошук у впорядкованому
# списку. Функція має підраховувати кількість порівнянь
# і повертати кортеж (index, comparisons), де index —
# індекс знайденого елемента (або -1, якщо елемент не знайдено).

# Початковий код:

# def iterative_binary_search(arr, target):
#     comparisons = 0  # Лічильник порівнянь
#     low = 0
#     high = len(arr) - 1
#     # Поки low <= high:
#     #     Обчисліть mid = (low + high) // 2
#     #     Збільшіть comparisons на 1
#     #     Якщо arr[mid] == target, поверніть (mid, comparisons)
#     #     Якщо arr[mid] < target, оновіть low = mid + 1, інакше high = mid - 1
#     # Якщо пошук не дав результату, поверніть (-1, comparisons)
#     pass

# data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# result = iterative_binary_search(data, 14)
# print("Результат пошуку 14:", result)


# ЗАВДАННЯ 2
# Реалізуйте рекурсивну функцію
# recursive_binary_search_log(arr, target, low=0, high=None, log=None),
# яка, окрім пошуку, зберігає у список лог (LIFO‑стек) усіх
# проміжних значень mid. Функція повертає кортеж (index, log).
# Початковий код:

# def recursive_binary_search_log(arr, target, low=0, high=None, log=None):
#     # Якщо high не задано, встановіть його рівним len(arr)-1
#     # Якщо log не задано, ініціалізуйте його як порожній список
#     # Якщо low > high, поверніть (-1, log)
#     # Обчисліть mid = (low + high) // 2 та додайте його до log
#     # Якщо arr[mid] == target, поверніть (mid, log)
#     # Якщо arr[mid] < target, рекурсивно викликайте функцію для правої половини
#     # Інакше – для лівої половини
#     pass

# sorted_list = [3, 7, 11, 15, 19, 23, 27, 31]
# index, log = recursive_binary_search_log(sorted_list, 19)
# print(f"Елемент 19 знайдено на позиції {index}")
# print("Лог індексів:", log)


# ЗАВДАННЯ 3
# Реалізуйте функцію
# binary_search_insertion_index(arr, target),
# яка знаходить позицію для вставки нового елемента
# target у відсортований список arr. Потім створіть функцію
# insert_with_binary_search(arr, target),
# яка вставляє елемент у знайдену позицію та повертає оновлений список.

# Початковий код:

# def binary_search_insertion_index(arr, target):
#     low = 0
#     high = len(arr)
#     # Використовуйте цикл while для знаходження позиції, де arr[mid] >= target
#     # Поверніть low як позицію для вставки
#     pass

# def insert_with_binary_search(arr, target):
#     # Використовуйте binary_search_insertion_index для знаходження позиції
#     # Вставте target у список за цією позицією та поверніть оновлений список
#     pass

# sorted_list = [2, 5, 8, 12, 16, 23, 38]
# new_list = insert_with_binary_search(sorted_list.copy(), 15)
# print("Оновлений список після вставки 15:", new_list)


