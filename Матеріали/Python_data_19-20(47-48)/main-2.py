# Навіщо потрібне сортування?

# 1. Коли дані відсортовані, можна застосувати
#     ефективні методи пошуку (наприклад, бінарний пошук),
#     що значно швидше за лінійний.
# 2. У відсортованому вигляді дані легше
#     переглядати, групувати, виявляти закономірності чи аномалії.
# 3. Деякі алгоритми (злиття структур, перебір
#     даних, унікальні операції) суттєво пришвидшуються,
#     якщо вхідні дані впорядковані.



# ЗАВДАННЯ 1
# Реалізуйте алгоритм пузиркового сортування для списку цілих чисел у зростальному порядку.

# Створіть функцію bubble_sort(arr), яка приймає список arr.
# Виконайте максимум n−1 проходів по списку, де n — довжина arr
# На кожному проході порівнюйте сусідні елементи й обмінюйте їх, якщо arr[j] > arr[j+1].
# Виведіть відсортований список.


# def bubble_sort(arr: list):
#     # Допишіть цикли порівняння і обміну для сусідів
#     for i in range(len(arr)):
#         for i in range(len(arr)-i-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#     return arr

# numbers = [5, 2, 9, 1, 7]
# bubble_sort(numbers)
# print(numbers)
# ---------------------------------------------------

# Завдання 2
# Доповніть базову реалізацію так, щоб після кожного
# проходу зовнішнього циклу виводилося проміжне
# значення списку. Це допоможе побачити процес «спливання» найбільших елементів.
# Після завершення кожного проходу виводити: print(f"Після проходу {i+1}: {arr}").
# Переконайтеся, що можна візуально простежити, як найбільші числа опиняються у кінці.


# def bubble_sort_steps(arr):
    # цикл від 0 до n-1
        # внутрішній цикл: порівнюємо сусідів
        # після завершення внутрішнього циклу: друк arr
#     for i in range(len(arr)):
#         for i in range(len(arr)-i-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#         print(arr)
#     return arr

# nums = [5, 2, 9, 1, 7]
# bubble_sort_steps(nums)
# ---------------------------------------------------


# ЗАВДАННЯ 3
# Змініть базовий алгоритм так, щоб список сортувався
# у спадному порядку (від більшого до меншого).

# Використайте такий самий цикл, але тепер
# при порівнянні (arr[j] < arr[j+1]) робіть обмін.
# Перевірте на різних прикладах.


# def bubble_sort_desc(arr):
#     pass
#     for i in range(len(arr)):
#         for i in range(len(arr)-i-1):
#             if arr[i] < arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#         print(arr)
#     return arr

# test_list = [3, 8, 2, 7, 1]
# bubble_sort_desc(test_list)
# print(test_list)
# ---------------------------------------------------


# ЗАВДАННЯ 4
# Додайте змінну swapped, яка відстежує, чи був
# хоч один обмін на поточному проході. Якщо
# жодного обміну не було — алгоритм може завершитися
# достроково, бо список уже впорядкований.

# На початку кожного проходу встановлюйте swapped = False.
# Якщо здійснено хоча б один обмін, swapped = True.
# Після внутрішнього циклу, якщо swapped == False, використайте break для припинення.


# def bubble_sort_optimized(arr):
#     pass
#     for i in range(len(arr)):
#         swapped = False
#         for i in range(len(arr)-i-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swapped = True

#         print(arr)
#         if not swapped:
#             return arr
#     return arr

# numbers = [2, 3, 4, 5, 6]
# bubble_sort_optimized(numbers)
# print(numbers)
# ---------------------------------------------------


# Завдання 5
# Напишіть варіацію алгоритму, яка під час сортування
# підраховує загальну кількість обмінів та виводить це число після завершення.

# Введіть лічильник count_swaps = 0.
# Щоразу, коли робите перестановку (arr[j], arr[j+1]),
# збільшуйте count_swaps += 1.
# Після завершення сортування виведіть:
# print("Загальна кількість обмінів:", count_swaps).

# def bubble_sort_with_count(arr):
#     pass
#     swapped_count = 0
#     for i in range(len(arr)):
#         swapped = False
#         for i in range(len(arr)-i-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swapped = True
#                 swapped_count += 1

#         print(arr)
#         if not swapped:
#             break
#     print(f"{swapped_count = }")
#     return arr

# data = [4, 3, 2, 1]
# bubble_sort_with_count(data)
# print(data)
# ---------------------------------------------------


# Завдання 6
# Уявімо, що маємо список словників ({'name': 'Alice', 'age': 30})
# і хочемо відсортувати за ключем 'age'.
# Використайте адаптацію Bubble Sort: порівнювати arr[j]['age'] та arr[j+1]['age'].

# Створіть список словників зі ключем 'age'.
# Реалізуйте bubble_sort_by_age(people), де порівняння здійснюється через people[j]['age'].
# Перевірте, що після сортування список розташований від найменшого age до найбільшого.


# def bubble_sort_by_age(people):
#     pass
#     swapped_count = 0
#     for i in range(len(people)):
#         swapped = False
#         for i in range(len(people)-i-1):
#             if people[i]["age"] > people[i+1]["age"]:
#                 people[i], people[i+1] = people[i+1], people[i]
#                 swapped = True
#                 swapped_count += 1

#         print(people)
#         if not swapped:
#             break
#     print(f"{swapped_count = }")
#     return people

# people_data = [
#     {'name': 'Bob', 'age': 25},
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Charlie', 'age': 20}
# ]
# bubble_sort_by_age(people_data)
# print(people_data)
# ---------------------------------------------------


# ЗАВДАННЯ 7
# Зробіть алгоритм, який після кожного
# обміну друкує стан списку. Це ще детальніше
# покаже весь процес «бульбашкового» підйому.

# Коли виконуєте arr[j], arr[j+1] = arr[j+1], arr[j],
# одразу робіть print(arr).
# Переконайтеся, що виводиться багато проміжних списків.


# def bubble_sort_verbose(arr):
#     pass
#     swapped_count = 0
#     for i in range(len(arr)):
#         swapped = False
#         for i in range(len(arr)-i-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 print(arr)
#                 swapped = True
#                 swapped_count += 1

#         if not swapped:
#             break
#     print(f"{swapped_count = }")
#     return arr

# nums = [5, 1, 4, 2, 8]
# bubble_sort_verbose(nums)
# ---------------------------------------------------


# ЗАВДАННЯ 8
# Після першого проходу найбільший елемент
# опиняється в кінці. Після другого — два найбільші.
# Зробіть так, щоб кожен наступний прохід на 1 елемент коротший.
# Тобто, на i-й ітерації внутрішній цикл має доходити лише до n - i - 1.

# Реалізуйте це в алгоритмі й перевірте, чи він працює коректно.
# Порівняйте з “повним” варіантом, де проходять до кінця.


# def bubble_sort_shortening(arr):
#     pass
#     swapped_count = 0
#     for i in range(len(arr)):
#         swapped = False
#         for i in range(len(arr)-i-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 print(arr)
#                 swapped = True
#                 swapped_count += 1

#         if not swapped:
#             break
#     print(f"{swapped_count = }")
#     return arr

# data = [4, 3, 2, 1, 5, 6]
# bubble_sort_shortening(data)
# print(data)