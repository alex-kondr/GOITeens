def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > curr:
                arr[j+1] = arr[j]
            else:
                j += 1
                break

        arr[j] = curr


# arr = [9, 4, 2, 7, 1, 6, 3]
# insertion_sort(arr)
# print(arr)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current


# ------------------------------------------------------------------
# ЗАВДАННЯ 1
# Змініть алгоритм сортування вставками так,
# щоб він відсортував список у спадному порядку (від більшого до меншого).

# При кожному кроці порівняйте поточний елемент з
# попередніми, але використайте логіку, при якій
# поточний елемент буде вставлено до тих, що менші за нього.
# Модифікуйте умову в циклі while відповідно.

# def insertion_sort_desc(arr):
#     n = len(arr)
#     for i in range(1, n):
#         current = arr[i]
#         j = i - 1
#         while j >= 0 and current > arr[j]:
#             # Додайте свій код тут: змістіть arr[j] вправо
#             j -= 1
#         # Вставте current на позицію j+1
#         # Додайте свій код тут

# test_list = [10, 3, 15, 7, 8, 23, 74, 18]
# insertion_sort_desc(test_list)
# print(test_list)
# ------------------------------------------------------------------

# ЗАВДАННЯ 2
# Додайте лічильник, який підраховує кількість порівнянь,
# що виконуються під час сортування вставками.

# Ініціалізуйте змінну count_comp = 0 перед внутрішнім циклом.
# Під час кожного порівняння у циклі while збільшуйте count_comp на 1.
# Після завершення сортування виведіть значення count_comp.

# def insertion_sort_with_comparisons(arr):
#     count_comp = 0
#     n = len(arr)
#     for i in range(1, n):
#         current = arr[i]
#         j = i - 1
#         while j >= 0 and current < arr[j]:
#             # Додайте збільшення count_comp
#             ...
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = current
#     # Додайте вивід count_comp
#     ...

# data = [12, 4, 7, 1, 9, 3, 6, 5]
# insertion_sort_with_comparisons(data)
# print(data)
# ------------------------------------------------------------------

# ЗАВДАННЯ 3
# Модифікуйте алгоритм сортування вставками для
# підрахунку кількості "зсувів" (кількість переміщень елементів) під час сортування.

# Ініціалізуйте змінну count_shifts = 0 перед внутрішнім циклом.
# Кожного разу, коли виконується присвоєння в циклі while
# (тобто, коли елемент зсувається вправо), збільшуйте count_shifts на 1.
# Після завершення сортування виведіть загальну кількість зсувів.

# def insertion_sort_with_shifts(arr):
#     count_shifts = 0
#     n = len(arr)
#     for i in range(1, n):
#         current = arr[i]
#         j = i - 1
#         while j >= 0 and current < arr[j]:
#             # Додайте збільшення count_shifts
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = current
#     # Виведіть count_shifts

# data = [12, 4, 7, 1, 9, 3, 6, 5]
# insertion_sort_with_shifts(data)
# print(data)
# ------------------------------------------------------------------

# ЗАВДАННЯ 4
# Реалізуйте сортування вставками для списку
# словників за певним ключем (наприклад, 'score').

# Створіть функцію insertion_sort_by_key(data, key),
# яка приймає список словників та ключ для сортування.
# Порівнюйте значення словників за цим ключем у циклі while.
# Переконайтеся, що список словників відсортовано за зростанням значень для заданого ключа.

# def insertion_sort_by_key(data, key):
#     n = len(data)
#     for i in range(1, n):
#         current = data[i]
#         j = i - 1
#         # Поки j >= 0 і значення за ключем у current менше, ніж у data[j]
#         while j >= 0 and current[key] < data[j][key]:
#             # Додайте свій код тут: перемістіть data[j] вправо
#             ...
#             j -= 1
#         # Вставте current на позицію j+1
#         # Додайте свій код тут
#         ...

# players = [
#     {'name': 'Alice', 'score': 50},
#     {'name': 'Bob', 'score': 20},
#     {'name': 'Charlie', 'score': 50},
#     {'name': 'David', 'score': 10}
# ]
# insertion_sort_by_key(players, 'score')
# print(players)
# ------------------------------------------------------------------


# ШВИДКЕ СОРТУВАННЯ
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[-1]
#     left = []
#     right = []
#     for i in range(len(arr)-1):
#         if arr[i] <= pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])

#     return quick_sort(left) + [pivot] + quick_sort(right)

# arr = [8, 2, 7, 9, 1, 3, 5, 4]
# print(quick_sort(arr))
# ------------------------------------------------------------------

# ЗАВДАННЯ 2
# Розширте реалізацію алгоритму швидкого сортування,
# щоб після кожного розбиття (partition) виводився поточний стан списку.
# ------------------------------------------------------------------

# ЗАВДАННЯ 3
# Змініть алгоритм швидкого сортування так, щоб
# список сортувався у спадному порядку (від більшого до меншого).
