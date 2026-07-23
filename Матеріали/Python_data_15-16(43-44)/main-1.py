# 🔑 Чотири властивості алгоритму
# Щоб послідовність дій називалась алгоритмом, вона повинна мати чотири властивості:
# 1. Скінченність (Finiteness). Алгоритм завжди завершується.
# 2. Визначеність (Definiteness). Кожен крок однозначний і зрозумілий.
# 3. Результативність (Effectiveness). Алгоритм завжди дає результат.
# 4. Масовість (Generality). Алгоритм працює для різних вхідних даних.

# Алгоритм Дейкстри (Dijkstra's Algorithm)
# import heapq

# def dijkstra(graph, start):
#     queue = []
#     heapq.heappush(queue, (0, start))
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0

#     while queue:
#         current_distance, current_vertex = heapq.heappop(queue)

#         if current_distance > distances[current_vertex]:
#             continue

#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight

#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(queue, (distance, neighbor))

#     return distances


# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }

# print(dijkstra(graph, "A"))


# Лінійний vs Бінарний пошук
# import random, time

# def linear_search(arr, x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1


# def binary_search(arr, x):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return mid


# size = 10000000
# data = sorted([random.randint(1, 1000000000) for _ in range(size)])
# target = random.choice(data)

# start_time = time.time()
# linear_search(data, target)
# linear_time = time.time() - start_time

# start_time = time.time()
# binary_search(data, target)
# binary_time = time.time() - start_time


# print(f"Лінійний пошук: {linear_time:.6f} секунд")
# print(f"Бінарний пошук: {binary_time:.100f} секунд")
# print(f"Бінарний швидший у {linear_time/binary_time:.0f} разів")


# Завдання 1. Визначення алгоритмів
# Для кожної ситуації визначте, чи є це алгоритмом. Якщо ні — поясніть, якої властивості не вистачає.
    # Рецепт приготування піци з чіткими кроками -> Так, це алгоритм.
    # "Зробіть щось цікаве" -> Ні, не вистачає визначеності.
    # Інструкція зі складання меблів IKEA -> Так, це алгоритм.
    # "Порахуйте всі прості числа" (без обмежень) -> Ні, не вистачає скінченності.
    # Функція len() в Python -> Так, це алгоритм.


# Завдання 3. Визначення Big O
# Визначте складність кожного фрагмента коду:

# Фрагмент A: -> O(1)
# def get_first(arr):
#     return arr[0]


# Фрагмент B: -> O(n)
# def find_max(arr):
#     max_val = arr[0]
#     for x in arr:
#         if x > max_val:
#             max_val = x
#     return max_val

# Фрагмент C: -> O(n^2)
# def has_duplicates(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i != j and arr[i] == arr[j]:
#                 return True
#     return False

# Фрагмент D: -> O(log n)
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


# Завдання 4. Порівняння сортувань
# Порівняйте Bubble Sort та вбудований sorted():
# import time
# import random

# def bubble_sort(arr):
#     n = len(arr)
#     arr = arr.copy()
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# # Тестуємо на різних розмірах
# for size in [100, 1000, 5000]:
#     data = [random.randint(1, 10000) for _ in range(size)]

#     start = time.time()
#     bubble_sort(data)
#     bubble_time = time.time() - start

#     start = time.time()
#     sorted(data)
#     sorted_time = time.time() - start

#     print(f"Розмір {size}:")
#     print(f"  Bubble Sort: {bubble_time:.4f} сек")
#     print(f"  sorted():    {sorted_time:.6f} сек")
#     print(f"  Різниця: {bubble_time/sorted_time:.0f}x")
#     print()

# Питання: -> O(n^2) та O(n log n)
# Чому різниця зростає при збільшенні розміру?
# Яку складність має Bubble Sort? А sorted()?


# Завдання 6.  Визначення Big O
# Для кожної функції визначте Big O та поясніть чому:

# Функція 1 -> O(n)
def sum_list(arr):
    total = 0
    for x in arr:
        total += x
    return total

# Функція 2 -> O(1)
def first_and_last(arr):
    return arr[0], arr[-1]

# Функція 3 -> O(n^2)
def all_pairs(arr):
    pairs = []
    for i in arr:
        for j in arr:
            pairs.append((i, j))
    return pairs

# Функція 4 -> O(log n)
def half_search(arr, target):
    while len(arr) > 0:
        mid = len(arr) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            arr = arr[mid+1:]
        else:
            arr = arr[:mid]
    return False


# Завдання 5. Оптимізація Big O
# Оптимізуйте код, щоб покращити Big O:

# Неоптимізований код -> O(n^2)
# def contains_duplicates_bad(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] == arr[j]:
#                 return True
#     return False

# # Оптимізований код -> O(n)
# def contains_duplicates_good(arr):
#     seen = set()
#     for x in arr:
#         if x in seen:
#             return True
#         seen.add(x)
#     return False
