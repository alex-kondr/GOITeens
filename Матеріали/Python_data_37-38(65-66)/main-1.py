# Жадібні алгоритми працюють за принципом вибору на кожному кроці рішення, яке здається найкращим в даній ситуації


# ПРАКТИЧНЕ ЗАВДАННЯ 1
# Касир має монети: 10, 5, 2, 1 грн. Потрібно видати решту 23 грн,
# використавши якомога менше монет. Натискай на найбільшу монету, яка підходить!

# result = []
# def change(coins,amount):
# pass

# print(change([10,5,2,1], 23))

# Правильний код
# result = []
# def change(coins,amount):
#     if amount == 0:
#         return result
#     else:
#         coin = max(list(filter(lambda x: x <= amount, coins)))
#         amount = amount - coin
#         result.append(coin)
#         return change(coins,amount)

# print(change([10,5,2,1], 23))


# ПРАКТИЧНЕ ЗАВДАННЯ 2
# Атракціон працює 10 хвилин, і є кілька дітей з різною тривалістю катання.
# Жадібна ідея: спочатку запускаємо тих, хто займає найменше
# часу — так встигнемо прокатати максимальну кількість дітей.

# kids = [("Аня",1),
#         ("Варя",3),
#         ("Денис",4),
#         ("Гриша",3),
#         ("Єва",5),
#         ("Бодя",2)]
# def greed_amount(kids,time):
# pass

# print(greed_amount(kids,10))

# Правильний код
# kids = [("Аня",1),
#         ("Варя",3),
#         ("Денис",4),
#         ("Гриша",3),
#         ("Єва",5),
#         ("Бодя",2)]

# def greed_amount(kids,time):
#     result = 0
#     kids_filtered = sorted(kids,key=lambda x:x[1])
#     print(kids_filtered)
#     for x in kids_filtered:
#         if time > x[1]:
#             time -= x[1]
#             print(time)
#             result += 1
#     return result
# print(greed_amount(kids,10))


# Отже, для суми 37 необхідно 4 монети: 25, 10, 1, 1
# def coin_change_greedy(amount, coins):
#     coins.sort(reverse=True)
#     result = []
#     for coin in coins:
#         while amount >= coin:
#             amount -= coin
#             result.append(coin)
#     if amount == 0:
#         return result
#     else:
#         return None

# print(coin_change_greedy(37, [25,10,5,1]))




# 🟢 Жадібні алгоритми — 15 Легких Задач із Розв'язками
# Жадібний алгоритм — це стратегія розв'язання задач, при якій на кожному кроці робиться локально найкращий вибір, без перегляду попередніх рішень.

# Задача 1 — Решта монетами
# Умова: Маємо монети номіналом [1, 5, 10, 25] копійок. Потрібно видати суму N копійок мінімальною кількістю монет.

# Вхід: N = 41
# Вихід: [25, 10, 5, 1] → 4 монети

# python

# def change(n, coins=[25, 10, 5, 1]):
#     result = []
#     for coin in coins:
#         while n >= coin:
#             result.append(coin)
#             n -= coin
#     return result
# print(change(41))  # [25, 10, 5, 1]


# Задача 2 — Максимальна кількість активностей
# Умова: Є список заходів із часом початку та кінця. Вибери максимальну кількість заходів, що не перетинаються.

# Вхід: [(1,3), (2,5), (3,9), (6,8)]
# Вихід: [(1,3), (3,9)] або [(1,3), (6,8)] → 2 заходи... (але жадібно → 3!)

# python

# def max_activities(activities):
#     # Сортуємо за часом завершення
#     activities.sort(key=lambda x: x[1])
#     selected = [activities[0]]
#     last_end = activities[0][1]
#     for start, end in activities[1:]:
#         if start >= last_end:
#             selected.append((start, end))
#             last_end = end
#     return selected
# acts = [(1, 3), (2, 5), (3, 9), (6, 8)]
# print(max_activities(acts))  # [(1, 3), (6, 8)]


# Задача 3 — Мінімальна кількість платформ
# Умова: Поїзди приїжджають і від'їжджають. Знайди мінімальну кількість платформ, щоб усі поїзди могли зупинитись.

# Вхід: arrivals = [9, 9, 12, 15], departures = [10, 12, 14, 18]
# Вихід: 2

# python

# def min_platforms(arrivals, departures):
#     arrivals.sort()
#     departures.sort()
#     platforms = 1
#     max_platforms = 1
#     i, j = 1, 0
#     while i < len(arrivals) and j < len(departures):
#         if arrivals[i] <= departures[j]:
#             platforms += 1
#             i += 1
#         else:
#             platforms -= 1
#             j += 1
#         max_platforms = max(max_platforms, platforms)
#     return max_platforms
# print(min_platforms([9, 9, 12, 15], [10, 12, 14, 18]))  # 2


# Задача 4 — Задача про рюкзак (дробовий)
# Умова: Є предмети з вартістю та вагою. Рюкзак вміщує W кг. Можна брати частини предметів. Максимізуй вартість.

# Вхід: items = [(60, 10), (100, 20), (120, 30)], W = 50
# Вихід: 240.0

# python

# def fractional_knapsack(items, W):
#     # Сортуємо за відношенням вартість/вага
#     items.sort(key=lambda x: x[0] / x[1], reverse=True)
#     total_value = 0.0
#     for value, weight in items:
#         if W >= weight:
#             total_value += value
#             W -= weight
#         else:
#             total_value += value * (W / weight)
#             break
#     return total_value
# items = [(60, 10), (100, 20), (120, 30)]
# print(fractional_knapsack(items, 50))  # 240.0


# Задача 5 — Мінімізація часу очікування
# Умова: n клієнтів чекають обслуговування. Час обслуговування кожного відомий. Мінімізуй сумарний час очікування.

# Вхід: [4, 2, 8, 1]
# Вихід: 14

# python

# def min_waiting_time(times):
#     times.sort()
#     total_wait = 0
#     for i, t in enumerate(times):
#         total_wait += t * (len(times) - i - 1)
#     return total_wait
# print(min_waiting_time([4, 2, 8, 1]))  # 14


# Задача 6 — Покриття відрізків точками
# Умова: Дано відрізки на числовій осі. Знайди мінімальну кількість точок, щоб кожен відрізок містив хоча б одну точку.

# Вхід: [(1, 3), (2, 5), (3, 6)]
# Вихід: 1 (точка 3 потрапляє в усі)

# python

# def min_points(segments):
#     segments.sort(key=lambda x: x[1])
#     points = []
#     last_point = float('-inf')
#     for start, end in segments:
#         if last_point < start:
#             last_point = end
#             points.append(end)
#     return len(points)
# print(min_points([(1, 3), (2, 5), (3, 6)]))  # 1


# Задача 7 — Максимальна сума підмасиву (жадібний підхід)
# Умова: Знайди підмасив із максимальною сумою (алгоритм Кадане).

# Вхід: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Вихід: 6 (підмасив [4, -1, 2, 1])

# python

# def max_subarray(nums):
#     max_sum = current = nums[0]
#     for num in nums[1:]:
#         current = max(num, current + num)
#         max_sum = max(max_sum, current)
#     return max_sum
# print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6


# Задача 8 — Найбільше число з цифр
# Умова: Дано масив невід'ємних чисел. Склади з них найбільше можливе число.

# Вхід: [3, 30, 34, 5, 9]
# Вихід: "9534330"

# python

# from functools import cmp_to_key
# def largest_number(nums):
#     def compare(a, b):
#         if a + b > b + a:
#             return -1
#         elif a + b < b + a:
#             return 1
#         return 0
#     nums = list(map(str, nums))
#     nums.sort(key=cmp_to_key(compare))
#     result = ''.join(nums)
#     return '0' if result[0] == '0' else result
# print(largest_number([3, 30, 34, 5, 9]))  # 9534330


# Задача 9 — Завдання з дедлайнами
# Умова: Є завдання з прибутком і дедлайном. Виконати можна лише 1 завдання за одиницю часу. Максимізуй прибуток.

# Вхід: [('A', 2, 100), ('B', 1, 19), ('C', 2, 27), ('D', 1, 25), ('E', 3, 15)]
# Вихід: Прибуток: 142

# python

# def job_scheduling(jobs):
#     jobs.sort(key=lambda x: x[2], reverse=True)
#     max_deadline = max(j[1] for j in jobs)
#     slots = [-1] * (max_deadline + 1)
#     total_profit = 0
#     for name, deadline, profit in jobs:
#         for t in range(deadline, 0, -1):
#             if slots[t] == -1:
#                 slots[t] = name
#                 total_profit += profit
#                 break
#     return total_profit
# jobs = [('A', 2, 100), ('B', 1, 19), ('C', 2, 27), ('D', 1, 25), ('E', 3, 15)]
# print(f"Прибуток: {job_scheduling(jobs)}")  # 142


# Задача 10 — Мінімальна кількість стрибків
# Умова: Масив чисел показує максимальну довжину стрибка з кожної позиції. Знайди мінімальну кількість стрибків до кінця масиву.

# Вхід: [2, 3, 1, 1, 4]
# Вихід: 2

# python

# def min_jumps(nums):
#     jumps = 0
#     current_end = 0
#     farthest = 0
#     for i in range(len(nums) - 1):
#         farthest = max(farthest, i + nums[i])
#         if i == current_end:
#             jumps += 1
#             current_end = farthest
#     return jumps
# print(min_jumps([2, 3, 1, 1, 4]))  # 2


# Задача 11 — Розподіл печива
# Умова: Є діти з рівнями жадібності g[] і печиво з розмірами s[].
# Дитина задоволена, якщо розмір печива ≥ її жадібності. Максимізуй кількість задоволених дітей.

# Вхід: g = [1, 2, 3], s = [1, 1]
# Вихід: 1

# python

# def find_content_children(g, s):
#     g.sort()
#     s.sort()
#     child = cookie = 0
#     while child < len(g) and cookie < len(s):
#         if s[cookie] >= g[child]:
#             child += 1
#         cookie += 1
#     return child
# print(find_content_children([1, 2, 3], [1, 1]))  # 1
# print(find_content_children([1, 2], [1, 2, 3]))  # 2


# Задача 12 — Мінімальний час для всіх завдань
# Умова: Є n завдань і k однакових машин. Знайди мінімально можливий максимальний час виконання, якщо завдання розподіляються між машинами.

# Вхід: tasks = [3, 2, 3], k = 2
# Вихід: 3

# python

# import heapq
# def min_max_time(tasks, k):
#     tasks.sort(reverse=True)
#     machines = [0] * k
#     heapq.heapify(machines)
#     for task in tasks:
#         least_loaded = heapq.heappop(machines)
#         heapq.heappush(machines, least_loaded + task)
#     return max(machines)
# print(min_max_time([3, 2, 3], 2))  # 5 → розподіл [3,2] і [3]
# print(min_max_time([1, 2, 3, 4, 5], 2))  # 9


# Задача 13 — Збираємо максимум квітів
# Умова: Уздовж доріжки ростуть квіти в позиціях. Ти можеш зробити не більше k кроків уліво або вправо від позиції 0. Знайди максимальну кількість квітів.

# Вхід: flowers = [1, 2, 5, 7, 8], k = 4
# Вихід: 4 (зупиняємось у 1, 2 → і йдемо вправо або навпаки)

# python

# def max_flowers(flowers, k):
#     n = len(flowers)
#     max_collected = 0
#     for left in range(n):
#         # Беремо left квітів зліва, решту — справа
#         right_steps = k - 2 * left
#         if right_steps < 0:
#             break
#         right = bisect_right_custom(flowers, right_steps)
#         max_collected = max(max_collected, left + right)
#     for right in range(n):
#         left_steps = k - 2 * right
#         if left_steps < 0:
#             break
#         left = bisect_right_custom(flowers, left_steps)
#         max_collected = max(max_collected, right + left)
#     return max_collected
# # Простіший варіант зі sliding window:
# def max_flowers_simple(flowers, k):
#     flowers.sort()
#     n = len(flowers)
#     max_count = 0
#     left = 0
#     for right in range(n):
#         while flowers[right] - flowers[left] > k:
#             left += 1
#         max_count = max(max_count, right - left + 1)
#     return max_count
# print(max_flowers_simple([1, 2, 5, 7, 8], 4))  # 2 (квіти 1 і 2, або 7 і 8)


# Задача 14 — Склади рядок без трьох однакових підряд
# Умова: Дано кількість символів a і b. Склади найдовший рядок, де немає трьох однакових символів підряд.

# Вхід: a = 4, b = 1
# Вихід: "aabaa" або "aab" тощо

# python

# def longest_diverse_string(a, b):
#     result = []
#     counts = [['a', a], ['b', b]]
#     while True:
#         counts.sort(key=lambda x: -x[1])
#         char, cnt = counts[0]
#         if cnt == 0:
#             break
#         # Додаємо до 2 символів найчастішого
#         take = 2 if cnt > counts[1][1] else 1
#         n = len(result)
#         if n >= 2 and result[-1] == result[-2] == char:
#             # Додаємо менш частий
#             if counts[1][1] == 0:
#                 break
#             result.append(counts[1][0])
#             counts[1][1] -= 1
#         else:
#             result.append(char)
#             counts[0][1] -= 1
#     return ''.join(result)
# print(longest_diverse_string(4, 1))  # aabaa або схожий


# Задача 15 — Мінімум видалень для унікальних символів
# Умова: Рядок містить лише малі латинські літери. Знайди мінімальну кількість видалень, щоб усі символи зустрічались унікальну кількість разів.

# Вхід: "aab"
# Вихід: 0 (a — 2 рази, b — 1 раз, всі частоти різні)

# Вхід: "aaabbbcc"
# Вихід: 2

# python

# from collections import Counter
# def min_deletions(s):
#     freq = sorted(Counter(s).values(), reverse=True)
#     deletions = 0
#     used = set()
#     for f in freq:
#         while f > 0 and f in used:
#             f -= 1
#             deletions += 1
#         if f > 0:
#             used.add(f)
#     return deletions
# print(min_deletions("aab"))         # 0
# print(min_deletions("aaabbbcc"))    # 2
# print(min_deletions("ceabaacb"))    # 2



# 📊 Зведена таблиця задач
# #	Назва задачі	Ключова ідея жадібності
# 1	Решта монетами	Брати найбільшу монету першою
# 2	Максимум активностей	Сортування за часом кінця
# 3	Мінімум платформ	Два вказівники на події
# 4	Дробовий рюкзак	Сортування за питомою вартістю
# 5	Мінімум очікування	Обслуговувати швидких першими
# 6	Покриття точками	Вибирати кінець відрізка
# 7	Максимальна сума (Кадане)	Продовжувати або починати з нуля
# 8	Найбільше число	Порівняння конкатенацій
# 9	Завдання з дедлайнами	Сортування за прибутком, заповнення слотів
# 10	Мінімум стрибків	Відстежувати найдальший досяжний
# 11	Розподіл печива	Сортування і двохпальцеве проходження
# 12	Мін. час на машинах	Завжди навантажувати найменш зайняту
# 13	Збираємо квіти	Sliding window по відстані
# 14	Рядок без 3 підряд	Завжди обирати найчастіший символ
# 15	Унікальні частоти	Зменшувати до вільного числа